---
type: tag
tag: correlation/loss-breakdown-missing
aliases: [correlation/loss-breakdown-missing]
group: correlation
group_name: 3. Simulation vs Bench
level: project
status: active
definition: Results are aggregated in a way that blocks diagnosing which mechanism is off.
highlights: 1
participants: 1
counted: 2026-11-17
project: 2026_demo-fluxbench
---

# correlation/loss-breakdown-missing

> Results are aggregated in a way that blocks diagnosing which mechanism is off.

Group: **3. Simulation vs Bench** · project tag · status **active**
Counts refresh when `tag_board.py` runs; the list below is live.

```base
filters:
  and:
    - note.type == "highlight"
    - note.tags.contains("correlation/loss-breakdown-missing")
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
