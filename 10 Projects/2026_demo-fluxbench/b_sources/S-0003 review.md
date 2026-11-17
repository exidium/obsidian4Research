---
type: review
source: "[[S-0003]]"
project: 2026_demo-fluxbench
blocks: s0003-0029 to s0003-0175
proposals: 25
status: pending
created: 2026-11-17
---

# Review: S-0003 (P-003, validation engineer, medical devices), blocks 0029 to 0175

Mode 1 proposals for the second part of the interview (00:08:52 to 01:04:48, about 56 minutes). Nothing has been created; every item below waits for accept / modify / reject by number.

## Already highlighted (blocks 0001 to 0028, not re-proposed)

| ID | Block | Title |
|---|---|---|
| H-S0003-0001 | ^s0003-0004 | Every discrepancy becomes a documented investigation |
| H-S0003-0002 | ^s0003-0006 | Kit capacitor revision explained the ripple gap |
| H-S0003-0003 | ^s0003-0008 | Loss shown as one number blocks diagnosis |
| H-S0003-0004 | ^s0003-0010 | Plots export, the numbers don't |
| H-S0003-0005 | ^s0003-0012 | A day of retyping per report |
| H-S0003-0006 | ^s0003-0014 | Temperature sweeps crash one in three |
| H-S0003-0007 | ^s0003-0016 | No place to report a crash |
| H-S0003-0008 | ^s0003-0018 | Trust earned project by project |
| H-S0003-0009 | ^s0003-0020 | Quality accepts a vendor statement, not a gut |
| H-S0003-0010 | ^s0003-0022 | Project forks named with dates and initials |
| H-S0003-0011 | ^s0003-0024 | Thermal model is less board-specific than assumed |
| H-S0003-0012 | ^s0003-0028 | CSV with assumptions in the header |

Where a new proposal deepens one of these, the rationale says so; the new blocks carry detail (numbers, mechanisms, consequences) the first 28 blocks did not.

## Proposals

### 1. No documentation for the person who checks

- **Block:** ^s0003-0034
- **Excerpt:** "There is a training course on the portal, I believe, but it is aimed at designers, how to pick a topology, how to size an inductor. There is nothing for the person who has to check the answer. I would have liked a page that said, here is what each result means, here is what it assumes, here is how accurate we think it is. That page would have saved me the first year."
- **Workspace tags:** insight/desire, sentiment/neutral, journey/support, experience/beginner
- **Project tags:** correlation/accuracy-statement-missing, tools/hidden-defaults
- [CONTEXT: Asked whether anyone trained them. The designer showed them how to open and run a project in about twenty minutes; the rest was learned by comparing results to measurements.]
- **Rationale:** Names a documentation audience the vendor does not serve (the validator) and specifies the page in three parts (meaning, assumptions, accuracy), which maps directly onto RQ1 and onto two existing project tags.

### 2. Every out-of-limit row needs an investigation number

