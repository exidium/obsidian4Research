#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = ["pyyaml"]
# ///
"""new_domain.py <slug> --title "RF Studio"   -> 00 Synthesis/<slug>/ with Landscape, What We Know, Open Questions, Study Index."""
import argparse, sys
from datetime import date
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from vaultlib import vault_root
ap = argparse.ArgumentParser(); ap.add_argument("slug"); ap.add_argument("--title", required=True)
a = ap.parse_args(); root = vault_root(); d = root / "00 Synthesis" / a.slug
if d.exists(): sys.exit(f"exists: {d}")
d.mkdir(parents=True)
tpl = (root / "_system/templates/synthesis.md").read_text(encoding="utf-8")
docs = {"Landscape": "What this domain covers; context for anyone new.",
        "What We Know": "Synthesised findings across all studies in this domain. Updated at the close of every study.",
        "Open Questions": "What we have not answered yet; inputs for future study planning.",
        "Study Index": "| Project | Phase | Status | Dates | Owner |\n|---|---|---|---|---|"}
for name, body in docs.items():
    (d / f"{name}.md").write_text(tpl.replace("{{domain}}", a.slug).replace("{{doc}}", name.lower().replace(" ", "-"))
                                   .replace("{{date}}", str(date.today())).replace("{{title}}", f"{a.title}: {name}") + f"\n{body}\n", encoding="utf-8")
print(f"created 00 Synthesis/{a.slug}/ ({', '.join(docs)})")
