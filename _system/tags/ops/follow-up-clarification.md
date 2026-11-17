---
type: tag
tag: ops/follow-up-clarification
aliases: [ops/follow-up-clarification]
group: ops
group_name: Research ops
level: workspace
status: active
definition: Something was unclear; verify with the participant.
highlights: 0
participants: 0
counted: 2026-11-17
---

# ops/follow-up-clarification

> Something was unclear; verify with the participant.

Group: **Research ops** · workspace tag · status **active**
Counts refresh when `tag_board.py` runs; the list below is live.

```base
filters:
  and:
    - note.type == "highlight"
    - note.tags.contains("ops/follow-up-clarification")
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
