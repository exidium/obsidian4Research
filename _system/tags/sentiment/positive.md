---
type: tag
tag: sentiment/positive
aliases: [sentiment/positive]
group: sentiment
group_name: Sentiment
level: workspace
status: active
definition: Clear satisfaction, praise, or delight expressed.
highlights: 4
participants: 2
counted: 2026-11-17
---

# sentiment/positive

> Clear satisfaction, praise, or delight expressed.

Group: **Sentiment** · workspace tag · status **active**
Counts refresh when `tag_board.py` runs; the list below is live.

```base
filters:
  and:
    - note.type == "highlight"
    - note.tags.contains("sentiment/positive")
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
