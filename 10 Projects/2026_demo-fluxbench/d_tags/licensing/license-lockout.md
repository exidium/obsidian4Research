---
type: tag
tag: licensing/license-lockout
aliases: [licensing/license-lockout]
group: licensing
group_name: 5. Licensing and Offline
level: project
status: active
definition: The tool locked the user out because a license check failed.
highlights: 3
participants: 1
counted: 2026-11-17
project: 2026_demo-fluxbench
---

# licensing/license-lockout

> The tool locked the user out because a license check failed.

Group: **5. Licensing and Offline** · project tag · status **active**
Counts refresh when `tag_board.py` runs; the list below is live.

```base
filters:
  and:
    - note.type == "highlight"
    - note.tags.contains("licensing/license-lockout")
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
