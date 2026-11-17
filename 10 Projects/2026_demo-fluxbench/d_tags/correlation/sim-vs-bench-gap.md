---
type: tag
tag: correlation/sim-vs-bench-gap
aliases: [correlation/sim-vs-bench-gap]
group: correlation
group_name: 3. Simulation vs Bench
level: project
status: active
definition: Participant compares a simulated value with a measurement or a trusted calculation and reports a gap.
highlights: 11
participants: 3
counted: 2026-11-17
project: 2026_demo-fluxbench
---

# correlation/sim-vs-bench-gap

> Participant compares a simulated value with a measurement or a trusted calculation and reports a gap.

Group: **3. Simulation vs Bench** · project tag · status **active**
Counts refresh when `tag_board.py` runs; the list below is live.

```base
filters:
  and:
    - note.type == "highlight"
    - note.tags.contains("correlation/sim-vs-bench-gap")
    - note.review != "rejected"
    - note.project == "2026_demo-fluxbench"
views:
  - type: table
    name: Highlights
    order:
      - file.name
      - note.participant
      - note.review
      - note.quote
      - note.tags
    sort:
      - property: file.name
        direction: ASC
```
