# Decision log

Numbered, dated, with the reason. Append new entries at the end; never edit or delete an old one. If a decision is reversed, add a new entry that says so and points back. Dates are the day the decision was recorded in the repository; decisions made in conversation between commits carry the commit date.

---

**D01 · 2026-11-05 · Files in git, not a SaaS.** The research repository is a folder of Markdown notes under git. Obsidian is the researcher's viewer; Claude Code skills do the work; the Dovetail loop (data → highlights → insights) is modelled, not copied.
*Why:* cost of the SaaS, no trace from a finding back to the recording, no way to customise the workflow, and every tool involved (SharePoint, GitHub, Confluence, Claude) is already approved in the organisation.

**D02 · 2026-11-05 · Two tag levels, like Dovetail.** Workspace tags (`_system/taxonomy.yaml`) are administrator-controlled and mirror the ADI boards; project tags (`d_tags/tags.yaml`) are per study, in numbered groups, with definitions. The AI may propose a project tag; only a human activates it.
*Why:* keeps cross-study comparison possible while letting each study name its own themes.

**D03 · 2026-11-05 · Transcripts are immutable; highlights anchor to blocks.** Every paragraph of a source note has a block ID (`^s0001-0012`); a highlight points to one block. Text and IDs never change after ingest; mistakes are fixed by re-ingesting under a new source ID.
*Why:* a quote must be checkable years later; anything that moves text breaks every link above it.

**D04 · 2026-11-05 · Pseudonymisation by design.** Participants are `P-###`. Names, employers and emails exist only in `_raw/` (gitignored). A pre-commit hook refuses `_raw/` and runs a PII scan on staged files.
*Why:* the repository must be safe to clone by anyone on the team; consent and identity stay where they are managed (Rally, SharePoint).

**D05 · 2026-11-05 · Insights cite highlights, never transcripts.** Evidence levels: strong (4+ highlights), emerging (2 to 3), insufficient (1, no insight document yet). Every insight carries a decision-forcing recommendation.
*Why:* keeps synthesis honest and small; the stranger test applies to every quote.

**D06 · 2026-11-17 · Media never enters git.** Recordings, clips and reels live in `_raw/<project>/`, which in production is the OneDrive-synced SharePoint study folder. Notes carry a path, a SHA-256 checksum, duration and timestamps. Clips are cut from the block timestamp, blurred in fixed regions, captioned and stamped with participant, source, timestamp and highlight ID. Internal participants appear in clips as text cards only.
*Why:* git is unsuited to video; the team has no authorisation to put recordings there; a checksum makes a replaced recording detectable.

**D07 · 2026-11-17 · Project layout.** Exactly three pages at a project root (`01 project`, `02 … review`, `03 tag board`) and lettered folders in reading order (`a_setup` with `boards/`, `b_sources` with `reference/`, `c_highlights`, `d_tags`, `e_insights`, `f_deliverables`). No deliverables manifest; the Reports table lists reports only; the Study Overview follows the ADI Study Overview sections with a numbered, book-style contents list; insights come first under Findings and are listed once.
*Why:* the researcher's reading order, and a root that stays readable in Obsidian, GitHub and Finder.

**D08 · 2026-11-17 · Link by file name, ID as display text.** `[[H-S0001-0003 Title|H-S0001-0003]]`, never a bare `[[H-S0001-0003]]`.
*Why:* Obsidian does not resolve alias-only links; the audit now errors on bare-ID links.

**D09 · 2026-11-17 · Transcript badges from Strange New Worlds; no markup, no other plugins.** The one community plugin ships in `.obsidian/plugins/`. No AI plugins, no Split Groups. Boards are native Bases.
*Why:* the transcript stays untouched (D03); the badge is computed from backlinks; fewer plugins, fewer approvals.

**D10 · 2026-11-17 · Every participant gets a persona.** If none fits, a new persona is proposed rather than one stretched. Personas are named `PE-## <role> who <one behaviour>`, use Jobs to be done rather than goals, and list where they appear (projects, insights, highlights). The persona property always shows ID and name.
*Why:* personas built from evidence stay honest; the naming passes the stranger test on a board.

**D11 · 2026-11-17 · Participants come from the Rally export.** `participants.py sync` writes public cards (role, experience, market, industry, region, consent flags, retention) and local identities. Consent is tracked in Rally and referenced by ID.
*Why:* one source of truth for recruitment and consent; the vault never becomes a second CRM.

**D12 · 2026-11-17 · Tagging is automatic; the review is the gate.** `research-highlight` writes highlights straight from the transcript as `proposed` with a confidence rating, triggered by ingest. The researcher accepts or rejects by exception on the review board or with `review.py`; nothing proposed reaches synthesis, a report or Confluence. Rejections are kept.
*Why:* tagging was the step the team most wanted automated; the human effort moves from typing to judging; the gate is logged with the researcher's ID.

