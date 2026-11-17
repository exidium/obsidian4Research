---
type: tag
tag: correlation/thermal-correlated
aliases: [correlation/thermal-correlated]
group: correlation
group_name: 3. Simulation vs Bench
level: project
status: active
definition: The thermal estimate matched hardware; apply to positive correlation moments.
highlights: 1
participants: 1
counted: 2026-11-17
project: 2026_demo-fluxbench
---

# correlation/thermal-correlated

> The thermal estimate matched hardware; apply to positive correlation moments.

Group: **3. Simulation vs Bench** · project tag · status **active**
Counts refresh when `tag_board.py` runs; the list below is live.

```base
filters:
  and:
    - note.type == "highlight"
    - note.tags.contains("correlation/thermal-correlated")
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
