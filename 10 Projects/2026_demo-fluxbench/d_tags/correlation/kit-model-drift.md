---
type: tag
tag: correlation/kit-model-drift
aliases: [correlation/kit-model-drift]
group: correlation
group_name: 3. Simulation vs Bench
level: project
status: active
definition: The evaluation kit's actual parts differ from the simulation model's defaults.
highlights: 5
participants: 2
counted: 2026-11-17
project: 2026_demo-fluxbench
---

# correlation/kit-model-drift

> The evaluation kit's actual parts differ from the simulation model's defaults.

Group: **3. Simulation vs Bench** · project tag · status **active**
Counts refresh when `tag_board.py` runs; the list below is live.

```base
filters:
  and:
    - note.type == "highlight"
    - note.tags.contains("correlation/kit-model-drift")
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
