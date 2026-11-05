---
type: insight
insight_id: I-2026_demo-fluxbench-07
project: 2026_demo-fluxbench
title: Long simulations block the interface or crash, and users adapt by saving first and waiting
status: draft
confidence: medium
participants: [P-001, P-003]
highlights: ['[[H-S0001-0006]]', '[[H-S0003-0006]]']
tags: [theme/pain, behavior/simulate, topic/performance]
published_to: ''
created: 2026-11-05
---

# Long simulations block the interface or crash, and users adapt by saving first and waiting

## Insight
An eleven-minute sweep with no progress indicator was mistaken for a hang and killed. Temperature sweeps crash about one run in three with no error. Both participants now schedule long runs around the problem rather than trusting the tool to finish.

## Evidence
![[H-S0001-0006]]
![[H-S0003-0006]]

## Implications
- Progress feedback and background execution for sweeps; crash reporting that doesn't require an account.
- Research: the crash rate is one participant's estimate; instrumenting would settle it.

## Open questions
- Are the crashes memory-related to sweep size? P-003's sweeps are larger than P-001's.
