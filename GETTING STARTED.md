# Getting started on a new computer

Two audiences: a **researcher** who will run studies in the vault, and a **reader** (PM, designer, manager) who only wants to browse. Readers need steps 1 to 3 and the "Finding your way" section. Researchers need everything.

## 1. Install (15 minutes, macOS)

```bash
# Tools
brew install git uv ffmpeg                 # git for the vault, uv runs the scripts, ffmpeg cuts clips
brew install --cask obsidian               # the vault browser
npm install -g @anthropic-ai/claude-code   # the skills runner (or: brew install --cask claude-code)
uv tool install mlx-whisper                # local transcription, Apple Silicon only (optional for readers)

# The vault
cd ~/Projects
git clone https://github.com/exidium/obsidian4Research.git    # ADI: the internal GitHub URL instead
cd obsidian4Research
bash _system/scripts/install_hooks.sh      # pre-commit hook: blocks _raw/ and scans for names
uv run _system/scripts/health.py           # should print five ok; "no local copy" of a recording is expected, see step 4
```

`claude` needs an Anthropic login the first time you run it (`claude` then `/login`). The vault's `.claude/settings.json` already allows the pipeline scripts and denies the agent any read of `_raw/`; nothing to configure.

## 2. Open the vault in Obsidian

Obsidian → Open folder as vault → choose `obsidian4Research`. When it asks whether to trust the vault's plugins, say yes: the only community plugin is **Strange New Worlds**, shipped in `.obsidian/plugins/`, and it is what shows the highlight badges in transcripts. Bases (boards and tables) and Canvas are core plugins and are already on. The CSS snippet that draws lines under headings is already enabled.

Switch to **Reading view** (Cmd+E) for the project pages; it renders the boards, callouts and embeds. Live Preview also works.

If a board shows as a grey box: Settings → Core plugins → Bases is off. Turn it on.

## 3. Look around (10 minutes)

Open `10 Projects/2026_demo-fluxbench/01 project`. It is a complete, fully fictional study, run through the whole pipeline. Use it as the map:

1. **Contents** at the top of the page: Study overview (introduction, research questions, participants), Findings (reports, insights), Operations & data (links to the review board and the tag board).
2. **Participants table** → click a persona (`PE-01 …`) → "Where they appear" lists the projects, insights and highlights behind that persona.
3. **Insights table** → open `I-…-01` → the evidence blocks are highlights. Click one (`H-S0001-0006`): verbatim quote, tags, confidence, and "Open in transcript", which lands on the exact line in `b_sources/S-0001`. In the transcript, the badge beside a block means a highlight references it; hover to see which.
4. **02 highlights review**: the Kanban of highlights waiting for a decision. Drag a card between proposed / accepted / rejected; that changes its `review` property.
5. **03 tag board**: tags as lanes, highlights as cards, one board per tag group. Click a tag for its definition and every highlight that carries it.
6. **f_deliverables**: the readout written from the insights.

Vault-wide: `20 Participants/` (one card per person, no names), `30 Personas/`, `_system/tag-board.md` (all tags across projects), `README.md` (what the skills do), `_system/schema.md` (every property of every note type).

## 4. Media, names and the raw zone

`_raw/` is gitignored. It is the only place that holds recordings, clips, reels and the participant key (names, employers, Rally IDs). It never travels through git.

- **In production** `_raw/<project>/` is the OneDrive-synced SharePoint study folder: open the folder in Finder, "Add shortcut to OneDrive", and symlink or copy it into `_raw/`. Clips and reels regenerate from the recordings.
- **For the demo on a new machine** copy `_raw/` from the old one (AirDrop, USB, or `rsync -a old:~/Projects/obsidian4Research/_raw/ _raw/`). It is about 300 MB. Without it, everything text-based works; the clip embeds show as missing files, `participants.py sync` has no export to read, and `media.py check` prints "no local copy" for each recording. That is expected and blocks nothing.
- To regenerate the demo from scratch instead (needs only the mock Rally export `_raw/rally/participants.json`): the commands are in `README.md` → Demo.

