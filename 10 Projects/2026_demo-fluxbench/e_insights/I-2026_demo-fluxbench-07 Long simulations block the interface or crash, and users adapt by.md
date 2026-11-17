---
type: insight
insight_id: I-2026_demo-fluxbench-07
aliases: [I-2026_demo-fluxbench-07]
title: 'Insight: Long simulations block the interface or crash, and users adapt by saving first and waiting'
project: 2026_demo-fluxbench
status: draft
evidence_level: emerging
participants: [P-001, P-003]
highlights: ['[[H-S0001-0006 Eleven-minute sweep looked like a hang|H-S0001-0006]]', '[[H-S0003-0006 Temperature sweeps crash one in three|H-S0003-0006]]']
research_question: 2
tags: [insight/pain-point, functionality/bug, tools/simulation-crash]
published_to: ''
created: 2026-11-06
reel: _raw/2026_demo-fluxbench/reels/I-2026_demo-fluxbench-07.mp4
reel_duration: 00:00:24
---

# Insight: Long simulations block the interface or crash, and users adapt by saving first and waiting

![[_raw/2026_demo-fluxbench/reels/I-2026_demo-fluxbench-07.mp4]]

## Finding
An eleven-minute sweep with no progress indicator was mistaken for a hang and killed; temperature sweeps crash about one run in three with no error.

## Severity and impact
Two participants, both with the heaviest workloads in the study. Both now schedule long runs around the problem rather than trusting the tool to finish.

## What this means
The crash rate is one participant's estimate and may be unknown to the vendor, because there is no in-tool way to report it (see the follow-up on defect reporting).

## Evidence
![[H-S0001-0006 Eleven-minute sweep looked like a hang]]
![[H-S0003-0006 Temperature sweeps crash one in three]]

## Recommendations
- Add progress feedback and background execution for sweeps, and crash reporting that doesn't require a portal account.
- Research: instrument sweep runs to settle the crash rate.

## Open questions
- Are the crashes related to sweep size? The validation engineer's sweeps are larger than the designer's.
