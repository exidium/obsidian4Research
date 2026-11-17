---
type: highlight
highlight_id: H-S0001-0013
aliases: [H-S0001-0013]
title: Sign-off is on the document, not the design
project: 2026_demo-fluxbench
source: '[[S-0001]]'
block: s0001-0040
participant: P-001
quote: He's not re-running anything. He can't, he doesn't have the tool. So the sign-off is on the document, not on the design file. Which means if I export the wrong revision, or I change a value after exporting and forget to re-export, the thing he signed isn't the thing that goes to layout. That has happened.
context: '[CONTEXT: Gated process described in block 0034: a preliminary design review before layout and a critical design review before fab, a six-page document with FluxBench plots pasted as images, three reviewers commenting in a review system, the lead mandatory.]'
tags: [insight/pain-point, sentiment/neutral, journey/integrate, sharing/pdf-review-loop, workflow/review-loop-described, sharing/reviewer-viewer-missing]
review: accepted
created_by: ai
model: claude-fable-5-1
skill_version: 0.3.0
created: 2026-11-17
reviewed_by: P-000
reviewed: 2026-11-17
---

> [!info]- Context
> [CONTEXT: Gated process described in block 0034: a preliminary design review before layout and a critical design review before fab, a six-page document with FluxBench plots pasted as images, three reviewers commenting in a review system, the lead mandatory.]

![[S-0001#^s0001-0040]]
[[S-0001#^s0001-0040|Open in transcript · S-0001 @ 00:14:30]]

**Rationale:** Names the structural risk of the PDF loop (the signed object and the built object can diverge) and the cause, a reviewer with no way to open the design.
