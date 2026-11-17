---
type: tag
tag: functionality/workaround
aliases: [functionality/workaround]
group: functionality
group_name: Functionality
level: workspace
status: active
definition: Participant describes a hack or alternative path to achieve their goal. Direct evidence of unmet need.
highlights: 7
participants: 3
counted: 2026-11-17
---

# functionality/workaround

> Participant describes a hack or alternative path to achieve their goal. Direct evidence of unmet need.

Group: **Functionality** · workspace tag · status **active**
Counts refresh when `tag_board.py` runs; the list below is live.

```base
filters:
  and:
    - note.type == "highlight"
    - note.tags.contains("functionality/workaround")
    - note.review != "rejected"
views:
  - type: table
    name: Highlights
    groupBy:
      property: note.project
      direction: ASC
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
