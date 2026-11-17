---
type: tag
tag: correlation/trust-per-result
aliases: [correlation/trust-per-result]
group: correlation
group_name: 3. Simulation vs Bench
level: project
status: active
definition: Trust is granted to one result type after it matched hardware and does not transfer to the tool's other results.
highlights: 1
participants: 1
counted: 2026-11-17
project: 2026_demo-fluxbench
---

# correlation/trust-per-result

> Trust is granted to one result type after it matched hardware and does not transfer to the tool's other results.

Group: **3. Simulation vs Bench** · project tag · status **active**
Counts refresh when `tag_board.py` runs; the list below is live.

```base
filters:
  and:
    - note.type == "highlight"
    - note.tags.contains("correlation/trust-per-result")
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
