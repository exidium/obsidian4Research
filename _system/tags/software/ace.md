---
type: tag
tag: software/ace
aliases: [software/ace]
group: software
group_name: Software
level: workspace
status: active
definition: ACE Analysis Control Evaluation platform.
highlights: 0
participants: 0
counted: 2026-11-17
---

# software/ace

> ACE Analysis Control Evaluation platform.

Group: **Software** · workspace tag · status **active**
Counts refresh when `tag_board.py` runs; the list below is live.

```base
filters:
  and:
    - note.type == "highlight"
    - note.tags.contains("software/ace")
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
