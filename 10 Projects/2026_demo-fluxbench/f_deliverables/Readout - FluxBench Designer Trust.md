---
type: deliverable
doc: readout
project: 2026_demo-fluxbench
title: 'Readout: Why engineers stop trusting FluxBench Designer, and what would bring them back'
audience: [FluxBench product owner, FAE lead, UX research sponsor]
status: draft
version: 1.0
date: 2026-11-17
contains_participant_data: quotes by participant ID
insights: [I-2026_demo-fluxbench-01, I-2026_demo-fluxbench-02, I-2026_demo-fluxbench-03, I-2026_demo-fluxbench-04, I-2026_demo-fluxbench-05, I-2026_demo-fluxbench-06, I-2026_demo-fluxbench-07]
published_to: https://analog.atlassian.net/wiki/spaces/SDPUXR/pages/388542423
---

# Readout: Why engineers stop trusting FluxBench Designer, and what would bring them back

> [!warning] Fictional demo
> The product, the vendor, the participants and every quote are invented. This report exists to show what a readout from the research vault looks like.

**Study:** [[10 Projects/2026_demo-fluxbench/01 project|2026-10 Discovery - FluxBench Designer Trust]] · three hour-long interviews, 14 to 16 October 2026 · 35 highlights · 7 insights
**For:** FluxBench product owner, FAE lead, UX research sponsor
**Status:** draft for discussion. All evidence is at the *emerging* level (two or three participants); nothing here is confirmed at scale.

## Summary

Engineers do not distrust FluxBench Designer because its models are wrong. They distrust it because it changes things without saying so, keeps its results on one machine, and hands over pictures where the downstream work needs numbers. Every participant has built a private workaround: a spreadsheet run in parallel, a one-page checklist of hidden defaults, a second laptop that never goes online, a day of retyping per validation report. The support load the FAE team carries is the aggregate of those workarounds.

Three things follow.

1. **The cheapest fix is also the biggest.** Tell the user what the tool changed, when, and under which model version. The FAE estimates this alone would halve tool-related support questions.
2. **Trust is granted per result, after one correlation with hardware.** The thermal estimate is already trusted for exactly that reason. A published accuracy statement per result type would let regulated customers accept the tool without re-proving it themselves.
3. **The design cannot leave the machine it was made on.** Until it can, review, support and hand-back will keep running on screenshots and PDFs, whatever the models do.

## What we did

Three semi-structured interviews over video call, recorded, transcribed and pseudonymised: an external hardware design engineer on a first design in the tool (P-001), an internal field applications engineer supporting about forty accounts (P-002), and an external validation engineer in a regulated industry whose job is to compare simulated and measured results (P-003). Highlights were proposed by AI, accepted or rejected by the researcher, and only accepted highlights fed the synthesis. Each finding below links to its insight note and to the highlights behind it, and each highlight links to its line in the transcript.

Three participants is a small base. Treat each finding as a hypothesis with early support, not a measured fact. The "next research" section says what would settle each one.

## Findings

### 1. Silent parameter changes, not model error, are what make results look wrong

Every time a participant called a result wrong, the tool had changed or assumed something without saying so. The commonest case: changing the part resets the switching frequency entered on the first screen. The designer lost an hour and then their trust; the FAE sees it weekly and calls it the top support cause; the validation engineer found the thermal model quietly scales a standard board rather than using the one described.

> It's not that it was wrong, it's that it didn't tell me it had changed something. (P-001, [[H-S0001-0005 Lost trust because the tool didn't say what it changed|H-S0001-0005]])

> Tell the user when you changed something they didn't ask for. That one change would cut my tool questions in half. (P-002, [[H-S0002-0011 Announce changes, halve support questions|H-S0002-0011]])

Insight: [[I-2026_demo-fluxbench-02 Silent parameter changes, not model error, are what make results look|I-2026_demo-fluxbench-02]]. Also [[H-S0001-0004 Part change silently reset switching frequency|H-S0001-0004]], [[H-S0002-0005 Silent reset is the top support cause|H-S0002-0005]], [[H-S0002-0006 Shadow checklist of hidden defaults|H-S0002-0006]], [[H-S0002-0012 Model updates change old results on reopen|H-S0002-0012]], [[H-S0003-0011 Thermal model is less board-specific than assumed|H-S0003-0011]].

