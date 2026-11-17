---
type: persona
persona_id: PE-02
aliases: [PE-02]
name: Field engineer who patches the tool's gaps for forty accounts
status: draft
archetype: Internal field applications engineer who absorbs the tool's gaps as support load and shadow documentation
participant_type: internal-engineer
markets: [market/broad-market]
participants: [P-002]
projects: [2026_demo-fluxbench]
evidence_highlights: 37
created: 2026-11-17
updated: 2026-11-17
insights: 5
---

# Field engineer who patches the tool's gaps for forty accounts

> Tell the user when you changed something they didn't ask for. That one change would cut my tool questions in half. (P-002)

## Who
Staff-level FAE with 10+ years, supporting around forty accounts across drives, lighting and medical. Sees the same tool failure many times a month, from many customers, and has built their own fixes: a one-page "Before You Trust The Number" checklist, a second laptop for licensing, a VM per project for customers under compliance.

## Jobs to be done
- When a customer says the tool is wrong, I want to see what the tool changed and which model version they used, so I can close the case in minutes instead of rebuilding the design.
- When I'm on a customer site with no network, I want the tool to keep working, so I never lose credibility in front of a customer.
- When a model or an eval kit is revised, I want customers told at the moment it matters, so repeat cases stop before they reach me.

## Behaviours
- Translates between customer language ("your tool lied to me") and engineering causes (a silently reset parameter).
- Distributes shadow documentation and runs short training sessions; measures success in cases per month.
- Knows every licensing workaround and when each is acceptable.
- Reports upstream through tickets and two developers they message directly; expects weeks for an answer.

## Pain points
- Silent parameter resets are the top support cause, and the vendor's own forum calls them "by design".
- Model updates that change old results on reopen, with no version stamp in the project file.
- Documentation organised by feature when customers arrive with a symptom.
- No shared, versioned way to pass a design between a customer and the FAE; everything is screenshots.

## What earns their trust
A change log in the tool, model versions stamped into project files, and a reporting channel with a ticket number they can give a customer.

## How to research with them
They talk in cases and numbers. Ask for the last five tickets, not for opinions; ask what they would cut from the tool, not only what they would add. Internal participant: quotes as text only, no voice or video in anything shared.

## Where they appear
<!-- appearances:start -->
**Participants:** [[20 Participants/P-002|P-002]]
**Projects:** [[10 Projects/2026_demo-fluxbench/01 project|2026_demo-fluxbench]]
**Sources:** [[S-0002]] (P-002, 2026-10-15)

