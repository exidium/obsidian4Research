---
type: tag
tag: workflow/review-loop-described
aliases: [workflow/review-loop-described]
group: workflow
group_name: 1. Workflow and Process
level: project
status: active
definition: Participant describes how a design gets reviewed and iterated with colleagues.
highlights: 4
participants: 2
counted: 2026-11-17
project: 2026_demo-fluxbench
---

# workflow/review-loop-described

> Participant describes how a design gets reviewed and iterated with colleagues.

Group: **1. Workflow and Process** · project tag · status **active**
Counts refresh when `tag_board.py` runs; the list below is live.

```base
filters:
  and:
    - note.type == "highlight"
    - note.tags.contains("workflow/review-loop-described")
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
