#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = ["pyyaml"]
# ///
"""Compact TSV of a project's highlights for synthesis (keeps context small).
  highlights_table.py <project_id> [--accepted-only] [--tag theme/pain]"""
import argparse, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from vaultlib import vault_root, iter_notes, as_list

ap = argparse.ArgumentParser()
ap.add_argument("project"); ap.add_argument("--accepted-only", action="store_true"); ap.add_argument("--tag")
a = ap.parse_args()
root = vault_root()
print("id\ttitle\tparticipant\ttags\treview\tquote\trationale")
n = 0
for p, fm, body in iter_notes(root, "highlight"):
    if fm.get("project") != a.project: continue
    if a.accepted_only and fm.get("review") != "accepted": continue
    tags = as_list(fm.get("tags"))
    if a.tag and a.tag not in tags: continue
    why = ""
    for line in body.splitlines():
        if line.startswith("**Rationale:**"):
            why = line.replace("**Rationale:**", "").strip()
    q = str(fm.get("quote", "")).replace("\t", " ").replace("\n", " ")
    print(f"{fm.get('highlight_id')}\t{fm.get('title','')}\t{fm.get('participant')}\t{', '.join(tags)}\t{fm.get('review')}\t{q}\t{why}")
    n += 1
print(f"# {n} highlights", file=sys.stderr)
