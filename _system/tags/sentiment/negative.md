---
type: tag
tag: sentiment/negative
aliases: [sentiment/negative]
group: sentiment
group_name: Sentiment
level: workspace
status: active
definition: Frustration, disappointment, or criticism expressed.
highlights: 20
participants: 3
counted: 2026-11-17
---

# sentiment/negative

> Frustration, disappointment, or criticism expressed.

Group: **Sentiment** · workspace tag · status **active**
Counts refresh when `tag_board.py` runs; the list below is live.

```base
filters:
  and:
    - note.type == "highlight"
    - note.tags.contains("sentiment/negative")
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
