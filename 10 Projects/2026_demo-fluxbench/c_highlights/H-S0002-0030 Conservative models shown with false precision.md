---
type: highlight
highlight_id: H-S0002-0030
aliases: [H-S0002-0030]
title: Conservative models shown with false precision
project: 2026_demo-fluxbench
source: '[[S-0002]]'
block: s0002-0112
participant: P-002
quote: But the tool presents every number with the same confidence, two decimal places, no indication. So a customer in battery storage sees eighty-nine point four percent, measures ninety-one, and concludes the tool is wrong, when actually the tool was deliberately pessimistic. If the number came with a note, 'this model is conservative by design, expect measured efficiency one to two points higher', the mismatch becomes reassurance instead of doubt. The information exists. The model team knows which models are which. It just never reaches the screen.
context: '[CONTEXT: Expanding on the third cause from `^s0002-0012`, conservative models. In `^s0002-0114` he adds he would rather the tool said "about eighty-nine to ninety-one" than "eighty-nine point four"; engineers accept ranges, not false precision.]'
tags: [insight/pain-point, functionality/new-feature-request, sentiment/negative, journey/validate, market/energy, correlation/accuracy-statement-missing, correlation/sim-vs-bench-gap]
review: accepted
created_by: ai
model: claude-fable-5-1
skill_version: 0.3.0
created: 2026-11-17
reviewed_by: P-000
reviewed: 2026-11-17
---

> [!info]- Context
> [CONTEXT: Expanding on the third cause from `^s0002-0012`, conservative models. In `^s0002-0114` he adds he would rather the tool said "about eighty-nine to ninety-one" than "eighty-nine point four"; engineers accept ranges, not false precision.]

![[S-0002#^s0002-0112]]
[[S-0002#^s0002-0112|Open in transcript · S-0002 @ 00:48:48]]

**Rationale:** RQ1 and RQ3 together: a measured result better than simulated still destroys trust when the tool hides its intent, and the fix is a label the model team can already supply.
