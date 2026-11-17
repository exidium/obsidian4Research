---
type: highlight
highlight_id: H-S0003-0023
aliases: [H-S0003-0023]
title: Two-week argument over an inductor in a stray copy
project: 2026_demo-fluxbench
source: '[[S-0003]]'
block: s0003-0090
participant: P-003
quote: Twice we have validated against a project that was not the designer's latest. One of those turned into a two week argument about a 60 millivolt transient difference, which turned out to be a different inductor in the two project files. Nobody had changed it on purpose. It had been changed in a copy that never came back.
context: '[CONTEXT: Files are named with dates and initials (H-S0003-0010). In ^s0003-0092 the asks are a change log inside the project, a diff between two project files, and a record of the model library version per run; in ^s0003-0146 a shared folder failed because the tool locks the open file and the second person saves a read-only copy under a new name.]'
tags: [insight/pain-point, sentiment/negative, journey/integrate, sharing/design-fork, tools/design-history-missing]
review: accepted
created_by: ai
model: claude-fable-5-1
skill_version: 0.3.0
created: 2026-11-17
reviewed_by: P-000
reviewed: 2026-11-17
---

> [!info]- Context
> [CONTEXT: Files are named with dates and initials (H-S0003-0010). In ^s0003-0092 the asks are a change log inside the project, a diff between two project files, and a record of the model library version per run; in ^s0003-0146 a shared folder failed because the tool locks the open file and the second person saves a read-only copy under a new name.]

![[S-0003#^s0003-0090]]
[[S-0003#^s0003-0090|Open in transcript · S-0003 @ 00:32:44]]

**Rationale:** A measurable consequence of design forks (two weeks, a 60 mV argument) that was in fact a hidden parameter difference, linking the sharing problem to the "wrong result" question (RQ2, RQ3).
