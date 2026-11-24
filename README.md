# obsidian4Research

A research repository built from tools the organisation already runs: **SharePoint** for recordings and anything sensitive, **GitHub** for the research itself as Markdown, **Confluence** for what the rest of the company reads, and **Claude Code** skills for the work in between. **Obsidian** is the researcher's browser over the Markdown: boards, tables, transcripts with evidence badges, embedded clips.

It replaces the core Dovetail loop (data entries → tagged highlights → insight documents) with files and git, following the ADI "Working with us" research conventions: Study Overview, SETUP and REFERENCE documents, workspace versus project tags, review-first AI tagging, evidence-linked insights with recommendations, domain synthesis. Every claim in a published finding traces back through a highlight to a transcript block, a timestamp, and a recording in SharePoint.

## Documentation

| Read | When |
|---|---|
| [GETTING STARTED.md](GETTING%20STARTED.md) | installing on a new computer, first tour, first study, troubleshooting |
| [_system/docs/operating-model.md](_system/docs/operating-model.md) | how it runs in the organisation: surfaces, people, access, uploads, where the skills run, the hosted machine |
| [_system/docs/decisions.md](_system/docs/decisions.md) | the decision log: numbered, dated, with the reason. Append; never rewrite |
| [_system/schema.md](_system/schema.md) | every note type and property, IDs, folder layout |
| [CLAUDE.md](CLAUDE.md) | the hard rules the skills obey |
| [.claude/skills/](.claude/skills/) | one `SKILL.md` per step of the research loop |
| [_system/docs/demo-runsheet.md](_system/docs/demo-runsheet.md) | the 20-minute demo on the fictional project |

## The three surfaces

| Surface | Holds | Who touches it |
|---|---|---|
| **SharePoint** (one study folder per project, synced with OneDrive) | recordings, clips, reels, the participant key, an `Inbox/` for drops; the whole folder of a restricted study | researchers with rights to that study |
| **GitHub** (one research repository) | the vault: project pages, transcripts, highlights, tags, insights, deliverables, skills, scripts | researchers (write), question-askers (read) |
| **Confluence** (the UX research space) | study pages, insights, readouts, published from the vault | everyone; Rovo indexes it |

There is no fourth surface. Readers use Confluence; people who want the evidence behind a finding ask a Claude Project synced from GitHub; researchers work in the vault.

## Who does what

| | Readers | Question-askers | Researchers |
|---|---|---|---|
| Who | product, design, management, most of the company | people who want the evidence behind an insight | the research team |
| Use | Confluence, Rovo | a Claude Project synced from GitHub (insights, highlights, participants, personas; never transcripts) | repo write, Obsidian, Claude Code, the SharePoint study folders |
| Setup | none | none (one person sets up the Project) | GETTING STARTED, about 15 minutes |

## Layout

```
00 Inbox/        drop transcripts or media here (or upload from the GitHub web page); ingest consumes them
00 Synthesis/    one folder per product domain (new_domain.py): Landscape, What We Know, Open Questions, Study Index
10 Projects/     one folder per study. Root pages: 01 project (Study Overview), 02 highlights review, 03 tag board.
                 Folders in reading order: a_setup/ (SETUP docs, boards/), b_sources/ (transcripts, reference/),
                 c_highlights/, d_tags/ (tags.yaml + tag pages), e_insights/, f_deliverables/
                 A restricted study is a SharePoint-only folder dropped here and ignored by git.
20 Participants/ one card per participant: role, experience, market, industry, region, consent, persona. No names.
30 Personas/     vault-wide personas; every participant is assigned one, or a new one is proposed
90 Archive/      closed projects, same structure
_system/         taxonomy.yaml, schema.md, templates/, scripts/, bases/, docs/, reports/, provenance.log
_raw/            local only, gitignored: media, clips, reels, the participant key. In production this is the
                 OneDrive-synced SharePoint study folder.
.claude/skills/  the eleven skills
.obsidian/       vault settings, the Strange New Worlds plugin, the CSS snippet
```

## The loop

