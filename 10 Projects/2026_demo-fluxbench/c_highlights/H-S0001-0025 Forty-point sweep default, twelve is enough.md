---
type: highlight
highlight_id: H-S0001-0025
aliases: [H-S0001-0025]
title: Forty-point sweep default, twelve is enough
project: 2026_demo-fluxbench
source: '[[S-0001]]'
block: s0001-0088
participant: P-001
quote: I only found that number because I went digging in the advanced panel for the frequency thing and saw a field called sweep resolution. Forty. Nobody needs forty points on an efficiency curve, you need maybe ten. I set it to twelve and the sweep came down to about three and a half minutes. Still locks the UI, but three minutes is a coffee, eleven minutes is a meeting. So there's a workaround, and it's another sticky note. It's also another default that cost me time before I knew it existed. Same pattern as the frequency. The tool had a sensible knob, hidden, set to a value that hurts.
context: '[CONTEXT: Block 0090: twelve points gave peak efficiency within a tenth of a percent and the same curve shape; the forty-point curve had a light-load wobble he thinks was numerical. The first run was killed at nine minutes, so the first attempt actually cost about twenty minutes.]'
tags: [functionality/workaround, insight/pain-point, sentiment/negative, journey/design, tools/hidden-defaults, tools/no-progress-feedback]
review: accepted
created_by: ai
model: claude-fable-5-1
skill_version: 0.3.0
created: 2026-11-17
reviewed_by: P-000
reviewed: 2026-11-17
---

> [!info]- Context
> [CONTEXT: Block 0090: twelve points gave peak efficiency within a tenth of a percent and the same curve shape; the forty-point curve had a light-load wobble he thinks was numerical. The first run was killed at nine minutes, so the first attempt actually cost about twenty minutes.]

![[S-0001#^s0001-0088]]
[[S-0001#^s0001-0088|Open in transcript · S-0001 @ 00:36:44]]

**Rationale:** A second hidden default with a measured cost (eleven minutes to three and a half) and no accuracy penalty, which makes the eleven-minute sweep a default-setting problem before it is a performance problem.
