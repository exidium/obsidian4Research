---
type: tag
tag: software/fluxbench-designer
aliases: [software/fluxbench-designer]
group: software
group_name: Software
level: workspace
status: active
definition: FICTIONAL demo product; delete for real use.
highlights: 2
participants: 1
counted: 2026-11-17
---

# software/fluxbench-designer

> FICTIONAL demo product; delete for real use.

Group: **Software** · workspace tag · status **active**
Counts refresh when `tag_board.py` runs; the list below is live.

```base
filters:
  and:
    - note.type == "highlight"
    - note.tags.contains("software/fluxbench-designer")
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
