---
type: tag
tag: selection/part-finder-stock
aliases: [selection/part-finder-stock]
group: selection
group_name: 8. Part Selection
level: project
status: active
definition: Part selection filtered by distributor stock; apply to selection moments.
highlights: 1
participants: 1
counted: 2026-11-17
project: 2026_demo-fluxbench
---

# selection/part-finder-stock

> Part selection filtered by distributor stock; apply to selection moments.

Group: **8. Part Selection** · project tag · status **active**
Counts refresh when `tag_board.py` runs; the list below is live.

```base
filters:
  and:
    - note.type == "highlight"
    - note.tags.contains("selection/part-finder-stock")
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
