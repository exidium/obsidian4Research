---
type: highlight
highlight_id: H-S0003-0025
aliases: [H-S0003-0025]
title: Sweep crash follows a steady memory climb
project: 2026_demo-fluxbench
source: '[[S-0003]]'
block: s0003-0096
participant: P-003
quote: It crashes about one time in three, usually between the sixth and eighth point. No dialog, no message, the window is just gone. We looked for a crash log in the usual places and found nothing. I watched the memory in the task manager during a sweep and it climbs steadily, around three gigabytes by the sixth point. I am guessing it is a leak, but I am a hardware person guessing about software, which is the same thing I complain about in reverse.
context: '[CONTEXT: Temperature sweep, ten points from minus 20 to plus 70 with a load step at each. In ^s0003-0098 the workaround is splitting into two runs of five points, which doubles the time, and "I have never seen a wrong number from a sweep, only a missing one." Deepens H-S0003-0006.]'
tags: [functionality/bug, insight/pain-point, sentiment/negative, journey/validate, tools/simulation-crash]
review: accepted
created_by: ai
model: claude-fable-5-1
skill_version: 0.3.0
created: 2026-11-17
reviewed_by: P-000
reviewed: 2026-11-17
---

> [!info]- Context
> [CONTEXT: Temperature sweep, ten points from minus 20 to plus 70 with a load step at each. In ^s0003-0098 the workaround is splitting into two runs of five points, which doubles the time, and "I have never seen a wrong number from a sweep, only a missing one." Deepens H-S0003-0006.]

![[S-0003#^s0003-0096]]
[[S-0003#^s0003-0096|Open in transcript · S-0003 @ 00:34:53]]

**Rationale:** Reproduction detail (point six to eight, about 3 GB, no log) that an engineering team can act on, plus the qualifying note that the crash loses time, not correctness (RQ3).
