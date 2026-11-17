---
type: tag
tag: journey/support
aliases: [journey/support]
group: journey
group_name: Journey stage
level: workspace
status: active
definition: Getting help; documentation, FAEs, portals, reporting problems.
highlights: 9
participants: 2
counted: 2026-11-17
---

# journey/support

> Getting help; documentation, FAEs, portals, reporting problems.

Group: **Journey stage** · workspace tag · status **active**
Counts refresh when `tag_board.py` runs; the list below is live.

```base
filters:
  and:
    - note.type == "highlight"
    - note.tags.contains("journey/support")
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
