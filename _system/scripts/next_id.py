#!/usr/bin/env python3
"""Print the next free ID.
  next_id.py participant
  next_id.py source
  next_id.py highlight S-0003
  next_id.py insight 2026_demo-fluxbench
"""
import csv, re, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from vaultlib import vault_root, iter_notes

root = vault_root()
kind = sys.argv[1] if len(sys.argv) > 1 else ""
nums = []
if kind == "participant":
    for _, fm, _ in iter_notes(root, "source"):
        m = re.match(r"P-(\d+)", str(fm.get("participant", "")))
        if m: nums.append(int(m.group(1)))
    key = root / "_raw" / "participants.csv"
    if key.exists():
        for row in csv.DictReader(key.open(encoding="utf-8")):
            m = re.match(r"P-(\d+)", row.get("id", ""))
            if m: nums.append(int(m.group(1)))
    print(f"P-{(max(nums) + 1) if nums else 1:03d}")
elif kind == "source":
    for _, fm, _ in iter_notes(root, "source"):
        m = re.match(r"S-(\d+)", str(fm.get("source_id", "")))
        if m: nums.append(int(m.group(1)))
    print(f"S-{(max(nums) + 1) if nums else 1:04d}")
elif kind == "highlight":
    sid = sys.argv[2].replace("-", "").lower()
    for _, fm, _ in iter_notes(root, "highlight"):
        m = re.match(rf"H-{sid.upper()}-(\d+)", str(fm.get("highlight_id", "")))
        if m: nums.append(int(m.group(1)))
    print(f"H-{sid.upper()}-{(max(nums) + 1) if nums else 1:04d}")
elif kind == "insight":
    proj = sys.argv[2]
    for _, fm, _ in iter_notes(root, "insight"):
        m = re.match(rf"I-{re.escape(proj)}-(\d+)", str(fm.get("insight_id", "")))
        if m: nums.append(int(m.group(1)))
    print(f"I-{proj}-{(max(nums) + 1) if nums else 1:02d}")
else:
    sys.exit(__doc__)
