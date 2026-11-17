---
type: tag
tag: journey/design
aliases: [journey/design]
group: journey
group_name: Journey stage
level: workspace
status: active
definition: Active design work; architecture, selection, configuration, simulation.
highlights: 25
participants: 3
counted: 2026-11-17
---

# journey/design

> Active design work; architecture, selection, configuration, simulation.

Group: **Journey stage** · workspace tag · status **active**
Counts refresh when `tag_board.py` runs; the list below is live.

```base
filters:
  and:
    - note.type == "highlight"
    - note.tags.contains("journey/design")
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
