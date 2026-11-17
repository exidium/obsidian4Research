---
type: tag
tag: experience/advanced
aliases: [experience/advanced]
group: experience
group_name: Experience level
level: workspace
status: active
definition: Participant's words indicate expert depth (teaches others, deep domain reasoning, edge-case fluency).
highlights: 9
participants: 3
counted: 2026-11-17
---

# experience/advanced

> Participant's words indicate expert depth (teaches others, deep domain reasoning, edge-case fluency).

Group: **Experience level** · workspace tag · status **active**
Counts refresh when `tag_board.py` runs; the list below is live.

```base
filters:
  and:
    - note.type == "highlight"
    - note.tags.contains("experience/advanced")
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
