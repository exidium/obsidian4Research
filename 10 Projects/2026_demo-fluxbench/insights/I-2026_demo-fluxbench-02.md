---
type: insight
insight_id: I-2026_demo-fluxbench-02
project: 2026_demo-fluxbench
title: Silent parameter changes, not model error, are what make results look wrong and drive support load
status: draft
confidence: high
participants: [P-001, P-002, P-003]
highlights: ['[[H-S0001-0004]]', '[[H-S0001-0005]]', '[[H-S0002-0005]]', '[[H-S0002-0006]]', '[[H-S0002-0011]]', '[[H-S0002-0012]]', '[[H-S0003-0011]]']
tags: [theme/expectation-gap, behavior/configure, topic/accuracy]
published_to: ''
created: 2026-11-05
---

# Silent parameter changes, not model error, are what make results look wrong and drive support load

## Insight
Changing a part resets parameters without notice; model updates change old results on reopen; the thermal model uses a standard board the user never sees. In each case the tool was arguably correct and the user concluded it was wrong. The FAE estimates that announcing changes would halve tool-related support questions, and has written shadow documentation to cover the gap.

## Evidence
![[H-S0001-0004]]
![[H-S0001-0005]]
![[H-S0002-0005]]
![[H-S0002-0006]]
![[H-S0002-0011]]
![[H-S0002-0012]]
![[H-S0003-0011]]

## Implications
- Announce every parameter the tool changes on the user's behalf, inline and at the moment it happens; log it in the project.
- Stamp model versions into project files and warn on open when a model has changed.
- Expose the thermal model's board assumption on the result itself.

## Open questions
- Which hidden defaults appear most often in the FAE's checklist? That is a prioritized backlog.
- Would users accept a 'what changed' dialog, or does it need to be passive?
