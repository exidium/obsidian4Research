# Demo run sheet: research repository on tools ADI already runs

20 minutes, one project (`2026_demo-fluxbench`, all synthetic), two windows side by side: Obsidian on the vault, a terminal in the vault folder with `claude` running. Confluence in a browser tab behind them.

## The night before

1. `cd ~/Projects/obsidian4Research && git pull && uv run _system/scripts/health.py` must print five `ok`.
2. `uv run _system/scripts/media.py check` must list S-0001 to S-0003 as present and unchanged. Play `_raw/2026_demo-fluxbench/clips/H-S0001-0006.mp4` once in QuickTime: picture, caption, audio.
3. `uv run _system/scripts/review.py pending` must show 35 pending (11 / 12 / 12). Do not accept them before the demo; they are the board.
4. Obsidian: open the vault, Reading view, zoom in twice (Cmd and `=`). Open and pin, in this order: `01 project`, `02 highlights review`, `I-2026_demo-fluxbench-01 …`, `S-0001`, `PE-01 …`. Close everything else. Check that Strange New Worlds badges show in `S-0001` and that the review board renders as a Kanban.
5. Terminal: font 18 or larger, `cd ~/Projects/obsidian4Research`, start `claude`, run `/skills` once so the list is cached, then type `uv run _system/scripts/review.py pending` so it is in the history.
6. Browser: logged in to analog.atlassian.net, tab open on the study page `SDPUXR/pages/388542371`, second tab on the readout `388542423`.
7. Do Not Disturb on, Slack and Teams closed, Dock hidden.
8. Say once at the start: participants, companies, voices and recordings are synthetic. The method is real, the data is not.

## The 20 minutes

### 0. Frame it (2 min, no screen)

Today a study's evidence is spread over Teams recordings, OneNote, Dovetail and decks; six months later nobody can find why a decision was made. This is a research repository built only from what ADI already runs: SharePoint for media, GitHub for the text, Confluence for findings, Claude for the work. Everything traces from a claim in a Confluence page to a second in a recording.

### 1. The project page (3 min, Obsidian)

Open `01 project`. Scroll the contents list; the study overview, questions, participants. Point at the participants table: role, experience, market, and a persona on every participant. Click `PE-01 Design engineer who trusts a result only after it matched the bench`: Jobs to be done, and "Where they appear" with the projects, insights and highlights that persona produced. Back.

Say: participant identity never enters this vault. Cards hold role and market; names stay in Rally and in a local file that git refuses to commit.

### 2. The evidence chain (4 min, Obsidian)

Open insight `I-01`. Evidence level, the recommendation, then the evidence blocks. Click one highlight (`H-S0001-0006`). On the highlight: the verbatim quote, tags, confidence, and the clip embedded under the block. Press play, 15 seconds: blurred face, blurred name plate, caption, the stamp with participant, source, timestamp and highlight ID.

Click "Open in transcript". You land on the line in `S-0001`; the badge beside it shows it is referenced by a highlight, and the surrounding lines show the ones that are not.

Say: the recording is 65 minutes in SharePoint; the clip was cut by a script from the block's timestamp; git only ever holds the pointer and a checksum. If anyone replaces the file, the health check says so.

### 3. Automatic tagging and the human gate (4 min, terminal and Obsidian)

Terminal: `uv run _system/scripts/review.py pending`. Three sources, 35 proposals waiting.

Obsidian: open `02 highlights review`. The board: proposed, accepted, rejected, every card with its confidence. Drag one card from proposed to accepted.

Terminal, in Claude: type `accept everything from S-0001`. Claude runs the accept command; the board updates when you switch back (11 cards moved). Say: an hour of interview produces 20 to 30 highlights in a few minutes; the researcher reads the low-confidence ones and skims the rest. Nothing proposed reaches an insight, a report or Confluence until a person accepts it. Every decision is logged with who made it.

If asked "can I see it tag something live": say yes, it takes about four minutes per hour of transcript, and offer to run `tag S-0003` after the meeting. Do not start it live.

### 4. Where the product team sees it (3 min, browser)

Confluence study page under SDP UX Research › Projects › 2026: the same page, with the insights and the readout, published from the vault by a sentence ("publish the study"). Open the readout: findings, quotes with highlight IDs, recommendations in order. Say: PMs never open Obsidian; they find this in Confluence search and Rovo. Then, back in Obsidian or QuickTime, play the first 20 seconds of reel `I-01` (`_raw/2026_demo-fluxbench/reels/I-2026_demo-fluxbench-01.mp4`): one video per insight, every cited highlight in sequence, for the readout meeting.

### 5. What runs it (2 min, terminal)

`ls .claude/skills` and open `research-highlight/SKILL.md` for ten seconds: the procedure is text, versioned with the vault, reviewable like code. `tail -5 _system/provenance.log`: every AI action with skill, source and model. `git log --oneline | head`: the whole history.

### 6. The ask (1 min)

One real study as a pilot: a SharePoint folder for the recordings, a repo on the internal GitHub, the SDP UX Research space we already have. Four weeks, one researcher, then decide.

## Live commands (copy from here)

```
uv run _system/scripts/review.py pending
uv run _system/scripts/review.py accept --source S-0001
uv run _system/scripts/media.py clip H-S0002-0004
uv run _system/scripts/health.py
```

Or in Claude: "what's pending", "accept everything from S-0001", "clip H-S0002-0004", "health check".

## Reset after a run

The live accept changes 11 highlight files. To put the board back for the next run:

```
git checkout -- "10 Projects/2026_demo-fluxbench/c_highlights"
```

and delete the last 11 `review-accepted` lines from `_system/provenance.log` (or leave them; nothing reads them during the demo).

## If something breaks

- Board does not render: scroll down on `02 highlights review` to the "Pending review" table, same data.
- Clip has no sound: say the voices are synthetic and show the transcript line instead; the stamp still proves the trace.
- Confluence is slow: the readout is the same text as `f_deliverables/Readout - FluxBench Designer Trust.md` in Obsidian.
- Claude does not answer: every sentence above has its command in "Live commands".

## Questions to expect

- **Where does the data live?** Media in SharePoint (never in git), transcripts and findings in GitHub as text, published findings in Confluence. One place per kind, all three already approved at ADI.
- **PII?** Names and employers exist only in `_raw/`, which the pre-commit hook refuses, and a scanner runs on every commit. Cards carry role, market and consent flags.
- **Does the AI decide what the findings are?** It proposes highlights with a confidence rating and drafts insights; a researcher accepts, rejects and rewrites. The gate is the review, and it is logged.
- **What does it cost?** Claude Code seats and the time of the researcher. No new SaaS, no per-seat research tool.
- **What about Dovetail?** The tag taxonomy is the same one; existing projects can be migrated study by study. Nothing has to move on day one.
- **Can another researcher use it?** Clone the repo, open it in Obsidian, the skills come with it. PMs need nothing but Confluence.
- **What happens when the recording changes?** The checksum fails the health check; clips stop until it is explained.
