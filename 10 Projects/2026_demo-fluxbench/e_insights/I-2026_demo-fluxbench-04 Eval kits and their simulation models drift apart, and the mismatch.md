---
type: insight
insight_id: I-2026_demo-fluxbench-04
aliases: [I-2026_demo-fluxbench-04]
title: 'Insight: Eval kits and their simulation models drift apart, and the mismatch surfaces at the moment of decision'
project: 2026_demo-fluxbench
status: draft
evidence_level: emerging
participants: [P-002, P-003]
highlights: ['[[H-S0002-0008 Eval kit revised, model not|H-S0002-0008]]', '[[H-S0002-0009 Small discrepancies lose the careful engineers|H-S0002-0009]]', '[[H-S0003-0002 Kit capacitor revision explained the ripple gap|H-S0003-0002]]']
research_question: 1
tags: [insight/pain-point, journey/evaluate, correlation/kit-model-drift]
published_to: ''
created: 2026-11-06
reel: _raw/2026_demo-fluxbench/reels/I-2026_demo-fluxbench-04.mp4
reel_duration: 00:00:40
---

# Insight: Eval kits and their simulation models drift apart, and the mismatch surfaces at the moment of decision

![[_raw/2026_demo-fluxbench/reels/I-2026_demo-fluxbench-04.mp4]]

## Finding
Kits get revised, models don't follow, and the difference shows up when a customer compares the two to decide whether to adopt the part.

## Severity and impact
Two participants, from both sides of the sale. The FAE puts it at one in four kits; the validation engineer closed the gap only by hand-entering the kit's actual parts.

## What this means
The simulate, buy the kit, measure flow is the vendor's strongest conversion path, and this is where it breaks for exactly the careful engineers the vendor wants.

## Evidence
![[H-S0002-0008 Eval kit revised, model not]]
![[H-S0002-0009 Small discrepancies lose the careful engineers]]
![[H-S0003-0002 Kit capacitor revision explained the ripple gap]]

## Recommendations
- Tie each kit revision to a model revision and ship the kit's actual BOM as a loadable preset in the tool.
- Research: quantify the one-in-four claim against kit revision records.

## Open questions
- How do customers find out which kit revision they have?
