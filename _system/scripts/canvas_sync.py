#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = ["pyyaml"]
# ///
"""Apply lane membership from a_setup/boards/tag-board.canvas back to the highlight notes.
  canvas_sync.py <project_id> [--dry-run]
A card's lanes (groups whose label starts with a taxonomy tag) replace that dimension's tags on the highlight.
Cards outside every lane are skipped. A lane whose tag is not in the taxonomy is added as `proposed`."""
import json, re, sys
from datetime import date
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from vaultlib import BOARDS, DIRS, vault_root, read_note, write_note, all_tags, load_project_tags, save_project_tags, as_list, find_by_id, id_from_name, WORKSPACE_DIMS

project = sys.argv[1] if len(sys.argv) > 1 else sys.exit(__doc__)
dry = "--dry-run" in sys.argv
root = vault_root(); tags = all_tags(root, project)
cpath = root / "10 Projects" / project / BOARDS / "tag-board.canvas"
data = json.loads(cpath.read_text(encoding="utf-8"))
TAG = re.compile(r"^([a-z]+/[a-z0-9-]+)")
lanes = []
for n in data["nodes"]:
    if n.get("type") == "group":
        m = TAG.match(n.get("label", "").strip())
        if m: lanes.append((m.group(1), n))
dims = {t.split("/")[0] for t, _ in lanes}
if len(dims) != 1: sys.exit(f"lanes must all belong to one dimension, found {sorted(dims)}")
dim = dims.pop()

def inside(card, g):
    cx, cy = card["x"] + card["width"] / 2, card["y"] + card["height"] / 2
    return g["x"] <= cx <= g["x"] + g["width"] and g["y"] <= cy <= g["y"] + g["height"]

membership = {}
for n in data["nodes"]:
    if n.get("type") != "file" or f"/{DIRS['highlights']}/" not in n.get("file", ""): continue
    hid = id_from_name(Path(n["file"]).stem)
    for t, g in lanes:
        if inside(n, g): membership.setdefault(hid, set()).add(t)
    membership.setdefault(hid, set())

new_tags = {t for s in membership.values() for t in s if t not in tags}
changed = 0; touched = []
for hid, want in sorted(membership.items()):
    p = find_by_id(root, project, "highlight", hid)
    if not p: print(f"skip {hid}: note not found"); continue
    if not want: print(f"skip {hid}: outside every lane"); continue
    fm, body = read_note(p)
    cur = as_list(fm.get("tags"))
    keep = [t for t in cur if not t.startswith(dim + "/")]
    cur_dim = [t for t in cur if t.startswith(dim + "/")]
    if set(cur_dim) == want: continue
    fm["tags"] = keep + sorted(want)
    changed += 1; touched.append(hid)
    print(f"{'would change' if dry else 'changed'} {hid}: {dim} {sorted(cur_dim)} -> {sorted(want)}")
    if not dry: write_note(p, fm, body)
if new_tags:
    if dim in WORKSPACE_DIMS:
        sys.exit(f"lanes {sorted(new_tags)} are not workspace tags; workspace boards are admin-controlled. Use a project tag group instead.")
    print("lanes not in project tags, " + ("would be " if dry else "") + "added as proposed: " + ", ".join(sorted(new_tags)))
    if not dry:
        pt = load_project_tags(root, project)
        grp = next((g for g in pt["groups"] if g["id"] == dim), None)
        if not grp:
            grp = {"id": dim, "name": dim, "tags": []}; pt["groups"].append(grp)
        for t in sorted(new_tags):
            grp.setdefault("tags", []).append({"id": t, "definition": "TODO: created from the canvas; define before activating",
                                               "status": "proposed", "proposed_by": "human", "created": str(date.today()),
                                               "evidence": [h for h in touched if t in membership[h]]})
        save_project_tags(root, project, pt)
print(f"{changed} highlight(s) {'would be ' if dry else ''}updated across {len(lanes)} lanes")
