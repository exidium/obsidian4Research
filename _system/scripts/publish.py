#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = ["pyyaml"]
# ///
"""Confluence bodies from vault notes (used by the research-publish skill).

  publish.py render <project> [--out DIR]    write one HTML body per page to DIR (default _system/publish/<project>/)
                                             and a manifest.json listing title, kind, source note, parent kind
  publish.py record <project> <note-id-or-page> <url>
                                             write `published_to` on the note after the page exists (the agent
                                             creates the page through the Confluence connector, then records it)

Pages produced for a project:
  study     from 01 project.md            title: "<project title>"
  readout   each f_deliverables/*.md       title: from the note
  insight   each e_insights/*.md           title: "Insight: <finding>"  (evidence embeds become quotes with their trace)

Rules: nothing from _raw/ is read; names never appear (quotes are by participant ID); wikilinks to notes that have a
`published_to` become Confluence links, others become plain text with the ID. Output follows the connector's HTML
format guide (plain HTML, data-type panels, no storage-format macros except toc/children)."""
from __future__ import annotations

import html, json, re, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from vaultlib import DIRS, PAGES, as_list, find_by_id, id_from_name, iter_notes, project_dir, read_note, vault_root, wikilink_target, write_note  # noqa: E402

TURN_RE = re.compile(r"^\[(\d{2}:\d{2}:\d{2})\].*?\^(s\d{4}-\d{4})\s*$", re.M | re.S)


# ---------------------------------------------------------------- vault lookups

class Vault:
    def __init__(self, root: Path, project: str):
        self.root, self.project = root, project
        self.pdir = project_dir(root, project)
        self.notes = {}        # stem -> (path, fm)
        self.by_id = {}        # highlight/insight/source id -> stem
        for p, fm, body in iter_notes(root):
            self.notes[p.stem] = (p, fm, body)
            for k in ("highlight_id", "insight_id", "source_id", "participant_id"):
                if fm.get(k):
                    self.by_id[fm[k]] = p.stem
        self.stamps = {}
        for p, fm, body in iter_notes(root, "source"):
            for m in TURN_RE.finditer(body):
                self.stamps[m.group(2)] = m.group(1)

    def resolve(self, target: str):
        stem = target.split("/")[-1].split("#")[0]
        if stem in self.notes:
            return self.notes[stem]
        if stem in self.by_id:
            return self.notes[self.by_id[stem]]
        return None

    def url(self, target: str) -> str | None:
        n = self.resolve(target)
        return (n[1].get("published_to") or None) if n else None


# ---------------------------------------------------------------- inline markdown -> html

