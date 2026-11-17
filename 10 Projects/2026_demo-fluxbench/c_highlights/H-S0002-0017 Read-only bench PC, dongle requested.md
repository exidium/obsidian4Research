---
type: highlight
highlight_id: H-S0002-0017
aliases: [H-S0002-0017]
title: Read-only bench PC, dongle requested
project: 2026_demo-fluxbench
source: '[[S-0002]]'
block: s0002-0048
participant: P-002
quote: A customer in telecom infrastructure has a bench PC that's been in read-only mode for a month because nobody wants to carry the offline activation files through IT again. They run the real simulations on an office laptop and walk them to the bench on a USB stick. Several customers have asked me for a floating license on their own server, or a hardware dongle, which sounds old-fashioned but they'd take it. A dongle doesn't care about guest Wi-Fi. I've passed both requests on. The answer has been that the licensing platform is a company-wide system, not a tool decision. Which is true and doesn't help the engineer on the bench.
context: '[CONTEXT: Asked whether customers hit the same lockout as he does on site. In `^s0002-0046` he describes the offline activation chain (request file, portal, response file) failing four times in five, usually from a clock drift or a docking-station fingerprint change.]'
tags: [insight/pain-point, functionality/workaround, functionality/new-feature-request, journey/validate, market/communications, licensing/license-lockout, licensing/offline-activation]
review: accepted
created_by: ai
model: claude-fable-5-1
skill_version: 0.3.0
created: 2026-11-17
reviewed_by: P-000
reviewed: 2026-11-17
---

> [!info]- Context
> [CONTEXT: Asked whether customers hit the same lockout as he does on site. In `^s0002-0046` he describes the offline activation chain (request file, portal, response file) failing four times in five, usually from a clock drift or a docking-station fingerprint change.]

![[S-0002#^s0002-0048]]
[[S-0002#^s0002-0048|Open in transcript · S-0002 @ 00:16:45]]

**Rationale:** RQ2 evidence that licensing breaks the design at the bench step specifically, with two customer feature asks (floating license, dongle) and an internal blocker (licensing is company-wide) that any recommendation has to route around.
