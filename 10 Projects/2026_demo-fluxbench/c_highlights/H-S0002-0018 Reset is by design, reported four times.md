---
type: highlight
highlight_id: H-S0002-0018
aliases: [H-S0002-0018]
title: Reset is "by design", reported four times
project: 2026_demo-fluxbench
source: '[[S-0002]]'
block: s0002-0052
participant: P-002
quote: The silent reset I've reported, in various forms, four times over three years. The response each time has been that it's by design, because the new part may not support the old parameter range, so resetting to the new part's defaults is 'safe'. Safe for the solver, maybe. Not safe for the engineer. I understand the reasoning. I just want a message that says 'I reset these five values, here's what they were.' That's a dialog box. It's not a rewrite.
context: '[CONTEXT: Asked whether anything comes back from his support tickets; he estimates one in five produces a visible change within six months.]'
tags: [insight/pain-point, functionality/new-feature-request, sentiment/negative, journey/support, tools/silent-parameter-reset, workflow/no-owner-for-wrong-number]
review: accepted
created_by: ai
model: claude-fable-5-1
skill_version: 0.3.0
created: 2026-11-17
reviewed_by: P-000
reviewed: 2026-11-17
---

> [!info]- Context
> [CONTEXT: Asked whether anything comes back from his support tickets; he estimates one in five produces a visible change within six months.]

![[S-0002#^s0002-0052]]
[[S-0002#^s0002-0052|Open in transcript · S-0002 @ 00:18:47]]

**Rationale:** Shows why the top RQ3 cause persists: the development team's framing of the reset as safe is a defensible solver decision that nobody has weighed against the engineer's experience, and the ask is scoped to a dialog, not a redesign.
