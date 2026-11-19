#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = ["pyyaml"]
# ///
"""Vault integrity audit. Prints a Markdown report; --write saves it to _system/reports/.
Exit 1 when errors exist (warnings alone exit 0)."""
import re, sys, subprocess
from datetime import date
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from vaultlib import vault_root, iter_notes, load_taxonomy, taxonomy_tags, blocks_in, norm, as_list, wikilink_target, load_project_tags, project_tag_index, id_from_name, WORKSPACE_DIMS, PAGES

root = vault_root(); tax = load_taxonomy(root); wtags = taxonomy_tags(tax); ptags_cache = {}

def tags_for(project):
    if project not in ptags_cache:
        try:
            pt = load_project_tags(root, project)
        except SystemExit:
            pt = {'groups': []}
        idx = project_tag_index(pt)
        for gid in {g['id'] for g in pt.get('groups') or []}:
            if gid in WORKSPACE_DIMS: E(f"{project}/tags.yaml: group id `{gid}` collides with a workspace dimension")
        ptags_cache[project] = {**wtags, **idx}
    return ptags_cache[project]
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
    elif t in ("overview", "hub", "review", "participant", "persona", "setup", "reference", "stimulus", "deliverable", "synthesis", "tag"): pass
    elif p.name != f"{PAGES['project']}.md": W(f"{rel}: no recognised `type`")

for pid, (rel, fm, _) in projects.items():
    if pid != Path(rel).parent.name: E(f"{rel}: project_id `{pid}` ≠ folder name")

used_tags = {}
for sid, (rel, fm, body) in sources.items():
    if not re.match(r"S-\d{4}$", str(sid)): E(f"{rel}: bad source_id {sid}")
    if fm.get("ris_status") not in ("raw", "in-progress", "review", "published", "excluded", "archived"): E(f"{rel}: bad ris_status {fm.get('ris_status')}")
    for k in ("entry_type", "methodology", "participant_type"):
        if not fm.get(k): W(f"{rel}: missing field {k}")
    if fm.get("participant_type") == "external-customer" and not fm.get("rally_id"): W(f"{rel}: external participant without rally_id (consent link)")
    if not fm.get("redacted"): W(f"{rel}: redacted is false; run scan_pii and set redacted: true")
    if not re.match(r"P-\d{3}$", str(fm.get("participant"))): E(f"{rel}: bad participant {fm.get('participant')}")
    blocks = blocks_in(body)
    sid_l = str(sid).replace("-", "").lower()
    expected = [f"{sid_l}-{i:04d}" for i in range(1, len(blocks) + 1)]
    if list(blocks) != expected: E(f"{rel}: block IDs not sequential/consistent with source_id")
    if not blocks: E(f"{rel}: no transcript blocks")
    if fm.get("project") not in projects: E(f"{rel}: project {fm.get('project')} has no 01 project.md")

hl_by_source = {}
for hid, (rel, fm, body) in highlights.items():
    sid = wikilink_target(fm.get("source"))
    hl_by_source.setdefault(sid, []).append(hid)
    tags = tags_for(fm.get("project"))
    if id_from_name(Path(rel).stem) != hid: E(f"{rel}: file name must start with {hid}")
    if hid not in as_list(fm.get("aliases")): E(f"{rel}: aliases must include {hid} (search)")
    if not fm.get("title"): W(f"{rel}: no title (stranger test: a reader should know what this is from the name)")
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
    if not any(t.split("/")[0] in WORKSPACE_DIMS for t in tl): E(f"{rel}: no workspace tag (every highlight needs at least one)")
    if len({t.split("/")[0] for t in tl}) < 2: W(f"{rel}: single-dimension tagging; combine e.g. insight + functionality + journey")
    if not any(t.split("/")[0] not in WORKSPACE_DIMS for t in tl): W(f"{rel}: no project tag (domain precision)")
    for t in tl:
        used_tags[t] = used_tags.get(t, 0) + 1
        if t not in tags: E(f"{rel}: tag `{t}` not in workspace taxonomy or project tags.yaml")
        elif tags[t].get("status") == "deprecated": E(f"{rel}: tag `{t}` is deprecated → {tags[t].get('merged_into')}")
    if "**Rationale:**" not in body: W(f"{rel}: missing 'Rationale' line")
    if len(str(fm.get("quote", "")).split()) < 8: W(f"{rel}: quote under 8 words; stranger test likely fails")

