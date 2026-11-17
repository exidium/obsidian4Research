---
type: highlight
highlight_id: H-S0002-0013
aliases: [H-S0002-0013]
title: Model got more honest, customer blamed the part
project: 2026_demo-fluxbench
source: '[[S-0002]]'
block: s0002-0034
participant: P-002
quote: They reopened it to add a second rail, and the efficiency curve had dropped about two points and the thermal estimate was warmer. Nothing in the schematic had changed. They assumed they'd fat-fingered something and spent a day comparing against a PDF export they'd luckily kept. Then they called me, and the first thing the engineer said was, 'Did your part get worse?' The part didn't get worse. The model got more honest. We'd updated the switching loss model for that family in the summer release, and the tool just applies the new model when you open an old design. There's no note, no changelog in the file, nothing.
context: '[CONTEXT: Asked to walk through the last time a model update changed an old design''s results. The customer was an industrial-drives account; the design had been signed off in the spring.]'
tags: [insight/pain-point, sentiment/negative, journey/design, market/industrial-automation, tools/model-version-drift, tools/design-history-missing]
review: accepted
created_by: ai
model: claude-fable-5-1
skill_version: 0.3.0
created: 2026-11-17
reviewed_by: P-000
reviewed: 2026-11-17
---

> [!info]- Context
> [CONTEXT: Asked to walk through the last time a model update changed an old design's results. The customer was an industrial-drives account; the design had been signed off in the spring.]

![[S-0002#^s0002-0034]]
[[S-0002#^s0002-0034|Open in transcript · S-0002 @ 00:10:04]]

**Rationale:** A concrete case showing the mechanism behind H-S0002-0012: the customer's first hypothesis was that the silicon had degraded, and only a kept PDF let them rule out their own error, which makes this RQ3 evidence that "wrong" results are attributed to the part rather than to a silent model change.
