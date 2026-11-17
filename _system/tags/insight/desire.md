---
type: tag
tag: insight/desire
aliases: [insight/desire]
group: insight
group_name: Insight
level: workspace
status: active
definition: Aspiration or wish; softer and more emotional than a feature request.
highlights: 4
participants: 2
counted: 2026-11-17
---

# insight/desire

> Aspiration or wish; softer and more emotional than a feature request.

Group: **Insight** · workspace tag · status **active**
Counts refresh when `tag_board.py` runs; the list below is live.

```base
filters:
  and:
    - note.type == "highlight"
    - note.tags.contains("insight/desire")
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