**D13 · 2026-11-17 · Clip edges from Whisper word timestamps; overlays from Pillow.** Clip boundaries are aligned to the quoted words with safe pads; the Homebrew ffmpeg lacks `drawtext`, so captions and stamps are PNGs rendered with Pillow.
*Why:* character-share timing cut words; the toolchain had to work on a stock Mac.

**D14 · 2026-11-17 · Confluence is the reader layer.** `research-publish` renders the study page and readout (insight pages optional) into the UX research space after a preview and an explicit yes, and writes the URLs back to the notes.
*Why:* that is where product and design already read; Rovo indexes it; no new tool for readers.

**D15 · 2026-11-19 · Scripts run with `uv run` and declare their dependencies inline.** No `python3 …`, no virtualenv.
*Why:* a fresh clone on a new Mac failed on `import yaml`; with inline metadata the only prerequisite is `uv`.

**D16 · 2026-11-20 · The demo repository is public, temporarily.** `exidium/obsidian4Research` was made public for the director demo; it returns to private afterwards. Real studies go only to the organisation's internal GitHub.
*Why:* the demo data is entirely fictional; a private repository shows a 404 to anyone not signed in.

**D17 · 2026-11-23 · Obsidian stays; VS Code is plan B.** Alternatives were weighed (VS Code with Markdown extensions, GitHub alone, Confluence plus Jira as the gate, Logseq and others, the existing SaaS, a custom web app). None matched Bases, block badges and embeds at zero infrastructure. The files are viewer-independent, so switching later costs the viewer, not the system.
*Why:* Obsidian is free for commercial use since 2025 and a local app; the ask to IT is "install an app", not "approve a service".

**D18 · 2026-11-23 · The review page is `02 highlights review`.** Renamed from "insights review" across templates, scripts and the demo.
*Why:* it reviews highlights; the old name misled the first viewer.

**D19 · 2026-11-23 · Three surfaces only; no third, visual UI.** SharePoint, GitHub, Confluence. No artifact, explorer or hosted web application for readers.
*Why:* readers who want something visual have Confluence and the SharePoint folder; a third copy of the data on another host adds an approval and a maintenance burden for no new capability.

**D20 · 2026-11-23 · Restricted studies are SharePoint-only folders.** The whole study folder lives in a SharePoint area with its own permissions, synced and dropped into `10 Projects/`, ignored by the main repository. No second repository. Trade-off accepted: no git history or pull-request review for those studies.
*Why:* GitHub permissions stop at the repository; a few sensitive studies with two or three people do not justify a repository each.

**D21 · 2026-11-23 · Question-askers get a Claude Project synced from GitHub, or Rovo.** Project knowledge: `e_insights`, `c_highlights`, `20 Participants`, `30 Personas`; never `b_sources`. No clone, no install. Claude Code on the web for someone who also wants to change something.
*Why:* a fifteen-minute install for a question was too much; Rovo covers what is published, the Project covers the evidence behind it.

**D22 · 2026-11-23 · Two upload routes, processing laptop-first.** Text through the GitHub web page into `00 Inbox/<project>/`; recordings into the SharePoint study folder's `Inbox/`, synced to `_raw/<project>/inbox/`. Both are processed by a researcher saying "ingest everything waiting" (or a morning `launchd` job). A GitHub Action is optional for text; a hosted machine is the post-pilot request.
*Why:* nobody should need git to contribute material; there is no runner yet, and the pilot must not depend on one.

**D23 · 2026-11-23 · Parked: Miro import and research-to-roadmap alignment.**
*Why:* neither blocks the pilot; both need the pilot's lessons first.

**D24 · 2026-11-24 · Hosted machine design.** An IT-owned machine with OneDrive and the repository runs the same skills headless on a schedule: local Whisper, ingest and automatic tagging, health gate, clips to SharePoint, a pull request per source, never a write to `main`. Only pseudonymised text leaves the machine. Publishing to Confluence stays a human action. Restricted studies are outside its scope. Requests, in order: machine, SharePoint service account, GitHub deploy key, Claude credential, egress, owner.
*Why:* the only way to process recordings unattended; the pilot proves the steps first, the machine only changes where they run.

**D25 · 2026-11-24 · Documentation lives in `_system/docs/`.** `README.md` is the front door, `GETTING STARTED.md` the onboarding, `operating-model.md` the organisational design, `decisions.md` this log, `demo-runsheet.md` the demo, `_system/schema.md` the note schema. Every non-obvious decision is appended here with its reason.
*Why:* the system is meant to be run by people who did not build it.