1. **New study**: "new project …" → `research-organize` creates the folder, the three root pages, seed tag groups and the SETUP templates. You write the introduction and the discussion guide.
2. **Participants**: export the study from Rally into `_raw/rally/`, "sync participants" → cards in `20 Participants/`, identities in `_raw/`, a persona per participant (`research-participants`, `research-persona`).
3. **Material in**: a transcript uploaded to `00 Inbox/<project>/` from the GitHub web page, or a recording dropped in the SharePoint study folder's `Inbox/`.
4. **Ingest and tag**: "ingest everything waiting" → `research-ingest` writes the source note (pseudonymised, PII-scanned, block IDs, recording linked with checksum) and hands off to `research-highlight`, which writes every highlight as `proposed` with a confidence rating. No one types tags.
5. **Review by exception**: `02 highlights review` is a Kanban of proposed / accepted / rejected. Drag cards, or "accept everything high from S-0004, reject 12 and 19". Nothing proposed goes further.
6. **Synthesize**: "synthesize the project" → `research-synthesize` reads accepted highlights only and writes insight notes with evidence levels and recommendations.
7. **Report**: "write the readout for the product owner" → `research-report` writes `f_deliverables/Readout - ….md` and registers it under Reports.
8. **Publish**: "publish the study to Confluence" → `research-publish` previews, waits for a yes, creates the pages, writes the URLs back.
9. **Video**: "clip H-S0004-0007", "reel for insight 02" → `research-clip` renders blurred, captioned, stamped clips into the SharePoint folder.
10. **Health**: "health check" before every commit → `research-audit` runs the audit, the PII scan, checksums, cards and personas.

## The skills

| Skill | Job | Typical ask |
|---|---|---|
| research-organize | taxonomy, structure, new projects, tag migrations, closing a study | "new project", "approve proposed tags", "close the study" |
| research-participants | Rally export → participant cards (public half) and identities (`_raw/`) | "sync participants", "consent status of P-003" |
| research-persona | match a participant to a persona or propose one; build, revise, merge personas | "assign a persona to P-004", "merge PE-02 into PE-05" |
| research-ingest | transcript or media → source note with stable block IDs, speakers, summary; triggers tagging | "ingest the inbox for P-004" |
| research-highlight | transcript → highlight notes, automatic, `proposed` with confidence; ask mode shows proposals first | "tag S-0003", "accept all high from S-0003", "what's pending" |
| research-synthesize | accepted highlights → themes → insight notes with evidence levels | "synthesize project X" |
| research-report | insights → stakeholder readout in `f_deliverables/` | "write the readout for the product owner" |
| research-publish | study page, insights, readouts → Confluence, URL written back | "publish the study to Confluence" |
| research-clip | recording → source pointer; highlight → clip; insight → reel | "link the recording to S-0004", "clip H-S0004-0007" |
| research-ask | questions from stakeholders answered from insights and highlights with IDs | "what do we know about licensing?" |
| research-audit | one health run with a dated report | "health check", "before I commit" |

## The scripts

All run with `uv run _system/scripts/<name>.py`; each declares its own dependency, so a fresh clone needs no Python setup. No arguments prints the usage.

| Script | Does |
|---|---|
| `new_project.py`, `new_domain.py` | scaffold a study, a product domain |
| `build_source.py` | transcript file (Whisper JSON, VTT, SRT, Dovetail export, plain text) → source note with block IDs |
| `transcribe.sh` | local Whisper on Apple Silicon; audio never leaves the machine |
| `next_id.py` | next free participant, source, highlight or insight ID |
| `review.py` | `pending`, `accept`, `reject`: the human gate in bulk, logged with the researcher ID |
| `highlights_table.py` | compact table of a project's highlights for synthesis (`--accepted-only`) |
| `tag_board.py`, `canvas_sync.py`, `migrate_tag.py` | generated boards and tag pages; lane drags back to tags; rename or merge a tag |
| `participants.py` | `sync` cards from the Rally export, `check` every source has a card and every card a persona |
| `personas.py` | `refresh` the "Where they appear" sections and counts, `check` |
| `media.py` | `link` a recording (checksum, duration, redaction regions), `clip`, `reel`, `check` |
| `publish.py` | render Confluence bodies from notes; `record` the URL back |
| `audit.py`, `scan_pii.py`, `health.py` | integrity, identity leaks, and the one run that does both plus media, cards, personas |
| `install_hooks.sh`, `provenance.sh` | the pre-commit hook; one provenance line per AI action |
| `demo_recording.py` | demo only: synthetic call recording for a fictional source |

