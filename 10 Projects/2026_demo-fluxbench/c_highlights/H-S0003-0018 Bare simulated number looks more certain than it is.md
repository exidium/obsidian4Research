---
type: highlight
highlight_id: H-S0003-0018
aliases: [H-S0003-0018]
title: Bare simulated number looks more certain than it is
project: 2026_demo-fluxbench
source: '[[S-0003]]'
block: s0003-0056
participant: P-003
quote: The simulated side has no uncertainty column, because the tool does not give one. It is a bare number sitting next to a measured number with error bars, and the bare number looks more certain than it is. That is backwards, and quality has noticed it too.
context: '[CONTEXT: Every measured value in the report carries an uncertainty from the instrument specification and the calibration record (about 0.3 of a point on efficiency, about five percent on ripple). "Within ten percent" means the simulated value falls inside the measured value plus its uncertainty plus the limit.]'
tags: [insight/pain-point, sentiment/negative, journey/validate, correlation/accuracy-statement-missing]
review: accepted
created_by: ai
model: claude-fable-5-1
skill_version: 0.3.0
created: 2026-11-17
reviewed_by: P-000
reviewed: 2026-11-17
---

> [!info]- Context
> [CONTEXT: Every measured value in the report carries an uncertainty from the instrument specification and the calibration record (about 0.3 of a point on efficiency, about five percent on ripple). "Within ten percent" means the simulated value falls inside the measured value plus its uncertainty plus the limit.]

![[S-0003#^s0003-0056]]
[[S-0003#^s0003-0056|Open in transcript · S-0003 @ 00:19:26]]

**Rationale:** Reframes the accuracy statement as a missing uncertainty column in a two-column table, a concrete form a PM can picture, and notes that the customer's quality function has spotted the asymmetry (RQ1).
