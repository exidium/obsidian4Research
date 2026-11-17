---
type: tag
tag: functionality/existing-feature
aliases: [functionality/existing-feature]
group: functionality
group_name: Functionality
level: workspace
status: active
definition: Participant references something that already exists (use to validate awareness).
highlights: 2
participants: 1
counted: 2026-11-17
---

# functionality/existing-feature

> Participant references something that already exists (use to validate awareness).

Group: **Functionality** · workspace tag · status **active**
Counts refresh when `tag_board.py` runs; the list below is live.

```base
filters:
  and:
    - note.type == "highlight"
    - note.tags.contains("functionality/existing-feature")
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
