# Operating model

How the research repository runs inside the organisation: which systems hold what, who uses which, how access is controlled, how material gets in, and where the skills run now and later. The vault itself is described in `README.md` and `_system/schema.md`; the reasons behind each choice are in `decisions.md`.

## 1. Three surfaces

| Surface | Holds | Who touches it |
|---|---|---|
| **SharePoint**, one study folder per project, synced with OneDrive | recordings, clips, reels, the participant key, an `Inbox/` for drops; the complete folder of a restricted study | researchers with rights to that study |
| **GitHub**, one research repository on the internal instance | the vault: project pages, transcripts, highlights, tags, insights, deliverables, skills, scripts | researchers (write), question-askers (read) |
| **Confluence**, the UX research space | study pages, insights, readouts, published from the vault | everyone; Rovo indexes it |

Nothing else. No separate web application, no explorer page, no third user interface. People who want something visual use Confluence; people who need the raw material and have the rights use the SharePoint folder.

## 2. Three kinds of people

| | Readers | Question-askers | Researchers |
|---|---|---|---|
| Who | product, design, management, most of the company | people who want the evidence behind an insight | the research team |
| Get | Confluence pages; Rovo for questions over what is published | a Claude Project whose knowledge is synced from GitHub: `e_insights`, `c_highlights`, `20 Participants`, `30 Personas`, never `b_sources`. They ask in plain chat; answers carry highlight IDs | repository write, Obsidian, Claude Code, the SharePoint study folders synced into `_raw/` |
| Setup | none | none; one person creates the Project and re-syncs it | `GETTING STARTED.md`, about 15 minutes plus the `_raw/` sync |
| Alternative | | Claude Code on the web opens the repository in a cloud sandbox for someone who also wants to change something | |

## 3. Access model

GitHub permissions stop at the repository: nobody can be given folder A without folder B. The model follows from that.

- **Normal studies** live in the shared repository. The whole research team sees all of them. This is the normal case and the point of a repository.
- **Restricted studies** are SharePoint-only. The study folder, in full (vault pages and `_raw/` material), lives in a SharePoint area whose permissions name the two or three people allowed in. Each of them syncs it and drops it into `10 Projects/` of their vault; the main repository ignores that path. Boards, scripts and skills work across it; nobody else has the folder or knows it exists. What is given up: git for that study (no history, no pull-request review, and simultaneous edits produce an OneDrive conflict copy). Accepted for a handful of sensitive studies. A restricted study that grows can get its own repository later without moving anything.
- **Recordings** have SharePoint permissions per study, independent of text access. Someone can hold a study's text and not its video.
- **Administrators** own `_system/` (taxonomy, templates, scripts, skills). CODEOWNERS on that path plus branch protection on `main` mean a change there needs an administrator's approval before it lands. Workspace tags are administrator-controlled; project tags belong to the project.
- **Viewers** have Confluence permissions and no GitHub account.
- **Downloads**: anyone with read on the repository can clone all of it. That is accepted for pseudonymised text; it is why recordings and names never enter the repository and why restricted studies are not in it.

## 4. Getting material in

| Material | Route | Then |
|---|---|---|
| Transcript (VTT, SRT, text, Dovetail export) | GitHub web page → `00 Inbox/<project>/` → "Add file → Upload files" → commit. No git installed. | a researcher says "ingest everything waiting" |
| Recording (with or without its VTT) | the study's SharePoint folder → `Inbox/` | syncs to `_raw/<project>/inbox/`; the same command |
| Reference documents (PRD, brief, competitive analysis) | `b_sources/reference/` through either route | `research-ingest` as a reference note |

Both inboxes end in `research-ingest` → source note → `research-highlight` → proposed highlights on `02 highlights review`. The browser upload bypasses the local pre-commit hook, so `.gitignore` refuses media under `00 Inbox/` and the health check catches size and identity on the next run. Recordings go to SharePoint, never to GitHub.

## 5. Where the skills run

The skills are files in the repository (`.claude/skills/`), but they only do anything where Claude Code runs.

**Now: the researcher's laptop.** On demand ("ingest everything waiting"), or a `launchd` job running `claude -p "ingest everything waiting"` every morning. Same seat, same data path as interactive use. The laptop has to be on; that is the only limitation. This is enough for the pilot.

**Optional, if easy to obtain: a GitHub Action.** Runs the same skills on every push to `00 Inbox/` and opens a pull request. Needs Actions with a runner, a service credential for Claude stored as a repository secret, and the Claude Code action allowed. It never sees SharePoint, so it handles text uploads only.

**After the pilot: a hosted machine.** The only option that processes recordings unattended. Described below.

## 6. The hosted machine

A researcher's laptop that never goes home: the same vault, skills and scripts, on an IT-owned machine, on a schedule.

