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
evidence_highlights: 12
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

**Highlights (12)**
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
<!-- appearances:end -->
