---
type: tag
tag: tools/hidden-defaults
aliases: [tools/hidden-defaults]
group: tools
group_name: 2. Tool Behaviour
level: project
status: active
definition: A parameter or assumption the tool applies without showing it on the main screens.
highlights: 4
participants: 3
counted: 2026-11-17
project: 2026_demo-fluxbench
---

# tools/hidden-defaults

> A parameter or assumption the tool applies without showing it on the main screens.

Group: **2. Tool Behaviour** · project tag · status **active**
Counts refresh when `tag_board.py` runs; the list below is live.

```base
filters:
  and:
    - note.type == "highlight"
    - note.tags.contains("tools/hidden-defaults")
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
