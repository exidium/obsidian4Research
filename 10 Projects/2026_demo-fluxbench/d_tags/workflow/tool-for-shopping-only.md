---
type: tag
tag: workflow/tool-for-shopping-only
aliases: [workflow/tool-for-shopping-only]
group: workflow
group_name: 1. Workflow and Process
level: project
status: active
definition: FluxBench is used only to pick the part and get a first schematic; the real design is done in a spreadsheet or another tool trusted to reopen.
highlights: 2
participants: 1
counted: 2026-11-17
project: 2026_demo-fluxbench
---

# workflow/tool-for-shopping-only

> FluxBench is used only to pick the part and get a first schematic; the real design is done in a spreadsheet or another tool trusted to reopen.

Group: **1. Workflow and Process** · project tag · status **active**
Counts refresh when `tag_board.py` runs; the list below is live.

```base
filters:
  and:
    - note.type == "highlight"
    - note.tags.contains("workflow/tool-for-shopping-only")
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
