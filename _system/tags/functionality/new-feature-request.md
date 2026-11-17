---
type: tag
tag: functionality/new-feature-request
aliases: [functionality/new-feature-request]
group: functionality
group_name: Functionality
level: workspace
status: active
definition: Participant explicitly asks for something that does not exist.
highlights: 30
participants: 3
counted: 2026-11-17
---

# functionality/new-feature-request

> Participant explicitly asks for something that does not exist.

Group: **Functionality** · workspace tag · status **active**
Counts refresh when `tag_board.py` runs; the list below is live.

```base
filters:
  and:
    - note.type == "highlight"
    - note.tags.contains("functionality/new-feature-request")
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
