---
type: tag
tag: sharing/design-fork
aliases: [sharing/design-fork]
group: sharing
group_name: 4. Sharing and Versions
level: project
status: active
definition: Two people hold divergent copies of a design with no way to tell which is current.
highlights: 2
participants: 1
counted: 2026-11-17
project: 2026_demo-fluxbench
---

# sharing/design-fork

> Two people hold divergent copies of a design with no way to tell which is current.

Group: **4. Sharing and Versions** · project tag · status **active**
Counts refresh when `tag_board.py` runs; the list below is live.

```base
filters:
  and:
    - note.type == "highlight"
    - note.tags.contains("sharing/design-fork")
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
