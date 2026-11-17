---
type: highlight
highlight_id: H-S0001-0028
aliases: [H-S0001-0028]
title: Raw plot data to overlay with the scope
project: 2026_demo-fluxbench
source: '[[S-0001]]'
block: s0001-0106
participant: P-001
quote: If I could export the load step as a CSV of time and voltage, I'd plot it myself in the same style as our bench captures, and then the correlation would be on the same axes, same colours, same cursors. That's how you build trust in a review. You put the simulation and the measurement on one graph and people see them overlap. Right now I'm comparing a raster image from the tool with a screenshot from the scope and saying, trust me, those are the same. They look similar. Similar isn't a number.
context: '[CONTEXT: Plot exports are raster and go fuzzy on a large screen (block 0100). Block 0108: this sits on the internal gotchas wiki as a wish; it has never been asked of the vendor.]'
tags: [functionality/new-feature-request, insight/desire, sentiment/neutral, journey/validate, export/plot-data-not-exportable, correlation/sim-vs-bench-gap]
review: accepted
created_by: ai
model: claude-fable-5-1
skill_version: 0.3.0
created: 2026-11-17
reviewed_by: P-000
reviewed: 2026-11-17
---

> [!info]- Context
> [CONTEXT: Plot exports are raster and go fuzzy on a large screen (block 0100). Block 0108: this sits on the internal gotchas wiki as a wish; it has never been asked of the vendor.]

![[S-0001#^s0001-0106]]
[[S-0001#^s0001-0106|Open in transcript · S-0001 @ 00:45:34]]

**Rationale:** Ties plot-data export directly to trust building in review (RQ1 and RQ2), not just convenience, and explains why image exports cannot close a correlation argument.
