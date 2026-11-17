#!/usr/bin/env python3
"""new_project.py <slug> --title "YYYY-MM Phase - Topic" [--phase discovery] [--owner P-000] [--domain product-tools/rf-studio]
                 [--year 2026] [--rally-study X]
Creates 10 Projects/YYYY_slug/ with 01 project.md (Study Overview), 02 insights review.md, 03 tag board.md, a_setup/, b_sources/, c_highlights/, d_tags/tags.yaml, e_insights/, f_deliverables/, setup/, reference/, sources/, highlights/, insights/, deliverables/."""
import argparse, json, sys, subprocess
from datetime import date
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from vaultlib import vault_root, DIRS, BOARDS, REFERENCE, PAGES

ap = argparse.ArgumentParser()
ap.add_argument("slug"); ap.add_argument("--title", required=True)
ap.add_argument("--phase", default="discovery", choices=["discovery","evaluation","validation","workshop","survey","benchmarking"])
ap.add_argument("--owner", default="P-000"); ap.add_argument("--domain", default="")
ap.add_argument("--year", default=str(date.today().year)); ap.add_argument("--rally-study", default="")
a = ap.parse_args()
root = vault_root(); pid = f"{a.year}_{a.slug}"; d = root / "10 Projects" / pid
if d.exists(): sys.exit(f"exists: {d}")
for sub in (*DIRS.values(), BOARDS, REFERENCE):
    (d / sub).mkdir(parents=True, exist_ok=True)
tpl = (root / "_system/templates/project.md").read_text(encoding="utf-8")
out = (tpl.replace("{{project_id}}", pid).replace("{{title}}", a.title.replace('"', "'")).replace("{{phase}}", a.phase)
          .replace("{{owner}}", a.owner).replace("{{domain}}", a.domain or "unassigned").replace("{{rally_study}}", a.rally_study))
(d / f"{PAGES['project']}.md").write_text(out, encoding="utf-8")
for tname, fname in (("insights-review", PAGES["review"]),):
    (d / f"{fname}.md").write_text((root / f"_system/templates/{tname}.md").read_text(encoding="utf-8").replace("{{project_id}}", pid), encoding="utf-8")
(d / DIRS["tags"] / "tags.yaml").write_text((root / "_system/templates/project-tags.yaml").read_text(encoding="utf-8").replace("{{project_id}}", pid), encoding="utf-8")
(d / DIRS["setup"] / "SETUP Research Brief.md").write_text("---\ntype: setup\ndoc: research-brief\n---\n\n# SETUP: Research Brief\n\n## Objective\n\n## Research questions\n\n## Hypotheses\n\n## Scope and constraints\n", encoding="utf-8")
(d / DIRS["setup"] / "SETUP Discussion Guide.md").write_text("---\ntype: setup\ndoc: discussion-guide\n---\n\n# SETUP: Discussion Guide\n\n## Warm-up\n\n## Core questions\n\n## Stimulus\n\n## Wrap-up\n", encoding="utf-8")
subprocess.run([sys.executable, str(Path(__file__).parent / "tag_board.py"), pid], check=True)
print(f"created 10 Projects/{pid}/ (01 project.md, 02 insights review.md, 03 tag board.md, a_setup/ with boards/, b_sources/ with reference/, c_highlights/, d_tags/tags.yaml, e_insights/, f_deliverables/)")
