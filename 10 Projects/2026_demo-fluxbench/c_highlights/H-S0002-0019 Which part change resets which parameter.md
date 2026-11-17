---
type: highlight
highlight_id: H-S0002-0019
aliases: [H-S0002-0019]
title: Which part change resets which parameter
project: 2026_demo-fluxbench
source: '[[S-0002]]'
block: s0002-0060
participant: P-002
quote: 'Changing the controller IC resets the most: switching frequency, soft-start time, current limit, compensation network, and the output capacitor selection if the new part has a different recommended set. Changing the inductor resets the saturation current derating and sometimes the DCR, which is the sneaky one because the number looks plausible. Changing the output capacitor resets the ESR to a generic value instead of the datasheet value, which is why ripple is the number one giveaway. Changing the package resets ambient temperature and the thermal resistance to board. I''ve mapped all of this by hand. Nobody has ever published it.'
context: '[CONTEXT: Asked which parameters actually reset. This is the content behind the "Before You Trust The Number" checklist (H-S0002-0006); in `^s0002-0086` he asks for an official page per topology listing exactly this.]'
tags: [experience/advanced, sentiment/neutral, journey/design, tools/silent-parameter-reset, tools/hidden-defaults]
review: accepted
created_by: ai
model: claude-fable-5-1
skill_version: 0.3.0
created: 2026-11-17
reviewed_by: P-000
reviewed: 2026-11-17
---

> [!info]- Context
> [CONTEXT: Asked which parameters actually reset. This is the content behind the "Before You Trust The Number" checklist (H-S0002-0006); in `^s0002-0086` he asks for an official page per topology listing exactly this.]

![[S-0002#^s0002-0060]]
[[S-0002#^s0002-0060|Open in transcript · S-0002 @ 00:22:31]]

**Rationale:** The complete reset map is the single most reusable piece of RQ3 evidence: it tells the product team which values a reset dialog must list and confirms the information exists only in one field engineer's head.
