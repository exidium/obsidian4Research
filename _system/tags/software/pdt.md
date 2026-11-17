---
type: tag
tag: software/pdt
aliases: [software/pdt]
group: software
group_name: Software
level: workspace
status: active
definition: Product Development Tools platform.
highlights: 0
participants: 0
counted: 2026-11-17
---

# software/pdt

> Product Development Tools platform.

Group: **Software** · workspace tag · status **active**
Counts refresh when `tag_board.py` runs; the list below is live.

```base
filters:
  and:
    - note.type == "highlight"
    - note.tags.contains("software/pdt")
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
