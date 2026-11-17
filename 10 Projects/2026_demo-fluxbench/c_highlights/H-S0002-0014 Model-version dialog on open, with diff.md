---
type: highlight
highlight_id: H-S0002-0014
aliases: [H-S0002-0014]
title: Model-version dialog on open, with diff
project: 2026_demo-fluxbench
source: '[[S-0002]]'
block: s0002-0038
participant: P-002
quote: 'Store the model version of every part in the project file. When the file opens with newer models available, show a dialog: these four parts have updated models, here''s what changed in one line each, do you want to keep the old models or update. And let me diff: old result versus new result side by side. That dialog alone would turn a day of panic into a two-minute decision. I also think the old models should stay available. Right now updating is one-way. If a customer qualified a design with the spring model and their validation report references those numbers, they need to be able to reproduce them. That''s not nostalgia, that''s a compliance requirement in a few of my markets.'
context: '[CONTEXT: Answer to "what would you want the tool to do instead" after the case in proposal 1. In `^s0002-0130` he adds that application updates and model updates should be separable, with models updating only on the user''s yes.]'
tags: [functionality/new-feature-request, insight/desire, sentiment/neutral, journey/design, tools/model-version-drift, tools/design-history-missing, tools/result-reproducibility]
review: accepted
created_by: ai
model: claude-fable-5-1
skill_version: 0.3.0
created: 2026-11-17
reviewed_by: P-000
reviewed: 2026-11-17
---

> [!info]- Context
> [CONTEXT: Answer to "what would you want the tool to do instead" after the case in proposal 1. In `^s0002-0130` he adds that application updates and model updates should be separable, with models updating only on the user's yes.]

![[S-0002#^s0002-0038]]
[[S-0002#^s0002-0038|Open in transcript · S-0002 @ 00:12:05]]

**Rationale:** The most specific feature ask in the interview, with a measurable claim ("a day of panic into a two-minute decision") and a compliance argument for keeping old models that turns a convenience into a requirement.
