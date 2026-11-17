---
type: tag
tag: competition/competitor-comparison
aliases: [competition/competitor-comparison]
group: competition
group_name: 9. Competition
level: project
status: active
definition: Participant compares FluxBench with another simulation tool on a named capability (change dialogue, plain files, scripting, part picker).
highlights: 3
participants: 2
counted: 2026-11-17
project: 2026_demo-fluxbench
---

# competition/competitor-comparison

> Participant compares FluxBench with another simulation tool on a named capability (change dialogue, plain files, scripting, part picker).

Group: **9. Competition** · project tag · status **active**
Counts refresh when `tag_board.py` runs; the list below is live.

```base
filters:
  and:
    - note.type == "highlight"
    - note.tags.contains("competition/competitor-comparison")
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
