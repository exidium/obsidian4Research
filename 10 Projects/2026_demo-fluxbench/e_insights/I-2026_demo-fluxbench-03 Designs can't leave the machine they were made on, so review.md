---
type: insight
insight_id: I-2026_demo-fluxbench-03
aliases: [I-2026_demo-fluxbench-03]
title: 'Insight: Designs can''t leave the machine they were made on, so review, support, and hand-back all run on screenshots and PDFs'
project: 2026_demo-fluxbench
status: draft
evidence_level: emerging
participants: [P-001, P-002, P-003]
highlights: ['[[H-S0001-0008 Design review runs on PDF exports|H-S0001-0008]]', '[[H-S0001-0011 No design history in the project file|H-S0001-0011]]', '[[H-S0002-0001 Version lock forces screenshots|H-S0002-0001]]', '[[H-S0002-0002 Rebuilding designs from screenshots|H-S0002-0002]]', '[[H-S0002-0010 Designs should be shared like the silicon|H-S0002-0010]]', '[[H-S0003-0004 Plots export, the numbers don''t|H-S0003-0004]]', '[[H-S0003-0010 Project forks named with dates and initials|H-S0003-0010]]']
research_question: 2
tags: [functionality/workaround, journey/integrate, sharing/file-version-lock]
published_to: ''
created: 2026-11-06
reel: _raw/2026_demo-fluxbench/reels/I-2026_demo-fluxbench-03.mp4
reel_duration: 00:01:12
---

# Insight: Designs can't leave the machine they were made on, so review, support, and hand-back all run on screenshots and PDFs

![[_raw/2026_demo-fluxbench/reels/I-2026_demo-fluxbench-03.mp4]]

## Finding
Project files refuse to open across versions, there is no link or shared representation, and no history inside a project.

## Severity and impact
Every participant has built a workaround: PDF rounds for design review, rebuilding from screenshots in support, filenames with dates and initials in validation. The FAE spends twenty to thirty minutes per support case rebuilding what a file would show.

## What this means
Sharing friction, not simulation accuracy, is what makes the tool a single-user instrument. The FAE frames the design as something that should be shared between vendor and customer like the silicon itself.

## Evidence
![[H-S0001-0008 Design review runs on PDF exports]]
![[H-S0001-0011 No design history in the project file]]
![[H-S0002-0001 Version lock forces screenshots]]
![[H-S0002-0002 Rebuilding designs from screenshots]]
![[H-S0002-0010 Designs should be shared like the silicon]]
![[H-S0003-0004 Plots export, the numbers don't]]
![[H-S0003-0010 Project forks named with dates and initials]]

## Recommendations
- Prioritise a forward-compatible or link-based design representation; it removes the screenshot loop in support and the PDF loop in review at once.
- Add design history inside the project (what changed, when); a smaller change that addresses two participants' versioning pains.
- Research: observe a real design review to measure how many rounds actually happen.

## Open questions
- Who else sees a design in a typical customer team, and with what tools?
- Is a read-only web view enough, or do reviewers need to edit?
