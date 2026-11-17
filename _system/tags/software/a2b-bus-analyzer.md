---
type: tag
tag: software/a2b-bus-analyzer
aliases: [software/a2b-bus-analyzer]
group: software
group_name: Software
level: workspace
status: active
definition: A2B audio bus tool.
highlights: 0
participants: 0
counted: 2026-11-17
---

# software/a2b-bus-analyzer

> A2B audio bus tool.

Group: **Software** · workspace tag · status **active**
Counts refresh when `tag_board.py` runs; the list below is live.

```base
filters:
  and:
    - note.type == "highlight"
    - note.tags.contains("software/a2b-bus-analyzer")
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
