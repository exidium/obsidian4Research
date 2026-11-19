# obsidian4Research

A file-based research repository: Obsidian for browsing and querying, Claude Code skills for ingesting, organizing, and analyzing. Replaces the core Dovetail loop (data entries → tagged highlights → insight docs) with Markdown, git, and a two-level tag taxonomy, following the ADI "Working with us" research conventions (Study Overview, SETUP/REFERENCE docs, workspace vs project tags, review-first AI tagging, evidence-linked insights with recommendations, domain synthesis).

Open this folder as an Obsidian vault. Run Claude Code from this folder to use the skills. New machine or new person: `GETTING STARTED.md`. Showing it to someone: `_system/docs/demo-runsheet.md`.

## Layout

```
00 Inbox/        drop transcripts or media here; ingest consumes them
00 Synthesis/    one folder per product domain: Landscape, What We Know, Open Questions, Study Index
20 Participants/ one card per participant (role, experience, market, industry, region, consent, persona); names stay in _raw/
30 Personas/     vault-wide personas; every participant is assigned one, or a new one is proposed
10 Projects/     one folder per study. Root pages: 01 project (Study Overview), 02 insights review, 03 tag board.
                 Folders in reading order: a_setup/ (SETUP docs, boards/), b_sources/ (transcripts, reference/), c_highlights/, d_tags/ (tags.yaml + tag pages), e_insights/, f_deliverables/
90 Archive/      closed projects, same structure
_system/         taxonomy.yaml, schema.md, templates/, scripts/, bases/, provenance.log
_raw/            local only, gitignored: media, clips, reels, participants.csv (the only place names live)
.claude/skills/  ten skills: ingest, highlight, synthesize, report, publish, clip, participants, persona, ask, organize, audit
```

## The skills

One skill per step of the research loop; each reads one level of the vault and writes the next.

| Skill | Job | Typical ask |
|---|---|---|
| research-ingest | media or transcript → source note with stable block IDs, speakers, summary | "ingest the file in the inbox for P-004 on project X" |
| research-organize | owns the taxonomy, structure, audits, tag migrations, new projects | "new project", "audit the vault", "approve proposed tags" |
| research-highlight | tags a transcript automatically into highlight notes (proposed, with confidence); ask mode shows proposals first | "tag S-0003", "accept all high from S-0003", "what's pending" |
| research-synthesize | accepted highlights → themes → evidence-linked insight notes with evidence levels | "synthesize project X" |
| research-report | insights → stakeholder readout in `f_deliverables/`, registered in the Reports table | "write the readout for the product owner" |
| research-publish | study page, insights, readouts → Confluence pages (SDP UX Research), URL written back to the note | "publish the study to Confluence" |
| research-participants | Rally export → participant cards (public half) and identities (`_raw/`); checks every source has a card | "sync participants", "consent status of P-003" |
| research-persona | match a participant to a persona or propose one; build, revise, merge personas from evidence | "assign a persona to P-004", "merge PE-02 into PE-05" |
| research-ask | questions from PMs answered from insights and highlights with citations and evidence levels | "what do we know about licensing?" |
| research-audit | one health run: audit, PII scan, recordings, cards, personas; dated report | "health check", "before I commit" |
| research-clip | recording → source pointer; highlight → blurred, captioned, stamped clip; insight → reel | "link the recording to S-0004", "clip H-S0004-0007", "make a reel for I-...-02" |

## Rules that keep it trustworthy

