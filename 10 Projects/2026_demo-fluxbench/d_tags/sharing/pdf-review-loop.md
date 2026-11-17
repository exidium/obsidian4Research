---
type: tag
tag: sharing/pdf-review-loop
aliases: [sharing/pdf-review-loop]
group: sharing
group_name: 4. Sharing and Versions
level: project
status: active
definition: Design review runs on exported PDFs rather than the design.
highlights: 5
participants: 2
counted: 2026-11-17
project: 2026_demo-fluxbench
---

# sharing/pdf-review-loop

> Design review runs on exported PDFs rather than the design.

Group: **4. Sharing and Versions** · project tag · status **active**
Counts refresh when `tag_board.py` runs; the list below is live.

```base
filters:
  and:
    - note.type == "highlight"
    - note.tags.contains("sharing/pdf-review-loop")
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
