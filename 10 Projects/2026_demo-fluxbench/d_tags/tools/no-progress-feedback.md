---
type: tag
tag: tools/no-progress-feedback
aliases: [tools/no-progress-feedback]
group: tools
group_name: 2. Tool Behaviour
level: project
status: active
definition: Long runs give no progress indication or block the interface.
highlights: 1
participants: 1
counted: 2026-11-17
project: 2026_demo-fluxbench
---

# tools/no-progress-feedback

> Long runs give no progress indication or block the interface.

Group: **2. Tool Behaviour** · project tag · status **active**
Counts refresh when `tag_board.py` runs; the list below is live.

```base
filters:
  and:
    - note.type == "highlight"
    - note.tags.contains("tools/no-progress-feedback")
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
