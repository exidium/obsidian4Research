---
type: tag
tag: tools/simulation-crash
aliases: [tools/simulation-crash]
group: tools
group_name: 2. Tool Behaviour
level: project
status: active
definition: The application closes or fails during a run.
highlights: 2
participants: 1
counted: 2026-11-17
project: 2026_demo-fluxbench
---

# tools/simulation-crash

> The application closes or fails during a run.

Group: **2. Tool Behaviour** · project tag · status **active**
Counts refresh when `tag_board.py` runs; the list below is live.

```base
filters:
  and:
    - note.type == "highlight"
    - note.tags.contains("tools/simulation-crash")
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