### 2. Engineers trust a result only after it has matched the bench

Trust is per result, not per tool. The designer trusts the thermal estimate because it came within a few degrees of the first prototype, and distrusts ripple because it disagreed with a spreadsheet that has shipped boards. For the validation engineer this is a process rule: quality accepts a vendor statement and rejects personal correlation, so every project starts from zero.

> Trust for me is correlation. Show me it matches hardware once and I'll use it. (P-001, [[H-S0001-0010 Trust is correlation|H-S0001-0010]])

> Our quality people would accept a vendor statement. They don't accept my gut. (P-003, [[H-S0003-0009 Quality accepts a vendor statement, not a gut|H-S0003-0009]])

Insight: [[I-2026_demo-fluxbench-01 Engineers trust a simulated result only after it has matched the|I-2026_demo-fluxbench-01]]. Also [[H-S0001-0003 Spreadsheet wins when tool and spreadsheet disagree|H-S0001-0003]], [[H-S0001-0009 Thermal estimate matched the first prototype|H-S0001-0009]], [[H-S0002-0009 Small discrepancies lose the careful engineers|H-S0002-0009]], [[H-S0003-0008 Trust earned project by project|H-S0003-0008]].

### 3. Designs can't leave the machine they were made on

Project files refuse to open across versions, there is no link or shared view, and no history inside a project. Review runs on PDF exports, support rebuilds designs from screenshots (twenty to thirty minutes a case, usually with one hidden parameter wrong), and validation names forks with dates and initials.

> Right now a FluxBench design is stuck on one machine. The silicon is a shared thing between us and the customer; the design should be too. (P-002, [[H-S0002-0010 Designs should be shared like the silicon|H-S0002-0010]])

> If I open a design from three weeks ago I can't tell what I changed. (P-001, [[H-S0001-0011 No design history in the project file|H-S0001-0011]])

