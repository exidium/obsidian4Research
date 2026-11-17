---
type: tag
tag: sentiment/neutral
aliases: [sentiment/neutral]
group: sentiment
group_name: Sentiment
level: workspace
status: active
definition: Factual statement with no emotional charge (typical for workflow descriptions).
highlights: 44
participants: 3
counted: 2026-11-17
---

# sentiment/neutral

> Factual statement with no emotional charge (typical for workflow descriptions).

Group: **Sentiment** · workspace tag · status **active**
Counts refresh when `tag_board.py` runs; the list below is live.

```base
filters:
  and:
    - note.type == "highlight"
    - note.tags.contains("sentiment/neutral")
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
