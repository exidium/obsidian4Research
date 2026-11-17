---
type: highlight
highlight_id: H-S0003-0035
aliases: [H-S0003-0035]
title: Three-degree thermal match holds only on kits
project: 2026_demo-fluxbench
source: '[[S-0003]]'
block: s0003-0160
participant: P-003
quote: The caveat, which I only understood later, is that both of those were kits, which look a lot like the reference board the model assumes. On our own board the number has been further off, in the direction you would expect from more copper. So the three degrees is true, with a condition I did not know I was stating.
context: '[CONTEXT: Thermal camera plus thermocouple on the kit after thirty minutes at fixed ambient; simulation 58 degrees, measured 56 and 55, on two projects. Qualifies the "within three degrees" in H-S0003-0008 and ties back to the reference-board assumption in H-S0003-0011.]'
tags: [sentiment/neutral, journey/validate, experience/advanced, correlation/thermal-correlated, tools/hidden-defaults]
review: accepted
created_by: ai
model: claude-fable-5-1
skill_version: 0.3.0
created: 2026-11-17
reviewed_by: P-000
reviewed: 2026-11-17
---

> [!info]- Context
> [CONTEXT: Thermal camera plus thermocouple on the kit after thirty minutes at fixed ambient; simulation 58 degrees, measured 56 and 55, on two projects. Qualifies the "within three degrees" in H-S0003-0008 and ties back to the reference-board assumption in H-S0003-0011.]

![[S-0003#^s0003-0160]]
[[S-0003#^s0003-0160|Open in transcript · S-0003 @ 00:58:45]]

**Rationale:** Qualifying evidence on the one positive correlation in the study: it holds under a condition the participant was unknowingly stating, so the thermal-correlated tag needs its condition recorded (RQ1).
