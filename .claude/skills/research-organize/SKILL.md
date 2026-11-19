---
name: research-organize
description: The librarian of the research vault. Sets up projects the ADI way (Study Overview, SETUP/REFERENCE docs, project tag groups), owns the workspace and project tag taxonomies, audits integrity, migrates tags, generates tag boards, closes studies into the domain synthesis. Use when the user says "new project", "new study", "set up", "audit the vault", "check the repo", "review proposed tags", "approve/reject tag", "merge/rename tag", "tag board", "sync the board", "close the study", "project status", or asks how the vault is organized. Never tags content itself; that is research-highlight and research-synthesize.
---

# research-organize

Keeps the vault trustworthy over time. Two things rot a research repository: tag drift and broken evidence links. Most of this skill is saying no, merging, or verifying. It mirrors the ADI "Working with us" conventions (Confluence, SDP UX Research space), so a researcher who knows Dovetail should recognise everything.

## Commands

### new project

1. Collect: slug (kebab-case), title in the form `YYYY-MM Phase - Topic` (phases: Discovery, Evaluation, Validation, Workshop, Survey, Benchmarking), owner `P-###`, domain (mirrors Dovetail folder placement, e.g. `product-tools/rf-studio`, `ecosystem/studio-ecosystems`, `platform-web/analog-com`, `programs`, `operations`), Rally study reference.
2. `uv run _system/scripts/new_project.py <slug> --title "<title>" --phase <phase> --owner P-### --domain <domain> --rally-study "<ref>"`
3. Open `01 project.md` and fill it with the user, keeping its three top-level sections (Study overview / Findings / Operations & data): an Introduction of at least two paragraphs (why the study exists, scope and out of scope, product space, audience by role, consent tracking), research questions and methodology, target participants. **A project without a filled Study Overview is a project nobody can use**; don't leave it blank.
4. Seed `d_tags/tags.yaml`: propose 3 to 6 numbered groups from the research questions, each tag with a definition that says when to apply it and when not. Watch the common distinctions: tool hard to use vs capability missing; difficulty choosing vs difficulty finding; one document vs consistency across documents; sentiment about a product vs about a process.
5. Put the discussion guide and brief into `a_setup/` as `SETUP ...` notes. Imported context (PRD, SOW, competitive reports) goes into `b_sources/reference/` as `REFERENCE ...` notes with `Source:` and `Last synced:` at the top. Stimulus shown to participants → `setup/STIMULUS ...`.
6. If the domain has no synthesis folder yet: `uv run _system/scripts/new_domain.py <domain-slug> --title "<Domain>"`, and add the project to its Study Index.
7. `bash _system/scripts/provenance.sh research-organize new-project <project_id>`

### audit

```bash
uv run _system/scripts/audit.py --write
```

Errors break traceability (missing blocks, non-verbatim quotes, unknown tags, highlight without a workspace tag, PII, file names not starting with their ID). Fix them or hand them to the user. Warnings are hygiene (single-dimension tagging, missing fields, highlight counts outside the 30/60/90-minute ranges, insights with one participant). Summarise in five lines and list the decisions the user must make. Run before synthesis and before any push to the shared remote.

### review proposed tags

Only project tags can be proposed. Workspace tags (`experience`, `functionality`, `insight`, `sentiment`, `ops`, `journey`, `software`, `market`) are admin-controlled by the UXR team; never add, rename, or deprecate them here. If a workspace change seems needed, tell the user to raise it with the UXR team.

1. Open the project's `d_tags/tags.yaml`; list every tag with `status: proposed`, its definition, and its `evidence` highlight IDs.
2. Show the quotes behind each (`uv run _system/scripts/highlights_table.py <project> --tag <tag>`) and recommend: **activate** (distinct concept, two or more participants, definition written), **merge** into an existing tag (`migrate_tag.py --project`), or **reject** (one-off, or an opinion rather than a behaviour, or a theme rather than a classification; themes are insights, not tags).
3. The user decides. Apply: set `status`, `decided` date. Never activate on your own.

### migrate tag

