---
type: highlight
highlight_id: H-S0002-0015
aliases: [H-S0002-0015]
title: VM per project to freeze the tool
project: 2026_demo-fluxbench
source: '[[S-0002]]'
block: s0002-0040
participant: P-002
quote: 'A customer in medical imaging told me their quality system treats a simulation report as a controlled document. If the tool can''t reproduce the report a year later, the report is worthless to their auditor. They asked me, and I''m quoting, ''How do I freeze the tool?'' My answer was: keep a virtual machine with that exact version and never touch it. They actually did that. They have a VM per project now. That''s a customer building their own version control because we don''t ship one.'
context: '[CONTEXT: Asked whether the compliance angle comes up often; he names medical and functional-safety markets.]'
tags: [functionality/workaround, insight/pain-point, sentiment/negative, journey/validate, market/digital-healthcare, tools/model-version-drift, tools/result-reproducibility]
review: accepted
created_by: ai
model: claude-fable-5-1
skill_version: 0.3.0
created: 2026-11-17
reviewed_by: P-000
reviewed: 2026-11-17
---

> [!info]- Context
> [CONTEXT: Asked whether the compliance angle comes up often; he names medical and functional-safety markets.]

![[S-0002#^s0002-0040]]
[[S-0002#^s0002-0040|Open in transcript · S-0002 @ 00:13:07]]

**Rationale:** RQ2 evidence that in regulated markets the design's life after simulation includes audits the tool cannot survive, and the VM-per-project workaround is the clearest cost signal for a model-pinning feature.
