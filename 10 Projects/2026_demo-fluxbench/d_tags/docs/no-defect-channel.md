---
type: tag
tag: docs/no-defect-channel
aliases: [docs/no-defect-channel]
group: docs
group_name: 6. Documentation and Support
level: project
status: active
definition: No practical way to report a bug from inside the tool.
highlights: 3
participants: 2
counted: 2026-11-17
project: 2026_demo-fluxbench
---

# docs/no-defect-channel

> No practical way to report a bug from inside the tool.

Group: **6. Documentation and Support** · project tag · status **active**
Counts refresh when `tag_board.py` runs; the list below is live.

```base
filters:
  and:
    - note.type == "highlight"
    - note.tags.contains("docs/no-defect-channel")
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
