#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = ["pyyaml"]
# ///
"""Participant cards from a Rally export.

  participants.py sync [<rally export .json>]      default: _raw/rally/participants.json
  participants.py check                             every source participant has a card, every card a persona

A participant is split in two, like a recording:
  20 Participants/P-###.md              public card: role, experience, market, industry, region, consent state,
                                        persona, studies. No name, employer or contact. In git.
  _raw/participants/P-### identity.md   name, employer, email: local only (the SharePoint/OneDrive key in
                                        production). The public card embeds it, so people with the key see the
                                        identity inline and everyone else sees a missing-file placeholder.

`persona` on an existing card is kept across syncs; everything else is rewritten from Rally.
The Rally export is read by this script only; never open it in Claude (names)."""
from __future__ import annotations

import csv, json, sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from vaultlib import iter_notes, read_note, vault_root, write_note, as_list  # noqa: E402

PUBLIC_DIR, KEY_DIR = "20 Participants", "_raw/participants"


def band(years) -> str:
    y = int(years or 0)
    return "0-2 years" if y <= 2 else "3-5 years" if y <= 5 else "6-10 years" if y <= 10 else "10+ years"


def sources_by_participant(root: Path) -> dict:
    out = {}
    for p, fm, _ in iter_notes(root, "source"):
        out.setdefault(fm.get("participant"), []).append((fm.get("project"), fm.get("source_id"), str(fm.get("date", ""))))
    return out


def card_body(pid: str, r: dict, studies: list) -> str:
    srcs = "\n".join(f"- [[{sid}]] · {proj} · {d}" for proj, sid, d in studies) or "- none yet"
    return f"""
# {pid} · {r['role']}

![[_raw/participants/{pid} identity]]

**{r.get('seniority', '')} {r['role'].lower()}**, {band(r.get('years_experience'))} in the role, {r.get('participant_type')} · {r.get('region', '')}{(' (' + r['country'] + ')') if r.get('country') else ''}.
Market `{r.get('market', '')}` · industry: {r.get('industry', '')}.

## Persona
Set `persona` in the properties to a note in `30 Personas/`. If no persona fits this person, create a new one (`status: proposed`) rather than forcing a match.

## Sessions
{srcs}

## Highlights

```base
filters:
  and:
    - note.type == "highlight"
    - note.participant == "{pid}"
    - note.review != "rejected"
views:
  - type: table
    name: Highlights
    groupBy:
      property: note.project
      direction: ASC
    order:
      - file.name
      - note.review
      - note.quote
      - note.tags
    sort:
      - property: file.name
        direction: ASC
```
"""


def cmd_sync(root: Path, export: Path):
    data = json.loads(export.read_text(encoding="utf-8"))
    rows = data["participants"] if isinstance(data, dict) else data
    pub, key = root / PUBLIC_DIR, root / KEY_DIR
    pub.mkdir(exist_ok=True); key.mkdir(parents=True, exist_ok=True)
    by_part = sources_by_participant(root)
    keyrows = []
    for r in rows:
        pid = r["participant_id"]
        studies = sorted(by_part.get(pid, []), key=lambda t: t[2])
        existing = pub / f"{pid}.md"
        persona = read_note(existing)[0].get("persona", "") if existing.exists() else ""
        c = r.get("consent") or {}
        fm = {
            "type": "participant", "participant_id": pid, "aliases": [pid],
            "participant_type": r.get("participant_type", ""), "role": r.get("role", ""), "seniority": r.get("seniority", ""),
            "experience": band(r.get("years_experience")), "years_experience": r.get("years_experience"),
            "market": r.get("market", ""), "industry": r.get("industry", ""), "region": r.get("region", ""), "country": r.get("country", ""),
            "company_size": r.get("company_size", ""), "tools": as_list(r.get("tools")),
            "persona": persona,
            "rally_id": r.get("rally_id", ""), "consent_status": c.get("status", ""), "consent_recording": bool(c.get("recording")),
            "consent_quotes": bool(c.get("quotes")), "consent_video_clips": bool(c.get("video_clips")), "retention_until": c.get("retention_until", ""),
            "projects": sorted({s[0] for s in studies}), "sources": [s[1] for s in studies],
            "rally_synced": str(date.today()),
        }
        write_note(existing, fm, card_body(pid, r, studies))
        write_note(key / f"{pid} identity.md", {"type": "identity", "participant_id": pid, "rally_id": r.get("rally_id", "")},
                   f"\n> [!danger] Identity · local key, never in git\n> **{r.get('name', '')}** · {r.get('company', '')} · {r.get('email', '')}\n> Rally `{r.get('rally_id', '')}` · consent {c.get('status', '')} {c.get('date', '')} · retention until {c.get('retention_until', '')}\n")
        keyrows.append([pid, r.get("name", ""), r.get("company", ""), r.get("role", ""), r.get("rally_id", ""), ";".join(fm["projects"])])
    with (root / "_raw" / "participants.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f); w.writerow(["id", "name", "company", "role", "rally_id", "projects"]); w.writerows(keyrows)
    print(f"synced {len(rows)} participant(s): cards in {PUBLIC_DIR}/, identities and participants.csv in _raw/ (local only)")
    missing = [pid for pid in by_part if pid and pid != "P-000" and not (pub / f"{pid}.md").exists()]
    if missing:
        print("sources cite participants with no card: " + ", ".join(sorted(missing)))


def cmd_check(root: Path):
    pub = root / PUBLIC_DIR
    bad = 0
    for pid in sorted(p for p in sources_by_participant(root) if p and p != "P-000"):
        card = pub / f"{pid}.md"
        if not card.exists():
            print(f"{pid}: no participant card (run participants.py sync)"); bad += 1; continue
        fm, _ = read_note(card)
        if not fm.get("persona"):
            print(f"{pid}: no persona assigned"); bad += 1
        elif not any(p.stem == str(fm["persona"]).strip("[]").split("|")[0].split("/")[-1] for p in (root / "30 Personas").glob("*.md")):
            print(f"{pid}: persona {fm['persona']} not found in 30 Personas/"); bad += 1
    print("ok" if not bad else f"{bad} problem(s)")
    sys.exit(1 if bad else 0)


def main():
    root = vault_root(Path(__file__).resolve().parent)
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    if cmd == "sync":
        cmd_sync(root, Path(sys.argv[2]) if len(sys.argv) > 2 else root / "_raw" / "rally" / "participants.json")
    elif cmd == "check":
        cmd_check(root)
    else:
        sys.exit(__doc__)


if __name__ == "__main__":
    main()
