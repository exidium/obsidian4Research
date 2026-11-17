---
type: tag
tag: sentiment/confused
aliases: [sentiment/confused]
group: sentiment
group_name: Sentiment
level: workspace
status: active
definition: Participant is uncertain, misunderstanding, or lost.
highlights: 1
participants: 1
counted: 2026-11-17
---

# sentiment/confused

> Participant is uncertain, misunderstanding, or lost.

Group: **Sentiment** · workspace tag · status **active**
Counts refresh when `tag_board.py` runs; the list below is live.

```base
filters:
  and:
    - note.type == "highlight"
    - note.tags.contains("sentiment/confused")
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
