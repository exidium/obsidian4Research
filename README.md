# obsidian4Research

A file-based research repository: Obsidian for browsing and querying, Claude Code skills for ingesting, organizing, and analyzing. Replaces the core Dovetail loop (sources → tagged highlights → insights) with Markdown, git, and a controlled tag taxonomy.

Open this folder as an Obsidian vault. Run Claude Code from this folder to use the skills.

## Layout

```
00 Inbox/        drop transcripts or media here; ingest consumes them
10 Projects/     one folder per study: project.md, sources/, highlights/, insights/
90 Archive/      closed projects, same structure
_system/         taxonomy.yaml, schema.md, templates/, scripts/, bases/, provenance.log
_raw/            local only, gitignored: media, participants.csv (the only place names live)
.claude/skills/  research-ingest, research-organize, research-process
```

## The three skills

| Skill | Job | Typical ask |
|---|---|---|
| research-ingest | media or transcript → source note with stable block IDs, speakers, summary | "ingest the file in the inbox for P-004 on project X" |
| research-organize | owns the taxonomy, structure, audits, tag migrations, new projects | "new project", "audit the vault", "approve proposed tags" |
| research-process | source → highlights; highlights → insights; insights → Confluence | "highlight S-0003", "synthesize project X", "publish insight I-..." |

## Rules that keep it trustworthy

- Transcripts are immutable after ingest. Block IDs never change.
- Highlights are atomic notes with frontmatter properties, one idea each, verbatim quote, linked to a source block.
- Insights are built from highlight notes only, never from raw transcripts, and every claim links to its evidence.
- Tags come from `_system/taxonomy.yaml`. The AI may *propose* a tag; only a human activates it.
- Names never enter git. Participants are `P-###`; the key lives in `_raw/participants.csv`. Consent is tracked in Rally, referenced by `rally_id`.
- Every AI action appends a line to `_system/provenance.log`.

## Setup

```bash
brew install ffmpeg
uv tool install mlx-whisper          # local transcription on Apple Silicon
bash _system/scripts/install_hooks.sh   # pre-commit PII scan
```

Then open the folder in Obsidian and enable the core Bases plugin. Suggested community plugins: Dataview, Tag Wrangler, Templater. No AI plugins; the skills do that work outside the app.

## Demo

`10 Projects/2026_demo-fluxbench` contains three fully fictional interviews about an invented product, run through the whole pipeline. Nothing in it refers to a real person, company, or product.