```
  PEOPLE                      SHAREPOINT                            HOSTED MACHINE (IT-owned, always on)
  ──────                      ──────────                            ────────────────────────────────────
                                                                    ┌──────────────────────────────────────┐
  researcher ──(1) drops ──▶  Study folder/                         │  OneDrive client (service account)    │
  recording + VTT             ├─ Inbox/            ◀──(2) sync──▶   │   _raw/<study>/inbox/   ← mirror     │
                              ├─ S-0004.mp4                         │   _raw/<study>/         ← mirror     │
                              ├─ clips/  reels/                     │   _raw/participants/    ← key        │
                              └─ participants/ (key)                │                                      │
                                                                    │  (3) scheduler: every 15 min / 07:00  │
  anyone ──(1b) uploads ──▶  GITHUB                                 │       └─▶ ingest.sh                   │
  transcript in browser       research repo                         │            │                          │
                              ├─ 00 Inbox/<study>/ ◀──(2b) pull──▶  │  (4) whisper, local  ─▶ transcript    │
                              ├─ 10 Projects/      ◀──(8) PR ─────  │  (5) claude -p "ingest everything     │
                              └─ .claude/skills/   ── same skills ▶ │        waiting"  (research-ingest +   │
                                      ▲                             │        research-highlight, auto mode) │
                                      │                             │        │ pseudonymised text only ─────┼──▶ Claude API
  researcher ◀──(9) PR + board ───────┘                             │        ▼                              │
  accepts / rejects in Obsidian,                                    │  (6) health.py ─ fail ─▶ notify, stop  │
  merges                                                            │        │ pass                         │
                                                                    │  (7) media.py link / clip → _raw/     │──▶ back to SharePoint via sync
                                                                    │  (8) git branch ingest/S-0004, push,  │
                                                                    │      open pull request                │
                                                                    └──────────────────────────────────────┘
  (10) publish to Confluence: still a human saying "publish", from any laptop
```

1. **Drop.** A researcher saves the recording and its VTT into the study's SharePoint `Inbox/`. Text-only material goes in through the GitHub web page (1b). Nobody runs anything.
2. **Sync.** The machine's OneDrive client, under a service account scoped to the study folders, mirrors them into `_raw/`. The participant key is in SharePoint too, so the machine can pseudonymise. `git pull` brings the GitHub inbox (2b).
3. **Trigger.** A scheduler runs `ingest.sh` every 15 minutes, or once a morning. Empty inboxes mean nothing happens.
4. **Transcribe locally.** A recording without a VTT goes through Whisper on the machine. Audio never leaves it.
5. **Skills, headless.** `claude -p "ingest everything waiting"` is Claude Code without a terminal, obeying the vault's `CLAUDE.md` and skills exactly as on a laptop. Source note (speakers mapped to `P-###`, PII scan, block IDs, recording linked with checksum and moved out of `Inbox/`), then every highlight as `proposed` with confidence. The only thing leaving the machine is pseudonymised text to the Claude API under the organisation's plan: the same path the laptop already uses.
6. **Health gate.** `health.py`. On failure nothing is pushed and the owning researcher is notified with the report.
7. **Media.** Clips for the new highlights are rendered into `_raw/<study>/clips/` and sync back up to SharePoint. No video touches GitHub.
8. **Pull request.** Commit on `ingest/S-0004`, push with a deploy key, open a pull request: "S-0004 ingested, 24 highlights proposed: 15 high, 7 medium, 2 low". Hook and PII scan run again on the server side.
9. **Human gate.** The researcher reads the pull request or the board, accepts and rejects, merges. The machine never writes to `main`.
10. **Publish stays human.** Synthesis, the readout and Confluence are a person's decision, from any laptop.

A nightly pass refreshes the cheap and safe things: `personas.py refresh`, `tag_board.py`, reels for insights that changed, `health.py` with its report. Also on a branch, also a pull request.

**What the machine holds and sends.** Holds: the repository, the mirrored study folders including the key, a Claude credential, a GitHub deploy key, a SharePoint service account; all owned by IT, no personal credentials. Sends out: pseudonymised text to the Claude API and to GitHub. Never a recording, never a name, never anything to Confluence on its own. Restricted studies are outside the service account's scope, so the machine never sees them; their researchers process them on their own laptops.

**What to request, in order.**

1. A machine: a Mac mini if local Whisper stays on `mlx_whisper` (the scripts as they are), or a Linux or Windows VM with `faster-whisper` on CPU (a one-file change). IT-managed, always on, no user sessions.
2. A SharePoint service account scoped to the study folders, and the OneDrive client allowed on that machine.
3. A GitHub machine user or deploy key with write to branches and no write to `main`.
4. A Claude credential for a non-person (an API key under the organisation's plan, or a Claude Code token), kept in the machine's keychain.
5. Network egress from that machine to the Claude API and to GitHub, nothing else.
6. An owner: who receives failure notifications and who rotates the credentials.

Items 1, 2 and 4 take time; 3, 5 and 6 take days. The pilot on a laptop proves steps 4 to 9 with real recordings; the machine only changes where they run.

## 7. The pilot

One current, well-organised study, run in the company environment on a researcher's laptop, compared against the existing process. It must show:

- onboarding from `GETTING STARTED.md` by someone who did not build the system;
- a real Teams recording through `media.py link` and `research-clip` (codec, gallery layout for the redaction regions, VTT speaker labels, two-hour sessions);
- whether a transcript line can seek the video (Media Extended plugin, `[[S-0004.mp4#t=290]]`); if yes, `build_source.py` adds a ▶ link per block; if no, clip-per-highlight is the documented path;
- the review gate against a researcher's manual scan for omissions;
- publishing to the real Confluence space.

Open with others: the internal GitHub repository; the SharePoint location and its permissions, with a legal review of the move from Dovetail.

## 8. Parked

- Miro import (board → source note with the board as origin; or PDF through the inbox).
- Linking findings to roadmap decisions (opportunity maps: problem → evidence → solution hypotheses).
