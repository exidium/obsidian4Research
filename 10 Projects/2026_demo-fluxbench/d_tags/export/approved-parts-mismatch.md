---
type: tag
tag: export/approved-parts-mismatch
aliases: [export/approved-parts-mismatch]
group: export
group_name: 7. Export and Handoff
level: project
status: active
definition: BOM export suggests parts outside the company's approved vendor list.
highlights: 1
participants: 1
counted: 2026-11-17
project: 2026_demo-fluxbench
---

# export/approved-parts-mismatch

> BOM export suggests parts outside the company's approved vendor list.

Group: **7. Export and Handoff** · project tag · status **active**
Counts refresh when `tag_board.py` runs; the list below is live.

```base
filters:
  and:
    - note.type == "highlight"
    - note.tags.contains("export/approved-parts-mismatch")
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
