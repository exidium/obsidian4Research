---
type: tag
tag: experience/intermediate
aliases: [experience/intermediate]
group: experience
group_name: Experience level
level: workspace
status: active
definition: Participant's words indicate working knowledge (competent use, some years of practice).
highlights: 0
participants: 0
counted: 2026-11-17
---

# experience/intermediate

> Participant's words indicate working knowledge (competent use, some years of practice).

Group: **Experience level** · workspace tag · status **active**
Counts refresh when `tag_board.py` runs; the list below is live.

```base
filters:
  and:
    - note.type == "highlight"
    - note.tags.contains("experience/intermediate")
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
