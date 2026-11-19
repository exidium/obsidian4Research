#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = ["pyyaml"]
# ///
"""Scan text files for identity leaks. Prints path:line<TAB>kind only, never the matched text.
  scan_pii.py [files...]      default: all .md/.txt/.yaml/.json/.base under the vault, excluding _raw
  scan_pii.py --staged        files staged in git (handles spaces in paths)
Exit 1 if anything is found. Names and companies come from _raw/participants.csv (if present)."""
import csv, re, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from vaultlib import vault_root

root = vault_root()
EMAIL = re.compile(r"[\w.+-]+@[\w-]+\.[\w.-]+")
PHONE = re.compile(r"(?<![\d:])\+?\d[\d .()-]{8,}\d(?![\d:])")
HEX_ID = re.compile(r"\"id\":\s*\"[0-9a-f]{16}\"")   # canvas node ids: 16 hex chars, digit-only ones look like phone numbers
ISO_DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
names = []
GENERIC = {"semiconductor", "robotics", "medical", "systems", "technologies", "industries", "solutions", "electronics",
           "devices", "group", "corporation", "company", "limited", "research", "researcher", "demo", "engineering", "labs"}
key = root / "_raw" / "participants.csv"
if key.exists():
    for row in csv.DictReader(key.open(encoding="utf-8")):
        name = (row.get("name") or "").strip()
        if name:
            names.append(name)                                   # full name
            names += [t for t in re.split(r"\s+", name) if len(t) >= 4 and t.lower() not in GENERIC]  # name tokens
        comp = (row.get("company") or "").strip()
        if comp:
            names.append(comp)                                   # whole company phrase only
name_re = re.compile(r"\b(" + "|".join(re.escape(n) for n in sorted(set(names), key=len, reverse=True)) + r")\b", re.I) if names else None

import subprocess
args = sys.argv[1:]
if args == ["--staged"]:
    out = subprocess.run(["git", "diff", "--cached", "--name-only", "--diff-filter=ACM", "-z"], capture_output=True, text=True, cwd=root).stdout
    args = [str(root / f) for f in out.split("\0") if f]
files = [Path(f) for f in args] or [p for p in root.rglob("*") if p.suffix in (".md", ".txt", ".yaml", ".yml", ".json", ".base", ".csv")]
hits = 0
for f in files:
    if not f.exists() or "_raw" in f.parts or ".git" in f.parts or ".obsidian" in f.parts:
        continue
    try:
        text = f.read_text(encoding="utf-8")
    except (UnicodeDecodeError, IsADirectoryError):
        continue
    for n, line in enumerate(text.splitlines(), 1):
        kinds = []
        if EMAIL.search(line) and "noreply@" not in line: kinds.append("email")
        for m in PHONE.finditer(line):
            if HEX_ID.search(line): break
            digits = re.sub(r"\D", "", m.group())
            if len(digits) >= 9 and not ISO_DATE.match(m.group().strip()): kinds.append("phone"); break
        if name_re and name_re.search(line): kinds.append("participant-name")
        for k in kinds:
            print(f"{f}:{n}\t{k}"); hits += 1
print(f"scan_pii: {hits} finding(s) in {len(files)} file(s)" + ("" if names else " (no participants.csv, name check skipped)"))
sys.exit(1 if hits else 0)
