---
name: research-ingest
description: Turn a recording or transcript into an immutable source note (data entry) in the research vault, with ADI's source fields set. Use when the user says "ingest", "transcribe", "upload", "add this interview/workshop/feedback session", "import the Teams/Krisp/Dovetail transcript", or drops a file in 00 Inbox and names a project and participant. Handles video, audio, Whisper JSON, SRT/VTT, Dovetail markdown exports, and plain-text transcripts. Produces b_sources/S-####.md with stable block IDs, speakers, summary, fields, and a provenance entry.
---

# research-ingest

A source note is Dovetail's "data entry": one piece of primary research that participants generated. Everything downstream hangs off it, so the rule that matters: **get it right once, then never touch the transcript again.** Reference material (PRDs, SOWs, competitive reports) and stimulus are *not* sources; they go in `b_sources/reference/` or `a_setup/` (see `research-organize`).

## Fields to establish (Dovetail "fields": they describe the source, not what was said)

| Field | Values | Notes |
|---|---|---|
| `project` | folder under `10 Projects/` | If missing, stop: `research-organize` → new project first. |
| `entry_type` | interview, workshop, feedback, survey, test, observation, demo, diary | Drives the title prefix `[Interview]`. |
| `methodology` | user-interview, usability-test, workshop, survey, guerilla-testing, demo, card-sorting, diary-study | |
| `participant` | `P-###` | Never a name. New person → `uv run _system/scripts/next_id.py participant`, then ask the user to add the row to `_raw/participants.csv` themselves. |
| `participant_type` | external-customer, internal-stakeholder, internal-engineer | Essential for weighting findings. |
| `role` | free text, job role | e.g. "RF applications engineer". No employer names. |
| `software_used` | `software/*` tags | Tools the participant *uses*, not tools they mentioned. |
| `interviewer` | `P-###` of the researcher | |
| `rally_id` | consent record reference | Required for external participants; audited. |
| `date`, `language` | | Default language `en`. |

Ask only for what you can't infer from the file name, the project's Study Overview, or the participants table in `01 project.md`.

## Procedure

### 1. Classify the input

- **Video or audio** (`mp4 mov m4a mp3 wav webm mkv`) → step 2.
- **Whisper JSON, SRT, VTT (Teams)** → step 3.
- **Dovetail markdown export** (`**Name (m:ss):** text`, from the Dovetail MCP `get_data_content`) → save the markdown to `00 Inbox/`, then step 3. Speaker names in it must be mapped with `--speaker-map`; `[CONTEXT:]` lines become `**Note:**` paragraphs.
- **Plain text or Markdown** with `Speaker: text` paragraphs → step 3.
- **Krisp** → fetch the transcript via the Krisp connector when the user wants its speaker labels, save to `00 Inbox/`, step 3.

### 2. Transcribe locally (media only)

```bash
mkdir -p "_raw/<project>"
bash _system/scripts/transcribe.sh "<media>" "_raw/<project>" mlx-community/whisper-large-v3-turbo [en|pt|de]
mv "<media>" "_raw/<project>/"
```

Minutes per hour of audio on Apple Silicon. The JSON path on the last line feeds step 3. Whisper gives no speakers; step 4 handles that. ADI's rule: recordings go into the system of record within 48 hours; here that means the transcript is in the vault and the media is in `_raw/`. After step 3, attach the recording to the source note with `research-clip` (`media.py link`), so highlights can be clipped later.

### 3. Build the source note

```bash
uv run _system/scripts/build_source.py --input "<file>" --project <project> --participant P-### \
  --entry-type interview --methodology user-interview --participant-type external-customer --role "<role>" \
  --interviewer P-000 --rally-id "<id>" --date YYYY-MM-DD --language en \
  --origin "_raw/<project>/<file>" --transcriber "mlx-whisper/large-v3-turbo|teams|krisp|dovetail-export|manual" \
  [--speaker-map "Name As It Appears=P-###,Researcher Name=Interviewer"]
```

