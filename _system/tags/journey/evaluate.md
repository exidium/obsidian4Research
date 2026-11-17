---
type: tag
tag: journey/evaluate
aliases: [journey/evaluate]
group: journey
group_name: Journey stage
level: workspace
status: active
definition: Comparing options, reading datasheets, trying eval boards, deciding what to adopt.
highlights: 9
participants: 3
counted: 2026-11-17
---

# journey/evaluate

> Comparing options, reading datasheets, trying eval boards, deciding what to adopt.

Group: **Journey stage** · workspace tag · status **active**
Counts refresh when `tag_board.py` runs; the list below is live.

```base
filters:
  and:
    - note.type == "highlight"
    - note.tags.contains("journey/evaluate")
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
