---
type: tag
tag: market/intelligent-buildings
aliases: [market/intelligent-buildings]
group: market
group_name: Market
level: workspace
status: active
definition: Smart building or BMS context.
highlights: 0
participants: 0
counted: 2026-11-17
---

# market/intelligent-buildings

> Smart building or BMS context.

Group: **Market** · workspace tag · status **active**
Counts refresh when `tag_board.py` runs; the list below is live.

```base
filters:
  and:
    - note.type == "highlight"
    - note.tags.contains("market/intelligent-buildings")
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
