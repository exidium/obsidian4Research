"""Shared helpers for the research vault scripts. Stdlib + PyYAML only."""
from __future__ import annotations
import os, re, sys, json
from datetime import date
from pathlib import Path
import yaml

NOTE_DIRS = ["10 Projects", "90 Archive"]
FM_RE = re.compile(r"\A---\n(.*?)\n---\n?", re.S)
BLOCK_RE = re.compile(r"\^(s\d{4}-\d{4})\s*$", re.M)


def vault_root(start: Path | None = None) -> Path:
    p = (start or Path.cwd()).resolve()
    for cand in [p, *p.parents]:
        if (cand / "_system" / "taxonomy.yaml").exists():
            return cand
    sys.exit("vault root not found (no _system/taxonomy.yaml above cwd)")


def read_note(path: Path):
    text = path.read_text(encoding="utf-8")
    m = FM_RE.match(text)
    if not m:
        return {}, text
    try:
        fm = yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError as e:
        sys.exit(f"bad frontmatter in {path}: {e}")
    return fm, text[m.end():]


class _Dumper(yaml.SafeDumper):
    """Block-style mappings, inline lists, unquoted ISO dates: what Obsidian expects."""


def _seq(dumper, data):
    return dumper.represent_sequence("tag:yaml.org,2002:seq", data, flow_style=True)


_Dumper.add_representer(list, _seq)
_DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def _coerce(v):
    if isinstance(v, str) and _DATE.match(v):
        return date.fromisoformat(v)
    if isinstance(v, list):
        return [_coerce(x) for x in v]
    return v


def dump_fm(fm: dict) -> str:
    return yaml.dump({k: _coerce(v) for k, v in fm.items()}, Dumper=_Dumper, sort_keys=False,
                     default_flow_style=False, allow_unicode=True, width=1000).rstrip("\n")


def write_note(path: Path, fm: dict, body: str):
    path.write_text(f"---\n{dump_fm(fm)}\n---\n{body}", encoding="utf-8")


def iter_notes(root: Path, note_type: str | None = None):
    for d in NOTE_DIRS:
        base = root / d
        if not base.exists():
            continue
        for p in sorted(base.rglob("*.md")):
            fm, body = read_note(p)
            if note_type and fm.get("type") != note_type:
                continue
            yield p, fm, body


def load_taxonomy(root: Path):
    return yaml.safe_load((root / "_system" / "taxonomy.yaml").read_text(encoding="utf-8"))


def save_taxonomy(root: Path, tax: dict):
    (root / "_system" / "taxonomy.yaml").write_text(
        yaml.dump(tax, Dumper=_Dumper, sort_keys=False, default_flow_style=False, allow_unicode=True, width=1000), encoding="utf-8")


def taxonomy_tags(tax: dict) -> dict:
    """tag id -> tag dict (with 'dimension' added)."""
    out = {}
    for dim, spec in (tax.get("dimensions") or {}).items():
        for t in spec.get("tags") or []:
            out[t["id"]] = {**t, "dimension": dim}
    return out


def blocks_in(body: str) -> dict:
    """block id -> paragraph text (without the id)."""
    out = {}
    for para in re.split(r"\n\s*\n", body):
        m = BLOCK_RE.search(para)
        if m:
            out[m.group(1)] = BLOCK_RE.sub("", para).strip()
    return out


def norm(s: str) -> str:
    return re.sub(r"\s+", " ", (s or "")).strip().lower()


def as_list(v):
    if v is None:
        return []
    return v if isinstance(v, list) else [v]


def wikilink_target(v: str) -> str:
    m = re.match(r"\[\[([^\]|#]+)", str(v or ""))
    return m.group(1).strip() if m else str(v or "").strip()