Insight: [[I-2026_demo-fluxbench-03 Designs can't leave the machine they were made on, so review|I-2026_demo-fluxbench-03]]. Also [[H-S0001-0008 Design review runs on PDF exports|H-S0001-0008]], [[H-S0002-0001 Version lock forces screenshots|H-S0002-0001]], [[H-S0002-0002 Rebuilding designs from screenshots|H-S0002-0002]], [[H-S0003-0010 Project forks named with dates and initials|H-S0003-0010]].

### 4. Exports serve presentation, not analysis

Plots export, the numbers behind them don't; loss comes as one figure that cannot be diagnosed; the BOM export ignores the customer's approved-vendor list. The validation engineer loses most of a one-day report to retyping cursor readings; the designer spends half an hour per export swapping parts.

> Give me the data behind every plot as a CSV with the assumptions in the header. That alone takes half a day off every report. (P-003, [[H-S0003-0012 CSV with assumptions in the header|H-S0003-0012]])

Insight: [[I-2026_demo-fluxbench-06 Exports serve presentation, not analysis pictures come out, the|I-2026_demo-fluxbench-06]]. Also [[H-S0001-0007 BOM export ignores the approved vendor list|H-S0001-0007]], [[H-S0003-0003 Loss shown as one number blocks diagnosis|H-S0003-0003]], [[H-S0003-0004 Plots export, the numbers don't|H-S0003-0004]], [[H-S0003-0005 A day of retyping per report|H-S0003-0005]].

### 5. Licensing assumes a connected machine; labs and customer sites aren't

Activation and periodic check-ins need outbound access that lab networks block and customer networks restrict. The designer's first twenty minutes were an activation detour; the FAE was locked out twice in front of customers and now carries a second laptop.

> Twice this year it locked me out in front of a customer. I now carry a second laptop that I activated at home and never connect to anything. (P-002, [[H-S0002-0003 Second laptop as a licensing workaround|H-S0002-0003]])

Insight: [[I-2026_demo-fluxbench-05 Licensing assumes a connected machine; labs and customer sites aren't|I-2026_demo-fluxbench-05]]. Also [[H-S0001-0001 Activation blocked on the lab network|H-S0001-0001]], [[H-S0002-0004 Thirty days of offline grace|H-S0002-0004]].

### 6. Eval kits and their simulation models drift apart

Kits get revised, models don't follow, and the gap shows up at the moment a careful customer compares the two to decide on the part. The FAE puts it at one kit in four; the validation engineer closed a ripple gap only by hand-entering the kit's actual capacitor.

> The kit had a different output capacitor, a revision change. Once I put the kit's actual parts into the simulation, the ripple came within ten percent. (P-003, [[H-S0003-0002 Kit capacitor revision explained the ripple gap|H-S0003-0002]])

Insight: [[I-2026_demo-fluxbench-04 Eval kits and their simulation models drift apart, and the mismatch|I-2026_demo-fluxbench-04]]. Also [[H-S0002-0008 Eval kit revised, model not|H-S0002-0008]].

### 7. Long simulations block the interface or crash, and nobody can report it

An eleven-minute sweep with no progress indicator was mistaken for a hang and killed. Temperature sweeps crash about one run in three with no error, and there is no way to report it without a portal account, so the vendor may not know the rate.

> A sweep over ten temperatures with a load step at each one crashes the application about one time in three. No error, it just closes. (P-003, [[H-S0003-0006 Temperature sweeps crash one in three|H-S0003-0006]])

Insight: [[I-2026_demo-fluxbench-07 Long simulations block the interface or crash, and users adapt by|I-2026_demo-fluxbench-07]]. Also [[H-S0001-0006 Eleven-minute sweep looked like a hang|H-S0001-0006]], [[H-S0003-0007 No place to report a crash|H-S0003-0007]].

## Recommendations, in the order we would take them

| # | Recommendation | Why first | Finding |
|---|---|---|---|
| 1 | Announce every parameter the tool changes on the user's behalf, inline and logged in the project; stamp model versions into project files and warn on open when a model changed | Smallest change with the largest claimed effect on trust and support load | 1 |
| 2 | Export plot data as CSV with assumptions in the header; break loss into conduction, switching and gate drive | Specified by the user, removes half a day per validation report | 4 |
| 3 | Publish a per-result accuracy statement and show it on the result; lead onboarding with the thermal estimate | Makes the tool admissible in regulated teams without private re-proving | 2 |
| 4 | Offline grace period sized to a field trip (the FAE said thirty days) and activation by file or code | Stops losing first impressions and credibility in front of customers | 5 |
| 5 | Tie each kit revision to a model revision; ship the kit's real BOM as a loadable preset | Protects the simulate, buy the kit, measure path that converts careful engineers | 6 |
| 6 | Progress feedback and background execution for sweeps; crash reporting without a portal account | Also gives the vendor the crash rate it currently can't see | 7 |
| 7 | A forward-compatible or link-based design representation, with history inside the project | The largest change, and the one that ends the screenshot and PDF loops | 3 |

Items 1 to 4 are, on what participants told us, within reach of a single release and would be felt in support numbers. Item 7 is the strategic one and deserves its own discovery.

## What we don't know yet, and the research that would settle it

- Whether an accuracy statement changes behaviour, or users only say it would. Test a mocked statement with new users.
- How often blocked lab networks occur across customer segments. A short survey through the FAE team.
- The real crash rate for sweeps. Instrument sweep runs.
- The kit-model drift rate. Compare kit revision records with model release dates; the one-in-four figure is one person's estimate.
- How many rounds a design review takes and who sees the design. Observe one real review.
- Whether FAEs hit the export wall; they were not asked.

## Appendix

**Participants.** [[20 Participants/P-001|P-001]], senior hardware design engineer, industrial robotics, first-time user. [[20 Participants/P-002|P-002]], staff field applications engineer, about forty accounts. [[20 Participants/P-003|P-003]], validation engineer, medical devices. Names and employers are held in the participant key, not in this report. Consent is tracked in Rally under DEMO-0001; external participants consented to recording, quotes and video clips, the internal participant to quotes only.

**Evidence levels.** Strong: four or more participants with consistent language. Emerging: two or three. Insufficient: one, kept as tagged highlights only. Everything in this readout is emerging.

**Traceability.** Each quote links to its highlight note, which links to the exact line of the pseudonymised transcript and, for external participants, to a stamped video clip. Every insight links to all of its highlights; each highlight carries its tags and the reviewer's decision.

**Related.** All seven insights are on the [[10 Projects/2026_demo-fluxbench/01 project|study overview]]; the full tag analysis is on [[10 Projects/2026_demo-fluxbench/03 tag board|the tag board]].