- Unmapped speaker names are replaced with `Speaker-N` and counted, never printed. If the script reports replacements, delete the note it wrote, get the mapping from the user, re-run.
- The title becomes `[Interview] P-### - DD Mon YYYY` automatically. Don't override unless the user has a reason.
- Never pass `--source-id` unless deliberately re-ingesting an archived ID.
- Skim the transcript once end to end. Technical terms and product names are where transcription errs; note anything that looks wrong for the user, but don't rewrite transcript text yourself beyond step 5.

### 4. Speakers, if missing

Whisper output has no `**Speaker:**` prefixes. Assign `**Interviewer:**` and `**P-###:**` by editing only the prefix of each paragraph. Don't reword, merge, split, or touch the trailing `^s####-####` IDs. Set `speakers_inferred: true`. Two voices are reliable; for three or more, label what you can and tell the user which paragraphs you were unsure about.

### 5. Redact

Names, employers, emails, phone numbers must not survive in the vault. Replace: participant → `P-###`; interviewer → `Interviewer`; colleagues → `[colleague]`; employer or customer company → `[company]`; email/phone → `[email]`/`[phone]`. Named ADI products and competitor products stay (they are tagged later). Then:

```bash
uv run _system/scripts/scan_pii.py "10 Projects/<project>/b_sources/S-####.md"
```

Zero findings → `redacted: true`. The scan only knows names in `_raw/participants.csv`, so still read for names yourself.

### 6. Summary and fields

Fill `## Summary` with five descriptive bullets: who the participant is in task terms, what they were doing, the three most concrete things they said. No interpretation; that is the highlight's job. Set `software_used` from what the participant says they use. Add the participant to the Study Overview's participants table (ID, type, role, date, status).

### 7. Finish

```bash
bash _system/scripts/provenance.sh research-ingest ingest S-####
```

`ris_status` stays `raw` until highlighting starts. Report: source ID, title, paragraph count, duration, speakers inferred or not, transcription doubts. Then: `research-clip` → `media.py link S-#### <recording>` to attach the recording (and decide the blur regions), and `research-participants` → `check` so the participant has a card and a persona. Then **run `research-highlight` in auto mode on the new source without being asked**: tagging is automatic; the researcher reviews the result on the board. Report both steps together: source written, N highlights proposed (by confidence), board link.

## Imports from the systems ADI already runs

| Source | How it arrives | What to do |
|---|---|---|
| **Teams recording** | The organiser downloads the recording and the VTT transcript from Stream/SharePoint (recordings don't land in a shared folder by themselves) and drops both in `00 Inbox/`. | VTT → step 3 with `--transcriber teams`. Teams VTT carries speaker names: map them with `--speaker-map "Name=P-###,Researcher=Interviewer"`; the script refuses unmapped names. Recording → `_raw/<project>/` via `research-clip` link. |
| **Krisp** | Fetch the transcript through the Krisp connector when the user wants Krisp's speaker labels; save as plain text in `00 Inbox/`. | Step 3 with `--transcriber krisp` and a speaker map. |
| **Dovetail export** (migration) | Dovetail MCP `get_data_content` gives markdown `**Name (m:ss):** text`; save it to `00 Inbox/<project>/`. Highlights and tags from Dovetail are not imported: the vault re-highlights review-first, and the Dovetail tags inform the project's `tags.yaml`. | Step 3 with `--transcriber dovetail-export`; `[CONTEXT:]` lines become `**Note:**` paragraphs. Record the Dovetail project URL in the source's `origin`. One Dovetail data entry → one source. |
| **Audio or video file** | Anyone drops it in `00 Inbox/`. | Step 2 (local Whisper), never a cloud transcription service. |

Whatever the import, the transcript is pseudonymised before the note is written, and the recording goes to `_raw/<project>/` (the SharePoint study folder in production), never into git.

## Never

- Modify transcript text after the note is written, except speaker prefixes and redaction tokens in this same run.
- Put a researcher annotation into the transcript. Context goes into the highlight note's `context` property (research-highlight), which keeps the transcript immutable and the annotation visible on the tag board.
- Write a real name anywhere, including conversation summaries.
- Read `_raw/participants.csv`.
- Ingest the same recording twice without archiving the first (`ris_status: archived`).
