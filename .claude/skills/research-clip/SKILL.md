---
name: research-clip
description: Attach interview recordings to source notes and cut pseudonymised video clips and highlight reels from them, without putting any video in git. Use when the user says "link the recording", "attach the video to S-####", "make a clip of H-…", "clip this highlight", "make a reel for insight I-…", "showreel", "blur the name/face", or "check the recordings". Clips are cut at the highlight's quote using the transcript timestamps, blurred where the source says, captioned from the pseudonymised transcript, and stamped with participant, source and timestamp.
---

# research-clip

Video is the most persuasive evidence and the most identifying. The rules that follow from that:

- **Media never enters git.** Recordings, clips, reels and frames live in `_raw/<project>/` (gitignored; the pre-commit hook refuses `_raw/`). Notes carry pointers: a path, a SharePoint URL, a checksum, timestamps.
- **In production, `_raw/<project>` is the OneDrive-synced SharePoint study folder** (or a symlink to it). Everyone with access to the study folder gets working embeds; everyone else sees a pointer. Removing a withdrawn participant's media is a SharePoint delete, not a git history rewrite.
- **Internal participants get no voice or video** (`participant_type: internal-*`). Their clips are text cards with the quote. `--allow-internal` exists for the research team's own review only; never use it for anything that will be shared.
- **Every clip is stamped** `P-### · S-#### @ hh:mm:ss · H-… · pseudonymised`, so any clip shown in a meeting traces back to its transcript line and recording.

All commands run from the vault root with `uv run` (installs Pillow and PyYAML on first use; needs `ffmpeg` and, for exact quote edges, `mlx_whisper`).

## 1. Link a recording to a source

After `research-ingest` has written the source note:

```bash
uv run _system/scripts/media.py link S-0004 "<path to recording>" [--url "<SharePoint link>"]
```

Moves the file to `_raw/<project>/S-0004.<ext>` and writes `recording`, `recording_url`, `recording_sha256`, `recording_duration` into the source frontmatter. Frontmatter only: the transcript is untouched.

## 2. Decide what to blur

```bash
uv run _system/scripts/media.py frame S-0004 00:05:00
```

Writes a still to `_raw/<project>/frames/`. The vault's settings stop you reading `_raw/`, and that is deliberate. **Ask the user** whether you may look at this one frame to place the boxes. If they agree, they grant the read; if not, they give you the boxes (Preview → Tools → Show Inspector shows pixel coordinates). Typical regions: the participant's name plate, their camera tile (face), a company logo or a screen share. Then re-link with the regions:

```bash
uv run _system/scripts/media.py link S-0004 "_raw/<project>/S-0004.mp4" --redact 658,476,318,42:name-plate --redact 857,198,176,176:face
```

Regions are fixed rectangles in recording pixels, blurred for the whole clip. A face that moves around the frame needs tracking, which this prototype doesn't do: say so rather than pretend.

## 3. Clip a highlight

```bash
uv run _system/scripts/media.py clip H-S0004-0007            # just the quote
uv run _system/scripts/media.py clip H-S0004-0007 --context  # the interviewer's question + the whole answer
uv run _system/scripts/media.py clip H-S0004-0007 --whole    # the whole turn, no question
```

How the edges are found: the highlight's block gives the turn's timestamp; the next turn's timestamp bounds it; trailing silence trims it; then local Whisper word timestamps find the quote inside the turn (falls back to pause detection if Whisper is missing). Output `_raw/<project>/clips/H-….mp4`; the highlight gets `clip`, `clip_kind`, `clip_start`, `clip_end` and an embed under its transcript block.

Check the result before anyone else sees it: read back `clip_start`/`clip_end` against the transcript, and for anything going to stakeholders, ask the user to watch it. If a clip starts or ends mid-word, re-run with `--whole`.

## 4. Reel for an insight

```bash
uv run _system/scripts/media.py reel I-<project>-02 [--context] [--force]
```

An intro card (finding, how many moments from how many participants, evidence level), then a numbered title card and a clip per cited highlight, in the order the insight lists them. Missing clips are cut on the way; `--force` recuts them. Output `_raw/<project>/reels/I-….mp4`; the insight gets `reel`, `reel_duration` and an embed under its heading.

To share a reel: upload it to the study's SharePoint folder (it's already there if `_raw/<project>` is the synced folder) and link it from the Confluence page, or attach it to the page so it plays inline. Never attach a reel that contains internal-participant video.

## 5. Check

```bash
uv run _system/scripts/media.py check [project]
```

Reports each recording as present and unchanged, missing locally (fine for people without access), or changed since it was linked (exit 1: someone replaced the file; investigate before cutting more clips).

## Provenance

`media.py` appends `link`, `clip` and `reel` lines to `_system/provenance.log` itself. Don't add them again.

## Don'ts

- Commit anything under `_raw/`, or move media out of it to make an embed work in GitHub.
- Read frames or recordings without the user's explicit OK for that file.
- Use `--allow-internal` for anything shared outside the research team.
- Edit the transcript to "fix" a clip. Clip edges come from the transcript; if it's wrong, re-ingest (see `research-ingest`).
- Run `demo_recording.py` on anything but the fictional demo project. It exists only to make synthetic recordings for demos.
