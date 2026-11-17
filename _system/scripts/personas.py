#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = ["pyyaml"]
# ///
"""Personas: keep the generated parts of each persona note in step with the vault.

  personas.py refresh      rewrite "Where they appear" (between the appearances markers) and the counts in the
                           frontmatter of every note in 30 Personas/, from participant cards, highlights and insights.
  personas.py check        every persona has at least one participant; every participant's persona exists.

Hand-written sections are never touched."""
from __future__ import annotations

import re, sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from vaultlib import PAGES, as_list, iter_notes, read_note, vault_root, wikilink_target, write_note, id_from_name  # noqa: E402

START, END = "<!-- appearances:start -->", "<!-- appearances:end -->"


def collect(root: Path):
    cards = {fm["participant_id"]: (p, fm) for p, fm, _ in iter_notes(root, "participant")}
    srcs = {fm["source_id"]: (p, fm) for p, fm, _ in iter_notes(root, "source")}
    hls = [(p, fm) for p, fm, _ in iter_notes(root, "highlight") if fm.get("review") != "rejected"]
    ins = [(p, fm) for p, fm, _ in iter_notes(root, "insight")]
    return cards, srcs, hls, ins


def appearances(root: Path, pids: list[str], cards, srcs, hls, ins) -> tuple[str, dict]:
    projects = sorted({pr for pid in pids for pr in as_list(cards.get(pid, (None, {}))[1].get("projects"))})
    my_srcs = [(sid, fm) for sid, (p, fm) in sorted(srcs.items()) if fm.get("participant") in pids]
    my_hls = [(p, fm) for p, fm in hls if fm.get("participant") in pids]
    my_ids = {fm["highlight_id"] for _, fm in my_hls}
    my_ins = [(p, fm) for p, fm in ins if any(id_from_name(wikilink_target(h)) in my_ids for h in as_list(fm.get("highlights")))]
    out = []
    out.append("**Participants:** " + ", ".join(f"[[20 Participants/{pid}|{pid}]]" for pid in pids))
    out.append("**Projects:** " + (", ".join(f"[[10 Projects/{pr}/{PAGES['project']}|{pr}]]" for pr in projects) or "none"))
    out.append("**Sources:** " + (", ".join(f"[[{sid}]] ({fm.get('participant')}, {fm.get('date')})" for sid, fm in my_srcs) or "none"))
    out.append("")
    out.append(f"**Insights ({len(my_ins)})**")
    for p, fm in sorted(my_ins, key=lambda t: t[1]["insight_id"]):
        n = sum(1 for h in as_list(fm.get("highlights")) if id_from_name(wikilink_target(h)) in my_ids)
        out.append(f"- [[{p.stem}|{fm['insight_id']}]] {re.sub(r'^Insight: ', '', fm.get('title', ''))} · {n} of their highlights · {fm.get('evidence_level')}")
    out.append("")
    out.append(f"**Highlights ({len(my_hls)})**")
    for p, fm in sorted(my_hls, key=lambda t: t[1]["highlight_id"]):
        out.append(f"- [[{p.stem}|{fm['highlight_id']}]] {fm.get('title', '')} · {', '.join(as_list(fm.get('tags')))}")
    return "\n".join(out), {"projects": projects, "evidence_highlights": len(my_hls), "insights": len(my_ins)}


def cmd_refresh(root: Path):
    cards, srcs, hls, ins = collect(root)
    n = 0
    for p, fm, body in iter_notes(root, "persona"):
        pids = [pid for pid, (cp, cfm) in cards.items() if p.stem in str(cfm.get("persona", ""))] or as_list(fm.get("participants"))
        block, counts = appearances(root, sorted(pids), cards, srcs, hls, ins)
        if START not in body or END not in body:
            body = body.rstrip("\n") + f"\n\n## Where they appear\n{START}\n{END}\n"
        body = re.sub(re.escape(START) + r".*?" + re.escape(END), START + "\n" + block + "\n" + END, body, flags=re.S)
        fm.update({"participants": sorted(pids), **counts, "updated": str(date.today())})
        write_note(p, fm, body); n += 1
    print(f"refreshed {n} persona(s)")


def cmd_check(root: Path):
    cards, *_ = collect(root)
    bad = 0
    stems = {p.stem for p, _, _ in iter_notes(root, "persona")}
    for p, fm, _ in iter_notes(root, "persona"):
        if not as_list(fm.get("participants")): print(f"{p.name}: no participants"); bad += 1
    for pid, (cp, cfm) in cards.items():
        target = wikilink_target(cfm.get("persona", "")).split("/")[-1]
        if not target: print(f"{pid}: no persona"); bad += 1
        elif target not in stems: print(f"{pid}: persona {target!r} not found"); bad += 1
    print("ok" if not bad else f"{bad} problem(s)"); sys.exit(1 if bad else 0)


if __name__ == "__main__":
    root = vault_root(Path(__file__).resolve().parent)
    {"refresh": cmd_refresh, "check": cmd_check}.get(sys.argv[1] if len(sys.argv) > 1 else "", lambda r: sys.exit(__doc__))(root)
