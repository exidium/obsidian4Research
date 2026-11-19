#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = ["pyyaml"]
# ///
"""Rename or merge a tag across notes and mark it deprecated.
  migrate_tag.py <old-tag> <new-tag> [--project <id>] [--dry-run]
Project tags need --project (edits that project's tags.yaml and notes). Workspace tags are admin-controlled:
the script will rewrite notes vault-wide but refuses to edit _system/taxonomy.yaml; do that with the UXR team."""
import argparse, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from vaultlib import vault_root, iter_notes, write_note, all_tags, load_project_tags, save_project_tags, WORKSPACE_DIMS

ap = argparse.ArgumentParser(); ap.add_argument("old"); ap.add_argument("new"); ap.add_argument("--project"); ap.add_argument("--dry-run", action="store_true")
a = ap.parse_args(); root = vault_root(); tags = all_tags(root, a.project)
for t in (a.old, a.new):
    if t not in tags: sys.exit(f"{t} is not a known tag" + ("" if a.project else " (pass --project for project tags)"))
changed = 0
for p, fm, body in iter_notes(root):
    if a.project and fm.get("project") != a.project: continue
    touched = False
    for prop in ("tags",):
        v = fm.get(prop)
        if isinstance(v, list) and a.old in v:
            fm[prop] = [x for x in v if x != a.old] + ([a.new] if a.new not in v else []); touched = True
    if touched:
        changed += 1; print(f"{'would update' if a.dry_run else 'updated'} {p.relative_to(root)}")
        if not a.dry_run: write_note(p, fm, body)
if a.old.split("/")[0] in WORKSPACE_DIMS:
    print("workspace tag: notes rewritten, taxonomy.yaml left untouched (admin-controlled)")
elif not a.dry_run and a.project:
    pt = load_project_tags(root, a.project)
    for g in pt["groups"]:
        for t in g.get("tags") or []:
            if t["id"] == a.old: t["status"] = "deprecated"; t["merged_into"] = a.new
            if t["id"] == a.new and t.get("status") == "proposed": t["status"] = "active"
    save_project_tags(root, a.project, pt)
print(f"{changed} note(s) {'would be ' if a.dry_run else ''}changed")
