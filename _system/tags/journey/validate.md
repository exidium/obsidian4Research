---
type: tag
tag: journey/validate
aliases: [journey/validate]
group: journey
group_name: Journey stage
level: workspace
status: active
definition: Testing on hardware, correlating, signing off.
highlights: 8
participants: 2
counted: 2026-11-17
---

# journey/validate

> Testing on hardware, correlating, signing off.

Group: **Journey stage** · workspace tag · status **active**
Counts refresh when `tag_board.py` runs; the list below is live.

```base
filters:
  and:
    - note.type == "highlight"
    - note.tags.contains("journey/validate")
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
