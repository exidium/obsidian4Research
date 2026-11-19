---
name: research-report
description: Write a stakeholder readout from a project's insights: Markdown report in f_deliverables/ with summary, method, findings with linked evidence, prioritised recommendations, open questions and appendix; registered in the Reports table of 01 project.md. Use when the user says "write the report", "create a readout", "summarise the study for the product owner", "one-pager for Alan", "update the readout", or after synthesis is complete. Reads insights and highlights only; audience and tone are set per report.
---

# research-report

A readout is the study rewritten for one audience and one decision. It is built from insights (the researcher's synthesis) and cites highlights (what participants said); it never reaches into transcripts. `MODEL` is the model you are running as.

## Before writing

1. Ask, or take from the request: **audience** (roles), **the decision it informs**, **format** (full readout, one-pager, exec summary), **tone** (neutral research register, or the user's voice with a sample for the humanizer).
2. `uv run _system/scripts/audit.py` clean; insights at least `draft`, preferably `reviewed`.
3. Read `01 project.md` (introduction, questions, participants) and every insight in `e_insights/`. Pull the quotes from `uv run _system/scripts/highlights_table.py <project> --accepted-only` (or all, flagged, if review isn't done).

## Structure (full readout)

1. **Header**: study link, sessions and dates, counts (highlights, insights), audience, status and version, the evidence-level caveat in one line.
2. **Summary**: one paragraph a director can read alone, then two to three headline findings with their consequence.
3. **What we did**: method, participants by role and type (IDs, never names), how analysis was done, the small-base caveat if it applies.
4. **Findings**: one section per insight, in order of importance for the decision, each with a two- or three-sentence account, one or two verbatim quotes as `(P-###, [[<highlight file>|H-id]])`, and the insight link plus its other highlight IDs.
5. **Recommendations, in the order to take them**: a table (#, recommendation, why first, finding), followed by one line on what is near-term and what is strategic.
6. **What we don't know yet, and the research that would settle it**: one bullet per open question, each with the method that answers it.
7. **Appendix**: participants (cards linked), evidence-level definitions, traceability note (quote → highlight → transcript line → clip), related pages.

A one-pager keeps 2, the top three of 5, and one line of 6. An exec summary is 2 alone.

## Writing rules

- Every number and claim traces to an insight or a highlight; nothing new is argued in the report.
- Quotes verbatim, by participant ID; link by file name with the ID as display text.
- Recommendations are the insights' recommendations, prioritised; don't invent effort estimates.
- No names, employers, or media. The internal-participant rule applies to any clip the report links.
- Plain prose, short sections, no dashes as connectors. For the user's own voice, run the `humanizer` skill with a writing sample; for a neutral readout, don't.

## Files and registration

- Write `f_deliverables/Readout - <topic>.md` (or `One-pager - <topic>.md`) with frontmatter `type: deliverable`, `doc: readout | one-pager | summary`, `project`, `title`, `audience`, `status: draft`, `version`, `date`, `contains_participant_data`, `insights` (IDs).
- Post-process ID links to file names (`vaultlib.find_by_id`), run `scan_pii.py` on the file.
- Add a row to `## Reports` in `01 project.md`: report, audience, date, where. Only reports go in that table.
- `bash _system/scripts/provenance.sh research-report report <project> $MODEL`.
- To publish it: `research-publish`. To present it: the deck builder in the ADI project (`04_deliverables`), on the ADI template.

## Never

- Quote a transcript line that isn't a highlight.
- Soften an evidence level or drop the caveat because the audience is senior.
- Put a name, an employer, or a video in the report.
