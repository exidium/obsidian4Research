---
type: tag
tag: functionality/bug
aliases: [functionality/bug]
group: functionality
group_name: Functionality
level: workspace
status: active
definition: Participant describes broken behaviour (not a gap; actually broken).
highlights: 3
participants: 3
counted: 2026-11-17
---

# functionality/bug

> Participant describes broken behaviour (not a gap; actually broken).

Group: **Functionality** · workspace tag · status **active**
Counts refresh when `tag_board.py` runs; the list below is live.

```base
filters:
  and:
    - note.type == "highlight"
    - note.tags.contains("functionality/bug")
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
