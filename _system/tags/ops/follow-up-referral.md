---
type: tag
tag: ops/follow-up-referral
aliases: [ops/follow-up-referral]
group: ops
group_name: Research ops
level: workspace
status: active
definition: Participant mentioned someone else we should talk to.
highlights: 0
participants: 0
counted: 2026-11-17
---

# ops/follow-up-referral

> Participant mentioned someone else we should talk to.

Group: **Research ops** · workspace tag · status **active**
Counts refresh when `tag_board.py` runs; the list below is live.

```base
filters:
  and:
    - note.type == "highlight"
    - note.tags.contains("ops/follow-up-referral")
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