## Rules that keep it trustworthy

- Transcripts are immutable after ingest. Block IDs never change.
- Highlights are atomic, titled notes: verbatim complete sentences, a context annotation when the stranger test needs it, two or three tags across dimensions, a rationale, a link to one source block and an "Open in transcript" link with the timestamp. In the transcript, Strange New Worlds shows which blocks have highlights; the transcript itself is never marked up.
- Tagging is automatic; the researcher is the gate, not the typist. Nothing `proposed` reaches synthesis, a report or Confluence. Rejections are kept.
- Insights are built from highlights only, never from transcripts. Evidence level: strong 4+, emerging 2 to 3, insufficient 1.
- Workspace tags mirror the ADI boards and are admin-controlled. Project tags live in `d_tags/tags.yaml` with definitions. The AI may propose a project tag; only a human activates it.
- Names never enter git. Participants are `P-###`; the key lives in `_raw/` only and comes from the Rally export. Consent is tracked in Rally.
- Video never enters git. Recordings, clips and reels stay in the SharePoint study folder; notes carry a path, a checksum and timestamps. Internal participants appear in clips as text only.
- Every AI action appends a line to `_system/provenance.log`. Every decision about the system goes in `_system/docs/decisions.md`.

## Views

- **Study Overview** (`01 project`): numbered contents, introduction, research questions and methodology, participants with personas, Reports table, insights table, links to the review board and the tag board.
- **Highlights review** (`02 highlights review`): Kanban of proposed / accepted / rejected with confidence; dragging a card sets its `review` property. Tables of pending and reviewed below it.
- **Tag board** (`03 tag board`): lanes are tag groups, cards are tags with definition and counts; one Kanban of highlights per group. Vault-wide: `_system/tag-board.md`.
- **Participants and personas**: `_system/bases/participants.base`, `personas.base`; each persona lists where it appears.
- **Transcripts**: each block carries its timestamp and a badge for every highlight that references it; the highlight embeds the block and, when a clip exists, the clip.

## Setup

See [GETTING STARTED.md](GETTING%20STARTED.md). In short: `brew install git uv ffmpeg`, Obsidian, Claude Code, `git clone`, `bash _system/scripts/install_hooks.sh`, `uv run _system/scripts/health.py`.

## Demo

`10 Projects/2026_demo-fluxbench` is a complete, entirely fictional study about an invented product: three hour-long interviews, 110 highlights, 7 insights, a readout, clips and reels. Nothing in it refers to a real person, company or product; it is safe in a public repository. The recordings are synthetic (text-to-speech placed at the transcript timestamps) and live in `_raw/`, not in git. To recreate them from the mock Rally export in `_raw/rally/participants.json`:

```bash
uv run _system/scripts/participants.py sync
uv run _system/scripts/demo_recording.py S-0001 --voice Samantha
uv run _system/scripts/demo_recording.py S-0002 --voice Karen
uv run _system/scripts/demo_recording.py S-0003 --voice Moira
# each prints its `media.py link` command; add --redact 857,198,176,176:face to blur the camera tile
for i in "10 Projects/2026_demo-fluxbench/e_insights/"I-*.md; do uv run _system/scripts/media.py reel "$(basename "$i" | cut -d' ' -f1)"; done
```

The demo itself is scripted in [_system/docs/demo-runsheet.md](_system/docs/demo-runsheet.md).

## Status (2026-11-24)

**Done.** The vault, eleven skills, the demo study end to end, Confluence publishing of a study page and readout, the clip and reel pipeline, participants and personas, automatic tagging with the review gate, onboarding guide, a verified fresh clone from GitHub.

**Next, in the organisation.** Pilot on one current study in the company environment; an internal GitHub repository; a dedicated SharePoint location for recordings with the legal review of the move from Dovetail; the access model written up; the upload routes documented; `research-ingest` reading both inboxes. Test with a real Teams recording: click-to-seek from transcript lines (Media Extended plugin), redaction regions on a real gallery layout, VTT speaker labels, two-hour sessions.

**After the pilot.** A hosted, IT-owned machine running the same skills on a schedule, so recordings are processed unattended. Described in the operating model.

**Parked.** Miro board import; linking findings to roadmap decisions (opportunity maps).
