---
type: tag
tag: correlation/accuracy-statement-missing
aliases: [correlation/accuracy-statement-missing]
group: correlation
group_name: 3. Simulation vs Bench
level: project
status: active
definition: Participant wants the vendor to state how accurate a result is meant to be.
highlights: 9
participants: 2
counted: 2026-11-17
project: 2026_demo-fluxbench
---

# correlation/accuracy-statement-missing

> Participant wants the vendor to state how accurate a result is meant to be.

Group: **3. Simulation vs Bench** · project tag · status **active**
Counts refresh when `tag_board.py` runs; the list below is live.

```base
filters:
  and:
    - note.type == "highlight"
    - note.tags.contains("correlation/accuracy-statement-missing")
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
