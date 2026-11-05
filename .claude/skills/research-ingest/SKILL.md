---
name: research-ingest
description: Turn a recording or transcript into an immutable source note in the research vault. Use when the user says "ingest", "transcribe", "add this interview/session/recording", "import the Teams/Krisp transcript", or drops a file in 00 Inbox and names a project and participant. Handles video, audio, Whisper JSON, SRT/VTT, and plain-text transcripts. Produces sources/S-####.md with stable block IDs, speakers, a summary, and a provenance entry.
---

# research-ingest

Everything downstream (highlights, insights) hangs off the source note this skill writes, so the one rule that matters: **get the transcript right once, then never touch it again.**

## Inputs to establish

Collect before running anything. Ask only for what you can't infer.

| Field | Where it comes from |
|---|---|
| `project` | Folder name under `10 Projects/`. List them if unknown. If it doesn't exist, stop and run `research-organize` → new project first. |
| `participant` | `P-###`. If the user gives a name, do **not** write it anywhere; run `python3 _system/scripts/next_id.py participant` for a new ID and tell the user to add the row to `_raw/participants.csv` themselves. |
| `rally_id` | Consent record reference. Ask once; empty is allowed but gets flagged in audits. |
| `date`, `method`, `language` | From the user or the file. Default method `method/interview`, language `en`. |
| input file | Path in `00 Inbox/` or anywhere local. |

## Procedure

### 1. Classify the input

- **Video or audio** (`mp4 mov m4a mp3 wav webm mkv`): go to step 2.
- **Whisper JSON, SRT, VTT**: go to step 3.
- **Plain text or Markdown** with `Speaker: text` paragraphs: go to step 3.
- **Krisp transcript**: if the user prefers Krisp for speaker names, use the Krisp connector to fetch the transcript as text, save it to `00 Inbox/`, then go to step 3.

### 2. Transcribe locally

```bash
mkdir -p "_raw/<project>"
bash _system/scripts/transcribe.sh "<media>" "_raw/<project>" mlx-community/whisper-large-v3-turbo [en|pt|de]
```

Takes a few minutes per hour of audio on Apple Silicon. Then move the media out of the inbox: `mv "<media>" "_raw/<project>/"`. The JSON path printed on the last line is the input for step 3. Whisper output has no speakers; step 4 handles that.

### 3. Build the source note

```bash
python3 _system/scripts/build_source.py --input "<file>" --project <project> --participant P-### \
  --date YYYY-MM-DD --method method/interview --rally-id "<id>" --language en \
  --origin "_raw/<project>/<file>" --transcriber "mlx-whisper/large-v3-turbo|teams|krisp|manual" \
  [--speaker-map "Name As It Appears=P-###,Other Name=Interviewer"]
```

- The script replaces any unmapped speaker name with `Speaker-N` and tells you how many it replaced, without printing the name. If it reports replacements, ask the user for the mapping and re-run with `--speaker-map` after deleting the note it wrote.
- Never pass `--source-id` unless re-ingesting a specific archived ID on purpose.
- Read the printed path. Open the note and skim the transcript once, end to end.

### 4. Speakers, if missing

If paragraphs have no `**Speaker:**` prefix (Whisper output), assign them: `**Interviewer:**` for the researcher, `**P-###:**` for the participant. Edit **only** the prefix of each paragraph. Do not reword text, merge or split paragraphs, or touch the trailing `^s####-####` IDs. Then set `speakers_inferred: true`.

Two-person interviews are reliable. For three or more voices, label what you can and tell the user which paragraphs you were unsure about.

### 5. Redact

Names, employers, emails, and phone numbers must not survive in the vault. Replace:

- participant name → `P-###`; interviewer name → `Interviewer`; colleagues → `[colleague]`
- employer or customer company → `[company]`; a named competitor product is fine to keep
- email/phone → `[email]` / `[phone]`

Only the replaced token changes; block IDs stay. Then run the check and set the property:

```bash
python3 _system/scripts/scan_pii.py "10 Projects/<project>/sources/S-####.md"
```

Zero findings → set `redacted: true`. The scan only knows names listed in `_raw/participants.csv`, so still read for names yourself.

### 6. Summary

Fill `## Summary` with five bullets: who the participant is in task terms (segment, not title), what they were doing, the three most concrete things they said. Describe, don't interpret. Interpretation belongs in highlights.

### 7. Finish

```bash
bash _system/scripts/provenance.sh research-ingest ingest S-####
```

Report: source ID, paragraph count, duration, whether speakers were inferred, anything you were unsure about. Suggest the next step: `research-process` → highlight S-####.

## Never

- Modify transcript text after the note is written, except speaker prefixes and redaction tokens in this same run.
- Write a real name anywhere, including this conversation's summaries.
- Read `_raw/participants.csv`.
- Ingest the same recording twice under two IDs without archiving the first.
