---
type: highlight
highlight_id: H-S0002-0036
aliases: [H-S0002-0036]
title: 'Near miss: corrected model, marginal inductor'
project: 2026_demo-fluxbench
source: '[[S-0002]]'
block: s0002-0132
participant: P-002
quote: 'They reopened the design months later for a cost-down, saw the inductor running hotter in the new simulation, and assumed it was the cost-down change. They nearly shipped the original design with a marginal inductor because the old simulation said it was fine. What saved them was an engineer who didn''t trust either number and measured it. So the tool didn''t cause harm, a careful engineer prevented it, but the tool did nothing to help. A note on open would have said: this part''s loss model was corrected, re-check the thermal margin.'
context: '[CONTEXT: Asked whether a model update ever caused real harm. The automotive-lighting customer had qualified the design with a model that underestimated inductor losses. In `^s0002-0134` he explains it never became a ticket because "silently applied a corrected model" is not a defect category.]'
tags: [insight/pain-point, sentiment/negative, journey/validate, market/automotive, tools/model-version-drift, correlation/sim-vs-bench-gap]
review: accepted
created_by: ai
model: claude-fable-5-1
skill_version: 0.3.0
created: 2026-11-17
reviewed_by: P-000
reviewed: 2026-11-17
---

> [!info]- Context
> [CONTEXT: Asked whether a model update ever caused real harm. The automotive-lighting customer had qualified the design with a model that underestimated inductor losses. In `^s0002-0134` he explains it never became a ticket because "silently applied a corrected model" is not a defect category.]

![[S-0002#^s0002-0132]]
[[S-0002#^s0002-0132|Open in transcript · S-0002 @ 00:57:41]]

**Rationale:** The highest-stakes story in the interview: a corrected model nearly caused a worse outcome than the wrong one because the change was silent, which makes the on-open note a safety argument rather than a convenience.
