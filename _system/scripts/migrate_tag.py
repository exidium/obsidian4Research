#!/usr/bin/env python3
"""Rename or merge a tag across the vault and mark it deprecated in the taxonomy.
  migrate_tag.py <old-tag> <new-tag> [--dry-run]
The new tag must already exist in the taxonomy (any status); it is set to active."""
import argparse, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from vaultlib import vault_root, iter_notes, read_note, write_note, load_taxonomy, save_taxonomy, taxonomy_tags, as_list

ap = argparse.ArgumentParser(); ap.add_argument("old"); ap.add_argument("new"); ap.add_argument("--dry-run", action="store_true")
a = ap.parse_args()
root = vault_root(); tax = load_taxonomy(root); tags = taxonomy_tags(tax)
if a.new not in tags: sys.exit(f"{a.new} is not in the taxonomy; add it first (research-organize)")
if a.old not in tags: sys.exit(f"{a.old} is not in the taxonomy")
PROPS = ("tags", "segment", "method", "product", "methods")
changed = 0
for p, fm, body in iter_notes(root):
    touched = False
    for prop in PROPS:
        if prop not in fm: continue
        v = fm[prop]
        if isinstance(v, list):
            if a.old in v:
                fm[prop] = [x for x in v if x != a.old] + ([a.new] if a.new not in v else []); touched = True
        elif v == a.old:
            fm[prop] = a.new; touched = True
    if touched:
        changed += 1
        print(f"{'would update' if a.dry_run else 'updated'} {p.relative_to(root)}")
        if not a.dry_run: write_note(p, fm, body)
if not a.dry_run:
    for dim in tax["dimensions"].values():
        for t in dim.get("tags") or []:
            if t["id"] == a.old: t["status"] = "deprecated"; t["merged_into"] = a.new
            if t["id"] == a.new: t["status"] = "active"
    save_taxonomy(root, tax)
print(f"{changed} note(s) {'would be ' if a.dry_run else ''}changed; taxonomy {'unchanged (dry run)' if a.dry_run else 'updated'}")
