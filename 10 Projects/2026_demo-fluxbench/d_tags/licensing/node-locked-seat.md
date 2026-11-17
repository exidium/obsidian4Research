---
type: tag
tag: licensing/node-locked-seat
aliases: [licensing/node-locked-seat]
group: licensing
group_name: 5. Licensing and Offline
level: project
status: active
definition: The licence is bound to one machine and needs periodic check-ins; deactivation and moves need the vendor or internet access.
highlights: 1
participants: 1
counted: 2026-11-17
project: 2026_demo-fluxbench
---

# licensing/node-locked-seat

> The licence is bound to one machine and needs periodic check-ins; deactivation and moves need the vendor or internet access.

Group: **5. Licensing and Offline** · project tag · status **active**
Counts refresh when `tag_board.py` runs; the list below is live.

```base
filters:
  and:
    - note.type == "highlight"
    - note.tags.contains("licensing/node-locked-seat")
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