**Insights (5)**
- [[I-2026_demo-fluxbench-01 Engineers trust a simulated result only after it has matched the|I-2026_demo-fluxbench-01]] Engineers trust a simulated result only after it has matched the bench, and the tool gives them no other basis · 1 of their highlights · emerging
- [[I-2026_demo-fluxbench-02 Silent parameter changes, not model error, are what make results look|I-2026_demo-fluxbench-02]] Silent parameter changes, not model error, are what make results look wrong and drive support load · 4 of their highlights · emerging
- [[I-2026_demo-fluxbench-03 Designs can't leave the machine they were made on, so review|I-2026_demo-fluxbench-03]] Designs can't leave the machine they were made on, so review, support, and hand-back all run on screenshots and PDFs · 3 of their highlights · emerging
- [[I-2026_demo-fluxbench-04 Eval kits and their simulation models drift apart, and the mismatch|I-2026_demo-fluxbench-04]] Eval kits and their simulation models drift apart, and the mismatch surfaces at the moment of decision · 2 of their highlights · emerging
- [[I-2026_demo-fluxbench-05 Licensing assumes a connected machine; labs and customer sites aren't|I-2026_demo-fluxbench-05]] Licensing assumes a connected machine; labs and customer sites aren't · 2 of their highlights · emerging

**Highlights (37)**
- [[H-S0002-0001 Version lock forces screenshots|H-S0002-0001]] Version lock forces screenshots · insight/pain-point, sentiment/negative, journey/support, sharing/file-version-lock, sharing/screenshot-support
- [[H-S0002-0002 Rebuilding designs from screenshots|H-S0002-0002]] Rebuilding designs from screenshots · functionality/workaround, insight/pain-point, sentiment/negative, journey/support, sharing/screenshot-support, tools/hidden-defaults
- [[H-S0002-0003 Second laptop as a licensing workaround|H-S0002-0003]] Second laptop as a licensing workaround · functionality/workaround, insight/pain-point, sentiment/negative, journey/support, licensing/license-lockout
- [[H-S0002-0004 Thirty days of offline grace|H-S0002-0004]] Thirty days of offline grace · functionality/new-feature-request, insight/desire, sentiment/neutral, journey/support, licensing/offline-activation
- [[H-S0002-0005 Silent reset is the top support cause|H-S0002-0005]] Silent reset is the top support cause · insight/pain-point, functionality/bug, sentiment/neutral, journey/support, tools/silent-parameter-reset
- [[H-S0002-0006 Shadow checklist of hidden defaults|H-S0002-0006]] Shadow checklist of hidden defaults · functionality/workaround, sentiment/neutral, journey/support, docs/shadow-docs, tools/hidden-defaults
- [[H-S0002-0007 Docs organised by feature, not symptom|H-S0002-0007]] Docs organised by feature, not symptom · insight/pain-point, sentiment/negative, journey/support, docs/feature-vs-symptom-docs
- [[H-S0002-0008 Eval kit revised, model not|H-S0002-0008]] Eval kit revised, model not · insight/pain-point, sentiment/negative, journey/evaluate, correlation/kit-model-drift
- [[H-S0002-0009 Small discrepancies lose the careful engineers|H-S0002-0009]] Small discrepancies lose the careful engineers · insight/pain-point, sentiment/negative, journey/evaluate, experience/advanced, correlation/kit-model-drift
- [[H-S0002-0010 Designs should be shared like the silicon|H-S0002-0010]] Designs should be shared like the silicon · insight/desire, functionality/new-feature-request, sentiment/neutral, journey/integrate, sharing/file-version-lock
- [[H-S0002-0011 Announce changes, halve support questions|H-S0002-0011]] Announce changes, halve support questions · functionality/new-feature-request, sentiment/neutral, journey/support, tools/silent-parameter-reset
- [[H-S0002-0012 Model updates change old results on reopen|H-S0002-0012]] Model updates change old results on reopen · insight/pain-point, sentiment/negative, journey/design, tools/model-version-drift
- [[H-S0002-0013 Model got more honest, customer blamed the part|H-S0002-0013]] Model got more honest, customer blamed the part · insight/pain-point, sentiment/negative, journey/design, market/industrial-automation, tools/model-version-drift, tools/design-history-missing
- [[H-S0002-0014 Model-version dialog on open, with diff|H-S0002-0014]] Model-version dialog on open, with diff · functionality/new-feature-request, insight/desire, sentiment/neutral, journey/design, tools/model-version-drift, tools/design-history-missing, tools/result-reproducibility
- [[H-S0002-0015 VM per project to freeze the tool|H-S0002-0015]] VM per project to freeze the tool · functionality/workaround, insight/pain-point, sentiment/negative, journey/validate, market/digital-healthcare, tools/model-version-drift, tools/result-reproducibility
- [[H-S0002-0016 Forty percent of cases are silent resets|H-S0002-0016]] Forty percent of cases are silent resets · insight/pain-point, sentiment/neutral, journey/support, tools/silent-parameter-reset, licensing/license-lockout, correlation/sim-vs-bench-gap, sharing/file-version-lock
- [[H-S0002-0017 Read-only bench PC, dongle requested|H-S0002-0017]] Read-only bench PC, dongle requested · insight/pain-point, functionality/workaround, functionality/new-feature-request, journey/validate, market/communications, licensing/license-lockout, licensing/offline-activation
- [[H-S0002-0018 Reset is by design, reported four times|H-S0002-0018]] Reset is "by design", reported four times · insight/pain-point, functionality/new-feature-request, sentiment/negative, journey/support, tools/silent-parameter-reset, workflow/no-owner-for-wrong-number
- [[H-S0002-0019 Which part change resets which parameter|H-S0002-0019]] Which part change resets which parameter · experience/advanced, sentiment/neutral, journey/design, tools/silent-parameter-reset, tools/hidden-defaults
- [[H-S0002-0020 Engineers forgive error, not silence|H-S0002-0020]] Engineers forgive error, not silence · insight/pain-point, sentiment/negative, journey/design, market/automotive, tools/silent-parameter-reset
- [[H-S0002-0021 Tool picks the part, spreadsheet designs|H-S0002-0021]] Tool picks the part, spreadsheet designs · insight/pain-point, sentiment/negative, journey/design, experience/advanced, market/communications, tools/silent-parameter-reset, workflow/tool-for-shopping-only
- [[H-S0002-0022 Half of site visits are offline by policy|H-S0002-0022]] Half of site visits are offline by policy · insight/pain-point, sentiment/neutral, journey/support, market/aerospace-defence, licensing/offline-activation
- [[H-S0002-0023 Checklist training halves cases, feature tour doesn't|H-S0002-0023]] Checklist training halves cases, feature tour doesn't · sentiment/neutral, journey/support, docs/shadow-docs, tools/hidden-defaults
- [[H-S0002-0024 The number that explains itself is believed|H-S0002-0024]] The number that explains itself is believed · insight/pain-point, functionality/new-feature-request, sentiment/negative, journey/design, tools/hidden-defaults, correlation/thermal-correlated
- [[H-S0002-0025 Competitors win on change summary and plain files|H-S0002-0025]] Competitors win on change summary and plain files · insight/desire, functionality/new-feature-request, sentiment/neutral, journey/evaluate, tools/silent-parameter-reset, sharing/file-version-lock
- [[H-S0002-0026 Yours is for shopping, theirs for designing|H-S0002-0026]] "Yours is for shopping, theirs for designing" · insight/pain-point, sentiment/negative, journey/design, market/industrial-automation, sharing/file-version-lock, selection/part-finder-stock, workflow/tool-for-shopping-only
- [[H-S0002-0027 Official tickets are a fifth of real cases|H-S0002-0027]] Official tickets are a fifth of real cases · insight/pain-point, functionality/new-feature-request, sentiment/neutral, journey/support
- [[H-S0002-0028 Cut news feed, 3D view, assistant, update nag|H-S0002-0028]] Cut news feed, 3D view, assistant, update nag · functionality/feature-removal-request, sentiment/negative, journey/design, tools/silent-parameter-reset
- [[H-S0002-0029 Shareable link read-only, every value, comments|H-S0002-0029]] Shareable link: read-only, every value, comments · functionality/new-feature-request, insight/desire, sentiment/neutral, journey/integrate, sharing/file-version-lock, sharing/screenshot-support
- [[H-S0002-0030 Conservative models shown with false precision|H-S0002-0030]] Conservative models shown with false precision · insight/pain-point, functionality/new-feature-request, sentiment/negative, journey/validate, market/energy, correlation/accuracy-statement-missing, correlation/sim-vs-bench-gap
- [[H-S0002-0031 QR code loads the board's real parts|H-S0002-0031]] QR code loads the board's real parts · functionality/new-feature-request, insight/pain-point, sentiment/neutral, journey/evaluate, correlation/kit-model-drift
- [[H-S0002-0032 Nobody owns the number was wrong|H-S0002-0032]] Nobody owns "the number was wrong" · insight/pain-point, sentiment/negative, journey/support, workflow/no-owner-for-wrong-number
- [[H-S0002-0033 Serious customers build rituals around the tool|H-S0002-0033]] Serious customers build rituals around the tool · functionality/workaround, insight/pain-point, sentiment/negative, journey/design, sharing/pdf-review-loop, tools/design-history-missing, tools/result-reproducibility
- [[H-S0002-0034 First hour sells, second hour unsells|H-S0002-0034]] First hour sells, second hour unsells · insight/pain-point, experience/beginner, sentiment/negative, journey/design, tools/silent-parameter-reset, tools/hidden-defaults
- [[H-S0002-0035 No warning is read as approval|H-S0002-0035]] No warning is read as approval · insight/pain-point, experience/beginner, sentiment/negative, journey/design, tools/hidden-defaults
- [[H-S0002-0036 Near miss corrected model, marginal inductor|H-S0002-0036]] Near miss: corrected model, marginal inductor · insight/pain-point, sentiment/negative, journey/validate, market/automotive, tools/model-version-drift, correlation/sim-vs-bench-gap
- [[H-S0002-0037 Three hygiene fixes, reset dialog first|H-S0002-0037]] Three hygiene fixes, reset dialog first · functionality/new-feature-request, sentiment/neutral, journey/support, tools/silent-parameter-reset, tools/model-version-drift, licensing/offline-activation
<!-- appearances:end -->
