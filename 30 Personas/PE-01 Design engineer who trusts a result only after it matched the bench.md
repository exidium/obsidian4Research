---
type: persona
persona_id: PE-01
aliases: [PE-01]
name: Design engineer who trusts a result only after it matched the bench
status: draft
archetype: External hardware design engineer who adopts a vendor tool only where the models force it
participant_type: external-customer
markets: [market/industrial-automation]
participants: [P-001]
projects: [2026_demo-fluxbench]
evidence_highlights: 36
created: 2026-11-17
updated: 2026-11-17
insights: 6
---

# Design engineer who trusts a result only after it matched the bench

> Trust for me is correlation. Show me it matches hardware once and I'll use it. (P-001)

## Who
Senior hardware designer, ten or more years in the role, in a mid-sized industrial company. Owns a spreadsheet that has shipped boards for years. Opens a vendor simulation tool only when a part family's models exist nowhere else. Works on a lab network that blocks outbound traffic; reviews run on PDF exports.

## Jobs to be done
- When a new part family only has models in the vendor's tool, I want a trustworthy starting design fast, so I can keep my schedule without learning a tool I didn't choose.
- When the tool and my spreadsheet disagree, I want to see what the tool assumed, so I can decide which number to believe before boards are ordered.
- When I hand a design to review, I want reviewers to see the design and its history, so sign-off doesn't run on screenshots.

## Behaviours
- Runs the tool and the spreadsheet side by side; when they disagree, the spreadsheet wins.
- Checks the advanced panel before believing any number; keeps private notes of parameters set, because the project file keeps no history.
- Grants trust per result: the thermal estimate that matched the bench is trusted, the ripple figure that disagreed is not.
- Rebuilds designs for colleagues as screenshots and PDFs because files cannot leave the machine.

## Pain points
- Parameters that change silently when a part is swapped (switching frequency reset).
- Long simulations with no progress feedback, read as hangs and killed.
- Activation and licensing that assume an internet connection at the bench.
- Exports built for presentation: BOM ignores the approved-vendor list, plots come without their numbers.

## What earns their trust
One demonstrated correlation with hardware, a visible banner for every parameter the tool changes on their behalf, and a design history inside the project file.

## How to research with them
Ask for the last disagreement between the tool and their own reference, and what they did next. They answer in specifics; vague questions get polite generalities.

## Where they appear
<!-- appearances:start -->
**Participants:** [[20 Participants/P-001|P-001]]
**Projects:** [[10 Projects/2026_demo-fluxbench/01 project|2026_demo-fluxbench]]
**Sources:** [[S-0001]] (P-001, 2026-10-14)

