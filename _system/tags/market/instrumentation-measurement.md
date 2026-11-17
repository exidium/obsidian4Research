---
type: tag
tag: market/instrumentation-measurement
aliases: [market/instrumentation-measurement]
group: market
group_name: Market
level: workspace
status: active
definition: Test and measurement context.
highlights: 0
participants: 0
counted: 2026-11-17
---

# market/instrumentation-measurement

> Test and measurement context.

Group: **Market** · workspace tag · status **active**
Counts refresh when `tag_board.py` runs; the list below is live.

```base
filters:
  and:
    - note.type == "highlight"
    - note.tags.contains("market/instrumentation-measurement")
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
