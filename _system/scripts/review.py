#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = ["pyyaml"]
# ///
"""Bulk review decisions on highlights (the human gate after automatic tagging).

  review.py pending [<project>] [--source S-####]                 what is waiting, grouped by source and confidence
  review.py accept  (<H-id> ... | --source S-#### | --project <p>) [--min-confidence high|medium|low] [--tag <tag>]
  review.py reject  (<H-id> ... | --source S-#### | --project <p>) [--max-confidence low|medium|high] [--tag <tag>] [--reason "..."]

Only `review`, `reviewed_by`, `reviewed` (and `review_note`) change; the highlight itself is never edited.
Every decision is appended to _system/provenance.log. Rejected highlights stay in the vault, out of synthesis."""
from __future__ import annotations

import os, sys
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from vaultlib import as_list, iter_notes, read_note, vault_root, wikilink_target, write_note  # noqa: E402

LEVELS = {"low": 0, "medium": 1, "high": 2}


def select(root, args):
    ids = [a for a in args if a.startswith("H-")]
    src = args[args.index("--source") + 1] if "--source" in args else None
    proj = args[args.index("--project") + 1] if "--project" in args else None
    tag = args[args.index("--tag") + 1] if "--tag" in args else None
    minc = LEVELS[args[args.index("--min-confidence") + 1]] if "--min-confidence" in args else None
    maxc = LEVELS[args[args.index("--max-confidence") + 1]] if "--max-confidence" in args else None
    for p, fm, body in iter_notes(root, "highlight"):
        if ids and fm.get("highlight_id") not in ids: continue
        if src and wikilink_target(fm.get("source")) != src: continue
        if proj and fm.get("project") != proj: continue
        if tag and tag not in as_list(fm.get("tags")): continue
        c = LEVELS.get(str(fm.get("confidence", "medium")), 1)
        if minc is not None and c < minc: continue
        if maxc is not None and c > maxc: continue
        yield p, fm, body


def decide(root, args, verdict):
    reason = args[args.index("--reason") + 1] if "--reason" in args else ""
    who = os.environ.get("RESEARCHER", "P-000"); n = 0; log = root / "_system" / "provenance.log"
    for p, fm, body in select(root, args):
        if fm.get("review") == verdict: continue
        fm["review"], fm["reviewed_by"], fm["reviewed"] = verdict, who, str(date.today())
        if reason: fm["review_note"] = reason
        write_note(p, fm, body); n += 1
        with log.open("a", encoding="utf-8") as f:
            f.write(f"{date.today()}T00:00:00Z\tresearch-highlight\treview-{verdict}\t{fm['highlight_id']}\t{who}\n")
    print(f"{verdict}: {n} highlight(s)")


def pending(root, args):
    proj = args[1] if len(args) > 1 and not args[1].startswith("--") else None
    rows = defaultdict(Counter); total = 0
    for p, fm, body in select(root, ["--project", proj] if proj else []):
        if fm.get("review") != "proposed": continue
        rows[wikilink_target(fm.get("source"))][str(fm.get("confidence", "medium"))] += 1; total += 1
    for sid in sorted(rows):
        c = rows[sid]; print(f"{sid}: {sum(c.values()):3}  high {c['high']:3}  medium {c['medium']:3}  low {c['low']:3}")
    print(f"pending: {total}" if total else "nothing pending")


if __name__ == "__main__":
    root = vault_root(Path(__file__).resolve().parent)
    a = sys.argv[1:]
    cmd = a[0] if a else ""
    if cmd == "pending": pending(root, a)
    elif cmd in ("accept", "reject"): decide(root, a[1:], "accepted" if cmd == "accept" else "rejected")
    else: sys.exit(__doc__)
