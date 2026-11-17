---
type: tag
tag: software/ltpowercad
aliases: [software/ltpowercad]
group: software
group_name: Software
level: workspace
status: active
definition: LTpowerCAD tool.
highlights: 0
participants: 0
counted: 2026-11-17
---

# software/ltpowercad

> LTpowerCAD tool.

Group: **Software** · workspace tag · status **active**
Counts refresh when `tag_board.py` runs; the list below is live.

```base
filters:
  and:
    - note.type == "highlight"
    - note.tags.contains("software/ltpowercad")
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