```bash
uv run _system/scripts/migrate_tag.py <old> <new> --project <id> --dry-run
uv run _system/scripts/migrate_tag.py <old> <new> --project <id>
```

The new tag must already exist. Old becomes `deprecated` with `merged_into`. Audit afterwards. For workspace tags the script rewrites notes but leaves `taxonomy.yaml` alone.

### tag board / sync the board

- `uv run _system/scripts/tag_board.py <project>` writes, from `taxonomy.yaml` and the project's `d_tags/tags.yaml`: tag pages (`_system/tags/<dim>/<slug>.md` for workspace tags, `10 Projects/<p>/d_tags/<group>/<slug>.md` for project tags; `type: tag`, definition, counts, and an inline base listing the tag's highlights live), `a_setup/boards/tags.base` (Kanban: lanes = tag groups, cards = tags; the Dovetail tag board), `a_setup/boards/tag-board.base` (highlight boards per group) and `03 tag board.md` (the page embedding all of them with definitions). Re-run after any change to tags.yaml or taxonomy.yaml and after each highlight run (counts and `tag_groups`). Tag pages of removed tags are deleted; deprecated tags keep theirs. `--all` → vault-wide equivalents in `_system/`.
- `uv run _system/scripts/tag_board.py <project> --canvas --dimension <dim-or-group>` → `a_setup/boards/tag-board.canvas`: one lane per tag, highlights as draggable cards. Default dimension `journey`.
- After the user drags cards: `uv run _system/scripts/canvas_sync.py <project> --dry-run`, then without the flag. A new lane labelled with an unknown project tag becomes `proposed`; a new workspace lane is refused. Regenerate the boards after sync.
- All boards are native Bases (Kanban per tag group, grouped by a formula). Re-tagging by drag happens on the canvas only. Tag pages are generated: never hand-edit them; edit `d_tags/tags.yaml` and re-run.

### project status

From `01 project.md`, `b_sources/`, `c_highlights/`, `e_insights/`: sources by `ris_status`, highlights by `review`, insights by `status` and `evidence_level`, participants covered by type. Report gaps: raw sources, highlights pending more than a week, research questions with no insight, emerging insights that need more participants.

### close the study

Checklist from ADI's "what done looks like":
1. All sources `ris_status: published` (or `excluded`), all highlights reviewed, insights written for strong and emerging themes with recommendations, each insight embedding its highlights.
2. `01 project.md` updated: findings summary under Insights, Reports table pointing at the files in `f_deliverables/` (note in the table whether a deliverable contains participant quotes, for GDPR traceability).
3. Update the domain synthesis: `00 Synthesis/<domain>/What We Know.md` with the new findings, `Open Questions.md`, `Study Index.md`.
4. `git mv "10 Projects/<id>" "90 Archive/<id>"` only if the user wants it out of the active list.
5. Remind the user that media in `_raw/<id>/` has its own retention and is theirs to delete.

## Taxonomy principles

- **Workspace first, project second.** Workspace tags are the cross-project backbone (a PM from any team understands them). Project tags add domain precision only someone in the study would understand.
- **Fields are not tags.** Participant type, role, market they work in, software they use: fields on the source. Market or software *being discussed*: tags on the highlight. They can legitimately differ.
- **Tags classify, insights theme.** "Data flow fragmentation" is a theme; it is written as an insight, not added as a tag.
- **Definitions are the tag.** Every project tag needs one that says when to apply it and when not.
- **Small.** A project board of about 30 to 60 tags across 5 to 9 numbered groups, like the RF study. Past that, merge.
- **Deprecate, never delete.** Old highlights must keep resolving.

## Structure rules

- Repo root is the vault. `project_id` equals the folder name. Highlight and insight file names start with their ID and carry an alias equal to the ID, so links by ID survive renames.
- Generated files (`tag-board.*`, audit reports) are never hand-edited.
- New cross-project views are `.base` files in `_system/bases/`, not Dataview queries.

## Finish every command

```bash
bash _system/scripts/provenance.sh research-organize <command> <target>
```
