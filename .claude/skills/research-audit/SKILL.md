---
name: research-audit
description: One health run for the vault: structural audit, PII scan, recording checksums, participant cards and personas, with a dated report in _system/reports/. Use when the user says "audit the vault", "health check", "is everything consistent", "run the checks", "before I commit", "before the demo", or before any publish or close-study step. Read-only; reports, never fixes on its own.
---

# research-audit

Five checks already exist as scripts; this skill runs them together, writes one report, and turns the findings into a to-do list for the right skill. It never edits notes: fixing is `research-organize` (structure and tags), `research-highlight` (quotes and review state), `research-participants` and `research-persona` (people), `research-clip` (media).

## Procedure

1. `uv run _system/scripts/health.py` runs, in order:
   - `audit.py`: IDs, block IDs, verbatim quotes, tags against the taxonomies, evidence links by file name, evidence levels, highlight counts per hour, recognised note types.
   - `scan_pii.py`: names and companies from the key, emails, phone numbers, anywhere outside `_raw/`.
   - `media.py check`: every linked recording present (or absent on this machine) and unchanged.
   - `participants.py check`: every source participant has a card, every card a persona.
   - `personas.py check`: every persona has participants, every card's persona exists.
   It writes `_system/reports/health-YYYY-MM-DD.md` and prints a summary; exit code 1 when anything is an error.
2. Read the report. For each finding, name the skill that fixes it and whether it blocks: PII and bad quotes block a commit and a publish; a missing persona blocks the study close; a missing recording on this machine blocks nothing.
3. Tell the user: errors, warnings worth acting on, what is noise, and the one command to run next. Don't fix anything unless asked; then hand over to the skill that owns the fix.
4. `bash _system/scripts/provenance.sh research-audit health all $MODEL`.

## When to insist on it

- Before `git commit` (the pre-commit hook only blocks `_raw/`; it does not run the audit).
- Before `research-publish` or `research-report`.
- Before `research-organize` → close the study.
- After `research-ingest` on a real source, with the PII finding list in hand.

## Reading the numbers

- Highlights per hour: 15 to 30 for an hour-long interview. Fewer means under-highlighting, more means filler; both are a `research-highlight` conversation, not an error.
- `journey/` marked UNVERIFIED is a standing note until the taxonomy is confirmed against the Dovetail board; not a defect in a study.
- A changed recording checksum means someone replaced the file; stop cutting clips until it is explained.