def inline(v: Vault, s: str) -> str:
    out, i = [], 0
    for m in re.finditer(r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]|`([^`]+)`|\*\*([^*]+)\*\*|\*([^*]+)\*|_([^_]+)_|\[([^\]]+)\]\((https?://[^)]+)\)", s):
        out.append(html.escape(s[i:m.start()])); i = m.end()
        if m.group(1) is not None:
            target, text = m.group(1), m.group(2) or m.group(1).split("/")[-1]
            n = v.resolve(target); url = v.url(target)
            if url:
                out.append(f'<a href="{html.escape(url)}">{html.escape(text)}</a>')
            elif n and n[1].get("type") == "participant":
                out.append(f"<strong>{html.escape(n[1]['participant_id'])}</strong> ({html.escape(str(n[1].get('role', '')))})")
            elif n and n[1].get("type") in ("highlight", "insight", "source"):
                nid = id_from_name(n[0].stem)
                out.append(f"<code>{html.escape(nid)}</code>" if text.strip() == nid else f"{html.escape(text)} (<code>{html.escape(nid)}</code>)")
            else:
                out.append(html.escape(text))
        elif m.group(7) is not None: out.append(f'<a href="{html.escape(m.group(8))}">{html.escape(m.group(7))}</a>')
        elif m.group(3) is not None: out.append(f"<code>{html.escape(m.group(3))}</code>")
        elif m.group(4) is not None: out.append(f"<strong>{inline(v, m.group(4))}</strong>")
        else: out.append(f"<em>{inline(v, m.group(5) or m.group(6))}</em>")
    out.append(html.escape(s[i:]))
    return "".join(out)


# ---------------------------------------------------------------- block markdown -> html

def evidence_block(v: Vault, hid: str) -> str:
    n = v.resolve(hid)
    if not n:
        return f"<p><code>{html.escape(hid)}</code> (highlight not found)</p>"
    fm = n[1]
    sid = wikilink_target(fm.get("source", "")); blk = fm.get("block", "")
    trace = f"{fm.get('participant')} · {sid} @ {v.stamps.get(blk, '?')} · {fm.get('highlight_id')}"
    tags = ", ".join(as_list(fm.get("tags")))
    ctx = f"<p><em>{html.escape(str(fm['context']))}</em></p>" if fm.get("context") else ""
    return (f"<blockquote><p>{html.escape(str(fm.get('quote', '')))}</p></blockquote>"
            f"<p style=\"font-size: 14px\"><strong>{html.escape(str(fm.get('title', '')))}</strong> · {html.escape(trace)} · tags: {html.escape(tags)}</p>{ctx}")


def table(v: Vault, rows: list[str]) -> str:
    cells = [[c.strip().replace("\\|", "|") for c in re.split(r"(?<!\\)\|", r.strip().strip("|"))] for r in rows if not re.match(r"^\s*\|?\s*:?-{2,}", r)]
    if not cells:
        return ""
    head, body = cells[0], cells[1:]
    h = "".join(f"<th>{inline(v, c)}</th>" for c in head)
    b = "".join("<tr>" + "".join(f"<td>{inline(v, c)}</td>" for c in r) + "</tr>" for r in body)
    return f"<table><thead><tr>{h}</tr></thead><tbody>{b}</tbody></table>"


def md_to_html(v: Vault, md: str, heading_shift: int = 0) -> str:
    lines = md.split("\n"); out = []; i = 0
    def flush_list(items, ordered):
        tag = "ol" if ordered else "ul"
        out.append(f"<{tag}>" + "".join(f"<li>{inline(v, it)}</li>" for it in items) + f"</{tag}>")
    while i < len(lines):
        l = lines[i]
        if not l.strip():
            i += 1; continue
        if l.startswith("<!--"):
            while i < len(lines) and "-->" not in lines[i]: i += 1
            i += 1; continue
        m = re.match(r"^(#{1,6})\s+(.*)", l)
        if m:
            lvl = min(6, len(m.group(1)) + heading_shift)
            out.append(f"<h{lvl}>{inline(v, m.group(2).strip())}</h{lvl}>"); i += 1; continue
        if l.startswith("> [!"):
            kind = re.match(r"> \[!(\w+)\]", l).group(1).lower()
            ptype = {"warning": "warning", "danger": "error", "info": "info", "abstract": "note", "tip": "info"}.get(kind, "note")
            title = re.sub(r"> \[!\w+\]-?\s*", "", l).strip()
            body = []
            i += 1
            while i < len(lines) and lines[i].startswith(">"):
                body.append(lines[i][1:].strip()); i += 1
            inner = (f"<p><strong>{inline(v, title)}</strong></p>" if title else "") + "".join(f"<p>{inline(v, b)}</p>" for b in body if b and not b.startswith("!["))
            out.append(f'<div data-type="panel-{ptype}">{inner or "<p></p>"}</div>'); continue
        if l.startswith(">"):
            body = []
            while i < len(lines) and lines[i].startswith(">"):
                body.append(lines[i][1:].strip()); i += 1
            out.append("<blockquote>" + "".join(f"<p>{inline(v, b)}</p>" for b in body if b) + "</blockquote>"); continue
        if l.startswith("|"):
            rows = []
            while i < len(lines) and lines[i].startswith("|"):
                rows.append(lines[i]); i += 1
            out.append(table(v, rows)); continue
        m = re.match(r"^!\[\[([^\]|#]+)(#[^\]|]+)?(\|[^\]]+)?\]\]", l.strip())
        if m:
            target = m.group(1)
            if target.endswith(".base") or target.startswith("_raw/"):
                i += 1; continue                      # Bases views and media have no Confluence equivalent
            n = v.resolve(target)
            if n and n[1].get("type") == "highlight":
                out.append(evidence_block(v, n[1]["highlight_id"]))
            elif n and n[1].get("type") == "source" and m.group(2):
                out.append(f"<p><code>{html.escape(id_from_name(n[0].stem))}</code> {html.escape(m.group(2))}</p>")
            i += 1; continue
        m = re.match(r"^(\s*)([-*]|\d+\.)\s+(.*)", l)
        if m:
            ordered = m.group(2)[0].isdigit(); items = []
            while i < len(lines) and re.match(r"^(\s*)([-*]|\d+\.)\s+", lines[i]):
                items.append(re.sub(r"^(\s*)([-*]|\d+\.)\s+", "", lines[i]).rstrip()); i += 1
            flush_list(items, ordered); continue
        para = []
        while i < len(lines) and lines[i].strip() and not re.match(r"^(#{1,6}\s|>|\||!\[\[|\s*[-*]\s|\s*\d+\.\s|<!--)", lines[i]):
            para.append(lines[i].rstrip()); i += 1
        if para:
            out.append("<p>" + "<br>".join(inline(v, p) for p in para) + "</p>")
        else:
            i += 1
    return "\n".join(out)


# ---------------------------------------------------------------- pages

def demo_panel(fm: dict) -> str:
    return ('<div data-type="panel-warning"><p><strong>Fictional demo.</strong> The product, the vendor, the participants and every quote are '
            'invented; the recordings are text-to-speech over authored transcripts. This page shows what a study published from the '
            'research vault looks like. Nothing here describes a real customer.</p></div>')


def study_page(v: Vault) -> tuple[str, str]:
    p = v.pdir / f"{PAGES['project']}.md"; fm, body = read_note(p)
    body = re.sub(r"## Contents\n.*?(?=\n# )", "", body, flags=re.S)            # Confluence gets a TOC macro instead
    body = re.sub(r"# Operations & data\n.*\Z", "", body, flags=re.S)         # vault-only boards
    body = re.sub(r"^> \[!warning\] Fictional demo project\n(>.*\n)+", "", body, flags=re.M)
    insights = sorted([n for n in v.notes.values() if n[1].get("type") == "insight" and n[1].get("project") == v.project], key=lambda n: n[1]["insight_id"])
    items = "".join(f"<li>{inline(v, '[[' + n[0].stem + '|' + re.sub(r'^Insight: ', '', n[1].get('title', '')) + ']]')} · {html.escape(str(n[1].get('evidence_level')))} · {html.escape(', '.join(as_list(n[1].get('participants'))))}</li>" for n in insights)
    body = body.replace("![[_system/bases/insights.base]]", "INSIGHTLISTPLACEHOLDER")
    htmlbody = md_to_html(v, body, heading_shift=0).replace("<p>INSIGHTLISTPLACEHOLDER</p>", f"<ul>{items}</ul>" if items else "")
    toc = ('<div data-type="extension" data-extension-key="toc" data-extension-type="com.atlassian.confluence.macro.core" '
           'data-parameters=\'{"macroParams":{"maxLevel":{"value":"2"}},"macroMetadata":{"schemaVersion":{"value":"1"},"title":"Table of Contents"}}\'></div>')
    meta = (f"<p><strong>Phase:</strong> {html.escape(str(fm.get('phase')))} · <strong>Status:</strong> {html.escape(str(fm.get('status')))} · "
            f"<strong>Dates:</strong> {html.escape(' to '.join(str(d) for d in as_list(fm.get('date_range'))))} · <strong>Rally study:</strong> {html.escape(str(fm.get('rally_study')))} · "
            f"<strong>Domain:</strong> {html.escape(str(fm.get('domain')))}</p>")
    return str(fm.get("title")), demo_panel(fm) + meta + toc + htmlbody


def insight_page(v: Vault, p: Path, fm: dict, body: str) -> tuple[str, str]:
    body = re.sub(r"^# .*\n", "", body, count=1, flags=re.M)
    body = re.sub(r"^!\[\[_raw/[^\n]*\n", "", body, flags=re.M)
    meta = (f"<p><strong>Evidence level:</strong> <span data-type=\"status\" data-color=\"{'green' if fm.get('evidence_level') == 'strong' else 'yellow' if fm.get('evidence_level') == 'emerging' else 'neutral'}\">{html.escape(str(fm.get('evidence_level')))}</span> · "
            f"<strong>Participants:</strong> {html.escape(', '.join(as_list(fm.get('participants'))))} · <strong>Research question:</strong> {html.escape(str(fm.get('research_question')))} · "
            f"<strong>Status:</strong> {html.escape(str(fm.get('status')))} · <strong>Tags:</strong> {html.escape(', '.join(as_list(fm.get('tags'))))} · <strong>ID:</strong> <code>{html.escape(fm['insight_id'])}</code></p>")
    return str(fm.get("title")), demo_panel(fm) + meta + md_to_html(v, body)


def deliverable_page(v: Vault, p: Path, fm: dict, body: str) -> tuple[str, str]:
    body = re.sub(r"^# .*\n", "", body, count=1, flags=re.M)
    body = re.sub(r"^> \[!warning\] Fictional demo\n(>.*\n)+", "", body, flags=re.M)
    meta = f"<p><strong>Status:</strong> {html.escape(str(fm.get('status')))} v{html.escape(str(fm.get('version')))} · <strong>Date:</strong> {html.escape(str(fm.get('date')))} · <strong>For:</strong> {html.escape(', '.join(as_list(fm.get('audience'))))}</p>"
    return str(fm.get("title")), demo_panel(fm) + meta + md_to_html(v, body)


def cmd_render(root: Path, project: str, out: Path):
    v = Vault(root, project); out.mkdir(parents=True, exist_ok=True)
    manifest = []
    t, b = study_page(v); (out / "study.html").write_text(b, encoding="utf-8")
    manifest.append({"kind": "study", "title": t, "file": "study.html", "note": f"{PAGES['project']}.md", "parent": "space"})
    for p, fm, body in sorted(iter_notes(root, "deliverable"), key=lambda n: n[0].name):
        if fm.get("project") != project or fm.get("doc") != "readout": continue
        t, b = deliverable_page(v, p, fm, body); f = f"readout-{p.stem[:40]}.html".replace(" ", "_")
        (out / f).write_text(b, encoding="utf-8"); manifest.append({"kind": "readout", "title": t, "file": f, "note": p.name, "parent": "study"})
    for p, fm, body in sorted(iter_notes(root, "insight"), key=lambda n: n[1]["insight_id"]):
        if fm.get("project") != project: continue
        t, b = insight_page(v, p, fm, body); f = f"{fm['insight_id']}.html"
        (out / f).write_text(b, encoding="utf-8"); manifest.append({"kind": "insight", "title": t, "file": f, "note": p.name, "parent": "study", "published_to": fm.get("published_to") or ""})
    (out / "manifest.json").write_text(json.dumps(manifest, indent=1), encoding="utf-8")
    for m in manifest:
        print(f"{m['kind']:8} {m['file']:45} {m['title'][:80]}")
    print(f"{len(manifest)} page bodies in {out}")


def cmd_record(root: Path, project: str, which: str, url: str):
    v = Vault(root, project)
    if which in ("study", PAGES["project"]):
        p = v.pdir / f"{PAGES['project']}.md"
    else:
        n = v.resolve(which)
        if not n: sys.exit(f"no note for {which}")
        p = n[0]
    fm, body = read_note(p); fm["published_to"] = url
    if fm.get("type") == "insight" and fm.get("status") == "draft":
        pass  # status stays the researcher's call; publishing a draft is allowed for the demo
    write_note(p, fm, body); print(f"{p.name}: published_to = {url}")


if __name__ == "__main__":
    root = vault_root(Path(__file__).resolve().parent)
    a = sys.argv[1:]
    if len(a) >= 2 and a[0] == "render":
        out = Path(a[a.index("--out") + 1]) if "--out" in a else root / "_system" / "publish" / a[1]
        cmd_render(root, a[1], out)
    elif len(a) == 4 and a[0] == "record":
        cmd_record(root, a[1], a[2], a[3])
    else:
        sys.exit(__doc__)
