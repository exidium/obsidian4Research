---
type: insight
insight_id: I-2026_demo-fluxbench-06
aliases: [I-2026_demo-fluxbench-06]
title: 'Insight: Exports serve presentation, not analysis: pictures come out, the numbers behind them don''t'
project: 2026_demo-fluxbench
status: draft
evidence_level: emerging
participants: [P-001, P-003]
highlights: ['[[H-S0001-0007 BOM export ignores the approved vendor list|H-S0001-0007]]', '[[H-S0003-0004 Plots export, the numbers don''t|H-S0003-0004]]', '[[H-S0003-0005 A day of retyping per report|H-S0003-0005]]', '[[H-S0003-0012 CSV with assumptions in the header|H-S0003-0012]]']
research_question: 2
tags: [functionality/new-feature-request, journey/integrate, export/plot-data-not-exportable]
published_to: ''
created: 2026-11-06
reel: _raw/2026_demo-fluxbench/reels/I-2026_demo-fluxbench-06.mp4
reel_duration: 00:00:44
---

# Insight: Exports serve presentation, not analysis: pictures come out, the numbers behind them don't

![[_raw/2026_demo-fluxbench/reels/I-2026_demo-fluxbench-06.mp4]]

## Finding
Plot exports and BOM CSVs exist, but the data behind plots doesn't export, loss figures aren't decomposed, and BOM parts ignore the customer's approved vendor list.

## Severity and impact
Two participants. The validation engineer spends most of a one-day report retyping numbers from pictures; the designer spends half an hour per export swapping parts.

## What this means
The tool's outputs are shaped for looking at, not for the downstream work they feed. The specification came from the user: CSV with assumptions in the header.

## Evidence
![[H-S0001-0007 BOM export ignores the approved vendor list]]
![[H-S0003-0004 Plots export, the numbers don't]]
![[H-S0003-0005 A day of retyping per report]]
![[H-S0003-0012 CSV with assumptions in the header]]

## Recommendations
- Ship CSV export of plot data with assumptions in the header; cheap, and removes half a day per validation report.
- Add preferred-parts lists at the BOM stage so export rework becomes configuration.
- Research: the FAE was not asked about export; check whether FAEs hit the same wall.

## Open questions
- What does the downstream report template actually need? A field-level look at the validation template would define the export.
