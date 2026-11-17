---
type: tag
tag: market/industrial-automation
aliases: [market/industrial-automation]
group: market
group_name: Market
level: workspace
status: active
definition: Factory automation or IIoT context.
highlights: 2
participants: 1
counted: 2026-11-17
---

# market/industrial-automation

> Factory automation or IIoT context.

Group: **Market** · workspace tag · status **active**
Counts refresh when `tag_board.py` runs; the list below is live.

```base
filters:
  and:
    - note.type == "highlight"
    - note.tags.contains("market/industrial-automation")
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
