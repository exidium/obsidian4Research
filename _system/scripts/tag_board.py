#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = ["pyyaml"]
# ///
"""Generate the live tag board for a project (or the vault).
  tag_board.py <project_id>
        -> 10 Projects/<project>/a_setup/boards/tag-board.base : one Kanban view per tag group (workspace dimension or
           project group), lanes = that group's tags, cards = highlights. Reads the notes live.
        -> 10 Projects/<project>/03 tag board.md : one section per group, each embedding its Kanban,
           with the group's tag definitions in a collapsed callout.
  tag_board.py --all
        -> _system/tag-board.md : same page across projects, embedding _system/bases/highlights-all.base.
  tag_board.py <project_id> --canvas [--dimension journey]
        -> 10 Projects/<project>/a_setup/boards/tag-board.canvas : one lane per tag of that dimension, highlights as
           draggable cards. Drag in Obsidian, then run canvas_sync.py to apply the new tags.
Also writes 10 Projects/<project>/a_setup/boards/tags.base (tag cards by group). Generated files live in a_setup/boards/ and d_tags/; the root holds 01 project, 02 insights review and 03 tag board.
Only the *structure* (which groups exist) is generated; every board reads the highlight notes live.
Re-run when a tag group is added to tags/tags.yaml. Never hand-edit the outputs (except by dragging)."""
import sys, json, random
from datetime import date
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from vaultlib import BOARDS, DIRS, PAGES, vault_root, iter_notes, load_taxonomy, taxonomy_tags, as_list, write_note, load_project_tags, project_tag_index, WORKSPACE_DIMS

DIM_NAMES = {"experience": "Experience level", "functionality": "Functionality", "insight": "Insight",
             "sentiment": "Sentiment", "ops": "Research ops", "journey": "Journey stage",
             "software": "Software", "market": "Market"}
CARD = ["file.name", "note.quote", "note.participant", "note.review"]

root = vault_root(); tax = load_taxonomy(root); tags = taxonomy_tags(tax)
argv = sys.argv[1:]
if not argv: sys.exit(__doc__)
arg = argv[0]; project = None if arg == "--all" else arg
canvas = "--canvas" in argv
dimension = argv[argv.index("--dimension") + 1] if "--dimension" in argv else "journey"

rows = []; paths = {}
for p, fm, body in iter_notes(root, "highlight"):
    if project and fm.get("project") != project: continue
    if fm.get("review") == "rejected": continue
    rows.append(fm); paths[fm["highlight_id"]] = p
by_tag = {}; all_by_tag = {}
for fm in rows:
    for t in as_list(fm.get("tags")):
        by_tag.setdefault(t, []).append(fm)
for p, fm, body in iter_notes(root, "highlight"):          # vault-wide counts for workspace tag pages
    if fm.get("review") == "rejected": continue
    for t in as_list(fm.get("tags")):
        all_by_tag.setdefault(t, []).append(fm)

# groups: id -> (display name, description, [tag ids])  — workspace dimensions first, then project groups
groups = {}
for dim, spec in tax["dimensions"].items():
    groups[dim] = (DIM_NAMES.get(dim, dim), spec.get("description", ""),
                   [t for t in tags if t.startswith(dim + "/")])
projects = [project] if project else sorted({fm["project"] for fm in rows})
for proj in projects:
    pt = load_project_tags(root, proj)
    tags.update(project_tag_index(pt))
    for g in pt.get("groups") or []:
        name = g.get("name", g["id"]) if project else f"{g.get('name', g['id'])} ({proj})"
        groups.setdefault(g["id"], (name, "project tag group", [t["id"] for t in g.get("tags") or []]))

def q(s): return json.dumps(str(s))

def kanban(name, formula_prop, extra=()):
    o = "\n".join(f"      - {x}" for x in [*CARD, *extra])
    return (f"  - type: kanban\n    name: {q(name)}\n    filters:\n      and:\n        - note.review != \"rejected\"\n"
            f"    groupBy:\n      property: {formula_prop}\n      direction: ASC\n    order:\n{o}\n")

