---
type: highlight
highlight_id: H-S0001-0033
aliases: [H-S0001-0033]
title: Trust does not generalise across results
project: 2026_demo-fluxbench
source: '[[S-0001]]'
block: s0001-0130
participant: P-001
quote: That's the thing I've noticed about trust with these tools, it doesn't generalise. The thermal matched, so I trust the thermal. The ripple didn't match, so I don't trust the ripple, and I'm also a bit suspicious of the efficiency number because I haven't checked it, and the start-up number I only half believe because I checked it on the scope once and it was close-ish. Each result earns its own trust separately. A tool that understood that would make it easy to check each result against hardware. Instead it presents everything with the same confidence, which is a confidence I don't share.
context: '[Q: Would the thermal result alone have kept you using it?] [CONTEXT: Block 0112: he wants a field to attach a measured value to each simulated one ("measured 290 millivolts, simulated 340"). Block 0134: trust has drifted up through familiarity with his checklist, "a weaker kind than trust by correlation"; the tool itself has not become more trustworthy.]'
tags: [insight/pain-point, sentiment/neutral, journey/validate, experience/advanced, correlation/trust-per-result]
review: accepted
created_by: ai
model: claude-fable-5-1
skill_version: 0.3.0
created: 2026-11-17
reviewed_by: P-000
reviewed: 2026-11-17
---

> [!info]- Context
> [Q: Would the thermal result alone have kept you using it?] [CONTEXT: Block 0112: he wants a field to attach a measured value to each simulated one ("measured 290 millivolts, simulated 340"). Block 0134: trust has drifted up through familiarity with his checklist, "a weaker kind than trust by correlation"; the tool itself has not become more trustworthy.]

![[S-0001#^s0001-0130]]
[[S-0001#^s0001-0130|Open in transcript · S-0001 @ 00:56:35]]

**Rationale:** Directly answers RQ1 with a model of trust that is per-result and bench-earned, and names the UI mismatch (uniform confidence) that a correlation-aware design could fix.
