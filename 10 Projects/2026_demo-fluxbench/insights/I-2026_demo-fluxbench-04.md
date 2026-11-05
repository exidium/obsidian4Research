---
type: insight
insight_id: I-2026_demo-fluxbench-04
project: 2026_demo-fluxbench
title: Eval kits and their simulation models drift apart, and the mismatch surfaces at the moment of decision
status: draft
confidence: medium
participants: [P-002, P-003]
highlights: ['[[H-S0002-0008]]', '[[H-S0002-0009]]', '[[H-S0003-0002]]']
tags: [theme/pain, topic/hardware-correlation, product/eval-kit]
published_to: ''
created: 2026-11-05
---

# Eval kits and their simulation models drift apart, and the mismatch surfaces at the moment of decision

## Insight
Kits get revised, models don't follow, and the difference shows up when a customer compares the two to decide whether to adopt the part. The FAE puts it at one in four kits. The validation engineer closed the gap only by hand-entering the kit's actual parts into the simulation.

## Evidence
![[H-S0002-0008]]
![[H-S0002-0009]]
![[H-S0003-0002]]

## Implications
- Tie each kit revision to a model revision and ship the kit's actual BOM as a loadable preset in the tool.
- Research: quantify the one-in-four claim against kit revision records.

## Open questions
- How do customers find out which kit revision they have?
