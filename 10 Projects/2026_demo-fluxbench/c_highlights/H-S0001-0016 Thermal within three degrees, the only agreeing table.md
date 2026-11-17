---
type: highlight
highlight_id: H-S0001-0016
aliases: [H-S0001-0016]
title: Thermal within three degrees, the only agreeing table
project: 2026_demo-fluxbench
source: '[[S-0001]]'
block: s0001-0052
participant: P-001
quote: The camera said 71 degrees on the FET case, the tool had predicted 68 at the junction with the copper area we'd agreed. Case and junction aren't the same thing, so if anything it's closer than it looks. The inductor was 54 measured against 51 predicted. That's within what I'd expect from the thermal camera alone. So I put the two numbers in the review document in a little table, predicted and measured, and my lead said, well, that's useful. From him that's high praise. It's the only table in the document where the two columns agree.
context: '[CONTEXT: Block 0050: the copper-area field gave the designer and the layout engineer a shared number to negotiate before layout (400 square millimetres under the FET), a conversation that normally happens after the prototype gets hot. Measurement: thermocouple and thermal camera, 6 A continuous, 25 degC ambient, twenty minutes to settle.]'
tags: [functionality/existing-feature, sentiment/positive, journey/validate, correlation/thermal-correlated]
review: accepted
created_by: ai
model: claude-fable-5-1
skill_version: 0.3.0
created: 2026-11-17
reviewed_by: P-000
reviewed: 2026-11-17
---

> [!info]- Context
> [CONTEXT: Block 0050: the copper-area field gave the designer and the layout engineer a shared number to negotiate before layout (400 square millimetres under the FET), a conversation that normally happens after the prototype gets hot. Measurement: thermocouple and thermal camera, 6 A continuous, 25 degC ambient, twenty minutes to settle.]

![[S-0001#^s0001-0052]]
[[S-0001#^s0001-0052|Open in transcript · S-0001 @ 00:20:09]]

**Rationale:** Puts numbers on the one trusted result and shows how a correlated figure converts a sceptical reviewer, the positive case against which the ripple failure should be read.
