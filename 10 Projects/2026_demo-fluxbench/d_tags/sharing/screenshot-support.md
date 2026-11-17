---
type: tag
tag: sharing/screenshot-support
aliases: [sharing/screenshot-support]
group: sharing
group_name: 4. Sharing and Versions
level: project
status: active
definition: Support happens via screenshots because the design itself cannot be shared.
highlights: 2
participants: 1
counted: 2026-11-17
project: 2026_demo-fluxbench
---

# sharing/screenshot-support

> Support happens via screenshots because the design itself cannot be shared.

Group: **4. Sharing and Versions** · project tag · status **active**
Counts refresh when `tag_board.py` runs; the list below is live.

```base
filters:
  and:
    - note.type == "highlight"
    - note.tags.contains("sharing/screenshot-support")
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
