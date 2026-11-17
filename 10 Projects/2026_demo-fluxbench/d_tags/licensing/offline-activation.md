---
type: tag
tag: licensing/offline-activation
aliases: [licensing/offline-activation]
group: licensing
group_name: 5. Licensing and Offline
level: project
status: active
definition: Activation or check-in needs network access the user does not have.
highlights: 2
participants: 2
counted: 2026-11-17
project: 2026_demo-fluxbench
---

# licensing/offline-activation

> Activation or check-in needs network access the user does not have.

Group: **5. Licensing and Offline** · project tag · status **active**
Counts refresh when `tag_board.py` runs; the list below is live.

```base
filters:
  and:
    - note.type == "highlight"
    - note.tags.contains("licensing/offline-activation")
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
