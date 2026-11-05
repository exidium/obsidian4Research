#!/usr/bin/env python3
"""new_project.py <slug> --title "..." [--owner P-000] [--year 2026] [--rally-study X]"""
import argparse, json, sys
from datetime import date
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from vaultlib import vault_root

ap = argparse.ArgumentParser()
ap.add_argument("slug"); ap.add_argument("--title", required=True)
ap.add_argument("--owner", default="P-000"); ap.add_argument("--year", default=str(date.today().year))
ap.add_argument("--rally-study", default="")
a = ap.parse_args()
root = vault_root()
pid = f"{a.year}_{a.slug}"
d = root / "10 Projects" / pid
if d.exists():
    sys.exit(f"exists: {d}")
for sub in ("sources", "highlights", "insights"):
    (d / sub).mkdir(parents=True)
tpl = (root / "_system/templates/project.md").read_text(encoding="utf-8")
out = tpl.replace("{{project_id}}", pid).replace("title: {{title}}", "title: " + json.dumps(a.title)).replace("{{title}}", a.title).replace("{{owner}}", a.owner).replace("{{date}}", str(date.today()))
out = out.replace('rally_study: ""', f'rally_study: "{a.rally_study}"')
(d / "project.md").write_text(out, encoding="utf-8")
print(f"created 10 Projects/{pid}/ (project.md, sources/, highlights/, insights/)")