if canvas:
    if not project: sys.exit("--canvas needs a project id")
    if dimension not in groups: sys.exit(f"unknown dimension/group {dimension}; known: {', '.join(groups)}")
    lanes = sorted([t for t in by_tag if t.startswith(dimension + "/")], key=lambda x: -len(by_tag[x]))
    if not lanes: sys.exit(f"no {dimension}/ tags in use")
    rnd = random.Random(42); nid = lambda: "%016x" % rnd.getrandbits(64)
    CW, CH, GAP, LW, PAD, HEAD = 440, 170, 16, 480, 20, 70
    nodes = [{"id": nid(), "type": "text", "x": 0, "y": -220, "width": 1100, "height": 150,
              "text": f"# Tag board · {project} · lanes = {dimension}/*\nDrag a card into another lane (or copy it into several), then run:\n`uv run _system/scripts/canvas_sync.py {project}` to update the tags. Cards outside every lane are left untouched.\nRegenerate the board: `uv run _system/scripts/tag_board.py {project} --canvas --dimension {dimension}`"}]
    colors = ["1", "2", "3", "4", "5", "6"]
    for i, t in enumerate(lanes):
        hs = sorted(by_tag[t], key=lambda x: x["highlight_id"])
        gx = i * (LW + 40); gh = HEAD + len(hs) * (CH + GAP) + PAD
        nodes.append({"id": nid(), "type": "group", "x": gx, "y": 0, "width": LW, "height": gh,
                      "label": f"{t} ({len(hs)})", "color": colors[i % len(colors)]})
        for j, h in enumerate(hs):
            nodes.append({"id": nid(), "type": "file", "file": str(paths[h['highlight_id']].relative_to(root)),
                          "x": gx + PAD, "y": HEAD + j * (CH + GAP), "width": CW, "height": CH})
    cpath = root / "10 Projects" / project / BOARDS / "tag-board.canvas"
    cpath.parent.mkdir(parents=True, exist_ok=True)
    cpath.write_text(json.dumps({"nodes": nodes, "edges": []}, indent=1), encoding="utf-8")
    print(f"wrote {cpath.relative_to(root)}: {len(lanes)} lanes ({dimension}), {len(nodes) - len(lanes) - 1} cards")
    sys.exit()

# ---- tag notes: one note per tag (Dovetail "tag page"), board = Kanban of tag notes grouped by tag group
WS_NAMES = [DIM_NAMES.get(d, d) for d in tax["dimensions"]]
def tag_note(tag_id, d, gid, gname, level, proj):
    slug = tag_id.split("/", 1)[1]
    hs = (all_by_tag if level == "workspace" else by_tag).get(tag_id, [])
    folder = (root / "_system" / "tags" / gid) if level == "workspace" else (root / "10 Projects" / proj / DIRS["tags"] / gid)
    folder.mkdir(parents=True, exist_ok=True)
    fm = {"type": "tag", "tag": tag_id, "aliases": [tag_id], "group": gid, "group_name": gname, "level": level,
          "status": d.get("status", "active"), "definition": d.get("definition", ""),
          "highlights": len(hs), "participants": len({h["participant"] for h in hs}), "counted": str(date.today())}
    if level == "project": fm["project"] = proj
    if d.get("merged_into"): fm["merged_into"] = d["merged_into"]
    flt = [f'    - note.type == "highlight"', f'    - note.tags.contains("{tag_id}")', '    - note.review != "rejected"']
    if level == "project": flt.append(f'    - note.project == "{proj}"')
    grp = "    groupBy:\n      property: note.project\n      direction: ASC\n" if level == "workspace" else ""
    body = (f"\n# {tag_id}\n\n> {d.get('definition', '')}\n\n"
            f"Group: **{gname}** · {level} tag · status **{fm['status']}**"
            + (f" · merged into `{d['merged_into']}`" if d.get("merged_into") else "") +
            f"\nCounts refresh when `tag_board.py` runs; the list below is live.\n\n"
            "```base\nfilters:\n  and:\n" + "\n".join(flt) + "\nviews:\n  - type: table\n    name: Highlights\n" + grp +
            "    order:\n      - file.name\n      - note.participant\n      - note.review\n      - note.quote\n      - note.tags\n"
            "    sort:\n      - property: file.name\n        direction: ASC\n```\n")
    write_note(folder / f"{slug}.md", fm, body)
    return folder / f"{slug}.md"

written = set()
for dim, spec in tax["dimensions"].items():
    for t in spec.get("tags") or []:
        written.add(tag_note(t["id"], t, dim, DIM_NAMES.get(dim, dim), "workspace", None))
for proj in projects:
    pt = load_project_tags(root, proj)
    for g in pt.get("groups") or []:
        for t in g.get("tags") or []:
            written.add(tag_note(t["id"], t, g["id"], g.get("name", g["id"]), "project", proj))
# remove tag notes for tags that no longer exist (deprecated tags keep their note)
scan = [root / "_system" / "tags"] + [root / "10 Projects" / proj / DIRS["tags"] for proj in projects]
stale = [p for d in scan if d.exists() for p in d.rglob("*.md") if p not in written]
for p in stale: p.unlink()
print(f"tag notes: {len(written)} written" + (f", {len(stale)} stale removed" if stale else ""))

def tags_base(path, scope_filter, group_order):
    go = "\n".join(f"      - {q(n)}" for n in group_order)
    txt = ("# Generated by _system/scripts/tag_board.py — Dovetail-style tag board: lanes = tag groups, cards = tags.\n"
           "# Click a card to open the tag page (definition + live list of its highlights).\n"
           "filters:\n  and:\n    - note.type == \"tag\"\n    - note.status != \"deprecated\"\n" + scope_filter +
           "views:\n  - type: kanban\n    name: Tag board\n    groupBy:\n      property: note.group_name\n      direction: ASC\n"
           f"    groupOrder:\n{go}\n    order:\n      - file.name\n      - note.definition\n      - note.highlights\n      - note.participants\n      - note.status\n"
           "  - type: table\n    name: All tags\n    groupBy:\n      property: note.group_name\n      direction: ASC\n"
           "    order:\n      - note.tag\n      - note.definition\n      - note.highlights\n      - note.participants\n      - note.status\n      - note.level\n"
           "    sort:\n      - property: note.highlights\n        direction: DESC\n")
    path.write_text(txt, encoding="utf-8")

