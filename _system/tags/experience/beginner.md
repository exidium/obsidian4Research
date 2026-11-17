---
type: tag
tag: experience/beginner
aliases: [experience/beginner]
group: experience
group_name: Experience level
level: workspace
status: active
definition: Participant's words indicate newness to the domain or tool (learning, first encounter, unfamiliarity).
highlights: 3
participants: 2
counted: 2026-11-17
---

# experience/beginner

> Participant's words indicate newness to the domain or tool (learning, first encounter, unfamiliarity).

Group: **Experience level** · workspace tag · status **active**
Counts refresh when `tag_board.py` runs; the list below is live.

```base
filters:
  and:
    - note.type == "highlight"
    - note.tags.contains("experience/beginner")
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
