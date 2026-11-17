---
type: tag
tag: software/interactive-engineering-solutions
aliases: [software/interactive-engineering-solutions]
group: software
group_name: Software
level: workspace
status: active
definition: IES platform.
highlights: 0
participants: 0
counted: 2026-11-17
---

# software/interactive-engineering-solutions

> IES platform.

Group: **Software** · workspace tag · status **active**
Counts refresh when `tag_board.py` runs; the list below is live.

```base
filters:
  and:
    - note.type == "highlight"
    - note.tags.contains("software/interactive-engineering-solutions")
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