## 5. Your first study, as a researcher

Open a terminal in the vault folder and start `claude`. Then talk to it; the skills answer to plain language. In order:

| Step | Say | What happens |
|---|---|---|
| Create | "new project: discovery on LTpowerCAD export, 6 external interviews" | `10 Projects/2026_…/` with `01 project`, `02 highlights review`, `03 tag board`, folders `a_setup` … `f_deliverables`, seed tag groups in `d_tags/tags.yaml`, SETUP templates |
| Fill in | write the introduction and the discussion guide in `01 project` and `a_setup/` | or ask Claude to draft them from your brief |
| Participants | export the study from Rally to `_raw/rally/`, then "sync participants" | cards in `20 Participants/`, identities in `_raw/`, a persona per participant (or a new one proposed for you to confirm) |
| After each interview | drop recording + transcript in `00 Inbox/`, then "ingest the inbox for P-004" | source note, pseudonymised, PII scanned, recording linked; then tagging runs by itself and reports "24 highlights proposed: 15 high, 7 medium, 2 low" |
| Review | open `02 highlights review`, or "accept everything high from S-0004, reject 12 and 19" | the human gate; nothing proposed goes further |
| Synthesize | "synthesize the project" | insight notes from accepted highlights, with evidence levels and recommendations; you edit and mark them reviewed |
| Report | "write the readout for the product owner" | `f_deliverables/Readout - ….md`, registered in the Reports table |
| Share | "publish the study to Confluence" | preview, your yes, then the page tree under SDP UX Research; URLs written back |
| Video | "clip H-S0004-0007", "reel for insight 02" | blurred, captioned, stamped clips and reels in `_raw/<project>/` |
| Keep clean | "health check" before every commit | audit, PII scan, recordings, cards, personas, dated report in `_system/reports/` |

Commit and push when a step is done; the pre-commit hook refuses anything from `_raw/` or anything that looks like a name. Every AI action is a line in `_system/provenance.log`.

The scripts behind the sentences, if you prefer the terminal: `uv run _system/scripts/<script>.py` with no arguments prints its usage. The ones you will use most are `review.py`, `media.py`, `participants.py`, `health.py`.

## 6. Rules you must know (the rest are in CLAUDE.md)

- Never edit a transcript after ingest; never change a block ID.
- Never put a name, employer or recording outside `_raw/`. Participants are `P-###`.
- Never move a `proposed` highlight into an insight, a report or Confluence yourself; accept it first.
- Never hand-edit the generated files (`a_setup/boards/`, `d_tags/<group>/`, `03 tag board.md`); the scripts rewrite them.
- Link notes by file name, with the ID as the display text. A bare `[[H-S0001-0006]]` does not resolve.

## 7. Windows or Linux

Everything except transcription and the demo voices works: `uv`, `ffmpeg`, `git` and Obsidian exist on all three. `mlx_whisper` is Apple Silicon only; on other machines, take the Teams transcript (VTT) and skip `transcribe.sh`. `demo_recording.py` uses macOS `say` and is demo-only.

## When something looks wrong

| Symptom | Cause | Fix |
|---|---|---|
| `health.py` fails on PII | a name reached a note | the report names the file; move the text to `_raw/` or replace with the ID |
| Clip embed shows "file not found" | `_raw/` not copied, or recording replaced | copy `_raw/`; `media.py check` says which |
| Board is empty | Bases off, or you are in Source mode | enable Bases, Cmd+E |
| No badges in transcripts | Strange New Worlds not trusted | Settings → Community plugins → enable |
| Claude says "X is not a function" after a pull | stale script cache | restart `claude` |
| Pre-commit blocks a commit | `_raw/` staged or a suspected name | `git restore --staged _raw`; or fix the file the hook names |
