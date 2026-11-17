---
type: review
source: "[[S-0001]]"
project: 2026_demo-fluxbench
blocks: s0001-0031 to s0001-0149
proposals: 25
status: pending
created: 2026-11-17
---

# Review: S-0001, blocks ^s0001-0031 to ^s0001-0149

Mode 1 (propose only). P-001, external hardware design engineer, first-time FluxBench user. The first ten minutes (blocks 0001 to 0030) were highlighted in an earlier run; this review covers the remaining 55 minutes. Nothing below has been created as a highlight; approve, modify or reject by number.

## Already highlighted (blocks 0001 to 0030, not re-proposed)

| Highlight | Block |
|---|---|
| [[H-S0001-0001 Activation blocked on the lab network\|H-S0001-0001]] | ^s0001-0004 |
| [[H-S0001-0002 Stock-aware part picker beats the spreadsheet\|H-S0001-0002]] | ^s0001-0006 |
| [[H-S0001-0003 Spreadsheet wins when tool and spreadsheet disagree\|H-S0001-0003]] | ^s0001-0008 |
| [[H-S0001-0004 Part change silently reset switching frequency\|H-S0001-0004]] | ^s0001-0010 |
| [[H-S0001-0005 Lost trust because the tool didn't say what it changed\|H-S0001-0005]] | ^s0001-0012 |
| [[H-S0001-0006 Eleven-minute sweep looked like a hang\|H-S0001-0006]] | ^s0001-0014 |
| [[H-S0001-0007 BOM export ignores the approved vendor list\|H-S0001-0007]] | ^s0001-0018 |
| [[H-S0001-0008 Design review runs on PDF exports\|H-S0001-0008]] | ^s0001-0020 |
| [[H-S0001-0009 Thermal estimate matched the first prototype\|H-S0001-0009]] | ^s0001-0024 |
| [[H-S0001-0010 Trust is correlation\|H-S0001-0010]] | ^s0001-0026 |
| [[H-S0001-0011 No design history in the project file\|H-S0001-0011]] | ^s0001-0028 |

## Proposals

### 1. Reviewer wants both numbers side by side

- **Block:** `^s0001-0038` · [00:13:27]
- **Excerpt:**
> What he asked for, which I thought was fair, was both numbers side by side in the document with a note on why they differ. I couldn't write the note, because at that point I didn't know why. That was an uncomfortable review.
- **Workspace tags:** `insight/pain-point`, `sentiment/negative`, `journey/integrate`
- **Project tags:** `workflow/review-loop-described`, `correlation/sim-vs-bench-gap`
- **Context:** [CONTEXT: The lead reviews PDF exports and asked whether the ripple figure came from the tool or the spreadsheet; the two disagreed by about thirty percent (block 0008), which was only traced to the silent frequency reset at the following review (block 0010).]
- **Rationale:** Shows that a sim-vs-reference gap is not a private doubt but a review artefact the engineer must explain, so an unexplained discrepancy costs a review round, not just an hour.

### 2. Sign-off is on the document, not the design

- **Block:** `^s0001-0040` · [00:14:30]
- **Excerpt:**
> He's not re-running anything. He can't, he doesn't have the tool. So the sign-off is on the document, not on the design file. Which means if I export the wrong revision, or I change a value after exporting and forget to re-export, the thing he signed isn't the thing that goes to layout. That has happened.
- **Workspace tags:** `insight/pain-point`, `sentiment/neutral`, `journey/integrate`
- **Project tags:** `sharing/pdf-review-loop`, `workflow/review-loop-described`, `PROPOSED: sharing/reviewer-viewer-missing`
- **Context:** [CONTEXT: Gated process described in block 0034: a preliminary design review before layout and a critical design review before fab, a six-page document with FluxBench plots pasted as images, three reviewers commenting in a review system, the lead mandatory.]
- **Rationale:** Names the structural risk of the PDF loop (the signed object and the built object can diverge) and the cause, a reviewer with no way to open the design.

### 3. Revision stamp and a read-only reviewer view

- **Block:** `^s0001-0044` · [00:16:27]
- **Excerpt:**
> At minimum a timestamp and the project file name on every page. Better would be a version number that increments each time I save. Best would be, and I know this is asking a lot, a way for the reviewer to open a read-only view of the actual design without needing a full license. Then the sign-off would be on the design, not on a picture of the design.
- **Workspace tags:** `functionality/new-feature-request`, `insight/desire`, `sentiment/neutral`, `journey/integrate`
- **Project tags:** `sharing/pdf-review-loop`, `PROPOSED: export/revision-stamp-missing`, `PROPOSED: sharing/reviewer-viewer-missing`
- **Context:** [CONTEXT: Prompted by a prior-project audit finding (block 0042): a review passed on stale plots after a late compensation change, and P-001 had to write the explanation. FluxBench PDFs carry no revision stamp, date or hash, which he says makes him "more paranoid, not less".]
- **Rationale:** A tiered, concrete ask (stamp, version, viewer) that directly addresses the divergence risk in proposal 2 and recurs in the wish list and the seat discussion.

### 4. Schematic retyped into CAD by hand

- **Block:** `^s0001-0046` · [00:17:21]
- **Excerpt:**
> That re-drawing step is where errors creep in. FluxBench shows me a schematic, I look at it, I type the same thing into the CAD tool. Twelve components, maybe twenty nets. I've done it wrong once already on this board, swapped the feedback divider values, top and bottom. Caught it in the review, luckily. There's supposedly a netlist export. I tried it, and it came out in a format our CAD tool didn't recognise, so I gave up after half an hour and went back to typing.
- **Workspace tags:** `insight/pain-point`, `functionality/workaround`, `sentiment/negative`, `journey/integrate`
- **Project tags:** `PROPOSED: export/handoff-as-picture`
- **Context:** [CONTEXT: Block 0048: the netlist is a generic text format, none of the two or three offered match their mainstream CAD tool, and a forum converter script failed on the first line. The layout engineer receives the hand-drawn CAD schematic either way.]
- **Rationale:** The first concrete defect caused by the handoff (a swapped divider) and evidence that the existing netlist export does not reach the tools customers use.

### 5. Thermal within three degrees, the only agreeing table

- **Block:** `^s0001-0052` · [00:20:09]
- **Excerpt:**
> The camera said 71 degrees on the FET case, the tool had predicted 68 at the junction with the copper area we'd agreed. Case and junction aren't the same thing, so if anything it's closer than it looks. The inductor was 54 measured against 51 predicted. That's within what I'd expect from the thermal camera alone. So I put the two numbers in the review document in a little table, predicted and measured, and my lead said, well, that's useful. From him that's high praise. It's the only table in the document where the two columns agree.
- **Workspace tags:** `functionality/existing-feature`, `sentiment/positive`, `journey/validate`
- **Project tags:** `correlation/thermal-correlated`
- **Context:** [CONTEXT: Block 0050: the copper-area field gave the designer and the layout engineer a shared number to negotiate before layout (400 square millimetres under the FET), a conversation that normally happens after the prototype gets hot. Measurement: thermocouple and thermal camera, 6 A continuous, 25 degC ambient, twenty minutes to settle.]
- **Rationale:** Puts numbers on the one trusted result and shows how a correlated figure converts a sceptical reviewer, the positive case against which the ripple failure should be read.

### 6. Everything leaves the tool as a picture

- **Block:** `^s0001-0054` · [00:21:06]
- **Excerpt:**
> But it's inside the tool, so I took a screenshot and sent it to her, and she pinned it on her second monitor. She said if it could come out as a drawing she could import, even a DXF of the recommended footprint cluster, she'd use it as a starting point. Instead she redraws it. Same story as my schematic. Everything that leaves the tool leaves as a picture, and every picture gets redrawn by a human on the other side.
- **Workspace tags:** `insight/pain-point`, `functionality/new-feature-request`, `sentiment/negative`, `journey/integrate`
- **Project tags:** `PROPOSED: export/handoff-as-picture`
- **Context:** [CONTEXT: "It" is the tool's layout-guidance panel (recommended placement, hot loop, input-cap position). Block 0056 gives the firmware case: the power-good delay reached code as a constant via a screenshot marked up by hand and a chat message.]
- **Rationale:** Generalises the handoff problem across three downstream roles (layout, firmware, review) in the participant's own words, with a specific format ask from the layout engineer.

### 7. One-page results table built by hand

- **Block:** `^s0001-0058` · [00:23:02]
- **Excerpt:**
> What would help is if I could export a little summary table. Start-up time, power-good delay, overcurrent behaviour, output ripple, efficiency at three load points. One page. Numbers, not plots. I could paste that into the interface control document and everyone would reference it. Right now I build that table by hand in a spreadsheet, going back and forth between the tool and the sheet, reading off cursors. It takes an hour and it's the kind of hour where you make a transcription error and don't find out for a month.
- **Workspace tags:** `functionality/new-feature-request`, `insight/pain-point`, `sentiment/negative`, `journey/integrate`
- **Project tags:** `export/report-retyping`
- **Context:** [CONTEXT: Asked whether the firmware team should read the tool's output directly; P-001 says they "want a number and a reason to believe it", not a simulation tool.]
- **Rationale:** A scoped, low-effort export that would replace an hour of error-prone retyping per design and serve the interface control document that other teams actually read.

### 8. Six people watched the sweep hang

- **Block:** `^s0001-0060` · [00:24:00]
- **Excerpt:**
> Eleven minutes, UI frozen, six people watching a window that says not responding. After three minutes somebody asked if it had crashed. After five the lead said, send me the PDF, and we moved on. So the one time the tool had an audience, the audience saw it hang. I haven't opened it in a meeting since.
- **Workspace tags:** `insight/pain-point`, `sentiment/negative`, `journey/integrate`
- **Project tags:** `tools/no-progress-feedback`, `sharing/pdf-review-loop`
- **Context:** [CONTEXT: The lead had asked for the efficiency curve live in a review call to skip another PDF round. The failure pushed P-001 back to pre-running everything and bringing pictures, "exactly the workflow I was trying to get away from".]
- **Rationale:** The blocking sweep (already highlighted at block 0014) is shown here damaging the tool's reputation with five other people and killing the one attempt to review the live design instead of exports.

### 9. Internal gotchas wiki beats vendor docs

- **Block:** `^s0001-0064` · [00:25:55]
- **Excerpt:**
> He'd actually written it in our internal wiki, a page called FluxBench gotchas, which I didn't know existed until he told me. It's got about eight items on it now. The frequency thing, the fact that the efficiency sweep locks the UI, a thing about the inductor library not having DCR for some parts so the loss comes out optimistic. That wiki page is more useful to me than the vendor's documentation, which is a bit of an indictment. It's also a page the vendor will never see.
- **Workspace tags:** `functionality/workaround`, `insight/pain-point`, `sentiment/negative`, `journey/support`
- **Project tags:** `docs/shadow-docs`, `docs/feature-vs-symptom-docs`
- **Context:** [CONTEXT: Block 0062: the vendor's user guide is organised by screen and its simulation-settings section does not say which parameters reset on a part change; P-001 looked specifically. Block 0136: the gotchas page will be the first thing the next three designers in the group receive, before they open the tool.]
- **Rationale:** A customer-side shadow document is both the real manual and an inventory of hidden behaviours (including a previously unmentioned one, missing inductor DCR), and the vendor has no visibility of it.

### 10. Vendor forum: known for two years, by design

- **Block:** `^s0001-0066` · [00:26:50]
- **Excerpt:**
> One of the threads had a reply from someone with a vendor badge saying it's by design, the frequency defaults to the part's recommended value when the part changes, and that's it. No follow-up, no note in the docs, no banner added. So it's a known thing, they've known for two years, and they've decided it's correct. Maybe it is correct. But three threads and a wiki page at one customer suggests that correct and clear aren't the same, and they're only measuring one of them.
- **Workspace tags:** `insight/pain-point`, `sentiment/negative`, `journey/support`
- **Project tags:** `tools/silent-parameter-reset`
- **Context:** [CONTEXT: Searched the vendor forum for "frequency reset" from his desk machine: three threads over two years, one reporting the same roughly thirty percent ripple discrepancy.]
- **Rationale:** Counter-evidence to the hypothesis that the top cause of "wrong" results is unknown to the vendor; the behaviour is documented in public threads and classified as correct, which reframes the fix as communication, not modelling.

### 11. Offline activation is enterprise-only

- **Block:** `^s0001-0072` · [00:29:16]
- **Excerpt:**
> The response came back in about a day and a half, which is fine, and it was a polite note saying activation requires internet access and suggesting I talk to my IT department about allowing the domain. Which is not an answer, it's a redirection. Our IT department does not open outbound ports because a software vendor would prefer it. I wrote back asking whether there was a file-based activation, like some other tools have, and the second response said that was available for enterprise licenses. We don't have an enterprise license. We have two seats.
- **Workspace tags:** `insight/pain-point`, `sentiment/negative`, `journey/support`
- **Project tags:** `licensing/offline-activation`
- **Context:** [CONTEXT: The only support ticket P-001 has raised. Block 0074: he reads the first reply as a template that did not engage with "lab network blocks outbound". Block 0076: a good reply would have offered a thirty-day activation file; for technical tickets he could not send the project file without a week-long approval and wants a scrubbed settings-only export.]
- **Rationale:** Reveals that a file-based activation exists but is gated by licence tier, so the lab-network pain already highlighted (block 0004) is a packaging decision, not a technical limit.

### 12. Never reported: the feedback channel is a nod

- **Block:** `^s0001-0078` · [00:32:03]
- **Excerpt:**
> Partly because by the time I understood it, I'd solved it, and reporting something you've solved feels like homework. Partly because the first support experience didn't suggest the report would land anywhere. And partly because I didn't know if it was a bug or a design choice. If it's a design choice I'd just be complaining. My colleague said he'd mentioned it to one of their field engineers at a trade show, and the field engineer nodded and wrote something down. Whether that went anywhere, no idea. That's the extent of our feedback channel. Nodding at a trade show.
- **Workspace tags:** `insight/pain-point`, `sentiment/negative`, `journey/support`
- **Project tags:** `docs/no-defect-channel`
- **Context:** [Q: Did you ever report the frequency reset issue to the vendor?] [CONTEXT: Block 0108: the in-tool feature request button opens the portal the lab network blocks, and replies from other vendors nine months later "trains you not to bother".]
- **Rationale:** Explains why the field team's view of causes may be incomplete: the engineer who hit the top issue never reported it, for three stated reasons the product team can act on.

### 13. Competitor shows a keep-or-reset dialogue

- **Block:** `^s0001-0080` · [00:32:58]
- **Excerpt:**
> It's a heavier tool. The install was bigger, the licensing was server based, and the simulation was slower, but it never hid anything from me. Every parameter was on one long settings page and when you changed a part it put up a dialogue saying these values will change, keep or reset, with a list. Which is exactly the thing I wanted FluxBench to do.
- **Workspace tags:** `insight/desire`, `sentiment/neutral`, `journey/evaluate`
- **Project tags:** `tools/silent-parameter-reset`, `PROPOSED: competition/competitor-benchmark`
- **Context:** [CONTEXT: A trial of Ampergy Workbench (fictional competitor) about a year earlier, not bought on price. Block 0082: FluxBench wins on the part picker ("the best I've used") and on day-one thermal set-up, loses on transparency; "If I could bolt Ampergy's settings dialogue onto FluxBench I'd be happy."]
- **Rationale:** Gives the product team a concrete interaction pattern the participant has seen work, and sets the expectation against which FluxBench's silent reset is judged.

### 14. Forty-point sweep default, twelve is enough

- **Block:** `^s0001-0088` · [00:36:44]
- **Excerpt:**
> I only found that number because I went digging in the advanced panel for the frequency thing and saw a field called sweep resolution. Forty. Nobody needs forty points on an efficiency curve, you need maybe ten. I set it to twelve and the sweep came down to about three and a half minutes. Still locks the UI, but three minutes is a coffee, eleven minutes is a meeting. So there's a workaround, and it's another sticky note. It's also another default that cost me time before I knew it existed. Same pattern as the frequency. The tool had a sensible knob, hidden, set to a value that hurts.
- **Workspace tags:** `functionality/workaround`, `insight/pain-point`, `sentiment/negative`, `journey/design`
- **Project tags:** `tools/hidden-defaults`, `tools/no-progress-feedback`
- **Context:** [CONTEXT: Block 0090: twelve points gave peak efficiency within a tenth of a percent and the same curve shape; the forty-point curve had a light-load wobble he thinks was numerical. The first run was killed at nine minutes, so the first attempt actually cost about twenty minutes.]
- **Rationale:** A second hidden default with a measured cost (eleven minutes to three and a half) and no accuracy penalty, which makes the eleven-minute sweep a default-setting problem before it is a performance problem.

### 15. Node lock keeps the tool off the lab bench

- **Block:** `^s0001-0094` · [00:39:37]
- **Excerpt:**
> Then I wanted to run it on the lab machine, next to the bench, where the scope is, because when you're correlating simulation against hardware you want them side by side. Couldn't. The second seat we have is assigned to my colleague. So I asked support, same ticket thread actually, whether I could move the license to the lab machine, and the answer was yes, deactivate on one and activate on the other, but the deactivation also needs the internet. So the lab machine can never have it.
- **Workspace tags:** `insight/pain-point`, `sentiment/negative`, `journey/validate`
- **Project tags:** `licensing/offline-activation`, `PROPOSED: licensing/node-locked-seat`
- **Context:** [CONTEXT: Block 0096: the thirty-day check-in is now a calendar entry, since the lab is a ten-minute walk in another building. Block 0118: the colleague's seat sat idle for six weeks and could not be borrowed; purchasing would prefer a floating licence like their CAD tool. Block 0098: "Every design decision that assumes connectivity is a decision against that person."]
- **Rationale:** Licensing blocks the exact activity the study is about, correlating simulation against hardware, by keeping the tool away from the scope.

### 16. Home-made lookup table covers seventy percent of the BOM

- **Block:** `^s0001-0104` · [00:44:33]
- **Excerpt:**
> I built a lookup table. In the spreadsheet, naturally. It maps the tool's suggested part numbers to our approved equivalents, by value and voltage and package. So now I export the CSV, paste it into the sheet, and a formula fills in our part number where it has a match. It's about seventy percent coverage. The other thirty percent are parts I haven't seen before, which I look up by hand and then add to the table. So it's getting faster. But this is me building the feature the tool should have. If the tool let me import a preferred parts list, even just a CSV with their number and my number, it would do this itself. I'd happily give them my lookup table as a starting point.
- **Workspace tags:** `functionality/workaround`, `functionality/new-feature-request`, `insight/pain-point`, `sentiment/neutral`, `journey/integrate`
- **Project tags:** `export/approved-parts-mismatch`
- **Context:** [CONTEXT: Blocks 0100 and 0102: half an hour of part-number search and replace per revision, four revisions so far; each revision cycle (change, re-run, export PDFs, paste, export BOM, fix BOM) is about an hour "of which the thinking was ten minutes".]
- **Rationale:** Quantifies the workaround for the approved-vendor gap already highlighted (block 0018) and specifies the minimum feature (a two-column CSV import) that would retire it.

### 17. Raw plot data to overlay with the scope

- **Block:** `^s0001-0106` · [00:45:34]
- **Excerpt:**
> If I could export the load step as a CSV of time and voltage, I'd plot it myself in the same style as our bench captures, and then the correlation would be on the same axes, same colours, same cursors. That's how you build trust in a review. You put the simulation and the measurement on one graph and people see them overlap. Right now I'm comparing a raster image from the tool with a screenshot from the scope and saying, trust me, those are the same. They look similar. Similar isn't a number.
- **Workspace tags:** `functionality/new-feature-request`, `insight/desire`, `sentiment/neutral`, `journey/validate`
- **Project tags:** `export/plot-data-not-exportable`, `correlation/sim-vs-bench-gap`
- **Context:** [CONTEXT: Plot exports are raster and go fuzzy on a large screen (block 0100). Block 0108: this sits on the internal gotchas wiki as a wish; it has never been asked of the vendor.]
- **Rationale:** Ties plot-data export directly to trust building in review (RQ1 and RQ2), not just convenience, and explains why image exports cannot close a correlation argument.

### 18. Trust fixes would double the seats

- **Block:** `^s0001-0120` · [00:52:02]
- **Excerpt:**
> Yes, and I'd argue for more seats. Specifically if my lead could review inside the tool, if the export carried a revision, and if it stopped changing things silently. With those three, I'd stop using the spreadsheet for new designs and I'd want the layout engineer to have a seat for the thermal side. That's four seats instead of two. So the fixes I'm asking for would roughly double what we pay them. I don't know if they've done that arithmetic. The features that build trust are the features that sell seats, because the people who don't trust it won't buy another one.
- **Workspace tags:** `insight/desire`, `sentiment/neutral`, `journey/evaluate`
- **Project tags:** `tools/silent-parameter-reset`, `PROPOSED: sharing/reviewer-viewer-missing`, `PROPOSED: export/revision-stamp-missing`
- **Context:** [Q: If the issues you've described were fixed, would it be worth more to you?] [CONTEXT: Block 0116: seats cost roughly two and a half thousand a year each, subsidised by the regulator vendor; today he would rather have one Ampergy seat than two FluxBench seats, "a trust question dressed up as a price question". Pricing is outside the study scope; the moment is kept for the trust-to-adoption link.]
- **Rationale:** Converts the trust problem into a business case the product owner can use: the three named fixes are the ones this customer says would expand the deployment.

### 19. Lost hours are invisible to the manager

- **Block:** `^s0001-0122` · [00:52:51]
- **Excerpt:**
> When I told him about the frequency thing he said, well, did the board work, and I said yes, and he said then what's the problem. Which from where he sits is fair. The board worked, the prototype matched thermally, we're on schedule. The hour I lost is invisible to him. The two hours of BOM editing are invisible. The walk to the desk machine every thirty days will be invisible. None of it shows up anywhere except in my own sense that the tool is fighting me. That's hard to put in a budget request.
- **Workspace tags:** `insight/pain-point`, `sentiment/negative`, `journey/evaluate`, `ops/follow-up-depth`
- **Project tags:** none fitting; leave with workspace tags
- **Context:** [CONTEXT: The manager bought the seats for the subsidy and the part models and does not use the tool.]
- **Rationale:** Unexpected finding: the friction the study is chasing does not surface in any metric the buyer sees, which explains why "the tool is wrong" reaches the field team as complaints rather than as churn; worth probing in a wider study.

### 20. Top five wishes, what-changed panel first

- **Block:** `^s0001-0124` · [00:53:47]
- **Excerpt:**
> One, a what changed panel. Any time the tool alters a value I didn't type, show me, with the old and new. Two, a preferred parts list I can import so the BOM comes out in our part numbers. Three, raw data export from every plot, CSV, time and value. Four, a revision stamp on every export, and ideally a version history inside the project file so I can see what I changed three weeks ago. Five, let me do something while the efficiency sweep runs, or at least show me a progress bar so I don't kill it. That's five. If I get a sixth, offline activation. If I get a seventh, a free viewer for reviewers.
- **Workspace tags:** `functionality/new-feature-request`, `insight/desire`, `sentiment/neutral`, `journey/design`
- **Project tags:** `tools/silent-parameter-reset`, `export/approved-parts-mismatch`, `export/plot-data-not-exportable`, `tools/design-history-missing`, `tools/no-progress-feedback`, `licensing/offline-activation`, `PROPOSED: export/revision-stamp-missing`, `PROPOSED: sharing/reviewer-viewer-missing`
- **Context:** [Q: Five things, in order.] [CONTEXT: Block 0126 continues to thirteen: cursor readouts printed on exported plots, a one-page summary table, a netlist format their CAD reads, DCR for every inductor or a flag where it is missing, tooltips that say more than the field name.]
- **Rationale:** The participant's own ranked backlog, which lets the team check its roadmap against a customer ordering rather than against the loudest single complaint.

### 21. One missing banner broke trust

- **Block:** `^s0001-0128` · [00:55:40]
- **Excerpt:**
> The what changed panel. Without question. Because that's the one that broke trust, and trust is the thing that decides whether I open the tool first or the spreadsheet first. Everything else is time. Time I can budget for. Trust I can't. If I'd seen a banner on day one saying frequency reset to 400 kilohertz, I'd never have had the thirty percent discrepancy, I'd never have spent the hour, and I'd probably have believed the ripple number the same way I believe the thermal one. One banner. The whole arc of my relationship with this tool turns on one banner they didn't put in.
- **Workspace tags:** `insight/pain-point`, `functionality/new-feature-request`, `sentiment/negative`, `journey/design`
- **Project tags:** `tools/silent-parameter-reset`
- **Context:** [Q: Of all those, which one would change your behaviour the most?] [CONTEXT: Block 0146, the magic-wand answer, says the same thing more broadly: "It tells me what it's doing", with every other complaint listed as downstream of that.]
- **Rationale:** The clearest statement of the study's central mechanism: trust, not time, decides which tool opens first, and one disclosure would have changed the outcome.

### 22. Trust does not generalise across results

- **Block:** `^s0001-0130` · [00:56:35]
- **Excerpt:**
> That's the thing I've noticed about trust with these tools, it doesn't generalise. The thermal matched, so I trust the thermal. The ripple didn't match, so I don't trust the ripple, and I'm also a bit suspicious of the efficiency number because I haven't checked it, and the start-up number I only half believe because I checked it on the scope once and it was close-ish. Each result earns its own trust separately. A tool that understood that would make it easy to check each result against hardware. Instead it presents everything with the same confidence, which is a confidence I don't share.
- **Workspace tags:** `insight/pain-point`, `sentiment/neutral`, `journey/validate`, `experience/advanced`
- **Project tags:** `PROPOSED: correlation/trust-per-result`
- **Context:** [Q: Would the thermal result alone have kept you using it?] [CONTEXT: Block 0112: he wants a field to attach a measured value to each simulated one ("measured 290 millivolts, simulated 340"). Block 0134: trust has drifted up through familiarity with his checklist, "a weaker kind than trust by correlation"; the tool itself has not become more trustworthy.]
- **Rationale:** Directly answers RQ1 with a model of trust that is per-result and bench-earned, and names the UI mismatch (uniform confidence) that a correlation-aware design could fix.

### 23. Defensive use with a seven-item checklist

- **Block:** `^s0001-0132` · [00:57:31]
- **Excerpt:**
> I open the spreadsheet first and get a rough design. Then I open FluxBench, pick the part, enter the same values, and immediately go to the advanced panel and check every field against what I meant. I've got a checklist for that, seven items, on a sticky note on the monitor. Then I run the load step and the thermal. I skip the efficiency sweep unless I'm choosing between parts, and when I do run it, twelve points. Then I export and fight the BOM. So I use it, but I use it defensively. I treat it like a colleague who's smart but doesn't tell you when they've changed the plan.
- **Workspace tags:** `functionality/workaround`, `sentiment/neutral`, `journey/design`
- **Project tags:** `tools/hidden-defaults`, `workflow/workflow-described`
- **Context:** [CONTEXT: The settled pattern after about five weeks of use. Block 0092: the tool is "actually pleasant" for a quick what-if (a 5 V sensor rail, buck versus linear, fifteen minutes, thermal only), "when you don't need to trust it very far".]
- **Rationale:** The actual day-to-day workflow of a retained user: spreadsheet first, tool second, every hidden field checked by hand, which shows what the tool has become in practice rather than what it was designed to be.

### 24. Spreadsheet trusted by habit, not rigour

- **Block:** `^s0001-0142` · [01:02:09]
- **Excerpt:**
> The real version is that both of them gave me numbers, neither of them told me their assumptions, and I believed the one I'd shipped with. That's not rigour, that's habit. The difference is I know what's in the spreadsheet because I wrote it, and I don't know what's in the tool because they didn't tell me. Fix the second thing and the spreadsheet loses most of its advantage. I don't love that conclusion, but there it is.
- **Workspace tags:** `sentiment/neutral`, `journey/validate`, `experience/advanced`
- **Project tags:** `tools/hidden-defaults`
- **Context:** [CONTEXT: Blocks 0138 and 0140: he has never checked the spreadsheet's ripple against the scope either and plans to check both on the next revision; "The tool might have been right all along, with the wrong frequency."]
- **Rationale:** Qualifying evidence against a simple "tool wrong, spreadsheet right" reading: the reference itself is unverified, and the participant locates the tool's disadvantage in disclosed assumptions, not accuracy.

### 25. Tool ignores derating rules

- **Block:** `^s0001-0144` · [01:03:05]
- **Excerpt:**
> Two, the tool doesn't know about derating. Our internal rules say a capacitor runs at no more than eighty percent of rated voltage, and the tool happily suggests a 16 volt cap on a 12 volt rail, which is seventy five percent, fine, but on the 48 volt side it suggested a 50 volt part. That fails our rule and I only caught it because I've been bitten before. A derating setting would be another thing on the wish list.
- **Workspace tags:** `functionality/new-feature-request`, `insight/pain-point`, `sentiment/negative`, `journey/design`
- **Project tags:** none fitting; leave with workspace tags (single passage, no pattern yet)
- **Context:** [Q: Anything we haven't covered?] [CONTEXT: The same block also notes the project file is a single binary blob that cannot be diffed or kept usefully in git, a pattern already covered by `tools/design-history-missing` (H-S0001-0011).]
- **Rationale:** A new class of "wrong" suggestion, a component that violates a customer design rule, caught only by experience; it was not in the earlier highlights or in the FAE causes list and could change the part-suggestion recommendation.

## Proposed project tags (for the researcher to decide)

Not created. Each has evidence in two or more blocks of this transcript.

| Proposed tag | Group | Definition | Evidence blocks |
|---|---|---|---|
| `export/revision-stamp-missing` | 7. Export and Handoff | Exports carry no timestamp, version or hash, so a reviewed PDF cannot be tied to a design state. | 0042, 0044, 0120, 0124 |
| `export/handoff-as-picture` | 7. Export and Handoff | Schematic, layout guidance or waveforms leave the tool only as an image or a hand-typed copy, and the recipient redraws them. | 0046, 0054, 0056 |
| `sharing/reviewer-viewer-missing` | 4. Sharing and Versions | A reviewer without a licence has no way to open the design, so sign-off happens on a picture of it. | 0040, 0044, 0118, 0120, 0124 |
| `licensing/node-locked-seat` | 5. Licensing and Offline | A node-locked licence cannot follow the engineer between desk and lab, or be lent while idle. | 0094, 0118 |
| `correlation/trust-per-result` | 3. Simulation vs Bench | Trust earned by one result does not transfer to other results from the same tool. | 0130, 0134, 0138 |
| `competition/competitor-benchmark` | 9. Competition (new group) | Participant compares the tool with a named competitor on a specific behaviour. | 0080, 0082, 0084, 0116 |

## Coverage summary

**RQ1. When do engineers trust a simulated result, and what makes them stop?** Strong coverage. Proposals 5, 21, 22, 23 and 24 give the mechanism (per-result trust, earned on the bench, lost on an undisclosed change), 1 and 17 show how trust is argued in review, 13 and 14 show the hidden-default pattern that erodes it. New since the first ten minutes: trust does not spread from one result to another (22), familiarity is a weaker substitute for correlation (22 context), and the reference the participant trusts is itself unverified (24).

**RQ2. Where does a design go after simulation, and what breaks on the way?** Strong coverage, the richest part of the new material. Review: 1, 2, 3, 8. Layout and CAD: 4, 6. Firmware and documents: 7. Purchasing: 16. Validation bench: 15, 17. Every path out of the tool is a picture or a retyped number (4, 6, 7), the signed artefact can diverge from the built one (2, 3), and the one live review attempt failed (8).

**RQ3. What do field engineers see as the top causes of "wrong" results?** Weak and indirect, as expected from a customer rather than an FAE. Relevant from this side: the vendor has classified the top cause as "by design" for two years (10), the customer never reported it and explains why (12), the customer-side gotchas list is an inventory of causes the vendor cannot see (9), and a new cause class, suggestions that violate customer derating rules (25). Cross-check against S-0002.

**Unexpected findings.** The silent reset is known and accepted by the vendor (10). File-based activation exists but is enterprise-only (11). The three trust fixes would, by this customer's account, double the seat count (18), while the cost of the friction is invisible to the buyer (19). A second hidden default (sweep resolution 40) triples run time with no accuracy gain (14). Derating is not modelled (25). A competitor already shows the keep-or-reset dialogue the participant wants (13).

**Qualifying evidence.** The thermal estimate is accurate to a few degrees and was called "useful" by a sceptical lead (5); the part picker is "the best I've used" (13 context); the tool is pleasant for low-stakes what-ifs (23 context); the participant admits the spreadsheet is trusted by habit and may be the wrong one (24); non-reporting is "partly on me" (12 context); trust has drifted slightly upward with familiarity (22 context). Pricing (18 context) is outside study scope and is kept only for the trust-to-adoption link.

**Not proposed, available if wanted.** 0036 (undershoot value not printed on the exported plot), 0056 (firmware constant via screenshot, used as context for 6), 0076 (scrubbed settings-only export for support tickets, context for 11), 0098 (connectivity assumptions), 0114 (tooltips repeat the field name; starting schematic praised for juniors), 0136 (gotchas page shapes the next users' first impression), 0146 (magic wand), 0148 (closing praise for the part picker).

**Total: 25 proposals** from blocks 0031 to 0149. Tag distribution and verification are in the run report.
