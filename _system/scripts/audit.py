#!/usr/bin/env python3
"""Vault integrity audit. Prints a Markdown report; --write saves it to _system/reports/.
Exit 1 when errors exist (warnings alone exit 0)."""
import re, sys, subprocess
from datetime import date
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from vaultlib import vault_root, iter_notes, load_taxonomy, taxonomy_tags, blocks_in, norm, as_list, wikilink_target

root = vault_root(); tax = load_taxonomy(root); tags = taxonomy_tags(tax)
errors, warns, info = [], [], []
E = lambda s: errors.append(s); W = lambda s: warns.append(s); I = lambda s: info.append(s)

sources, highlights, insights, projects = {}, {}, {}, {}
for p, fm, body in iter_notes(root):
    t = fm.get("type")
    rel = str(p.relative_to(root))
    if t == "source": sources[fm.get("source_id")] = (rel, fm, body)
    elif t == "highlight": highlights[fm.get("highlight_id")] = (rel, fm, body)
    elif t == "insight": insights[fm.get("insight_id")] = (rel, fm, body)
    elif t == "project": projects[fm.get("project_id")] = (rel, fm, body)
    elif t == "overview": pass
    elif p.name != "project.md": W(f"{rel}: no recognised `type`")

for pid, (rel, fm, _) in projects.items():
    if pid != Path(rel).parent.name: E(f"{rel}: project_id `{pid}` ≠ folder name")

used_tags = {}
for sid, (rel, fm, body) in sources.items():
    if not re.match(r"S-\d{4}$", str(sid)): E(f"{rel}: bad source_id {sid}")
    if fm.get("status") not in ("ingested", "highlighted", "archived"): E(f"{rel}: bad status {fm.get('status')}")
    if not fm.get("redacted"): W(f"{rel}: redacted is false; run scan_pii and set redacted: true")
    if not re.match(r"P-\d{3}$", str(fm.get("participant"))): E(f"{rel}: bad participant {fm.get('participant')}")
    blocks = blocks_in(body)
    sid_l = str(sid).replace("-", "").lower()
    expected = [f"{sid_l}-{i:04d}" for i in range(1, len(blocks) + 1)]
    if list(blocks) != expected: E(f"{rel}: block IDs not sequential/consistent with source_id")
    if not blocks: E(f"{rel}: no transcript blocks")
    if fm.get("project") not in projects: E(f"{rel}: project {fm.get('project')} has no project.md")

hl_by_source = {}
for hid, (rel, fm, body) in highlights.items():
    sid = wikilink_target(fm.get("source"))
    hl_by_source.setdefault(sid, []).append(hid)
    if sid not in sources: E(f"{rel}: source {sid} not found"); continue
    srel, sfm, sbody = sources[sid]
    if fm.get("participant") != sfm.get("participant"): E(f"{rel}: participant ≠ source participant")
    if fm.get("project") != sfm.get("project"): E(f"{rel}: project ≠ source project")
    blocks = blocks_in(sbody)
    b = str(fm.get("block", ""))
    if b not in blocks: E(f"{rel}: block ^{b} not in {sid}")
    elif norm(fm.get("quote")) not in norm(blocks[b]): E(f"{rel}: quote is not verbatim from block ^{b}")
    if f"[[{sid}#^{b}]]" not in body: W(f"{rel}: body does not embed its block")
    if fm.get("review") not in ("proposed", "accepted", "rejected"): E(f"{rel}: bad review {fm.get('review')}")
    tl = as_list(fm.get("tags"))
    if not any(t.startswith("theme/") for t in tl): E(f"{rel}: no theme/ tag")
    if not any(t.startswith(("behavior/", "topic/")) for t in tl): W(f"{rel}: no behavior/ or topic/ tag")
    for t in tl + as_list(fm.get("segment")):
        used_tags[t] = used_tags.get(t, 0) + 1
        if t not in tags: E(f"{rel}: tag `{t}` not in taxonomy")
        elif tags[t].get("status") == "deprecated": E(f"{rel}: tag `{t}` is deprecated → {tags[t].get('merged_into')}")
    if "**Why it matters:**" not in body: W(f"{rel}: missing 'Why it matters' line")

for sid, (rel, fm, _) in sources.items():
    n = len(hl_by_source.get(sid, []))
    if fm.get("status") == "ingested" and n: W(f"{rel}: has {n} highlights but status is still ingested")
    if fm.get("status") == "highlighted" and not n: W(f"{rel}: status highlighted but no highlights")

for iid, (rel, fm, body) in insights.items():
    hls = [wikilink_target(h) for h in as_list(fm.get("highlights"))]
    if len(hls) < 1: E(f"{rel}: no highlights cited")
    parts = set()
    for h in hls:
        if h not in highlights: E(f"{rel}: cites missing highlight {h}"); continue
        parts.add(highlights[h][1].get("participant"))
        if highlights[h][1].get("review") == "rejected": E(f"{rel}: cites rejected highlight {h}")
        if f"[[{h}]]" not in body: W(f"{rel}: {h} listed but not embedded in Evidence")
    declared = set(as_list(fm.get("participants")))
    if declared != parts: W(f"{rel}: participants {sorted(declared)} ≠ evidence participants {sorted(parts)}")
    exp = "low" if len(parts) <= 1 else "medium" if len(parts) == 2 else "high"
    if fm.get("confidence") != exp: W(f"{rel}: confidence {fm.get('confidence')} but evidence supports {exp} ({len(parts)} participants)")
    if fm.get("status") not in ("draft", "reviewed", "published"): E(f"{rel}: bad status")
    if fm.get("status") == "published" and not fm.get("published_to"): E(f"{rel}: published without published_to")
    for t in as_list(fm.get("tags")):
        if t not in tags: E(f"{rel}: tag `{t}` not in taxonomy")

proposed = [t for t, d in tags.items() if d.get("status") == "proposed"]
unused = [t for t, d in tags.items() if d.get("status") == "active" and t not in used_tags and d["dimension"] in ("theme", "behavior", "topic")]
if proposed: I("Proposed tags awaiting a decision: " + ", ".join(proposed))
if unused: I(f"Active tags never used ({len(unused)}): " + ", ".join(unused))

try:
    pii = subprocess.run([sys.executable, str(Path(__file__).parent / "scan_pii.py")], capture_output=True, text=True, cwd=root)
    for line in pii.stdout.splitlines():
        if "\t" in line: E(f"PII: {line}")
except Exception as ex:
    W(f"scan_pii failed: {ex}")

rep = [f"# Vault audit {date.today()}", "",
       f"Projects {len(projects)} · Sources {len(sources)} · Highlights {len(highlights)} · Insights {len(insights)}", "",
       f"Errors {len(errors)} · Warnings {len(warns)}", ""]
for title, items in (("Errors", errors), ("Warnings", warns), ("Info", info)):
    if items: rep += [f"## {title}", *[f"- {x}" for x in items], ""]
if used_tags:
    rep += ["## Tag usage", "| tag | highlights |", "|---|---|", *[f"| {t} | {n} |" for t, n in sorted(used_tags.items(), key=lambda x: -x[1])], ""]
out = "\n".join(rep)
print(out)
if "--write" in sys.argv:
    p = root / "_system" / "reports" / f"audit-{date.today()}.md"; p.write_text(out, encoding="utf-8"); print(f"saved {p.relative_to(root)}")
sys.exit(1 if errors else 0)
