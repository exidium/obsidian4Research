---
type: tag
tag: market/digital-healthcare
aliases: [market/digital-healthcare]
group: market
group_name: Market
level: workspace
status: active
definition: Medical or healthcare tech context.
highlights: 6
participants: 2
counted: 2026-11-17
---

# market/digital-healthcare

> Medical or healthcare tech context.

Group: **Market** · workspace tag · status **active**
Counts refresh when `tag_board.py` runs; the list below is live.

```base
filters:
  and:
    - note.type == "highlight"
    - note.tags.contains("market/digital-healthcare")
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
