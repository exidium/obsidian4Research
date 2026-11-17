---
type: tag
tag: export/report-retyping
aliases: [export/report-retyping]
group: export
group_name: 7. Export and Handoff
level: project
status: active
definition: Numbers are retyped by hand into reports because no data export exists.
highlights: 1
participants: 1
counted: 2026-11-17
project: 2026_demo-fluxbench
---

# export/report-retyping

> Numbers are retyped by hand into reports because no data export exists.

Group: **7. Export and Handoff** · project tag · status **active**
Counts refresh when `tag_board.py` runs; the list below is live.

```base
filters:
  and:
    - note.type == "highlight"
    - note.tags.contains("export/report-retyping")
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
