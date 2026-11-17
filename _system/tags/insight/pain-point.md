---
type: tag
tag: insight/pain-point
aliases: [insight/pain-point]
group: insight
group_name: Insight
level: workspace
status: active
definition: Any moment of frustration, friction, or failure.
highlights: 23
participants: 3
counted: 2026-11-17
---

# insight/pain-point

> Any moment of frustration, friction, or failure.

Group: **Insight** · workspace tag · status **active**
Counts refresh when `tag_board.py` runs; the list below is live.

```base
filters:
  and:
    - note.type == "highlight"
    - note.tags.contains("insight/pain-point")
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
