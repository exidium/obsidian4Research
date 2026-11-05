---
type: insight
insight_id: I-2026_demo-fluxbench-06
project: 2026_demo-fluxbench
title: 'Exports serve presentation, not analysis: pictures come out, the numbers behind them don''t'
status: draft
confidence: medium
participants: [P-001, P-003]
highlights: ['[[H-S0001-0007]]', '[[H-S0003-0004]]', '[[H-S0003-0005]]', '[[H-S0003-0012]]']
tags: [theme/need, behavior/export, topic/collaboration]
published_to: ''
created: 2026-11-05
---

# Exports serve presentation, not analysis: pictures come out, the numbers behind them don't

## Insight
Plot exports and BOM CSVs exist, but the data behind plots doesn't export, loss figures aren't decomposed, and BOM parts ignore the customer's approved vendor list. The validation engineer spends most of a one-day report retyping numbers from pictures, and the designer spends half an hour per export swapping parts.

## Evidence
![[H-S0001-0007]]
![[H-S0003-0004]]
![[H-S0003-0005]]
![[H-S0003-0012]]

## Implications
- CSV export of plot data with assumptions in the header, as P-003 specified, is cheap and removes half a day per report.
- Preferred-parts lists at the BOM stage turn export rework into configuration.
- Research: P-002 was not asked about export; check whether FAEs hit the same wall.

## Open questions
- What does the downstream report template actually need? A field-level look at P-003's Word template would define the export.
