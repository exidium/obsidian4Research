---
type: highlight
highlight_id: H-S0003-0014
aliases: [H-S0003-0014]
title: Every out-of-limit row needs an investigation number
project: 2026_demo-fluxbench
source: '[[S-0003]]'
block: s0003-0036
participant: P-003
quote: We have a form, an investigation record, with a number, the parameter, the simulated value, the measured value, the acceptance limit, and then a root cause section and a closure section. It gets opened the day the discrepancy is confirmed, and it does not close until a second engineer signs it. The report then references the investigation number next to the row in the simulated versus measured table. So for the 5 volt rail there were two of them, one for ripple and one for efficiency, and the report points at both. Nothing in the table is allowed to be a surprise without a number next to it.
context: '[CONTEXT: Deepens H-S0003-0001. "Documented investigation" in practice: a numbered form with fields, a second signature, and a cross-reference from the report table.]'
tags: [sentiment/neutral, journey/validate, market/digital-healthcare, workflow/workflow-described, workflow/quality-system-constraint]
review: accepted
created_by: ai
model: claude-fable-5-1
skill_version: 0.3.0
created: 2026-11-17
reviewed_by: P-000
reviewed: 2026-11-17
---

> [!info]- Context
> [CONTEXT: Deepens H-S0003-0001. "Documented investigation" in practice: a numbered form with fields, a second signature, and a cross-reference from the report table.]

![[S-0003#^s0003-0036]]
[[S-0003#^s0003-0036|Open in transcript · S-0003 @ 00:11:32]]

**Rationale:** The concrete artefact behind "every discrepancy becomes an investigation" explains why a simulation gap costs days rather than minutes in this market (RQ2) and why nothing fits the existing project tags: the cost is set by the quality system, not the tool.
