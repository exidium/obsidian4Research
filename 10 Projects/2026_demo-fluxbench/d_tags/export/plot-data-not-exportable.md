---
type: tag
tag: export/plot-data-not-exportable
aliases: [export/plot-data-not-exportable]
group: export
group_name: 7. Export and Handoff
level: project
status: active
definition: Plots export as images but the underlying numbers do not.
highlights: 2
participants: 1
counted: 2026-11-17
project: 2026_demo-fluxbench
---

# export/plot-data-not-exportable

> Plots export as images but the underlying numbers do not.

Group: **7. Export and Handoff** · project tag · status **active**
Counts refresh when `tag_board.py` runs; the list below is live.

```base
filters:
  and:
    - note.type == "highlight"
    - note.tags.contains("export/plot-data-not-exportable")
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
