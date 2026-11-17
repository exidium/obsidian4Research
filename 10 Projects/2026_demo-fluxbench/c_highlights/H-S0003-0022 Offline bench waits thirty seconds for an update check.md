---
type: highlight
highlight_id: H-S0003-0022
aliases: [H-S0003-0022]
title: Offline bench waits thirty seconds for an update check
project: 2026_demo-fluxbench
source: '[[S-0003]]'
block: s0003-0078
participant: P-003
quote: The bench PCs are on an isolated network, no internet. Software installs go through IT with a ticket, and updates happen quarterly if we are lucky. FluxBench runs on the bench PC and on my office laptop, and moving a project between them is a USB stick. Every time the tool starts on the bench it tries to check for updates, waits about thirty seconds, then gives up. Thirty seconds, several times a day, for a machine that will never see the internet. Small thing, but it sets the tone.
context: '[CONTEXT: Asked about lab constraints. The offline bench recurs through the interview: FAE model updates arrive on a USB stick, the support portal and app notes are reachable only from the office laptop, and any crash reporter "has to work offline".]'
tags: [insight/pain-point, sentiment/negative, journey/validate, licensing/offline-activation]
review: accepted
created_by: ai
model: claude-fable-5-1
skill_version: 0.3.0
created: 2026-11-17
reviewed_by: P-000
reviewed: 2026-11-17
---

> [!info]- Context
> [CONTEXT: Asked about lab constraints. The offline bench recurs through the interview: FAE model updates arrive on a USB stick, the support portal and app notes are reachable only from the office laptop, and any crash reporter "has to work offline".]

![[S-0003#^s0003-0078]]
[[S-0003#^s0003-0078|Open in transcript · S-0003 @ 00:28:24]]

**Rationale:** The lab environment (air-gapped bench, quarterly IT-ticketed updates, USB transfer) is a constraint every later recommendation must satisfy; the update check is a network check-in the user cannot complete, the closest fit to the offline-activation tag (RQ2).
