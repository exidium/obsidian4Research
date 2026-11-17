---
type: tag
tag: workflow/workflow-described
aliases: [workflow/workflow-described]
group: workflow
group_name: 1. Workflow and Process
level: project
status: active
definition: Participant describes how they actually do a step of their work.
highlights: 1
participants: 1
counted: 2026-11-17
project: 2026_demo-fluxbench
---

# workflow/workflow-described

> Participant describes how they actually do a step of their work.

Group: **1. Workflow and Process** · project tag · status **active**
Counts refresh when `tag_board.py` runs; the list below is live.

```base
filters:
  and:
    - note.type == "highlight"
    - note.tags.contains("workflow/workflow-described")
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
