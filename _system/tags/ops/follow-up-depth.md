---
type: tag
tag: ops/follow-up-depth
aliases: [ops/follow-up-depth]
group: ops
group_name: Research ops
level: workspace
status: active
definition: This topic needs deeper probing in a future session.
highlights: 3
participants: 2
counted: 2026-11-17
---

# ops/follow-up-depth

> This topic needs deeper probing in a future session.

Group: **Research ops** · workspace tag · status **active**
Counts refresh when `tag_board.py` runs; the list below is live.

```base
filters:
  and:
    - note.type == "highlight"
    - note.tags.contains("ops/follow-up-depth")
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
