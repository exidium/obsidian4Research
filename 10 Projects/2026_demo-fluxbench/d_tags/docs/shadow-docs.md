---
type: tag
tag: docs/shadow-docs
aliases: [docs/shadow-docs]
group: docs
group_name: 6. Documentation and Support
level: project
status: active
definition: Someone outside the product team wrote their own guide to compensate for the official docs.
highlights: 5
participants: 3
counted: 2026-11-17
project: 2026_demo-fluxbench
---

# docs/shadow-docs

> Someone outside the product team wrote their own guide to compensate for the official docs.

Group: **6. Documentation and Support** · project tag · status **active**
Counts refresh when `tag_board.py` runs; the list below is live.

```base
filters:
  and:
    - note.type == "highlight"
    - note.tags.contains("docs/shadow-docs")
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
