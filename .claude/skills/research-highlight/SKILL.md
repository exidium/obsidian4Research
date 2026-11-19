---
name: research-highlight
description: Tag one transcript automatically into highlight notes (verbatim excerpts, workspace and project tags, context, rationale, confidence), written as review: proposed for the researcher to accept or reject by exception on the review board, modelled on ADI's Research Tagging Reviewer. Use when the user says "tag S-####", "highlight this source", "review S-####", "what's pending", "accept all high-confidence from S-####", "reject H-…", or automatically after research-ingest finishes a source. Also has an ask mode that presents numbered proposals in chat before writing.
---

# research-highlight

Tagging runs on its own; the human reviews the result, not the plan. One source per run. The skill writes highlights directly as `review: proposed`; **nothing proposed reaches synthesis, a report or Confluence until a researcher accepts it** (`highlights_table.py --accepted-only`, `research-synthesize`, `research-publish` all gate on it). `MODEL` is the model you are running as (provenance and `model:` properties).

```
source (transcript)  →  auto: highlights as review: proposed (+ b_sources/S-#### review.md as the log)
                     →  researcher accepts / rejects by exception: review board, or review.py
accepted highlights  →  research-synthesize
```

## Modes

- **auto** (default; "tag S-0004", and the hand-off from `research-ingest`): run the Review procedure below, then write every proposal as a highlight note in one pass. Rate each `confidence: high | medium | low` (high: verbatim, complete thought, tags unambiguous, clearly answers a research question; low: borderline relevance, tag choice uncertain, or needs context the block doesn't give). Report the counts by confidence and point to the board.
- **ask** ("propose first", "show me before writing"): stop after the review doc and present the numbered proposals; write only what the user approves, as `review: accepted`.

## Review procedure (both modes)

1. **Context.** Read `01 project.md` (research questions, hypotheses, participants), `a_setup/` docs if present, `_system/taxonomy.yaml` (workspace tags) and the project's `d_tags/tags.yaml`. You may only propose tags from these two files, plus project tags you flag as `PROPOSED`.
2. **Read the whole transcript** once, end to end. Confirm `redacted: true`; if not, stop and send the user to `research-ingest` step 5. If the source already has highlights, list them by block ID and never re-propose those blocks.
3. **Walk it again and select passages** that address a research question, reveal something unexpected, or could change a recommendation: pain points, positive moments, workflow descriptions, feature requests, workarounds, surprises, emotional signals, numbers, counter-evidence. Participant speech only; skip pleasantries and anything you cannot quote verbatim.
4. **For each passage, draft a proposal:**
   - **Title**: 3 to 8 words that pass the stranger test on a tag board ("Latency documentation gap").
   - **Excerpt**: verbatim participant speech, complete sentences, from one block. If the thought spans two blocks, take the block with the key sentence and put the other in context.
   - **Stranger test**: would a PM who never saw the transcript understand it? If not, extend the excerpt within the block or add `[CONTEXT: ...]` (`[Q: ...]`, `[OBS: ...]`, `[NOTE: ...]` also exist). Brief; it frames the quote, it is not the insight.
   - **Tags**, workspace first then project, usually 2 to 3 across dimensions plus project tags. Frustration → pain-point + negative + functionality tag + journey; explicit ask → new-feature-request + desire + journey; praise → existing-feature + positive + journey; workflow → neutral + journey; confusion → confused + pain-point; workaround → workaround + pain-point + journey; ADI product named → `software/*`; market discussed → `market/*`; someone to interview → `ops/follow-up-referral`. Tag what is discussed, not who is talking. No fitting project tag → workspace tags only; a repeated untaggable pattern → `PROPOSED: <group>/<slug>` with a one-line definition. Never propose workspace tags.
   - **Rationale**: one sentence.
   - One passage, several signals → one proposal, several tags. Two topics in one breath → two proposals.
5. **Coverage summary**: proposals per research question; strong, weak or missing coverage; unexpected findings; qualifying evidence that prevents oversimplification.
6. **Write the review doc** `b_sources/S-#### review.md`:
   ```yaml
   type: review
   source: "[[S-####]]"
   project: <project>
   blocks: s####-0001 to s####-0149      # the range reviewed
   proposals: <count>
   status: pending                       # pending | implemented
   created: YYYY-MM-DD
   ```
   Expected counts: 30 min → 8 to 15, 60 min → 15 to 30, 90 min → 25 to 40.
7. Verify with a small script that every excerpt is a whitespace-normalised substring of its block and every tag exists. `bash _system/scripts/provenance.sh research-highlight review S-#### $MODEL`. In **ask** mode, stop here and present the proposals for accept / modify / reject by number.

## Write the highlights

1. **auto**: all proposals. **ask**: the approved numbers. Before writing, list existing highlights for the source and skip any block already highlighted.
2. For each: `uv run _system/scripts/next_id.py highlight S-####`, then write `c_highlights/H-S####-#### <title>.md` from `_system/templates/highlight.md`. File name is the ID plus the title; `aliases` contains the ID; `quote` is the excerpt exactly as in the block; `context` holds the annotation; `{{timestamp}}` is the block's `[hh:mm:ss]` (the "Open in transcript" link). `review: proposed` in auto mode (`accepted` only for proposals the user approved in ask mode), `confidence`, `created_by: ai`, `model`, `skill_version: 0.4.0`, `created`.
3. `PROPOSED` project tags: append to `d_tags/tags.yaml` under the right group with `status: proposed`, `proposed_by: ai`, `definition`, `evidence: [H-...]`. `research-organize` activates them.
4. Set the review doc `status: implemented` and the source `ris_status: review`. `uv run _system/scripts/audit.py`; fix what it reports for this source (a non-verbatim quote is the usual error).
5. `uv run _system/scripts/tag_board.py <project>` and `... --canvas`; `uv run _system/scripts/personas.py refresh` (persona appearance lists).
6. `bash _system/scripts/provenance.sh research-highlight implement S-#### $MODEL`. Report: count by confidence, tag distribution, proposed project tags, doubts, and point the user to `02 insights review.md` (or `review.py pending`) to accept or reject by exception.

## The human gate (review by exception)

- `uv run _system/scripts/review.py pending [<project>]`: what is waiting, by source and confidence.
- Board: `02 insights review.md`, drag between proposed / accepted / rejected; cards show confidence, so the researcher reads the low ones and skims the high ones.
- Bulk: `uv run _system/scripts/review.py accept --source S-0004 --min-confidence high`, `review.py reject H-S0004-0012 H-S0004-0019 --reason "interviewer speech"`, `review.py accept --project <p> --tag insight/pain-point`. Each decision is logged to provenance with the researcher ID (`RESEARCHER=P-0xx`).
- The user can also say it ("accept all high from S-0004, reject 12 and 19") and you run the commands.
- Rejected highlights keep `review: rejected` and drop out of boards and synthesis. Never delete evidence.
- A clip for a highlight: `research-clip`.

## Never

- Let a `proposed` highlight into synthesis, a report or Confluence; the gate is the review, not the tagging.
- Change transcript text or block IDs to make a quote fit.
- Invent a tag string, or add a workspace tag. A new project tag is written `status: proposed` in `d_tags/tags.yaml`; `research-organize` activates it.
- Read anything under `_raw/`.
