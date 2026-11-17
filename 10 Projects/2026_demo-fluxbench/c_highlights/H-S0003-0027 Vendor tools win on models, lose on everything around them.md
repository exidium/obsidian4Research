---
type: highlight
highlight_id: H-S0003-0027
aliases: [H-S0003-0027]
title: Vendor tools win on models, lose on everything around them
project: 2026_demo-fluxbench
source: '[[S-0003]]'
block: s0003-0116
participant: P-003
quote: RailForge exports everything to CSV and has a scripting console. I never did a formal correlation there, so I cannot say its models are worse, but the engineers around me trusted them less. Tessaline is a web tool, so useless on an offline bench, but its report generation was impressive. One click and you get a PDF with every parameter the run used, defaults included. None of the three has an accuracy statement. The vendor specific tools win on models and lose on everything around the models. The general tools are the reverse.
context: '[CONTEXT: RailForge and Tessaline Power Studio are fictional competitor tools from the participant''s previous employer and a last-year evaluation. In ^s0003-0118 the wish list is RailForge''s scripting console and CSV export, Tessaline''s parameter page in the report, and FluxBench''s models; in ^s0003-0080 the bench instruments are already script-driven and the simulation "cannot be driven the same way".]'
tags: [sentiment/neutral, journey/evaluate, export/plot-data-not-exportable, correlation/accuracy-statement-missing, competition/competitor-comparison, export/scripting-interface-missing]
review: accepted
created_by: ai
model: claude-fable-5-1
skill_version: 0.3.0
created: 2026-11-17
reviewed_by: P-000
reviewed: 2026-11-17
---

> [!info]- Context
> [CONTEXT: RailForge and Tessaline Power Studio are fictional competitor tools from the participant's previous employer and a last-year evaluation. In ^s0003-0118 the wish list is RailForge's scripting console and CSV export, Tessaline's parameter page in the report, and FluxBench's models; in ^s0003-0080 the bench instruments are already script-driven and the simulation "cannot be driven the same way".]

![[S-0003#^s0003-0116]]
[[S-0003#^s0003-0116|Open in transcript · S-0003 @ 00:42:56]]

**Rationale:** The only competitor benchmark in the study: FluxBench's moat is the models, its deficits (CSV, scripting, parameter page) are already solved elsewhere, and no competitor offers an accuracy statement, which would be a differentiator (RQ1).
