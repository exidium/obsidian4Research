---
type: highlight
highlight_id: H-S0003-0034
aliases: [H-S0003-0034]
title: Fast discrepancies are visible, slow ones hidden
project: 2026_demo-fluxbench
source: '[[S-0003]]'
block: s0003-0152
participant: P-003
quote: 'Every fast one was a parameter mismatch I could see on the screen: a wrong load value, a wrong input voltage, a part I could compare. Every slow one was something hidden: the reference board in the thermal model, the switching loss inside one number, the capacitor revision on page fourteen. Fast means I can see what the tool assumed. Slow means I have to infer it from the result. There is no third category in my notes.'
context: '[CONTEXT: Asked what makes a discrepancy fast to resolve. In ^s0003-0154, a page stating what a run assumed would turn "half the investigations" into a five-minute checklist instead of a two-day search; in ^s0003-0088, "every assumption I have found so far, I found by accident or by failure".]'
tags: [insight/pain-point, sentiment/neutral, journey/validate, tools/hidden-defaults]
review: accepted
created_by: ai
model: claude-fable-5-1
skill_version: 0.3.0
created: 2026-11-17
reviewed_by: P-000
reviewed: 2026-11-17
---

> [!info]- Context
> [CONTEXT: Asked what makes a discrepancy fast to resolve. In ^s0003-0154, a page stating what a run assumed would turn "half the investigations" into a five-minute checklist instead of a two-day search; in ^s0003-0088, "every assumption I have found so far, I found by accident or by failure".]

![[S-0003#^s0003-0152]]
[[S-0003#^s0003-0152|Open in transcript · S-0003 @ 00:55:55]]

**Rationale:** A single rule from the participant's own records that explains the whole investigation cost: visibility of assumptions, not model accuracy, decides whether a gap takes minutes or days (RQ1, RQ3).
