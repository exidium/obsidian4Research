---
type: tag
tag: workflow/quality-system-constraint
aliases: [workflow/quality-system-constraint]
group: workflow
group_name: 1. Workflow and Process
level: project
status: active
definition: A rule of the participant's quality system (acceptance limit, controlled document, software assessment, audit) that governs whether a simulated value may count as evidence.
highlights: 3
participants: 1
counted: 2026-11-17
project: 2026_demo-fluxbench
---

# workflow/quality-system-constraint

> A rule of the participant's quality system (acceptance limit, controlled document, software assessment, audit) that governs whether a simulated value may count as evidence.

Group: **1. Workflow and Process** · project tag · status **active**
Counts refresh when `tag_board.py` runs; the list below is live.

```base
filters:
  and:
    - note.type == "highlight"
    - note.tags.contains("workflow/quality-system-constraint")
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