**Insights (6)**
- [[I-2026_demo-fluxbench-01 Engineers trust a simulated result only after it has matched the|I-2026_demo-fluxbench-01]] Engineers trust a simulated result only after it has matched the bench, and the tool gives them no other basis · 3 of their highlights · emerging
- [[I-2026_demo-fluxbench-02 Silent parameter changes, not model error, are what make results look|I-2026_demo-fluxbench-02]] Silent parameter changes, not model error, are what make results look wrong and drive support load · 2 of their highlights · emerging
- [[I-2026_demo-fluxbench-03 Designs can't leave the machine they were made on, so review|I-2026_demo-fluxbench-03]] Designs can't leave the machine they were made on, so review, support, and hand-back all run on screenshots and PDFs · 2 of their highlights · emerging
- [[I-2026_demo-fluxbench-05 Licensing assumes a connected machine; labs and customer sites aren't|I-2026_demo-fluxbench-05]] Licensing assumes a connected machine; labs and customer sites aren't · 1 of their highlights · emerging
- [[I-2026_demo-fluxbench-06 Exports serve presentation, not analysis pictures come out, the|I-2026_demo-fluxbench-06]] Exports serve presentation, not analysis: pictures come out, the numbers behind them don't · 1 of their highlights · emerging
- [[I-2026_demo-fluxbench-07 Long simulations block the interface or crash, and users adapt by|I-2026_demo-fluxbench-07]] Long simulations block the interface or crash, and users adapt by saving first and waiting · 1 of their highlights · emerging

**Highlights (36)**
- [[H-S0001-0001 Activation blocked on the lab network|H-S0001-0001]] Activation blocked on the lab network · insight/pain-point, sentiment/negative, journey/discover, software/fluxbench-designer, licensing/offline-activation
- [[H-S0001-0002 Stock-aware part picker beats the spreadsheet|H-S0001-0002]] Stock-aware part picker beats the spreadsheet · functionality/existing-feature, sentiment/positive, journey/design, software/fluxbench-designer, selection/part-finder-stock
- [[H-S0001-0003 Spreadsheet wins when tool and spreadsheet disagree|H-S0001-0003]] Spreadsheet wins when tool and spreadsheet disagree · insight/pain-point, functionality/workaround, sentiment/negative, journey/design, correlation/sim-vs-bench-gap
- [[H-S0001-0004 Part change silently reset switching frequency|H-S0001-0004]] Part change silently reset switching frequency · insight/pain-point, functionality/bug, sentiment/negative, journey/design, tools/silent-parameter-reset, tools/hidden-defaults
- [[H-S0001-0005 Lost trust because the tool didn't say what it changed|H-S0001-0005]] Lost trust because the tool didn't say what it changed · insight/pain-point, sentiment/negative, journey/design, tools/silent-parameter-reset
- [[H-S0001-0006 Eleven-minute sweep looked like a hang|H-S0001-0006]] Eleven-minute sweep looked like a hang · insight/pain-point, sentiment/negative, journey/design, tools/no-progress-feedback
- [[H-S0001-0007 BOM export ignores the approved vendor list|H-S0001-0007]] BOM export ignores the approved vendor list · insight/pain-point, functionality/new-feature-request, sentiment/negative, journey/integrate, export/approved-parts-mismatch
- [[H-S0001-0008 Design review runs on PDF exports|H-S0001-0008]] Design review runs on PDF exports · functionality/workaround, sentiment/neutral, journey/integrate, sharing/pdf-review-loop, workflow/review-loop-described
- [[H-S0001-0009 Thermal estimate matched the first prototype|H-S0001-0009]] Thermal estimate matched the first prototype · functionality/existing-feature, sentiment/positive, journey/validate, correlation/thermal-correlated
- [[H-S0001-0010 Trust is correlation|H-S0001-0010]] Trust is correlation · sentiment/neutral, journey/validate, experience/advanced, correlation/sim-vs-bench-gap
- [[H-S0001-0011 No design history in the project file|H-S0001-0011]] No design history in the project file · insight/pain-point, sentiment/negative, journey/design, tools/design-history-missing
- [[H-S0001-0012 Reviewer wants both numbers side by side|H-S0001-0012]] Reviewer wants both numbers side by side · insight/pain-point, sentiment/negative, journey/integrate, workflow/review-loop-described, correlation/sim-vs-bench-gap
- [[H-S0001-0013 Sign-off is on the document, not the design|H-S0001-0013]] Sign-off is on the document, not the design · insight/pain-point, sentiment/neutral, journey/integrate, sharing/pdf-review-loop, workflow/review-loop-described, sharing/reviewer-viewer-missing
- [[H-S0001-0014 Revision stamp and a read-only reviewer view|H-S0001-0014]] Revision stamp and a read-only reviewer view · functionality/new-feature-request, insight/desire, sentiment/neutral, journey/integrate, sharing/pdf-review-loop, export/revision-stamp-missing, sharing/reviewer-viewer-missing
- [[H-S0001-0015 Schematic retyped into CAD by hand|H-S0001-0015]] Schematic retyped into CAD by hand · insight/pain-point, functionality/workaround, sentiment/negative, journey/integrate, export/handoff-as-picture
- [[H-S0001-0016 Thermal within three degrees, the only agreeing table|H-S0001-0016]] Thermal within three degrees, the only agreeing table · functionality/existing-feature, sentiment/positive, journey/validate, correlation/thermal-correlated
- [[H-S0001-0017 Everything leaves the tool as a picture|H-S0001-0017]] Everything leaves the tool as a picture · insight/pain-point, functionality/new-feature-request, sentiment/negative, journey/integrate, export/handoff-as-picture
- [[H-S0001-0018 One-page results table built by hand|H-S0001-0018]] One-page results table built by hand · functionality/new-feature-request, insight/pain-point, sentiment/negative, journey/integrate, export/report-retyping
- [[H-S0001-0019 Six people watched the sweep hang|H-S0001-0019]] Six people watched the sweep hang · insight/pain-point, sentiment/negative, journey/integrate, tools/no-progress-feedback, sharing/pdf-review-loop
- [[H-S0001-0020 Internal gotchas wiki beats vendor docs|H-S0001-0020]] Internal gotchas wiki beats vendor docs · functionality/workaround, insight/pain-point, sentiment/negative, journey/support, docs/shadow-docs, docs/feature-vs-symptom-docs
- [[H-S0001-0021 Vendor forum known for two years, by design|H-S0001-0021]] Vendor forum: known for two years, by design · insight/pain-point, sentiment/negative, journey/support, tools/silent-parameter-reset
- [[H-S0001-0022 Offline activation is enterprise-only|H-S0001-0022]] Offline activation is enterprise-only · insight/pain-point, sentiment/negative, journey/support, licensing/offline-activation
- [[H-S0001-0023 Never reported the feedback channel is a nod|H-S0001-0023]] Never reported: the feedback channel is a nod · insight/pain-point, sentiment/negative, journey/support, docs/no-defect-channel
- [[H-S0001-0024 Competitor shows a keep-or-reset dialogue|H-S0001-0024]] Competitor shows a keep-or-reset dialogue · insight/desire, sentiment/neutral, journey/evaluate, tools/silent-parameter-reset, competition/competitor-comparison
- [[H-S0001-0025 Forty-point sweep default, twelve is enough|H-S0001-0025]] Forty-point sweep default, twelve is enough · functionality/workaround, insight/pain-point, sentiment/negative, journey/design, tools/hidden-defaults, tools/no-progress-feedback
- [[H-S0001-0026 Node lock keeps the tool off the lab bench|H-S0001-0026]] Node lock keeps the tool off the lab bench · insight/pain-point, sentiment/negative, journey/validate, licensing/offline-activation, licensing/node-locked-seat
- [[H-S0001-0027 Home-made lookup table covers seventy percent of the BOM|H-S0001-0027]] Home-made lookup table covers seventy percent of the BOM · functionality/workaround, functionality/new-feature-request, insight/pain-point, sentiment/neutral, journey/integrate, export/approved-parts-mismatch
- [[H-S0001-0028 Raw plot data to overlay with the scope|H-S0001-0028]] Raw plot data to overlay with the scope · functionality/new-feature-request, insight/desire, sentiment/neutral, journey/validate, export/plot-data-not-exportable, correlation/sim-vs-bench-gap
- [[H-S0001-0029 Trust fixes would double the seats|H-S0001-0029]] Trust fixes would double the seats · insight/desire, sentiment/neutral, journey/evaluate, tools/silent-parameter-reset, sharing/reviewer-viewer-missing, export/revision-stamp-missing
- [[H-S0001-0030 Lost hours are invisible to the manager|H-S0001-0030]] Lost hours are invisible to the manager · insight/pain-point, sentiment/negative, journey/evaluate, ops/follow-up-depth
- [[H-S0001-0031 Top five wishes, what-changed panel first|H-S0001-0031]] Top five wishes, what-changed panel first · functionality/new-feature-request, insight/desire, sentiment/neutral, journey/design, tools/silent-parameter-reset, export/approved-parts-mismatch, export/plot-data-not-exportable, tools/design-history-missing, tools/no-progress-feedback, licensing/offline-activation, export/revision-stamp-missing, sharing/reviewer-viewer-missing
- [[H-S0001-0032 One missing banner broke trust|H-S0001-0032]] One missing banner broke trust · insight/pain-point, functionality/new-feature-request, sentiment/negative, journey/design, tools/silent-parameter-reset
- [[H-S0001-0033 Trust does not generalise across results|H-S0001-0033]] Trust does not generalise across results · insight/pain-point, sentiment/neutral, journey/validate, experience/advanced, correlation/trust-per-result
- [[H-S0001-0034 Defensive use with a seven-item checklist|H-S0001-0034]] Defensive use with a seven-item checklist · functionality/workaround, sentiment/neutral, journey/design, tools/hidden-defaults, workflow/workflow-described
- [[H-S0001-0035 Spreadsheet trusted by habit, not rigour|H-S0001-0035]] Spreadsheet trusted by habit, not rigour · sentiment/neutral, journey/validate, experience/advanced, tools/hidden-defaults
- [[H-S0001-0036 Tool ignores derating rules|H-S0001-0036]] Tool ignores derating rules · functionality/new-feature-request, insight/pain-point, sentiment/negative, journey/design
<!-- appearances:end -->
