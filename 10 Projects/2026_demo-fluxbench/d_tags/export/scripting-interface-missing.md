---
type: tag
tag: export/scripting-interface-missing
aliases: [export/scripting-interface-missing]
group: export
group_name: 7. Export and Handoff
level: project
status: active
definition: No command line, scripting or batch interface to drive simulation runs from the user's own automation.
highlights: 2
participants: 1
counted: 2026-11-17
project: 2026_demo-fluxbench
---

# export/scripting-interface-missing

> No command line, scripting or batch interface to drive simulation runs from the user's own automation.

Group: **7. Export and Handoff** · project tag · status **active**
Counts refresh when `tag_board.py` runs; the list below is live.

```base
filters:
  and:
    - note.type == "highlight"
    - note.tags.contains("export/scripting-interface-missing")
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
