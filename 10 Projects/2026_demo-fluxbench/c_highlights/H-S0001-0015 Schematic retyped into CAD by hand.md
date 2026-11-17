---
type: highlight
highlight_id: H-S0001-0015
aliases: [H-S0001-0015]
title: Schematic retyped into CAD by hand
project: 2026_demo-fluxbench
source: '[[S-0001]]'
block: s0001-0046
participant: P-001
quote: That re-drawing step is where errors creep in. FluxBench shows me a schematic, I look at it, I type the same thing into the CAD tool. Twelve components, maybe twenty nets. I've done it wrong once already on this board, swapped the feedback divider values, top and bottom. Caught it in the review, luckily. There's supposedly a netlist export. I tried it, and it came out in a format our CAD tool didn't recognise, so I gave up after half an hour and went back to typing.
context: '[CONTEXT: Block 0048: the netlist is a generic text format, none of the two or three offered match their mainstream CAD tool, and a forum converter script failed on the first line. The layout engineer receives the hand-drawn CAD schematic either way.]'
tags: [insight/pain-point, functionality/workaround, sentiment/negative, journey/integrate, export/handoff-as-picture]
review: accepted
created_by: ai
model: claude-fable-5-1
skill_version: 0.3.0
created: 2026-11-17
reviewed_by: P-000
reviewed: 2026-11-17
---

> [!info]- Context
> [CONTEXT: Block 0048: the netlist is a generic text format, none of the two or three offered match their mainstream CAD tool, and a forum converter script failed on the first line. The layout engineer receives the hand-drawn CAD schematic either way.]

![[S-0001#^s0001-0046]]
[[S-0001#^s0001-0046|Open in transcript · S-0001 @ 00:17:21]]

**Rationale:** The first concrete defect caused by the handoff (a swapped divider) and evidence that the existing netlist export does not reach the tools customers use.