- **Block:** ^s0003-0036
- **Excerpt:** "We have a form, an investigation record, with a number, the parameter, the simulated value, the measured value, the acceptance limit, and then a root cause section and a closure section. It gets opened the day the discrepancy is confirmed, and it does not close until a second engineer signs it. The report then references the investigation number next to the row in the simulated versus measured table. So for the 5 volt rail there were two of them, one for ripple and one for efficiency, and the report points at both. Nothing in the table is allowed to be a surprise without a number next to it."
- **Workspace tags:** sentiment/neutral, journey/validate, market/digital-healthcare
- **Project tags:** workflow/workflow-described, `PROPOSED: workflow/quality-system-constraint` (a rule of the participant's quality system, such as an acceptance limit, a controlled document, a software assessment or an audit, that governs whether and how a simulated value may count as evidence)
- [CONTEXT: Deepens H-S0003-0001. "Documented investigation" in practice: a numbered form with fields, a second signature, and a cross-reference from the report table.]
- **Rationale:** The concrete artefact behind "every discrepancy becomes an investigation" explains why a simulation gap costs days rather than minutes in this market (RQ2) and why nothing fits the existing project tags: the cost is set by the quality system, not the tool.

### 3. Acceptance limits decide what the tool costs

- **Block:** ^s0003-0038
- **Excerpt:** "For that rail it was two points on efficiency, twenty percent on ripple, five degrees on hotspot temperature. Anything inside the limit gets a line in the table and nothing else. Anything outside becomes an investigation. Three points on efficiency and forty percent on ripple were both outside, so two investigations. The limits are not about the tool, they are about the product, but in practice they decide how much of my time the tool costs me."
- **Workspace tags:** sentiment/neutral, journey/validate, market/digital-healthcare
- **Project tags:** correlation/sim-vs-bench-gap, `PROPOSED: workflow/quality-system-constraint`
- [CONTEXT: The limits come from the design verification plan, written before any measurement.]
- **Rationale:** Gives the numbers that turn a 3-point efficiency gap and a 1.4x ripple gap into two investigations; a product owner can use these limits to judge which model deviations matter to a medical customer (RQ1, RQ2).

### 4. The model was right, the bookkeeping cost three days

- **Block:** ^s0003-0046
- **Excerpt:** "So one capacitor revision cost us roughly three days across two people, for a result that in the end was fine. That is the part I would like someone to hear. The model was right. The bookkeeping around it was wrong, and the bookkeeping is where the days go."
- **Workspace tags:** insight/pain-point, sentiment/negative, journey/validate
- **Project tags:** correlation/kit-model-drift
- [CONTEXT: Closing the ripple investigation from H-S0003-0002: the eval kit's revision C used two 22 uF capacitors of a different dielectric, found in a revision table on page fourteen of the kit document; half a day went on establishing which revision the board even was.]
- **Rationale:** Qualifying evidence that the "wrong result" was not model error but kit documentation drift, and a cost figure (three days, two people) the FAE lead can weigh against publishing kit revisions in the model (RQ3).

### 5. Loss breakdown exists internally but is not shown

- **Block:** ^s0003-0052
- **Excerpt:** "He said the loss model is built that way internally, it is just not shown. He even had a slide with a breakdown from a different internal tool, conduction, switching, gate drive, nicely stacked. So the data exists somewhere in the building. Seeing that slide was slightly maddening, if I am honest."
- **Workspace tags:** insight/pain-point, functionality/new-feature-request, sentiment/negative, journey/support
- **Project tags:** correlation/loss-breakdown-missing
- [CONTEXT: Asked whether they had requested the loss breakdown by mechanism; the FAE answered in the same visit as the crash report. Deepens H-S0003-0003.]
- **Rationale:** Unexpected: the loss breakdown the validator needs already exists in the vendor's model, so the gap is a display decision rather than a modelling effort, which changes the cost side of any recommendation.

### 6. Bare simulated number looks more certain than it is

- **Block:** ^s0003-0056
- **Excerpt:** "The simulated side has no uncertainty column, because the tool does not give one. It is a bare number sitting next to a measured number with error bars, and the bare number looks more certain than it is. That is backwards, and quality has noticed it too."
- **Workspace tags:** insight/pain-point, sentiment/negative, journey/validate
- **Project tags:** correlation/accuracy-statement-missing
- [CONTEXT: Every measured value in the report carries an uncertainty from the instrument specification and the calibration record (about 0.3 of a point on efficiency, about five percent on ripple). "Within ten percent" means the simulated value falls inside the measured value plus its uncertainty plus the limit.]
- **Rationale:** Reframes the accuracy statement as a missing uncertainty column in a two-column table, a concrete form a PM can picture, and notes that the customer's quality function has spotted the asymmetry (RQ1).

### 7. Transposed digit turned a discrepancy into a pass

- **Block:** ^s0003-0064
- **Excerpt:** "He reopens the project and spot checks a third of the numbers. Last year he caught a transposed digit in a thermal value that turned a discrepancy into a pass on paper. That is exactly what quality worries about, a human copying numbers from a screen, and they are right to. If the numbers came out as a file, the reviewer would diff two files instead of squinting at a cursor."
- **Workspace tags:** insight/pain-point, sentiment/negative, journey/validate
- **Project tags:** export/report-retyping, workflow/review-loop-described
- [CONTEXT: Asked how they know the roughly fifty cursor-read simulation numbers were typed correctly: "I do not, until the reviewer checks." Deepens H-S0003-0005 with the failure mode.]
- **Rationale:** Turns retyping from a time cost into a safety and compliance risk (a false pass in a medical validation report), the strongest argument for data export in this transcript (RQ2).

### 8. Accuracy statement must read like a datasheet

- **Block:** ^s0003-0070
- **Excerpt:** "It needs to be a controlled document. Title, revision number, date, and the tool version range it applies to. Then per result type: efficiency, ripple, hotspot temperature, transient response, each with a typical deviation and a maximum deviation. Then the conditions: parts match the library, operation within the stated range, board within what the thermal model assumes. Then the basis: how many boards, which kits, what instruments. Exactly like a datasheet, typical and max with conditions. If it just says accurate, it is useless."
- **Workspace tags:** functionality/new-feature-request, insight/desire, sentiment/neutral, journey/validate
- **Project tags:** correlation/accuracy-statement-missing
- [CONTEXT: Asked what a vendor accuracy statement would need to contain to be acceptable. In ^s0003-0072 they add that quality would not want the raw data behind it, only a revisioned document someone at the vendor is accountable for; in ^s0003-0068 quality's third question on every report is "a basis for believing the simulated values", currently answered with the participant's own correlation history.]
- **Rationale:** The specification of the accuracy statement (structure, per-result typ/max, conditions, basis) is directly actionable and sets the bar for what would count; extends H-S0003-0009 from "would accept" to "what exactly".

### 9. A PNG is a picture of a result, not a result

- **Block:** ^s0003-0076
- **Excerpt:** "But a PNG is a picture of a result, not a result. It has no version, no parameters, no date except the file date, and you cannot check it. The reviewer cannot put a cursor on a PNG. Twice I have been asked, which run is this plot from, and I had to answer from my file naming convention, which is a convention and not a record. If the plot came out next to a CSV with the same name and a header, the picture would be the illustration and the file would be the evidence. Right now the picture is the evidence, and it is the weakest thing in the report."
- **Workspace tags:** insight/pain-point, functionality/new-feature-request, sentiment/negative, journey/validate
- **Project tags:** export/plot-data-not-exportable
- [CONTEXT: Asked what quality thinks of PNG plots as evidence; they accept them "because that is what everyone has".]
- **Rationale:** Explains why the export gap is an evidence-quality problem for an audited customer, not a convenience problem, and proposes the exact shape of the fix (CSV beside the PNG, same name, header) (RQ2).

### 10. Offline bench waits thirty seconds for an update check

- **Block:** ^s0003-0078
- **Excerpt:** "The bench PCs are on an isolated network, no internet. Software installs go through IT with a ticket, and updates happen quarterly if we are lucky. FluxBench runs on the bench PC and on my office laptop, and moving a project between them is a USB stick. Every time the tool starts on the bench it tries to check for updates, waits about thirty seconds, then gives up. Thirty seconds, several times a day, for a machine that will never see the internet. Small thing, but it sets the tone."
- **Workspace tags:** insight/pain-point, sentiment/negative, journey/validate
- **Project tags:** licensing/offline-activation
- [CONTEXT: Asked about lab constraints. The offline bench recurs through the interview: FAE model updates arrive on a USB stick, the support portal and app notes are reachable only from the office laptop, and any crash reporter "has to work offline".]
- **Rationale:** The lab environment (air-gapped bench, quarterly IT-ticketed updates, USB transfer) is a constraint every later recommendation must satisfy; the update check is a network check-in the user cannot complete, the closest fit to the offline-activation tag (RQ2).

### 11. Two-week argument over an inductor in a stray copy

- **Block:** ^s0003-0090
- **Excerpt:** "Twice we have validated against a project that was not the designer's latest. One of those turned into a two week argument about a 60 millivolt transient difference, which turned out to be a different inductor in the two project files. Nobody had changed it on purpose. It had been changed in a copy that never came back."
- **Workspace tags:** insight/pain-point, sentiment/negative, journey/integrate
- **Project tags:** sharing/design-fork, tools/design-history-missing
- [CONTEXT: Files are named with dates and initials (H-S0003-0010). In ^s0003-0092 the asks are a change log inside the project, a diff between two project files, and a record of the model library version per run; in ^s0003-0146 a shared folder failed because the tool locks the open file and the second person saves a read-only copy under a new name.]
- **Rationale:** A measurable consequence of design forks (two weeks, a 60 mV argument) that was in fact a hidden parameter difference, linking the sharing problem to the "wrong result" question (RQ2, RQ3).

### 12. Archived installers are the only way to reproduce a number

- **Block:** ^s0003-0094
- **Excerpt:** "If quality asks me to reproduce a result from a report, I need the tool version on page one of that report, not the one on my laptop. We had a case: re-ran a thermal from a report that was eight months old, got four degrees different, and it took a day to work out it was a model update, not the board, not the chamber. Now the version is recorded on page one, and the installer is archived with the report. It is the only way I can promise to reproduce a number."
- **Workspace tags:** functionality/workaround, insight/pain-point, sentiment/neutral, journey/validate
- **Project tags:** tools/model-version-drift
- [CONTEXT: In ^s0003-0144 they were twice asked to re-run a simulation in front of an auditor; the archived installer "saved me the second time". In ^s0003-0142 the parameters the tool defaulted are written nowhere, so a run is "reproducible in practice, usually, and not provably". In ^s0003-0156 release notes saying "improved models" give no way to size the risk of an update, so updates are delayed.]
- **Rationale:** Silent model updates force a regulated customer to archive installers (against IT's wishes) to keep results reproducible under audit; strong evidence for model versioning and change notification, the follow-up the project note already flags (RQ1, RQ2).

### 13. Sweep crash follows a steady memory climb

- **Block:** ^s0003-0096
- **Excerpt:** "It crashes about one time in three, usually between the sixth and eighth point. No dialog, no message, the window is just gone. We looked for a crash log in the usual places and found nothing. I watched the memory in the task manager during a sweep and it climbs steadily, around three gigabytes by the sixth point. I am guessing it is a leak, but I am a hardware person guessing about software, which is the same thing I complain about in reverse."
- **Workspace tags:** functionality/bug, insight/pain-point, sentiment/negative, journey/validate
- **Project tags:** tools/simulation-crash
- [CONTEXT: Temperature sweep, ten points from minus 20 to plus 70 with a load step at each. In ^s0003-0098 the workaround is splitting into two runs of five points, which doubles the time, and "I have never seen a wrong number from a sweep, only a missing one." Deepens H-S0003-0006.]
- **Rationale:** Reproduction detail (point six to eight, about 3 GB, no log) that an engineering team can act on, plus the qualifying note that the crash loses time, not correctness (RQ3).

### 14. A channel for circuit questions, none for tool questions

- **Block:** ^s0003-0104
- **Excerpt:** "When I bring a tool question, export, crash, versions, he writes it down and I can see he has no path for it either. I do not think that is his fault. The vendor has built a channel for circuit questions and no channel for tool questions, and the validation engineer only ever has tool questions. So the visit is useful for the designer and polite for me."
- **Workspace tags:** insight/pain-point, sentiment/negative, journey/support
- **Project tags:** docs/no-defect-channel
- [CONTEXT: The FAE visits every couple of months, usually at the designer's request, and brings model updates on a USB stick to get past the offline bench. In ^s0003-0100 the crash report handed to the FAE three months earlier has no visible status: "Not knowing is what costs me, because I plan around it." In ^s0003-0102 the ask is an offline crash report, a ticket number, and a known-issues list.]
- **Rationale:** Explains structurally why tool defects do not reach the product team (the FAE channel is built for circuit questions) and why this role in particular is unheard; reframes H-S0003-0007 from a missing button to a missing channel (RQ3).

### 15. Vendor tools win on models, lose on everything around them

- **Block:** ^s0003-0116
- **Excerpt:** "RailForge exports everything to CSV and has a scripting console. I never did a formal correlation there, so I cannot say its models are worse, but the engineers around me trusted them less. Tessaline is a web tool, so useless on an offline bench, but its report generation was impressive. One click and you get a PDF with every parameter the run used, defaults included. None of the three has an accuracy statement. The vendor specific tools win on models and lose on everything around the models. The general tools are the reverse."
- **Workspace tags:** sentiment/neutral, journey/evaluate
- **Project tags:** export/plot-data-not-exportable, correlation/accuracy-statement-missing, `PROPOSED: tools/competitor-comparison` (participant compares FluxBench with another simulation tool on a named capability), `PROPOSED: export/scripting-interface-missing` (no command line, scripting or batch interface to drive simulation runs from the user's own automation)
- [CONTEXT: RailForge and Tessaline Power Studio are fictional competitor tools from the participant's previous employer and a last-year evaluation. In ^s0003-0118 the wish list is RailForge's scripting console and CSV export, Tessaline's parameter page in the report, and FluxBench's models; in ^s0003-0080 the bench instruments are already script-driven and the simulation "cannot be driven the same way".]
- **Rationale:** The only competitor benchmark in the study: FluxBench's moat is the models, its deficits (CSV, scripting, parameter page) are already solved elsewhere, and no competitor offers an accuracy statement, which would be a differentiator (RQ1).

### 16. Nobody chooses a simulation tool, the controller does

- **Block:** ^s0003-0120
- **Excerpt:** "It is always the parts. Nobody chooses a simulation tool. They choose a controller, and the tool arrives with it. Which means the tool is never evaluated the way an instrument would be. I ran a three week evaluation on our last power analyzer. The simulation tool got installed on a Tuesday because the FAE had a USB stick."
- **Workspace tags:** sentiment/neutral, journey/evaluate, experience/advanced, ops/follow-up-depth
- **Project tags:** `PROPOSED: tools/competitor-comparison`
- [CONTEXT: Asked why the previous employer chose RailForge.]
- **Rationale:** Unexpected framing of adoption: the tool is never evaluated, so trust is never established at the start and has to be earned per result later (RQ1); worth probing in a wider study.

### 17. Frequency change quietly reset a related parameter

- **Block:** ^s0003-0126
- **Excerpt:** "And one I had not hit: she changed the switching frequency and a related parameter quietly reset to a default. The design engineer told her that one was known on their side. Known on their side, not on mine, and not in the tool. So it went on the sheet."
- **Workspace tags:** insight/pain-point, sentiment/negative, journey/design
- **Project tags:** tools/silent-parameter-reset, docs/shadow-docs
- [CONTEXT: What tripped up the junior engineer despite the twelve-item checklist; "the sheet" is the team's known-gaps sheet. Converges with P-001's silent reset after a part change (S-0001).]
- **Rationale:** A second participant, in a different role and company, hits the silent parameter reset, lifting that pattern toward emerging evidence; also shows the knowledge living in people ("known on their side") rather than in the tool (RQ3).

### 18. Trust lives in a checklist, not in the tool

- **Block:** ^s0003-0128
- **Excerpt:** "She trusts the checklist. That is the honest state of things: the trust lives in a document we maintain, not in the tool. If I leave, the trust leaves with the document, and whoever comes next starts earning it project by project like I did. A vendor that understood that would be asking for our checklist, because it is a list of everything their product failed to say."
- **Workspace tags:** insight/pain-point, sentiment/negative, journey/validate
- **Project tags:** docs/shadow-docs
- [CONTEXT: Asked whether the junior engineer trusts the tool. The twelve-item checklist (^s0003-0124) covers save before sweeps, check the advanced panel before trusting a number, record kit revision and tool version, the thermal reference board, and where the known-gaps sheet lives; in ^s0003-0130 the known-gaps sheet is "probably the most read document I have written".]
- **Rationale:** The clearest answer in the transcript to RQ1: trust is externalised into a self-maintained document that the vendor could read as a defect list; extends H-S0003-0008 from the individual to the team.

### 19. Accuracy statement would turn yellow cells white

- **Block:** ^s0003-0138
- **Excerpt:** "We give those cells a yellow background in the table, and each yellow cell needs a justification sentence. Right now the justification is, model correlated on prior projects, see reports such and such. An accuracy statement from the vendor would turn yellow cells into white ones, because the justification becomes a reference to a controlled document instead of a reference to me. That is the most concrete thing it would change, fewer yellow cells and fewer questions."
- **Workspace tags:** insight/desire, sentiment/neutral, journey/validate, market/digital-healthcare
- **Project tags:** correlation/accuracy-statement-missing, `PROPOSED: workflow/quality-system-constraint`
- [CONTEXT: Yellow cells are simulated-only rows: component tolerance extremes, ambient above the chamber's 70 degrees, fault conditions nobody wants to create on a real board (^s0003-0136). In ^s0003-0074 the quality system requires software that generates verification evidence to be assessed for intended use; the participant's one-page assessment says the measurement, not the simulation, is the evidence, which "works until a yellow cell".]
- **Rationale:** The most concrete, countable outcome of an accuracy statement for a regulated customer (fewer flagged cells, fewer audit questions), and the point where the simulation is the only evidence (RQ1).

### 20. Phone photo of a histogram in a report

- **Block:** ^s0003-0140
- **Excerpt:** "It has a tolerance sweep, I set it to two hundred runs and it took about an hour. The result was a histogram on screen with no export, not even the PNG route for that one. I photographed the screen with my phone and pasted the photo into the report. The reviewer asked whether that was a joke. It was not. That picture says everything about the export situation in one image."
- **Workspace tags:** insight/pain-point, functionality/workaround, sentiment/negative, journey/validate
- **Project tags:** export/plot-data-not-exportable
- [CONTEXT: Asked whether they had used the tool's tolerance analysis.]
- **Rationale:** The extreme case of the export gap (a tolerance histogram with no export path at all) and a vivid, stranger-proof illustration for a readout (RQ2).

### 21. Sometimes the bench is wrong, not the model

- **Block:** ^s0003-0150
- **Excerpt:** "A thermal measurement where I had the thermocouple on the wrong side of the inductor, in the airflow shadow. Simulation said 61 degrees, I measured 52, and the simulation was right. It took me a week to accept that. So I am not saying the tool is wrong. I am saying I cannot tell which of us is wrong fast enough, and the cost of finding out is the same whoever it turns out to be."
- **Workspace tags:** sentiment/neutral, journey/validate, experience/advanced
- **Project tags:** correlation/sim-vs-bench-gap
- [CONTEXT: Asked whether they had ever been the one who was wrong; these cases are documented as investigations too.]
- **Rationale:** Counter-evidence that keeps the study honest: the "wrong result" was the measurement, and the real problem is the time to tell which side is wrong (RQ1, RQ3).

### 22. Fast discrepancies are visible, slow ones hidden

- **Block:** ^s0003-0152
- **Excerpt:** "Every fast one was a parameter mismatch I could see on the screen: a wrong load value, a wrong input voltage, a part I could compare. Every slow one was something hidden: the reference board in the thermal model, the switching loss inside one number, the capacitor revision on page fourteen. Fast means I can see what the tool assumed. Slow means I have to infer it from the result. There is no third category in my notes."
- **Workspace tags:** insight/pain-point, sentiment/neutral, journey/validate
- **Project tags:** tools/hidden-defaults
- [CONTEXT: Asked what makes a discrepancy fast to resolve. In ^s0003-0154, a page stating what a run assumed would turn "half the investigations" into a five-minute checklist instead of a two-day search; in ^s0003-0088, "every assumption I have found so far, I found by accident or by failure".]
- **Rationale:** A single rule from the participant's own records that explains the whole investigation cost: visibility of assumptions, not model accuracy, decides whether a gap takes minutes or days (RQ1, RQ3).

### 23. Three-degree thermal match holds only on kits

- **Block:** ^s0003-0160
- **Excerpt:** "The caveat, which I only understood later, is that both of those were kits, which look a lot like the reference board the model assumes. On our own board the number has been further off, in the direction you would expect from more copper. So the three degrees is true, with a condition I did not know I was stating."
- **Workspace tags:** sentiment/neutral, journey/validate, experience/advanced
- **Project tags:** correlation/thermal-correlated, tools/hidden-defaults
- [CONTEXT: Thermal camera plus thermocouple on the kit after thirty minutes at fixed ambient; simulation 58 degrees, measured 56 and 55, on two projects. Qualifies the "within three degrees" in H-S0003-0008 and ties back to the reference-board assumption in H-S0003-0011.]
- **Rationale:** Qualifying evidence on the one positive correlation in the study: it holds under a condition the participant was unknowingly stating, so the thermal-correlated tag needs its condition recorded (RQ1).

### 24. Numbers out, assumptions visible, accuracy statement

- **Block:** ^s0003-0170
- **Excerpt:** "A simulation run produces a folder, not a plot. CSVs with assumptions in the header, a parameters page, the plot images, and a hash. An accuracy statement as a controlled document with a revision. A change log and a diff for project files. A crash button that works offline and gives me a number. A scripting interface so the bench and the simulation run from the same list. And a loss breakdown by mechanism. If I had to order them: numbers out, assumptions visible, accuracy statement. The rest are comfort, and I would take comfort."
- **Workspace tags:** functionality/new-feature-request, insight/desire, sentiment/neutral, journey/integrate
- **Project tags:** export/plot-data-not-exportable, correlation/accuracy-statement-missing, `PROPOSED: export/scripting-interface-missing`
- [CONTEXT: The "magic wand" question: the tool as they would want it in two years. Every item traces to an earlier story in this transcript.]
- **Rationale:** The participant's own ranked roadmap, with none of it a new simulation technique; a direct input to prioritisation and a check on whether the readout's recommendations match the customer's order (RQ1, RQ2).

### 25. The models are good, the complaints are around them

- **Block:** ^s0003-0172
- **Excerpt:** "The people who build these tools should sit in a validation lab for a week and watch someone read numbers off a cursor. And tell whoever reads this that the models are good. I complain because they are worth the effort. If they were bad, I would have stopped using the tool and nobody would be hearing any of this."
- **Workspace tags:** sentiment/positive, functionality/existing-feature, journey/validate
- **Project tags:** none
- [CONTEXT: Closing remark, unprompted. Echoes ^s0003-0026, "the things I complain about are all around the simulation, not the simulation itself".]
- **Rationale:** Positive qualifying evidence that prevents the readout from reading as "the tool is wrong": the models are the reason the participant stays, and the asks are all tooling around them (RQ1).

## Proposed project tags (for the researcher to decide)

| Proposed ID | Group | Definition | Evidence in this run |
|---|---|---|---|
| `workflow/quality-system-constraint` | 1. Workflow and Process | A rule of the participant's quality system (acceptance limit, controlled document, software assessment, audit) that governs whether and how a simulated value may count as evidence. | 2, 3, 19; context in ^s0003-0068, ^s0003-0074, ^s0003-0144 |
| `tools/competitor-comparison` | 2. Tool Behaviour | Participant compares FluxBench with another simulation tool on a named capability. | 15, 16; also ^s0003-0114, ^s0003-0118 |
| `export/scripting-interface-missing` | 7. Export and Handoff | No command line, scripting or batch interface to drive simulation runs from the user's own automation. | 15, 24; also ^s0003-0080, ^s0003-0118 |

The accuracy-statement pattern is covered by the existing `correlation/accuracy-statement-missing`; the "what did this run assume" pattern (1, 22, 23, 24) is covered by `tools/hidden-defaults`. No new tag is proposed for either.

## Coverage summary

**RQ1. When do engineers trust a simulated result, and what makes them stop?** Strong coverage: 1, 6, 8, 15, 16, 18, 19, 21, 22, 23, 24, 25. The answer from this participant is that trust is never granted by the tool and never established at adoption (16); it is earned per result, written into a self-maintained checklist and known-gaps sheet (18), and would be replaceable by a vendor accuracy statement in the form of a controlled document with typical and maximum deviations under stated conditions (8, 19). What stops trust is not model error but hidden assumptions (22, 23).

**RQ2. Where does a design go after simulation, and what breaks on the way?** Strong coverage: 2, 3, 7, 9, 10, 11, 12, 20, plus 24. The design goes into a test plan, a two-stage bench (kit, then own board), a numbered investigation per out-of-limit row, a Word report with PNGs and cursor-read numbers, a PDF in the design history file, peer and quality review, and an email hand-back with a modified project (2, 3, 7, 9). What breaks: numbers are retyped and a transposed digit once produced a false pass (7), PNGs are the evidence and cannot be checked (9, 20), project copies diverge (11), model updates change old results so installers are archived (12), and the bench is air-gapped (10).

**RQ3. What do field engineers see as the top causes of "wrong" results?** Indirect coverage only, since P-003 is a customer, not an FAE: 4, 5, 11, 13, 14, 17, 21, 22. From the customer side, the causes of a "wrong" result were kit documentation drift (4), hidden assumptions (22), a forked project file (11), a silent parameter reset (17), and once the bench itself (21); the one genuine model gap (efficiency) is undiagnosable because the breakdown is hidden, although it exists internally (5). 14 explains why these reach the FAE and go no further.

**Weak or no coverage:** licensing and activation proper (only the update check in 10); part selection (`selection/*`, nothing in this transcript); `journey/discover` and `journey/design` (the participant designs little, 17 is the only design-stage moment); `docs/feature-vs-symptom-docs` (present in ^s0003-0108, where searching the in-tool help for "export" returned the file menu page, left unproposed to stay within 25; worth adding if the researcher wants a docs data point from this participant); the FAE's own view of causes, which only S-0002 can supply.

**Unexpected findings:** the loss breakdown exists in the vendor's internal tools and is simply not displayed (5); the vendor's support channel is structurally built for circuit questions and the validator "only ever has tool questions" (14); simulation tools are never evaluated at adoption because the controller choice brings the tool with it (16); a second participant in a different company reports the silent parameter reset (17); a tolerance histogram can only leave the tool as a phone photo (20).

**Qualifying evidence (prevents oversimplification):** the model was right and the bookkeeping cost three days (4); the crash loses time, never correctness (13, context); the bench was wrong once and the simulation right (21); the three-degree thermal match holds only on kits (23); the efficiency bias is consistent in direction and size across five projects, so the participant corrects for it (^s0003-0158, unproposed, "a haircut is not a method"); the models are good and the complaints are about what surrounds them (25). Transient response is the least predictable result, "correlate per board, do not assume" (^s0003-0164, unproposed; candidate if the researcher wants a third `correlation/sim-vs-bench-gap` data point).

**Total:** 25 proposals from 25 distinct blocks (^s0003-0034 to ^s0003-0172), none overlapping the 12 existing highlights.
