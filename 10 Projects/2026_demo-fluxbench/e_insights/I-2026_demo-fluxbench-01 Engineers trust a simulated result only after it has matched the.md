---
type: insight
insight_id: I-2026_demo-fluxbench-01
aliases: [I-2026_demo-fluxbench-01]
title: 'Insight: Engineers trust a simulated result only after it has matched the bench, and the tool gives them no other basis'
project: 2026_demo-fluxbench
status: draft
evidence_level: emerging
participants: [P-001, P-002, P-003]
highlights: ['[[H-S0001-0003 Spreadsheet wins when tool and spreadsheet disagree|H-S0001-0003]]', '[[H-S0001-0009 Thermal estimate matched the first prototype|H-S0001-0009]]', '[[H-S0001-0010 Trust is correlation|H-S0001-0010]]', '[[H-S0002-0009 Small discrepancies lose the careful engineers|H-S0002-0009]]', '[[H-S0003-0008 Trust earned project by project|H-S0003-0008]]', '[[H-S0003-0009 Quality accepts a vendor statement, not a gut|H-S0003-0009]]']
research_question: 1
tags: [insight/pain-point, journey/validate, correlation/accuracy-statement-missing]
published_to: ''
created: 2026-11-06
reel: _raw/2026_demo-fluxbench/reels/I-2026_demo-fluxbench-01.mp4
reel_duration: 00:01:03
---

# Insight: Engineers trust a simulated result only after it has matched the bench, and the tool gives them no other basis

![[_raw/2026_demo-fluxbench/reels/I-2026_demo-fluxbench-01.mp4]]

## Finding
Trust is granted per result, not per tool. A number is believed once it has been correlated with a measurement and doubted until then.

## Severity and impact
All three participants, unprompted, described the same mechanism. For the validation engineer it is a process requirement, not a preference: quality teams accept a vendor statement and reject personal correlation.

## What this means
Because the tool states no accuracy envelope, every user repeats the correlation privately, and in regulated teams the private result isn't even admissible. The thermal estimate is already trusted because it correlated once; that is the pattern to reproduce.

## Evidence
![[H-S0001-0003 Spreadsheet wins when tool and spreadsheet disagree]]
![[H-S0001-0009 Thermal estimate matched the first prototype]]
![[H-S0001-0010 Trust is correlation]]
![[H-S0002-0009 Small discrepancies lose the careful engineers]]
![[H-S0003-0008 Trust earned project by project]]
![[H-S0003-0009 Quality accepts a vendor statement, not a gut]]

## Recommendations
- Publish a per-result accuracy statement (typical deviation from measurement when parts match) and show it on the result.
- Lead onboarding with the thermal estimate, the result users already find correlates, to seed trust early.
- Research: we have not tested whether an accuracy statement changes behaviour, only that users say it would.

## Open questions
- Which results do users correlate first, and does the order matter for adoption?
- How do teams without a bench decide what to believe?
