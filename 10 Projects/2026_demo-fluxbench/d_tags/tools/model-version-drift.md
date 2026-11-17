---
type: tag
tag: tools/model-version-drift
aliases: [tools/model-version-drift]
group: tools
group_name: 2. Tool Behaviour
level: project
status: active
definition: Results of an old design change because a part model was updated.
highlights: 1
participants: 1
counted: 2026-11-17
project: 2026_demo-fluxbench
---

# tools/model-version-drift

> Results of an old design change because a part model was updated.

Group: **2. Tool Behaviour** · project tag · status **active**
Counts refresh when `tag_board.py` runs; the list below is live.

```base
filters:
  and:
    - note.type == "highlight"
    - note.tags.contains("tools/model-version-drift")
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
