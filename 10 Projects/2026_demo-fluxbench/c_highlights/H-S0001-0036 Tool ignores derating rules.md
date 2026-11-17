---
type: highlight
highlight_id: H-S0001-0036
aliases: [H-S0001-0036]
title: Tool ignores derating rules
project: 2026_demo-fluxbench
source: '[[S-0001]]'
block: s0001-0144
participant: P-001
quote: Two, the tool doesn't know about derating. Our internal rules say a capacitor runs at no more than eighty percent of rated voltage, and the tool happily suggests a 16 volt cap on a 12 volt rail, which is seventy five percent, fine, but on the 48 volt side it suggested a 50 volt part. That fails our rule and I only caught it because I've been bitten before. A derating setting would be another thing on the wish list.
context: '[Q: Anything we haven''t covered?] [CONTEXT: The same block also notes the project file is a single binary blob that cannot be diffed or kept usefully in git, a pattern already covered by `tools/design-history-missing` (H-S0001-0011).]'
tags: [functionality/new-feature-request, insight/pain-point, sentiment/negative, journey/design]
review: accepted
created_by: ai
model: claude-fable-5-1
skill_version: 0.3.0
created: 2026-11-17
reviewed_by: P-000
reviewed: 2026-11-17
---

> [!info]- Context
> [Q: Anything we haven't covered?] [CONTEXT: The same block also notes the project file is a single binary blob that cannot be diffed or kept usefully in git, a pattern already covered by `tools/design-history-missing` (H-S0001-0011).]

![[S-0001#^s0001-0144]]
[[S-0001#^s0001-0144|Open in transcript · S-0001 @ 01:03:05]]

**Rationale:** A new class of "wrong" suggestion, a component that violates a customer design rule, caught only by experience; it was not in the earlier highlights or in the FAE causes list and could change the part-suggestion recommendation.
