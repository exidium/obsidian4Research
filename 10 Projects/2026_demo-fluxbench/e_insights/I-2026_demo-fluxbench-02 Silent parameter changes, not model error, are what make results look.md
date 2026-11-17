---
type: insight
insight_id: I-2026_demo-fluxbench-02
aliases: [I-2026_demo-fluxbench-02]
title: 'Insight: Silent parameter changes, not model error, are what make results look wrong and drive support load'
project: 2026_demo-fluxbench
status: draft
evidence_level: emerging
participants: [P-001, P-002, P-003]
highlights: ['[[H-S0001-0004 Part change silently reset switching frequency|H-S0001-0004]]', '[[H-S0001-0005 Lost trust because the tool didn''t say what it changed|H-S0001-0005]]', '[[H-S0002-0005 Silent reset is the top support cause|H-S0002-0005]]', '[[H-S0002-0006 Shadow checklist of hidden defaults|H-S0002-0006]]', '[[H-S0002-0011 Announce changes, halve support questions|H-S0002-0011]]', '[[H-S0002-0012 Model updates change old results on reopen|H-S0002-0012]]', '[[H-S0003-0011 Thermal model is less board-specific than assumed|H-S0003-0011]]']
research_question: 3
tags: [insight/pain-point, functionality/bug, tools/silent-parameter-reset]
published_to: ''
created: 2026-11-06
reel: _raw/2026_demo-fluxbench/reels/I-2026_demo-fluxbench-02.mp4
reel_duration: 00:01:09
---

# Insight: Silent parameter changes, not model error, are what make results look wrong and drive support load

![[_raw/2026_demo-fluxbench/reels/I-2026_demo-fluxbench-02.mp4]]

## Finding
In every case where a participant called a result wrong, the tool had changed or assumed something without saying so, and the result itself was arguably correct.

## Severity and impact
Three of three participants. The FAE sees the part-change reset weekly, names it the top support cause, and estimates that announcing changes would halve tool-related questions. Support has written shadow documentation to cover the gap.

## What this means
Opacity is being read as inaccuracy. The cheapest trust fix in the study is also a support-cost fix: tell the user what changed, when it changed, and which model version a design used.

## Evidence
![[H-S0001-0004 Part change silently reset switching frequency]]
![[H-S0001-0005 Lost trust because the tool didn't say what it changed]]
![[H-S0002-0005 Silent reset is the top support cause]]
![[H-S0002-0006 Shadow checklist of hidden defaults]]
![[H-S0002-0011 Announce changes, halve support questions]]
![[H-S0002-0012 Model updates change old results on reopen]]
![[H-S0003-0011 Thermal model is less board-specific than assumed]]

## Recommendations
- Announce every parameter the tool changes on the user's behalf, inline at the moment it happens, and log it in the project.
- Stamp model versions into project files and warn on open when a model has changed.
- Expose the thermal model's board assumption on the result itself.

## Open questions
- Which hidden defaults appear most often in the FAE's checklist? That is a prioritised backlog.
- Would users accept a 'what changed' dialog, or does it need to be passive?
