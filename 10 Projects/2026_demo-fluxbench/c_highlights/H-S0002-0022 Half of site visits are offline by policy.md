---
type: highlight
highlight_id: H-S0002-0022
aliases: [H-S0002-0022]
title: Half of site visits are offline by policy
project: 2026_demo-fluxbench
source: '[[S-0002]]'
block: s0002-0068
participant: P-002
quote: Of the forty accounts, I'd say twelve have labs where my laptop can't get out at all. Three of those are defense-adjacent, and there I'm not even allowed to bring the laptop into the room, so I work from a printout. Another ten or so have guest Wi-Fi that works but blocks the specific port the license check uses, so the tool thinks it's offline anyway. The remaining ones are fine. So roughly half my customer visits happen under conditions the tool wasn't designed for. And it's the restricted sites that have the most serious projects. The customer who air-gaps their lab is the customer who is going to ship ten thousand units.
context: '[CONTEXT: In `^s0002-0070` he describes the defense-adjacent loop: design built at the office, printed, discussed on paper, re-run in the hotel; a five-minute iteration takes a day. In `^s0002-0074` he says the check-in interval (about forty-eight hours, three failures to read-only) is undocumented and unwarned.]'
tags: [insight/pain-point, sentiment/neutral, journey/support, market/aerospace-defence, licensing/offline-activation]
review: accepted
created_by: ai
model: claude-fable-5-1
skill_version: 0.3.0
created: 2026-11-17
reviewed_by: P-000
reviewed: 2026-11-17
---

> [!info]- Context
> [CONTEXT: In `^s0002-0070` he describes the defense-adjacent loop: design built at the office, printed, discussed on paper, re-run in the hotel; a five-minute iteration takes a day. In `^s0002-0074` he says the check-in interval (about forty-eight hours, three failures to read-only) is undocumented and unwarned.]

![[S-0002#^s0002-0068]]
[[S-0002#^s0002-0068|Open in transcript · S-0002 @ 00:26:20]]

**Rationale:** Sizes the licensing problem (half of visits) and inverts the usual priority argument: the accounts the tool serves worst are the highest-volume ones, which should change how the offline-grace ask is weighed against piracy concerns.
