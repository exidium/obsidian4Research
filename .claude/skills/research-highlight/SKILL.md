---
name: research-highlight
description: Review one transcript for tagging and turn approved proposals into highlight notes, modelled on ADI's Research Tagging Reviewer. Use when the user says "review S-####", "highlight this source", "propose highlights", "tag the transcript", "implement proposals 3, 5 and 7", "accept H-…", "what's pending review", or after research-ingest finishes a source. Proposals first (numbered, verbatim excerpts, workspace and project tags, context, rationale, coverage summary); the researcher decides; only then are highlight notes written. Never tags autonomously.
---

# research-highlight

Two modes, one source per run. The agent is a **reviewer, not an autonomous tagger**: it proposes, the researcher decides, then it implements. `MODEL` is the model you are running as (provenance and `model:` properties).

```
source (transcript)   →  proposals (b_sources/S-#### review.md)
approved proposals    →  highlight notes (c_highlights/H-S####-#### <title>.md)
```

## Mode 1: review S-#### (propose)

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
7. Verify with a small script that every excerpt is a whitespace-normalised substring of its block and every tag exists. Present the proposals for accept / modify / reject by number. `bash _system/scripts/provenance.sh research-highlight review S-#### $MODEL`.

## Mode 2: implement

1. Take the approved numbers ("implement everything" means all). Before writing, list existing highlights for the source and skip any block already highlighted.
2. For each: `python3 _system/scripts/next_id.py highlight S-####`, then write `c_highlights/H-S####-#### <title>.md` from `_system/templates/highlight.md`. File name is the ID plus the title; `aliases` contains the ID; `quote` is the excerpt exactly as in the block; `context` holds the annotation; `{{timestamp}}` is the block's `[hh:mm:ss]` (the "Open in transcript" link). `review: accepted` when the user approved it explicitly, otherwise `proposed`. `created_by: ai`, `model`, `skill_version: 0.3.0`, `created`.
3. `PROPOSED` project tags: append to `d_tags/tags.yaml` under the right group with `status: proposed`, `proposed_by: ai`, `definition`, `evidence: [H-...]`. `research-organize` activates them.
4. Set the review doc `status: implemented` and the source `ris_status: review`. `python3 _system/scripts/audit.py`; fix what it reports for this source (a non-verbatim quote is the usual error).
5. `python3 _system/scripts/tag_board.py <project>` and `... --canvas`; `uv run _system/scripts/personas.py refresh` (persona appearance lists).
6. `bash _system/scripts/provenance.sh research-highlight implement S-#### $MODEL`. Report count, tag distribution, proposed tags, doubts, and point the user to `02 insights review.md` to accept or reject.

## Review support (any time)

- "what's pending": `python3 _system/scripts/highlights_table.py <project>` filtered to `proposed`, grouped by tag.
- The user reviews on the board in `02 insights review.md` (drag between proposed / accepted / rejected), edits `review:` on the note, or tells you ("accept 3 and 5, reject 7", or by ID). Apply with a frontmatter edit only, then `provenance.sh research-highlight review-decision <ids> $MODEL`.
- Rejected highlights keep `review: rejected`. Never delete evidence.
- A clip for a highlight: `research-clip`.

## Never

- Write a highlight the user has not seen as a proposal.
- Change transcript text or block IDs to make a quote fit.
- Invent a tag string, or add a workspace tag.
- Read anything under `_raw/`.