if project:
    pgroups = [g.get("name", g["id"]) for g in (load_project_tags(root, project).get("groups") or [])]
    (root / "10 Projects" / project / BOARDS).mkdir(parents=True, exist_ok=True)
    tags_base(root / "10 Projects" / project / BOARDS / "tags.base",
              "    - or:\n        - file.folder.startsWith(\"_system/tags\")\n        - file.folder.startsWith(" + q(f"10 Projects/{project}/{DIRS['tags']}") + ")\n",
              WS_NAMES + pgroups)
else:
    tags_base(root / "_system" / "bases" / "tags-all.base", "    - file.folder.startsWith(\"_system/tags\")\n", WS_NAMES)

# ---- .base (per project only; the vault-wide page uses _system/bases/highlights-all.base)
if project:
    b = ["# Generated by _system/scripts/tag_board.py — one Kanban per tag group, lanes = that group's tags.",
         "# Reads highlight notes live. Re-run the script when a tag group is added to tags.yaml.",
         "filters:", "  and:", '    - note.type == "highlight"', f"    - note.project == {q(project)}",
         "formulas:"]
    for gid in groups:
        # one tag per group per highlight is the rule; join() keeps it a single value for grouping
        b.append(f"  {gid}: 'note.tags.filter(value.startsWith(\"{gid}/\")).join(\", \")'")
    b.append("views:")
    for gid, (name, _, _) in groups.items():
        b.append(kanban(name, f"formula.{gid}", ["note.tags"]).rstrip("\n"))
    b.append(kanban("By participant", "note.participant", ["note.tags"]).rstrip("\n"))
    b.append(kanban("By review status", "note.review", ["note.tags"]).rstrip("\n"))
    b += ["  - type: table", "    name: All highlights", "    order:", "      - file.name", "      - note.participant",
          "      - note.tags", "      - note.review", "      - note.quote",
          "    sort:", "      - property: file.name", "        direction: ASC"]
    bpath = root / "10 Projects" / project / BOARDS / "tag-board.base"
    bpath.write_text("\n".join(b) + "\n", encoding="utf-8")
    base_ref = f"10 Projects/{project}/{BOARDS}/tag-board.base"
else:
    base_ref = "_system/bases/highlights-all.base"

# ---- .md page of live embeds
out = [f"# Tag board{'' if project else ' (all projects)'}", "",
       "Every board reads the highlight notes live. "
       f"Structure generated {date.today()} by `uv run _system/scripts/tag_board.py {arg}`; re-run when a tag group is added.", "",
       "## Tag board",
       "Lanes are tag groups, cards are tags (with definition and counts). Click a tag to open its page with the live list of its highlights. Native Bases, no plugin.",
       f"![[{f'10 Projects/{project}/{BOARDS}/tags.base' if project else '_system/bases/tags-all.base'}#Tag board]]", "",
       "## Highlights · one board per group", "Lanes are the group's tags. Native Bases, no plugin needed. To re-tag by dragging, use the canvas. Expand a group:", ""]
for gid, (name, desc, gtags) in groups.items():
    if not project and gid not in WORKSPACE_DIMS: continue   # vault-wide page: workspace dimensions only
    out += [f"> [!abstract]- {name}" + (f" · {desc}" if desc and desc != "project tag group" else ""),
            f"> ![[{base_ref}#{name}]]", ">"]
    for t in gtags:
        d = tags.get(t, {}); st = d.get("status", "active")
        out.append(f"> - `{t}` {'· **' + st + '** ' if st != 'active' else ''}· {d.get('definition', '')}")
    out.append("")
if project:
    out += ["## Other views", f"![[{base_ref}#By participant]]", "", f"![[{base_ref}#By review status]]", "",
            f"[[10 Projects/{project}/{BOARDS}/tag-board.canvas|tag-board.canvas]] · drag cards between lanes, then `uv run _system/scripts/canvas_sync.py {project}`.", ""]
fm = {"type": "overview", "project": project or "all", "generated": str(date.today())}
target = (root / "10 Projects" / project / f"{PAGES['tagboard']}.md") if project else (root / "_system" / "tag-board.md")
write_note(target, fm, "\n" + "\n".join(out) + "\n")
print(f"wrote {target.relative_to(root)}" + (f" and {bpath.relative_to(root)}" if project else "") +
      f": {len([g for g in groups if project or g in WORKSPACE_DIMS])} groups, {len(by_tag)} tags in use, {len(rows)} highlights")
