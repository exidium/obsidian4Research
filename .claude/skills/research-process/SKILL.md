---
name: research-process
description: Analysis engine of the research vault. Turns a source note into tagged highlight notes, turns a project's highlights into evidence-linked insight notes, and publishes insights to Confluence. Use when the user says "highlight", "tag", "code this transcript", "synthesize", "find themes", "write insights", "what did we learn in project X", "publish insight", or names an S-#### or project after ingest. Reads the taxonomy; never invents tags silently.
---

# research-process

Three modes. Each reads one level and writes the next, never skipping a level.

```
source (transcript)  →  highlight   : one source per run
highlights           →  insight     : one project per run, reads highlights only
insight              →  Confluence  : one insight per run
```

Set `MODEL` to the model you are running as (for provenance and `model:` properties).

## Mode 1: highlight S-####

**Goal:** 6 to 15 highlights per hour of interview, each a single idea, verbatim, traceable.

1. Open `_system/taxonomy.yaml` and keep the active tags in mind. Open the source note. Confirm `redacted: true`; if not, stop and send the user to `research-ingest` step 5.
2. Read the whole transcript once before extracting anything. Note the participant's segment (task-based).
3. Walk the transcript again and pick spans. Prefer, in order: behaviors observed or described, pains with a concrete trigger, workarounds, needs stated in outcome terms, mental models, trust statements. Feature requests last. Skip interviewer speech, pleasantries, and anything you can't quote verbatim.
4. For each span:
   - `python3 _system/scripts/next_id.py highlight S-####`
   - Copy `_system/templates/highlight.md` into `highlights/H-S####-####.md`.
   - `block`: the paragraph's ID without the caret. `quote`: the exact sentence(s) from that paragraph, trimmed, no edits, no ellipsis in the middle.
   - `tags`: one `theme/` tag, at least one `behavior/` or `topic/` tag, optionally `product/`. `segment`: one tag.
   - `Why it matters`: one sentence of your reading. Not a paraphrase.
   - `review: proposed`, `created_by: ai`, `model`, `created`.
5. If a concept recurs and no active tag fits, add it to the taxonomy under the right dimension with `status: proposed`, `proposed_by: ai`, a definition, and `evidence: [H-...]`. Then use it. Tell the user it needs their decision. Don't propose more than three tags per source.
6. Set the source's `status: highlighted`. Run `python3 _system/scripts/audit.py` and fix anything it reports for this source (non-verbatim quotes are the usual error).
7. `bash _system/scripts/provenance.sh research-process highlight S-#### $MODEL`
8. Report: count, tag distribution, proposed tags, and where you were unsure. Point the user to the "Highlights pending review" view in the project note.

Quality bar: a reader who sees only the highlight note, without the transcript, should understand what happened and why it matters.

## Mode 2: synthesize <project>

**Goal:** insights a stakeholder would act on, each backed by cited highlights, with honest confidence.

1. Run `python3 _system/scripts/audit.py`. Don't synthesize over errors.
2. Pull the evidence table. **This is the only input.** Do not open transcripts.
   ```bash
   python3 _system/scripts/highlights_table.py <project>                # all
   python3 _system/scripts/highlights_table.py <project> --accepted-only  # if the user has reviewed
   ```
   If the user hasn't reviewed yet, say so and proceed on proposed highlights, marking the insights `draft`.
   Over about 150 rows: first group by `theme/` tag (`--tag theme/pain` etc.) and synthesize per theme group.
3. Cluster. Group highlights that answer the same research question or describe the same mechanism. Co-occurring tags are a hint, not the rule. A cluster needs at least two participants to become an insight; a one-participant cluster becomes a **signal**, written the same way but with `confidence: low` and a title that starts with "Signal:".
4. For each cluster, write `insights/I-<project>-##.md` from the template:
   - `title` is a claim with a verb, not a topic. "Engineers rerun simulations because they don't trust cached results", not "Simulation trust".
   - `## Insight`: two or three sentences. Mechanism, not summary.
   - `## Evidence`: embed every supporting highlight `![[H-...]]`. List them in `highlights:` too. Set `participants` from the evidence. `confidence`: low 1, medium 2, high 3+ participants.
   - `## Implications`: for product and for research (what we still don't know).
   - `## Open questions`: what the next session should probe.
   - `tags`: the two or three taxonomy tags that best index it.
5. Write one more note if useful: `insights/I-<project>-00-overview.md` with `type: overview` (the audit skips it) that lists the insights in priority order with one line each. Skip it for fewer than three insights.
6. Update the project note `status: synthesizing` if it was `active`. Audit again.
7. `bash _system/scripts/provenance.sh research-process synthesize <project> $MODEL`
8. Report: number of insights and signals, which research questions remain unanswered, highlights you left unused and why.

Don'ts: no insight without evidence links; no quoting a participant beyond what the highlight holds; no aggregating counts across projects unless the user asks for a cross-project synthesis explicitly.

## Mode 3: publish I-...

1. The insight must be `status: reviewed` (a human read it). If it is `draft`, ask.
2. Render for stakeholders: title, insight, implications, then evidence as attributed quotes (`P-003, validating design`), never transcript excerpts, never IDs that mean nothing to the reader. Keep the highlight ID in a small footer for traceability back to the vault.
3. Use the `atlassian-docs` skill to create or update the Confluence page in the space the user names.
4. Set `published_to` to the page URL, `status: published`.
5. `bash _system/scripts/provenance.sh research-process publish I-... $MODEL`

## Review support (any time)

"show me what's pending" → `highlights_table.py <project>` filtered to `proposed`, grouped by tag, ten per page. The user edits `review:` in Obsidian or tells you decisions; apply them with a frontmatter edit only. Rejected highlights stay in the folder with `review: rejected`; never delete evidence.
