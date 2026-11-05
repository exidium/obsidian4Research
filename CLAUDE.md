# Vault conventions for Claude

This folder is an Obsidian vault and a research repository. Read `_system/schema.md` before creating or editing any note. Use the three skills in `.claude/skills/` for research work; don't improvise the pipeline.

## Hard rules

1. **Never modify transcript text or block IDs** in a source note after `status: ingested`. Fix mistakes by re-ingesting under a new source ID and archiving the old one.
2. **Never write a participant's name, employer, or email** into any file outside `_raw/`. Use `P-###`. If you see a name in a transcript, replace it with the participant ID or `[company]` during ingest.
3. **Never read `_raw/participants.csv` into context.** Scripts match names from it and report line numbers; you act on the report.
4. **Tags come only from `_system/taxonomy.yaml`.** Tags with `status: active` may be applied freely. If a needed tag doesn't exist, add it with `status: proposed` and an `evidence` list, then apply it. Never silently invent a tag string.
5. **Insights cite highlights, not transcripts.** Synthesis reads `highlights/` only. If you need more context for a highlight, open its single linked block, not the whole source.
6. **Append to `_system/provenance.log`** after every ingest, highlight run, synthesis, or publish, one line:
   `ISO-date<TAB>skill<TAB>action<TAB>target-id<TAB>model`.
7. **Frontmatter properties, not inline hashtags.** All queryable metadata goes in frontmatter so Bases can read it.
8. **One source per highlight run. One project per synthesis run.** Don't batch across projects.

## IDs

- Participant `P-001`, source `S-0001`, highlight `H-S0001-0003` (source + sequence), insight `I-<project>-01`, project folder `YYYY_slug`.
- Block IDs inside a source: `^s0001-0012` (lowercase source id + 4-digit paragraph number).
- Next free IDs: `python3 _system/scripts/next_id.py participant|source|highlight <S-id>|insight <project>`.

## Where things go

- New study: `research-organize` → `new project`. Creates `10 Projects/YYYY_slug/{project.md,sources,highlights,insights}`.
- Drop files in `00 Inbox/`. Ingest moves media to `_raw/<project>/` and writes `sources/S-####.md`.
- Highlights go in `highlights/H-S####-####.md`, insights in `insights/I-<project>-##.md`.
- Vault-wide views are `.base` files in `_system/bases/`; embed them in project notes.

## Model note

This vault is used under an ADI Claude Enterprise account. The demo project (`2026_demo-fluxbench`) is entirely fictional and safe for a public or personal repo. Real projects go to ADI's GitHub only.
