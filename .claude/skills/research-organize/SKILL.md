---
name: research-organize
description: The librarian of the research vault. Owns the tag taxonomy, folder structure, templates, Bases views, audits, and tag migrations. Use when the user says "new project", "new study", "audit the vault", "check the repo", "review proposed tags", "approve/reject tag", "merge/rename tag", "archive project", "project status", or asks how the vault is organized. Never tags content itself; that is research-process.
---

# research-organize

This skill keeps the vault trustworthy over time. The two things that rot a research repository are tag drift and broken links, so most of what it does is say no, merge, or verify.

## Commands

### new project

1. Ask for: slug (kebab-case), title, owner participant ID (the researcher, e.g. `P-000`), Rally study reference. Never write names.
2. `python3 _system/scripts/new_project.py <slug> --title "<title>" --owner P-000 --rally-study "<ref>"`
3. Open the created `project.md`, fill the research questions with the user, set `methods` and `product` from active taxonomy tags.
4. `bash _system/scripts/provenance.sh research-organize new-project <project_id>`

### audit

```bash
python3 _system/scripts/audit.py --write
```

Read the report. Errors are things that break traceability (missing blocks, non-verbatim quotes, unknown tags, PII). Fix them or hand them to the user; don't leave them. Warnings are hygiene. Summarize the report in five lines and list the decisions the user has to make (proposed tags, orphaned sources).

Run the audit before any synthesis run and before any push to the shared remote.

### review proposed tags

1. Open `_system/taxonomy.yaml`, list every tag with `status: proposed`, with its definition and `evidence` highlight IDs.
2. For each, show the user the quotes behind it (`python3 _system/scripts/highlights_table.py <project> --tag <tag>`) and recommend one of:
   - **activate**: the concept is distinct and recurs across two or more participants
   - **merge** into an existing tag: same concept, different words → `migrate_tag.py`
   - **reject**: one-off, or an opinion rather than a behavior/need → `migrate_tag.py` into the nearest active tag, or remove the tag from its highlights
3. Only the user decides. Apply the decision: edit `status`, add `decided` date. Never activate a tag on your own.

### migrate tag

```bash
python3 _system/scripts/migrate_tag.py <old> <new> --dry-run   # show impact
python3 _system/scripts/migrate_tag.py <old> <new>
```

The new tag must exist in the taxonomy first. Old tag becomes `deprecated` with `merged_into`. Run `audit.py` afterwards.

### add tag (human-requested)

Append under the right dimension with `status: active`, a one-sentence `definition` that says when to use it and when not to, and `created`. Check for synonyms first: grep the taxonomy for the key noun. If a near-synonym exists, propose using that instead.

### archive project

1. Audit first; no errors allowed.
2. `git mv "10 Projects/<id>" "90 Archive/<id>"`, set `status: closed` in `project.md`.
3. Remind the user that media under `_raw/<id>/` has a retention date; it is theirs to delete.

### project status

Read `project.md` and count: sources by status, highlights by review state, insights by status, participants covered. Report gaps: sources not highlighted, highlights pending for more than a week, insights with a single participant.

## Taxonomy principles (apply when judging tags)

- **Dimension first.** Every tag belongs to exactly one dimension: product, method, segment, behavior, theme, topic. A proposed tag with no clear dimension is usually two tags or none.
- **Behavior over topic.** "what were they doing" retrieves better than "what was it about". Push proposals toward `behavior/` when possible.
- **Segments are task-based.** `segment/validating-design`, never `segment/senior-engineer`.
- **Definitions are the tag.** A tag without a definition that says when *not* to use it will be misapplied within a month.
- **Small taxonomy.** Under about sixty active tags across all dimensions. If a dimension grows past fifteen, look for merges.
- **Deprecate, never delete.** Old highlights must keep resolving.

## Structure rules

- Repo root is the vault. Dotfolders (`.claude`, `.git`, `.obsidian`) are invisible to Obsidian.
- Project folders are `YYYY_slug`; `project_id` equals the folder name.
- `_system/` holds everything that is not research content. Scripts never write outside `10 Projects`, `90 Archive`, `_system`, `_raw`.
- Bases views live in `_system/bases/` and are embedded in project notes; edit the `.base` file, not the embed.
- If the user wants a new cross-project view, add a `.base` file rather than a Dataview query, so it works without a community plugin.

## Finish every command

```bash
bash _system/scripts/provenance.sh research-organize <command> <target>
```
