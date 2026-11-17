---
type: tag
tag: functionality/feature-removal-request
aliases: [functionality/feature-removal-request]
group: functionality
group_name: Functionality
level: workspace
status: active
definition: Participant wants something taken away or simplified.
highlights: 0
participants: 0
counted: 2026-11-17
---

# functionality/feature-removal-request

> Participant wants something taken away or simplified.

Group: **Functionality** · workspace tag · status **active**
Counts refresh when `tag_board.py` runs; the list below is live.

```base
filters:
  and:
    - note.type == "highlight"
    - note.tags.contains("functionality/feature-removal-request")
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
