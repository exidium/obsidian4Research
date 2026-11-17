#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = ["pyyaml"]
# ///
"""One health run: audit, PII scan, recordings, participants, personas. Writes _system/reports/health-YYYY-MM-DD.md.
  health.py [project]      exit 1 when any check reports an error"""
from __future__ import annotations

import re, subprocess, sys
from datetime import date
from pathlib import Path

here = Path(__file__).resolve().parent
sys.path.insert(0, str(here))
from vaultlib import vault_root  # noqa: E402

root = vault_root(here)
project = sys.argv[1] if len(sys.argv) > 1 else ""
PY = [sys.executable]
checks = [
    ("Structure and evidence (audit.py)", PY + [str(here / "audit.py")]),
    ("PII outside _raw (scan_pii.py)", PY + [str(here / "scan_pii.py")]),
    ("Recordings (media.py check)", ["uv", "run", "-q", str(here / "media.py"), "check"] + ([project] if project else [])),
    ("Participant cards (participants.py check)", ["uv", "run", "-q", str(here / "participants.py"), "check"]),
    ("Personas (personas.py check)", ["uv", "run", "-q", str(here / "personas.py"), "check"]),
]
out, failed = [f"# Vault health {date.today()}", ""], 0
for title, cmd in checks:
    p = subprocess.run(cmd, cwd=root, capture_output=True, text=True)
    text = (p.stdout + p.stderr).strip()
    if title.startswith("Structure"):
        m = re.search(r"Errors (\d+) · Warnings (\d+)", text)
        errs, warns = (int(m.group(1)), int(m.group(2))) if m else (p.returncode, 0)
        status = "FAIL" if errs else "ok"
        body = "\n".join(l for l in text.splitlines() if l.startswith("- ") or l.startswith("Errors"))
    elif title.startswith("PII"):
        n = int(re.search(r"scan_pii: (\d+) finding", text).group(1)) if "scan_pii:" in text else p.returncode
        status = "FAIL" if n else "ok"; errs = n; body = text
    else:
        status = "FAIL" if p.returncode else "ok"; errs = p.returncode; body = text
    failed += 1 if status == "FAIL" else 0
    out += [f"## {title}: {status}", "", "```", body or "(no output)", "```", ""]
    print(f"{status:4} {title}")
rep = root / "_system" / "reports"; rep.mkdir(exist_ok=True)
f = rep / f"health-{date.today()}.md"
f.write_text("\n".join(out), encoding="utf-8")
print(f"report: {f.relative_to(root)} · {failed} failing check(s)")
sys.exit(1 if failed else 0)
