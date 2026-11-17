---
type: tag
tag: tools/silent-parameter-reset
aliases: [tools/silent-parameter-reset]
group: tools
group_name: 2. Tool Behaviour
level: project
status: active
definition: The tool changed a value the user had set
highlights: 4
participants: 2
counted: 2026-11-17
project: 2026_demo-fluxbench
---

# tools/silent-parameter-reset

> The tool changed a value the user had set

Group: **2. Tool Behaviour** · project tag · status **active**
Counts refresh when `tag_board.py` runs; the list below is live.

```base
filters:
  and:
    - note.type == "highlight"
    - note.tags.contains("tools/silent-parameter-reset")
    - note.review != "rejected"
    - note.project == "2026_demo-fluxbench"
views:
  - type: table
    name: Highlights
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
