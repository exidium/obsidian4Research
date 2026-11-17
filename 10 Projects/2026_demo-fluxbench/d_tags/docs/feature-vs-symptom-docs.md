---
type: tag
tag: docs/feature-vs-symptom-docs
aliases: [docs/feature-vs-symptom-docs]
group: docs
group_name: 6. Documentation and Support
level: project
status: active
definition: Documentation is organised by feature while users search by symptom.
highlights: 2
participants: 2
counted: 2026-11-17
project: 2026_demo-fluxbench
---

# docs/feature-vs-symptom-docs

> Documentation is organised by feature while users search by symptom.

Group: **6. Documentation and Support** · project tag · status **active**
Counts refresh when `tag_board.py` runs; the list below is live.

```base
filters:
  and:
    - note.type == "highlight"
    - note.tags.contains("docs/feature-vs-symptom-docs")
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
