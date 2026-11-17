---
type: tag
tag: sharing/reviewer-viewer-missing
aliases: [sharing/reviewer-viewer-missing]
group: sharing
group_name: 4. Sharing and Versions
level: project
status: active
definition: Reviewers and leads cannot open a design without a full licence; there is no read-only viewer or link.
highlights: 4
participants: 1
counted: 2026-11-17
project: 2026_demo-fluxbench
---

# sharing/reviewer-viewer-missing

> Reviewers and leads cannot open a design without a full licence; there is no read-only viewer or link.

Group: **4. Sharing and Versions** · project tag · status **active**
Counts refresh when `tag_board.py` runs; the list below is live.

```base
filters:
  and:
    - note.type == "highlight"
    - note.tags.contains("sharing/reviewer-viewer-missing")
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