for sid, (rel, fm, _) in sources.items():
    n = len(hl_by_source.get(sid, []))
    if fm.get("ris_status") == "raw" and n: W(f"{rel}: has {n} highlights but ris_status is still raw")
    if fm.get("ris_status") in ("review", "published") and not n: W(f"{rel}: ris_status {fm.get('ris_status')} but no highlights")
    dur = fm.get("duration_min") or 0
    if n and dur >= 25:
        lo, hi = (8, 15) if dur < 45 else (15, 30) if dur < 75 else (25, 40)
        if n < lo: W(f"{rel}: {n} highlights for {dur} min; expected {lo}-{hi} (under-highlighting?)")
        if n > hi: W(f"{rel}: {n} highlights for {dur} min; expected {lo}-{hi} (over-highlighting?)")

for iid, (rel, fm, body) in insights.items():
    hls = [id_from_name(wikilink_target(h)) for h in as_list(fm.get("highlights"))]
    for h in as_list(fm.get("highlights")):
        if " " not in wikilink_target(h): E(f"{rel}: `{h}` links a bare ID; link the file name with the ID as display text ([[<file name>|{wikilink_target(h)}]])")
    for m in re.finditer(r"!?\[\[(H-S\d{4}-\d{4}|I-[\w-]+-\d{2})(\]\]|\|)", body): E(f"{rel}: bare ID link {m.group(0)} does not resolve; use the file name")
    if len(hls) < 1: E(f"{rel}: no highlights cited")
    parts = set()
    for h in hls:
        if h not in highlights: E(f"{rel}: cites missing highlight {h}"); continue
        parts.add(highlights[h][1].get("participant"))
        if highlights[h][1].get("review") == "rejected": E(f"{rel}: cites rejected highlight {h}")
        if not re.search(rf"!\[\[{re.escape(h)}( [^\]|#]*)?\]\]", body): W(f"{rel}: {h} listed but not embedded in Evidence")
    declared = set(as_list(fm.get("participants")))
    if declared != parts: W(f"{rel}: participants {sorted(declared)} ≠ evidence participants {sorted(parts)}")
    exp = "insufficient" if len(parts) <= 1 else "emerging" if len(parts) <= 3 else "strong"
    if fm.get("evidence_level") != exp: W(f"{rel}: evidence_level {fm.get('evidence_level')} but evidence supports {exp} ({len(parts)} participants)")
    if exp == "insufficient": W(f"{rel}: single-participant evidence; ADI guidance is not to write an insight doc yet")
    if id_from_name(Path(rel).stem) != iid: E(f"{rel}: file name must start with {iid}")
    if iid not in as_list(fm.get("aliases")): E(f"{rel}: aliases must include {iid}")
    for sec in ("## Finding", "## Evidence", "## Recommendations"):
        if sec not in body: W(f"{rel}: missing section {sec}")
    if fm.get("status") not in ("draft", "reviewed", "published"): E(f"{rel}: bad status")
    if fm.get("status") == "published" and not fm.get("published_to"): E(f"{rel}: published without published_to")
    for t in as_list(fm.get("tags")):
        if t not in tags_for(fm.get("project")): E(f"{rel}: tag `{t}` not in taxonomy")

for proj, tags in ptags_cache.items():
    proposed = [t for t, d in tags.items() if d.get("status") == "proposed"]
    nodef = [t for t, d in tags.items() if d.get("level") == "project" and (not d.get("definition") or d["definition"].startswith("TODO"))]
    if proposed: I(f"{proj}: proposed project tags awaiting a decision: " + ", ".join(proposed))
    if nodef: W(f"{proj}: project tags without a real definition: " + ", ".join(nodef))
if "journey" in tax["dimensions"] and "UNVERIFIED" in tax["dimensions"]["journey"].get("description", ""):
    I("journey/ stage list is marked UNVERIFIED; confirm against the *Journey Stage board in Dovetail")

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
