# Vault conventions for Claude

This folder is an Obsidian vault and a research repository. Read `_system/schema.md` before creating or editing any note. Use the skills in `.claude/skills/` for research work; don't improvise the pipeline. Ingest (`research-ingest`), highlight (`research-highlight`), synthesize (`research-synthesize`), report (`research-report`), publish (`research-publish`), clip (`research-clip`), participants and personas (`research-participants`, `research-persona`), questions from stakeholders (`research-ask`), structure and taxonomy (`research-organize`), health (`research-audit`).

## Hard rules

1. **Never modify transcript text or block IDs** in a source note after `ris_status` leaves `raw`. Fix mistakes by re-ingesting under a new source ID and archiving the old one.
2. **Never write a participant's name, employer, or email** into any file outside `_raw/`. Use `P-###`. If you see a name in a transcript, replace it with the participant ID or `[company]` during ingest.
3. **Never read `_raw/participants.csv` into context.** Scripts match names from it and report line numbers; you act on the report.
4. **Two tag levels, like Dovetail.** Workspace tags live in `_system/taxonomy.yaml` (experience, functionality, insight, sentiment, ops, journey, software, market) and are admin-controlled: never add, rename, or deprecate them. Project tags live in each project's `d_tags/tags.yaml` in numbered groups with definitions. Priority: existing workspace tag, then existing project tag, then leave untagged, then propose a project tag (`status: proposed`, with evidence) for the researcher to decide. Every highlight carries at least one workspace tag. Never invent a tag string.
5. **Insights cite highlights, not transcripts.** Synthesis reads `c_highlights/` only. If you need more context for a highlight, open its single linked block, not the whole source.
6. **Tagging is automatic; the review is the gate.** `research-highlight` writes highlights straight from the transcript as `review: proposed` with a `confidence`; `research-ingest` triggers it. Nothing `proposed` reaches synthesis, a report or Confluence until a researcher accepts it (board in `02 highlights review.md`, or `review.py`). Rejections are kept, never deleted.
7. **Append to `_system/provenance.log`** after every ingest, highlight run, synthesis, or publish, one line:
   `ISO-date<TAB>skill<TAB>action<TAB>target-id<TAB>model`.
8. **Never mark up a transcript to show highlights.** The signal comes from the Strange New Worlds plugin reading backlinks; highlights link to their block (`![[S-0001#^s0001-0014]]` plus an "Open in transcript" link with the timestamp).
9. **Frontmatter properties, not inline hashtags.** All queryable metadata goes in frontmatter so Bases can read it.
10. **One source per review run. One project per synthesis run.** Don't batch across projects.
11. **Every non-obvious decision about the system goes in `_system/docs/decisions.md`**: numbered, dated, with the reason. Append; never rewrite. The organisational design (surfaces, people, access, uploads, where the skills run) is `_system/docs/operating-model.md`; keep it in step.

## Participants and personas (vault-wide)

- Every participant has a card in `20 Participants/P-###.md`, written by `participants.py sync` from the Rally export. The card carries role, experience, market, industry, region and consent state, never a name or employer; those live only in `_raw/participants/P-### identity.md` and `_raw/participants.csv`, which the card embeds for people who hold the key.
- **Every participant is assigned a persona** from `30 Personas/` (`persona: "[[30 Personas/PE-03 Validation engineer who must prove every simulated number|PE-03 Validation engineer who must prove every simulated number]]"` on the card: always the ID **and** the name as the display text, never the bare ID). The project's participants table in `01 project.md` has a Persona column with the same link. If no existing persona fits the person, create a new persona note (`status: proposed`, with the evidence it rests on) rather than stretching one; the researcher merges or retires personas later. Personas are vault-wide, not per project, and are built from participant cards plus accepted highlights.
- `participants.py check` fails when a source cites a participant without a card or a card has no persona.

## IDs

- Participant `P-001`, persona `PE-01` (file name `PE-01 <role> who <one behaviour>`, e.g. `PE-01 Design engineer who trusts a result only after it matched the bench`; no adjectives, no metaphors, no invented first names), source `S-0001`, highlight `H-S0001-0003` (source + sequence), insight `I-<project>-01`, project folder `YYYY_slug`.
- Highlight and insight **file names are the ID followed by a title** that passes the stranger test (`H-S0001-0003 Spreadsheet wins when tool and spreadsheet disagree.md`), with `aliases: [ID]` for search. **Link by file name with the ID as display text**: `[[H-S0001-0003 Spreadsheet wins when tool and spreadsheet disagree|H-S0001-0003]]`, embed as `![[<file name>]]`. A bare `[[H-S0001-0003]]` does not resolve in Obsidian (aliases only feed autocomplete). `uv run _system/scripts/next_id.py` and `vaultlib.find_by_id()` give you the file name. Source titles follow `[Interview] P-001 - 14 Oct 2026`.
- Block IDs inside a source: `^s0001-0012` (lowercase source id + 4-digit paragraph number).
- Next free IDs: `uv run _system/scripts/next_id.py participant|source|highlight <S-id>|insight <project>`.

## Where things go

- New study: `research-organize` → `new project`. Creates `10 Projects/YYYY_slug/` with three root pages, `01 project.md` (Study Overview), `02 highlights review.md`, `03 tag board.md`, and lettered folders in reading order: `a_setup/` (SETUP docs and `boards/`), `b_sources/` (transcripts and `reference/`), `c_highlights/`, `d_tags/` (`tags.yaml` and tag pages), `e_insights/`, `f_deliverables/`. Nothing else goes at the project root.
- Source state is `ris_status` (raw, in-progress, review, published, excluded, archived), as in Dovetail.
- Drop files in `00 Inbox/`. Ingest moves media to `_raw/<project>/` and writes `b_sources/S-####.md`.
- Highlights go in `c_highlights/H-S####-#### <title>.md`, insights in `e_insights/I-<project>-## <finding>.md`.
- Vault-wide views are `.base` files in `_system/bases/`; embed them in project notes.
- Tag pages (`_system/tags/`, `10 Projects/<p>/d_tags/`) and boards (`a_setup/boards/`: `tags.base`, `tag-board.base`, `tag-board.canvas`, `tag-board.md`) are generated by `tag_board.py` from the taxonomies; never hand-edit them, edit `d_tags/tags.yaml` and re-run.

## Model note

This vault is used under an ADI Claude Enterprise account. The demo project (`2026_demo-fluxbench`) is entirely fictional and safe for a public or personal repo. Real projects go to ADI's GitHub only.
