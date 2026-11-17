---
type: tag
tag: export/revision-stamp-missing
aliases: [export/revision-stamp-missing]
group: export
group_name: 7. Export and Handoff
level: project
status: active
definition: Exports (PDF, plots, BOM) carry no revision or version stamp, so a reviewed artefact can diverge from the built design without anyone noticing.
highlights: 3
participants: 1
counted: 2026-11-17
project: 2026_demo-fluxbench
---

# export/revision-stamp-missing

> Exports (PDF, plots, BOM) carry no revision or version stamp, so a reviewed artefact can diverge from the built design without anyone noticing.

Group: **7. Export and Handoff** · project tag · status **active**
Counts refresh when `tag_board.py` runs; the list below is live.

```base
filters:
  and:
    - note.type == "highlight"
    - note.tags.contains("export/revision-stamp-missing")
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
