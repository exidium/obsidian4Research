---
type: persona
persona_id: PE-03
aliases: [PE-03]
name: Validation engineer who must prove every simulated number
status: draft
archetype: Validation engineer in a regulated industry for whom every simulation claim must become a documented, reproducible investigation
participant_type: external-customer
markets: [market/digital-healthcare]
participants: [P-003]
projects: [2026_demo-fluxbench]
evidence_highlights: 12
created: 2026-11-17
updated: 2026-11-17
insights: 6
---

# Validation engineer who must prove every simulated number

> Numbers out, not just pictures. Give me the data behind every plot and tell me what you assumed. (P-003)

## Who
Mid-career validation engineer, 6 to 10 years, in a large medical-device company under a quality system. Does not design with the tool; compares what it predicted with what the bench measured, and writes it up for reviewers who accept a vendor statement but not a gut feeling.

## Jobs to be done
- When simulation and bench disagree, I want the numbers and assumptions behind every plot, so I can find the cause and close the investigation.
- When quality reviews my report, I want a vendor accuracy statement per result type, so simulated figures are admissible without my personal correlation.
- When I reopen a project months later, I want the same result under the same model version, so an auditor can reproduce it.

## Behaviours
- Opens a numbered investigation for each discrepancy and keeps acceptance limits per result type.
- Retypes plot cursors into spreadsheets because exports carry pictures, not numbers; loses about a day per report to it.
- Forks project files with dates and initials because the tool has no versioning; archives installers.
- Works on offline bench PCs; moves files by USB stick.

## Pain points
- Loss shown as one number, so a mismatch cannot be diagnosed.
- Temperature sweeps that crash one time in three, with nowhere to report it.
- Model updates that shift old results on reopen, which breaks reproducibility for auditors.
- Eval kits and their simulation models drifting apart (a capacitor revision explained a ripple gap).

## What earns their trust
A vendor accuracy statement (controlled document, version range, typical and maximum error per result type, conditions), a CSV with assumptions in its header, and a change log with a diff between versions.

## How to research with them
Ask to walk through one investigation from first discrepancy to signed report. They are precise and slightly weary; give them time and they will show you the spreadsheet.

## Where they appear
<!-- appearances:start -->
**Participants:** [[20 Participants/P-003|P-003]]
**Projects:** [[10 Projects/2026_demo-fluxbench/01 project|2026_demo-fluxbench]]
**Sources:** [[S-0003]] (P-003, 2026-10-16)

**Insights (6)**
- [[I-2026_demo-fluxbench-01 Engineers trust a simulated result only after it has matched the|I-2026_demo-fluxbench-01]] Engineers trust a simulated result only after it has matched the bench, and the tool gives them no other basis · 2 of their highlights · emerging
- [[I-2026_demo-fluxbench-02 Silent parameter changes, not model error, are what make results look|I-2026_demo-fluxbench-02]] Silent parameter changes, not model error, are what make results look wrong and drive support load · 1 of their highlights · emerging
- [[I-2026_demo-fluxbench-03 Designs can't leave the machine they were made on, so review|I-2026_demo-fluxbench-03]] Designs can't leave the machine they were made on, so review, support, and hand-back all run on screenshots and PDFs · 2 of their highlights · emerging
- [[I-2026_demo-fluxbench-04 Eval kits and their simulation models drift apart, and the mismatch|I-2026_demo-fluxbench-04]] Eval kits and their simulation models drift apart, and the mismatch surfaces at the moment of decision · 1 of their highlights · emerging
- [[I-2026_demo-fluxbench-06 Exports serve presentation, not analysis pictures come out, the|I-2026_demo-fluxbench-06]] Exports serve presentation, not analysis: pictures come out, the numbers behind them don't · 3 of their highlights · emerging
- [[I-2026_demo-fluxbench-07 Long simulations block the interface or crash, and users adapt by|I-2026_demo-fluxbench-07]] Long simulations block the interface or crash, and users adapt by saving first and waiting · 1 of their highlights · emerging

**Highlights (12)**
- [[H-S0003-0001 Every discrepancy becomes a documented investigation|H-S0003-0001]] Every discrepancy becomes a documented investigation · sentiment/neutral, journey/validate, market/digital-healthcare, correlation/sim-vs-bench-gap, workflow/workflow-described
- [[H-S0003-0002 Kit capacitor revision explained the ripple gap|H-S0003-0002]] Kit capacitor revision explained the ripple gap · functionality/workaround, sentiment/neutral, journey/validate, correlation/kit-model-drift, correlation/sim-vs-bench-gap
- [[H-S0003-0003 Loss shown as one number blocks diagnosis|H-S0003-0003]] Loss shown as one number blocks diagnosis · insight/pain-point, functionality/new-feature-request, sentiment/negative, journey/validate, correlation/loss-breakdown-missing
- [[H-S0003-0004 Plots export, the numbers don't|H-S0003-0004]] Plots export, the numbers don't · insight/pain-point, functionality/new-feature-request, sentiment/negative, journey/integrate, export/plot-data-not-exportable
- [[H-S0003-0005 A day of retyping per report|H-S0003-0005]] A day of retyping per report · insight/pain-point, sentiment/negative, journey/integrate, export/report-retyping
- [[H-S0003-0006 Temperature sweeps crash one in three|H-S0003-0006]] Temperature sweeps crash one in three · functionality/bug, insight/pain-point, sentiment/negative, journey/validate, tools/simulation-crash
- [[H-S0003-0007 No place to report a crash|H-S0003-0007]] No place to report a crash · insight/pain-point, sentiment/negative, journey/support, ops/follow-up-depth, docs/no-defect-channel
- [[H-S0003-0008 Trust earned project by project|H-S0003-0008]] Trust earned project by project · insight/pain-point, sentiment/neutral, journey/validate, correlation/accuracy-statement-missing
- [[H-S0003-0009 Quality accepts a vendor statement, not a gut|H-S0003-0009]] Quality accepts a vendor statement, not a gut · insight/desire, functionality/new-feature-request, sentiment/neutral, journey/validate, market/digital-healthcare, correlation/accuracy-statement-missing
- [[H-S0003-0010 Project forks named with dates and initials|H-S0003-0010]] Project forks named with dates and initials · functionality/workaround, insight/pain-point, sentiment/negative, journey/integrate, sharing/design-fork
- [[H-S0003-0011 Thermal model is less board-specific than assumed|H-S0003-0011]] Thermal model is less board-specific than assumed · sentiment/confused, insight/pain-point, journey/design, tools/hidden-defaults
- [[H-S0003-0012 CSV with assumptions in the header|H-S0003-0012]] CSV with assumptions in the header · functionality/new-feature-request, insight/desire, sentiment/neutral, journey/integrate, export/plot-data-not-exportable
<!-- appearances:end -->
