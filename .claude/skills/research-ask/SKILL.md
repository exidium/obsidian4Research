---
name: research-ask
description: Answer a question from the research in the vault with citations, for product managers and stakeholders who don't read transcripts. Use when someone asks "what do we know about X", "did anyone mention Y", "what did customers say about licensing", "is there evidence for Z", "which participants talked about exports", or any question that should be answered from insights and highlights rather than from general knowledge. Answers from insights first, then highlights, with evidence levels and IDs; never from raw transcripts, never with names.
---

# research-ask

The answer to "what do we know about X" is the researcher's synthesis, not a pile of quotes. So the skill reads top-down: insights, then highlights, and only reaches a transcript block when the user asks for the context of one specific highlight. Every claim carries an ID a reader can click. `MODEL` is the model you are running as.

## Procedure

1. **Scope.** If the question names a project, stay in it; otherwise search the whole vault (`10 Projects/` and `90 Archive/`), and say which studies the answer draws on.
2. **Insights first.** Search `e_insights/` titles, findings and tags (`grep -ril "<term>" "10 Projects/"*/e_insights/`). An insight that answers the question is the answer; quote its finding, evidence level, participants and recommendation, and link it.
3. **Then highlights.** `uv run _system/scripts/highlights_table.py <project> --tag <tag>` when a tag matches the topic, or a case-insensitive grep over `c_highlights/` for the term and its synonyms. Only `review: accepted` or `proposed` highlights, never `rejected`. Group by participant; count participants, not quotes.
4. **Then personas and participants** when the question is about who: `30 Personas/` and `20 Participants/` cards (public half only).
5. **Answer** in this shape:
   - One paragraph: what we know, how strong it is (strong / emerging / single mention / nothing), and from which studies.
   - Evidence: up to five highlights as short verbatim quotes with `P-### · H-S####-#### ` (and the study if more than one), and the insight IDs they belong to.
   - What we don't know: the gap, and whether a study is planned.
   - If the vault has nothing: say so plainly, name the nearest topic that does have evidence, and offer `research-organize` → research backlog.
6. **Context for one highlight** on request: open only its linked block (`![[S-#####^block]]`), never the whole source.
7. `bash _system/scripts/provenance.sh research-ask ask "<question>" $MODEL` (questions are a signal for the backlog).

## Evidence language

- 4+ participants with consistent language: "strong evidence".
- 2 to 3: "emerging, from n participants".
- 1: "one participant said"; never generalise it.
- Insights are the researcher's interpretation; highlights are what participants said. Keep the two distinguishable in the answer.

## Never

- Answer from general knowledge about the product or market and present it as research.
- Quote a transcript line that is not a highlight.
- Name a participant, an employer, or anything from `_raw/`.
- Promote evidence: a single mention stays a single mention.
