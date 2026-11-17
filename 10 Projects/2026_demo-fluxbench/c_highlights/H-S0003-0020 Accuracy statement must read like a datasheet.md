---
type: highlight
highlight_id: H-S0003-0020
aliases: [H-S0003-0020]
title: Accuracy statement must read like a datasheet
project: 2026_demo-fluxbench
source: '[[S-0003]]'
block: s0003-0070
participant: P-003
quote: 'It needs to be a controlled document. Title, revision number, date, and the tool version range it applies to. Then per result type: efficiency, ripple, hotspot temperature, transient response, each with a typical deviation and a maximum deviation. Then the conditions: parts match the library, operation within the stated range, board within what the thermal model assumes. Then the basis: how many boards, which kits, what instruments. Exactly like a datasheet, typical and max with conditions. If it just says accurate, it is useless.'
context: '[CONTEXT: Asked what a vendor accuracy statement would need to contain to be acceptable. In ^s0003-0072 they add that quality would not want the raw data behind it, only a revisioned document someone at the vendor is accountable for; in ^s0003-0068 quality''s third question on every report is "a basis for believing the simulated values", currently answered with the participant''s own correlation history.]'
tags: [functionality/new-feature-request, insight/desire, sentiment/neutral, journey/validate, correlation/accuracy-statement-missing]
review: accepted
created_by: ai
model: claude-fable-5-1
skill_version: 0.3.0
created: 2026-11-17
reviewed_by: P-000
reviewed: 2026-11-17
---

> [!info]- Context
> [CONTEXT: Asked what a vendor accuracy statement would need to contain to be acceptable. In ^s0003-0072 they add that quality would not want the raw data behind it, only a revisioned document someone at the vendor is accountable for; in ^s0003-0068 quality's third question on every report is "a basis for believing the simulated values", currently answered with the participant's own correlation history.]

![[S-0003#^s0003-0070]]
[[S-0003#^s0003-0070|Open in transcript · S-0003 @ 00:24:53]]

**Rationale:** The specification of the accuracy statement (structure, per-result typ/max, conditions, basis) is directly actionable and sets the bar for what would count; extends H-S0003-0009 from "would accept" to "what exactly".
