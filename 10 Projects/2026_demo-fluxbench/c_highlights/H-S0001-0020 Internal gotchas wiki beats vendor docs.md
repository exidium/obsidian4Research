---
type: highlight
highlight_id: H-S0001-0020
aliases: [H-S0001-0020]
title: Internal gotchas wiki beats vendor docs
project: 2026_demo-fluxbench
source: '[[S-0001]]'
block: s0001-0064
participant: P-001
quote: He'd actually written it in our internal wiki, a page called FluxBench gotchas, which I didn't know existed until he told me. It's got about eight items on it now. The frequency thing, the fact that the efficiency sweep locks the UI, a thing about the inductor library not having DCR for some parts so the loss comes out optimistic. That wiki page is more useful to me than the vendor's documentation, which is a bit of an indictment. It's also a page the vendor will never see.
context: '[CONTEXT: Block 0062: the vendor''s user guide is organised by screen and its simulation-settings section does not say which parameters reset on a part change; P-001 looked specifically. Block 0136: the gotchas page will be the first thing the next three designers in the group receive, before they open the tool.]'
tags: [functionality/workaround, insight/pain-point, sentiment/negative, journey/support, docs/shadow-docs, docs/feature-vs-symptom-docs]
review: accepted
created_by: ai
model: claude-fable-5-1
skill_version: 0.3.0
created: 2026-11-17
reviewed_by: P-000
reviewed: 2026-11-17
---

> [!info]- Context
> [CONTEXT: Block 0062: the vendor's user guide is organised by screen and its simulation-settings section does not say which parameters reset on a part change; P-001 looked specifically. Block 0136: the gotchas page will be the first thing the next three designers in the group receive, before they open the tool.]

![[S-0001#^s0001-0064]]
[[S-0001#^s0001-0064|Open in transcript · S-0001 @ 00:25:55]]

**Rationale:** A customer-side shadow document is both the real manual and an inventory of hidden behaviours (including a previously unmentioned one, missing inductor DCR), and the vendor has no visibility of it.
