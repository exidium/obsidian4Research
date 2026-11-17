---
type: highlight
highlight_id: H-S0003-0006
aliases: [H-S0003-0006]
title: Temperature sweeps crash one in three
project: 2026_demo-fluxbench
source: '[[S-0003]]'
block: s0003-0014
participant: P-003
quote: a sweep over ten temperatures with a load step at each one crashes the application about one time in three. No error, it just closes.
context: '[OBS: Participant now saves before every sweep and runs them over lunch.]'
tags: [functionality/bug, insight/pain-point, sentiment/negative, journey/validate, tools/simulation-crash]
review: proposed
created_by: ai
model: claude-fable-5-1
skill_version: 0.2.0
created: 2026-11-06
clip: _raw/2026_demo-fluxbench/clips/H-S0003-0006.mp4
clip_kind: video
clip_start: '00:04:16.0'
clip_end: '00:04:24.5'
---

> [!info]- Context
> [OBS: Participant now saves before every sweep and runs them over lunch.]

![[S-0003#^s0003-0014]]
[[S-0003#^s0003-0014|Open in transcript · S-0003 @ 00:04:08]]

![[_raw/2026_demo-fluxbench/clips/H-S0003-0006.mp4]]

**Rationale:** Heavy sweeps are the validation workload, and they are the runs that crash.
