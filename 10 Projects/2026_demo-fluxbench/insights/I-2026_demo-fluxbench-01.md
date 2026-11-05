---
type: insight
insight_id: I-2026_demo-fluxbench-01
project: 2026_demo-fluxbench
title: Engineers trust a simulated result only after it has matched the bench, and the tool gives them no other basis
status: draft
confidence: high
participants: [P-001, P-002, P-003]
highlights: ['[[H-S0001-0003]]', '[[H-S0001-0009]]', '[[H-S0001-0010]]', '[[H-S0002-0009]]', '[[H-S0003-0008]]', '[[H-S0003-0009]]']
tags: [theme/trust, topic/hardware-correlation, topic/accuracy]
published_to: ''
created: 2026-11-05
---

# Engineers trust a simulated result only after it has matched the bench, and the tool gives them no other basis

## Insight
Trust is granted per result, not per tool. Each participant described the same mechanism: a number is believed once it has been correlated with a measurement, and doubted until then. Because the tool states no accuracy envelope, every user repeats that correlation privately, and in regulated teams the private result isn't even admissible.

## Evidence
![[H-S0001-0003]]
![[H-S0001-0009]]
![[H-S0001-0010]]
![[H-S0002-0009]]
![[H-S0003-0008]]
![[H-S0003-0009]]

## Implications
- Publish a per-result accuracy statement (typical deviation from measurement when parts match). P-003 would cite it in validation reports instead of re-deriving it.
- Lead onboarding with the thermal estimate, the result users already find correlates, to seed trust early.
- Research: we haven't tested whether an accuracy statement would actually change behavior, only that users say it would.

## Open questions
- Which results do users correlate first, and does the order matter for adoption?
- How do teams without a bench (early concept phase) decide what to believe?