- Transcripts are immutable after ingest. Block IDs never change.
- Highlights are atomic, titled notes: verbatim complete sentences, a context annotation when the stranger test needs it, 2-3 tags across dimensions, a rationale, linked to a source block. Each one embeds its transcript block and carries an "Open in transcript" link with the timestamp; in the transcript, Strange New Worlds shows which blocks have highlights.
- Tagging is automatic: `research-highlight` writes highlights from the transcript as `proposed` with a confidence rating, triggered by ingest. The researcher is the gate, not the typist: accept or reject by exception on the review board or with `review.py`; nothing proposed reaches synthesis, reports or Confluence.
- Insights are built from highlight notes only, never from raw transcripts. Each has a finding, severity, interpretation, embedded evidence, and a decision-forcing recommendation. Evidence level: strong 4+, emerging 2-3, insufficient 1 (no insight doc yet).
- Workspace tags mirror the ADI boards and are admin-controlled. Project tags live in `d_tags/tags.yaml` with definitions. The AI may *propose* a project tag; only a human activates it.
- Names never enter git. Participants are `P-###` with a public card in `20 Participants/`; the key (`_raw/participants.csv`, `_raw/participants/*identity.md`) is local only and comes from the Rally export via `participants.py sync`. Consent is tracked in Rally, referenced by `rally_id`.
- Every AI action appends a line to `_system/provenance.log`.
- Video never enters git. Recordings, clips and reels stay in `_raw/<project>/`, which in production is the OneDrive-synced SharePoint study folder; notes carry a path, checksum and timestamps. Internal participants appear in clips as text only.

## Running it unattended (production shape)

The same skills run without a laptop: a GitHub Action on the research repo (ADI's internal GitHub) runs `research-highlight` in auto mode on every new or changed source note and opens a pull request with the proposed highlights; the researcher's review is the PR plus the board. The Claude Code GitHub Action is the runner; the vault's `CLAUDE.md` and skills are its instructions; `health.py` is the check on the PR. Recordings stay in the SharePoint study folder, so the action never sees media or names.

## Setup

```bash
brew install ffmpeg
uv tool install mlx-whisper          # local transcription on Apple Silicon
bash _system/scripts/install_hooks.sh   # pre-commit PII scan
brew install uv                      # media.py runs with `uv run` (pulls Pillow on first use)
```

Then open the folder in Obsidian and enable the core Bases plugin. The boards are native Bases. One community plugin ships in `.obsidian/plugins/`: **Strange New Worlds**, which badges every transcript block that a highlight references (hover to see the highlights, click to open one). Transcripts themselves stay untouched. No AI plugins; the skills do that work outside the app.

## Demo

`10 Projects/2026_demo-fluxbench` contains three fully fictional interviews about an invented product, run through the whole pipeline: Study Overview, project tags, 35 titled highlights with context annotations, 7 insight docs, tag board and canvas. Nothing in it refers to a real person, company, or product.

The demo also has participants, personas and video. The Rally export is mocked in `_raw/rally/participants.json` (fictional people, not in git). The recordings are synthetic (macOS text-to-speech placed at the transcript timestamps, the fictional name on the call tile) and are not in git; recreate everything with:

```bash
uv run _system/scripts/participants.py sync          # cards from the mock Rally export in _raw/rally/
uv run _system/scripts/demo_recording.py S-0001 --voice Samantha   # name plate comes from the Rally export
uv run _system/scripts/demo_recording.py S-0002 --voice Karen
uv run _system/scripts/demo_recording.py S-0003 --voice Moira
# each prints its `media.py link` command; add --redact 857,198,176,176:face to blur the camera tile too
for i in "10 Projects/2026_demo-fluxbench/e_insights/"I-*.md; do uv run _system/scripts/media.py reel "$(basename "$i" | cut -d' ' -f1)"; done
```

## Views

- **Tag board (Dovetail-style):** the Study Overview embeds `a_setup/boards/tags.base` → lanes are tag groups, cards are tags with definition and counts. Click a tag to open its page: definition, counts, and a live table of its highlights (workspace tag pages group by project). Tag pages live in `_system/tags/<dimension>/` (workspace) and `10 Projects/<p>/tags/<group>/` (project); `tag_board.py` writes them from the taxonomies and refreshes counts. Native Bases.
- **Highlight boards:** `03 tag board.md` per project has one native Kanban per tag group (lanes are the group's tags), plus boards by participant and review status. Vault-wide: `_system/tag-board.md`, `_system/bases/tags-all.base`, `_system/bases/highlights-all.base`.
- **Review board:** each project's `02 insights review.md` is a Kanban with proposed / accepted / rejected lanes (`_system/bases/highlights-review.base`); dragging a card sets its `review` property. Only accepted highlights feed synthesis.
- **Per project:** `01 project` links to `02 insights review` and `03 tag board` and embeds the insights table; `a_setup/boards/tag-board.canvas` has lanes you can drag cards between, then `canvas_sync.py` re-tags.
