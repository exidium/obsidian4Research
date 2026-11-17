---
type: review
source: '[[S-0002]]'
project: 2026_demo-fluxbench
blocks: s0002-0031 to s0002-0148
proposals: 25
status: implemented
created: 2026-11-17
implemented: 2026-11-17
---

# S-0002 review: proposals for blocks ^s0002-0031 to ^s0002-0148

P-002, internal field applications engineer, about forty accounts. The first 9 minutes (blocks `^s0002-0001` to `^s0002-0030`) already carry 12 highlights, listed below; this review covers only the remaining 55 minutes. Nothing here has been created; every item is a proposal for the researcher to accept, modify, or reject by number.

## Already highlighted (not re-proposed)

| Highlight | Block |
|---|---|
| [[H-S0002-0001 Version lock forces screenshots\|H-S0002-0001]] | `^s0002-0004` |
| [[H-S0002-0002 Rebuilding designs from screenshots\|H-S0002-0002]] | `^s0002-0006` |
| [[H-S0002-0003 Second laptop as a licensing workaround\|H-S0002-0003]] | `^s0002-0008` |
| [[H-S0002-0004 Thirty days of offline grace\|H-S0002-0004]] | `^s0002-0010` |
| [[H-S0002-0005 Silent reset is the top support cause\|H-S0002-0005]] | `^s0002-0012` |
| [[H-S0002-0006 Shadow checklist of hidden defaults\|H-S0002-0006]] | `^s0002-0014` |
| [[H-S0002-0007 Docs organised by feature, not symptom\|H-S0002-0007]] | `^s0002-0016` |
| [[H-S0002-0008 Eval kit revised, model not\|H-S0002-0008]] | `^s0002-0020` |
| [[H-S0002-0009 Small discrepancies lose the careful engineers\|H-S0002-0009]] | `^s0002-0022` |
| [[H-S0002-0010 Designs should be shared like the silicon\|H-S0002-0010]] | `^s0002-0026` |
| [[H-S0002-0011 Announce changes, halve support questions\|H-S0002-0011]] | `^s0002-0028` |
| [[H-S0002-0012 Model updates change old results on reopen\|H-S0002-0012]] | `^s0002-0030` |

## Proposed project tags (status: proposed, researcher decides)

Three patterns in the new material have no fitting project tag. Each is marked `PROPOSED:` where it is used below.

| Proposed tag | Definition | Evidence (blocks) |
|---|---|---|
| `PROPOSED: tools/result-reproducibility` | A qualified design cannot reproduce its earlier numbers because model updates are one-way; customers freeze installs (VMs, old laptops) to keep a result reproducible for audits. | `^s0002-0038`, `^s0002-0040`, `^s0002-0124` |
| `PROPOSED: workflow/tool-for-shopping-only` | FluxBench is used only to pick the part and get a first schematic; the real design is done in a spreadsheet or another tool the engineer trusts to reopen. | `^s0002-0064`, `^s0002-0096` |
| `PROPOSED: workflow/no-owner-for-wrong-number` | Causes of a wrong result are split across the tool, model and eval-kit teams; no role owns the customer's experience of "the number was wrong", so the field engineer absorbs it. | `^s0002-0052`, `^s0002-0118`, `^s0002-0136` (not proposed as a highlight) |

## Proposals

### 1. Model got more honest, customer blamed the part

- **Block:** `^s0002-0034` · [00:10:04] · [[S-0002#^s0002-0034]]
- **Excerpt:**
  > They reopened it to add a second rail, and the efficiency curve had dropped about two points and the thermal estimate was warmer. Nothing in the schematic had changed. They assumed they'd fat-fingered something and spent a day comparing against a PDF export they'd luckily kept. Then they called me, and the first thing the engineer said was, 'Did your part get worse?' The part didn't get worse. The model got more honest. We'd updated the switching loss model for that family in the summer release, and the tool just applies the new model when you open an old design. There's no note, no changelog in the file, nothing.
- **Workspace tags:** `insight/pain-point`, `sentiment/negative`, `journey/design`, `market/industrial-automation`
- **Project tags:** `tools/model-version-drift`, `tools/design-history-missing`
- **Context:** [CONTEXT: Asked to walk through the last time a model update changed an old design's results. The customer was an industrial-drives account; the design had been signed off in the spring.]
- **Rationale:** A concrete case showing the mechanism behind H-S0002-0012: the customer's first hypothesis was that the silicon had degraded, and only a kept PDF let them rule out their own error, which makes this RQ3 evidence that "wrong" results are attributed to the part rather than to a silent model change.

### 2. Model-version dialog on open, with diff

- **Block:** `^s0002-0038` · [00:12:05] · [[S-0002#^s0002-0038]]
- **Excerpt:**
  > Store the model version of every part in the project file. When the file opens with newer models available, show a dialog: these four parts have updated models, here's what changed in one line each, do you want to keep the old models or update. And let me diff: old result versus new result side by side. That dialog alone would turn a day of panic into a two-minute decision. I also think the old models should stay available. Right now updating is one-way. If a customer qualified a design with the spring model and their validation report references those numbers, they need to be able to reproduce them. That's not nostalgia, that's a compliance requirement in a few of my markets.
- **Workspace tags:** `functionality/new-feature-request`, `insight/desire`, `sentiment/neutral`, `journey/design`
- **Project tags:** `tools/model-version-drift`, `tools/design-history-missing`, `PROPOSED: tools/result-reproducibility`
- **Context:** [CONTEXT: Answer to "what would you want the tool to do instead" after the case in proposal 1. In `^s0002-0130` he adds that application updates and model updates should be separable, with models updating only on the user's yes.]
- **Rationale:** The most specific feature ask in the interview, with a measurable claim ("a day of panic into a two-minute decision") and a compliance argument for keeping old models that turns a convenience into a requirement.

### 3. VM per project to freeze the tool

- **Block:** `^s0002-0040` · [00:13:07] · [[S-0002#^s0002-0040]]
- **Excerpt:**
  > A customer in medical imaging told me their quality system treats a simulation report as a controlled document. If the tool can't reproduce the report a year later, the report is worthless to their auditor. They asked me, and I'm quoting, 'How do I freeze the tool?' My answer was: keep a virtual machine with that exact version and never touch it. They actually did that. They have a VM per project now. That's a customer building their own version control because we don't ship one.
- **Workspace tags:** `functionality/workaround`, `insight/pain-point`, `sentiment/negative`, `journey/validate`, `market/digital-healthcare`
- **Project tags:** `tools/model-version-drift`, `PROPOSED: tools/result-reproducibility`
- **Context:** [CONTEXT: Asked whether the compliance angle comes up often; he names medical and functional-safety markets.]
- **Rationale:** RQ2 evidence that in regulated markets the design's life after simulation includes audits the tool cannot survive, and the VM-per-project workaround is the clearest cost signal for a model-pinning feature.

### 4. Forty percent of cases are silent resets

- **Block:** `^s0002-0042` · [00:13:59] · [[S-0002#^s0002-0042]]
- **Excerpt:**
  > Over the last twelve months I've logged between twenty-five and forty tool cases a month, average around thirty. That's just me. A case is anything from a five-minute reply to a two-day investigation. If I weigh them, roughly forty percent are the silent reset, twenty percent are license and installation, fifteen percent are model versus bench mismatch, ten percent are file compatibility, and the rest is a long tail of 'where is the button'. The silent reset ones are quick individually, maybe twenty minutes each, but there are so many of them. The license ones are the ones that eat afternoons.
- **Workspace tags:** `insight/pain-point`, `sentiment/neutral`, `journey/support`
- **Project tags:** `tools/silent-parameter-reset`, `licensing/license-lockout`, `correlation/sim-vs-bench-gap`, `sharing/file-version-lock`
- **Context:** [CONTEXT: From a personal spreadsheet he keeps "because nobody else does". In `^s0002-0046` he puts license cases at two to four hours each; in `^s0002-0102` he estimates official ticket counts at a fifth of this volume.]
- **Rationale:** The only quantified cause distribution in the study, directly answering RQ3 and giving the product team a ranking by frequency and by time cost that differ (resets by count, licensing by hours).

### 5. Read-only bench PC, dongle requested

- **Block:** `^s0002-0048` · [00:16:45] · [[S-0002#^s0002-0048]]
- **Excerpt:**
  > A customer in telecom infrastructure has a bench PC that's been in read-only mode for a month because nobody wants to carry the offline activation files through IT again. They run the real simulations on an office laptop and walk them to the bench on a USB stick. Several customers have asked me for a floating license on their own server, or a hardware dongle, which sounds old-fashioned but they'd take it. A dongle doesn't care about guest Wi-Fi. I've passed both requests on. The answer has been that the licensing platform is a company-wide system, not a tool decision. Which is true and doesn't help the engineer on the bench.
- **Workspace tags:** `insight/pain-point`, `functionality/workaround`, `functionality/new-feature-request`, `journey/validate`, `market/communications`
- **Project tags:** `licensing/license-lockout`, `licensing/offline-activation`
- **Context:** [CONTEXT: Asked whether customers hit the same lockout as he does on site. In `^s0002-0046` he describes the offline activation chain (request file, portal, response file) failing four times in five, usually from a clock drift or a docking-station fingerprint change.]
- **Rationale:** RQ2 evidence that licensing breaks the design at the bench step specifically, with two customer feature asks (floating license, dongle) and an internal blocker (licensing is company-wide) that any recommendation has to route around.

### 6. Reset is "by design", reported four times

- **Block:** `^s0002-0052` · [00:18:47] · [[S-0002#^s0002-0052]]
- **Excerpt:**
  > The silent reset I've reported, in various forms, four times over three years. The response each time has been that it's by design, because the new part may not support the old parameter range, so resetting to the new part's defaults is 'safe'. Safe for the solver, maybe. Not safe for the engineer. I understand the reasoning. I just want a message that says 'I reset these five values, here's what they were.' That's a dialog box. It's not a rewrite.
- **Workspace tags:** `insight/pain-point`, `functionality/new-feature-request`, `sentiment/negative`, `journey/support`
- **Project tags:** `tools/silent-parameter-reset`, `PROPOSED: workflow/no-owner-for-wrong-number`
- **Context:** [CONTEXT: Asked whether anything comes back from his support tickets; he estimates one in five produces a visible change within six months.]
- **Rationale:** Shows why the top RQ3 cause persists: the development team's framing of the reset as safe is a defensible solver decision that nobody has weighed against the engineer's experience, and the ask is scoped to a dialog, not a redesign.

### 7. Which part change resets which parameter

- **Block:** `^s0002-0060` · [00:22:31] · [[S-0002#^s0002-0060]]
- **Excerpt:**
  > Changing the controller IC resets the most: switching frequency, soft-start time, current limit, compensation network, and the output capacitor selection if the new part has a different recommended set. Changing the inductor resets the saturation current derating and sometimes the DCR, which is the sneaky one because the number looks plausible. Changing the output capacitor resets the ESR to a generic value instead of the datasheet value, which is why ripple is the number one giveaway. Changing the package resets ambient temperature and the thermal resistance to board. I've mapped all of this by hand. Nobody has ever published it.
- **Workspace tags:** `experience/advanced`, `sentiment/neutral`, `journey/design`
- **Project tags:** `tools/silent-parameter-reset`, `tools/hidden-defaults`
- **Context:** [CONTEXT: Asked which parameters actually reset. This is the content behind the "Before You Trust The Number" checklist (H-S0002-0006); in `^s0002-0086` he asks for an official page per topology listing exactly this.]
- **Rationale:** The complete reset map is the single most reusable piece of RQ3 evidence: it tells the product team which values a reset dialog must list and confirms the information exists only in one field engineer's head.

### 8. Engineers forgive error, not silence

- **Block:** `^s0002-0062` · [00:23:24] · [[S-0002#^s0002-0062]]
- **Excerpt:**
  > A customer in automotive lighting, a very experienced engineer, said something I wrote down: 'I don't mind a tool being wrong. I mind a tool being wrong quietly.' That's the whole problem in one sentence. Experienced engineers forgive error. They do not forgive silence. The junior ones are worse off, because they don't even know the parameter exists, so they can't form the suspicion. They just see a number and either trust it or don't, and either way they've learned nothing.
- **Workspace tags:** `insight/pain-point`, `sentiment/negative`, `journey/design`, `market/automotive`
- **Project tags:** `tools/silent-parameter-reset`
- **Context:** [CONTEXT: Asked what customers say when they discover the reset; the two most common phrases are "I didn't touch that" and "your tool lied to me".]
- **Rationale:** The sharpest RQ1 statement in the study: trust is lost on silence rather than inaccuracy, and the mechanism differs by experience level, which argues against "better models" as the fix.

### 9. Tool picks the part, spreadsheet designs

- **Block:** `^s0002-0064` · [00:24:21] · [[S-0002#^s0002-0064]]
- **Excerpt:**
  > If the tool gets one number silently wrong in front of a careful engineer, they go back to their spreadsheet, and the spreadsheet is fifteen years old and they trust it completely. I've had a customer in telecom infrastructure tell me, 'I'll use your tool to pick the part, and my spreadsheet to design the converter.' That's the outcome we don't want. We want the design done in the tool so the design stays with our parts.
- **Workspace tags:** `insight/pain-point`, `sentiment/negative`, `journey/design`, `experience/advanced`, `market/communications`
- **Project tags:** `tools/silent-parameter-reset`, `PROPOSED: workflow/tool-for-shopping-only`
- **Context:** [CONTEXT: Asked why careful engineers are the ones he most wants in the tool: they buy the kit, measure properly and push designs to production.]
- **Rationale:** Answers RQ1's "what makes them stop" with the exit path (a trusted spreadsheet) and states the business consequence the product team cares about: the design, and the part choice, leave the tool.

### 10. Half of site visits are offline by policy

- **Block:** `^s0002-0068` · [00:26:20] · [[S-0002#^s0002-0068]]
- **Excerpt:**
  > Of the forty accounts, I'd say twelve have labs where my laptop can't get out at all. Three of those are defense-adjacent, and there I'm not even allowed to bring the laptop into the room, so I work from a printout. Another ten or so have guest Wi-Fi that works but blocks the specific port the license check uses, so the tool thinks it's offline anyway. The remaining ones are fine. So roughly half my customer visits happen under conditions the tool wasn't designed for. And it's the restricted sites that have the most serious projects. The customer who air-gaps their lab is the customer who is going to ship ten thousand units.
- **Workspace tags:** `insight/pain-point`, `sentiment/neutral`, `journey/support`, `market/aerospace-defence`
- **Project tags:** `licensing/offline-activation`
- **Context:** [CONTEXT: In `^s0002-0070` he describes the defense-adjacent loop: design built at the office, printed, discussed on paper, re-run in the hotel; a five-minute iteration takes a day. In `^s0002-0074` he says the check-in interval (about forty-eight hours, three failures to read-only) is undocumented and unwarned.]
- **Rationale:** Sizes the licensing problem (half of visits) and inverts the usual priority argument: the accounts the tool serves worst are the highest-volume ones, which should change how the offline-grace ask is weighed against piracy concerns.

### 11. Checklist training halves cases, feature tour doesn't

- **Block:** `^s0002-0082` · [00:35:13] · [[S-0002#^s0002-0082]]
- **Excerpt:**
  > For accounts where I've done the checklist-based session, tool cases drop by about half, and the ones that remain are the harder ones, model mismatches and license. That's a real number from my spreadsheet, not a feeling. The feature-tour version of the session didn't move the number at all. Which tells you something: people don't need to know what the tool can do. They need to know what it does without telling them.
- **Workspace tags:** `sentiment/neutral`, `journey/support`
- **Project tags:** `docs/shadow-docs`, `tools/hidden-defaults`
- **Context:** [CONTEXT: Asked how he measures whether training worked: cases from the account three months after versus three months before. The session is forty-five minutes, nominally on the silicon, twice a month to five to ten engineers.]
- **Rationale:** Unexpected and recommendation-changing: "more training" (one of the obvious answers the study was meant to test) works only when it teaches the tool's silent behaviour, so training content, not training volume, is the lever.

### 12. The number that explains itself is believed

- **Block:** `^s0002-0092` · [00:39:43] · [[S-0002#^s0002-0092]]
- **Excerpt:**
  > What I want to hover and see is: 'default from the generic capacitor model; the datasheet value for the part you selected is this; click to apply.' That's a tooltip that does work. The one place where a tooltip is actually good is the thermal estimate, where it lists the assumptions, and that's the one number customers come to trust fastest. That's not a coincidence. The one number that explains itself is the one number people believe.
- **Workspace tags:** `insight/pain-point`, `functionality/new-feature-request`, `sentiment/negative`, `journey/design`
- **Project tags:** `tools/hidden-defaults`, `correlation/thermal-correlated`
- **Context:** [CONTEXT: Asked about in-tool help; tooltips exist for about a third of fields and mostly repeat the field name ("ESR": "equivalent series resistance").]
- **Rationale:** RQ1 evidence with a built-in positive control: the thermal estimate is the one result that states its assumptions and the one customers trust fastest, which is a testable design pattern rather than a complaint.

### 13. Competitors win on change summary and plain files

- **Block:** `^s0002-0094` · [00:40:37] · [[S-0002#^s0002-0094]]
- **Excerpt:**
  > The competing silicon vendor has a tool called Coilwright, which is honestly a bit uglier than ours but has one feature customers mention: it shows a change summary when you swap a part. A yellow box: 'the following values were updated'. That's it. That's the whole feature, and I've had customers show it to me on their screen as a way of asking why we don't do it. The other is a third-party tool called Rheostat that's vendor-neutral, slower, less pretty, but its project files are a plain text format and they've opened every version since the beginning. Engineers who've been burned by file compatibility move to it and don't come back.
- **Workspace tags:** `insight/desire`, `functionality/new-feature-request`, `sentiment/neutral`, `journey/evaluate`
- **Project tags:** `tools/silent-parameter-reset`, `sharing/file-version-lock`
- **Context:** [CONTEXT: Both competitor tools are fictional. In `^s0002-0098` he adds that FluxBench is ahead on first result time, thermal estimate, stock integration and licensing, "we win the demo and lose the design review".]
- **Rationale:** Customers are demonstrating the two missing features on competitor screens, which both validates the asks and shows the churn path (file compatibility) is one-way.

### 14. "Yours is for shopping, theirs for designing"

- **Block:** `^s0002-0096` · [00:41:34] · [[S-0002#^s0002-0096]]
- **Excerpt:**
  > Mostly both, which is the worst outcome for us, because they use our tool for the part finder and the quick first schematic, which they genuinely like, and then they rebuild the design in Rheostat for the real work, because they trust it to reopen next year. So we get the credit for the first ten minutes and they do the two months of real design somewhere we can't see. I've had a customer in industrial drives say exactly that: 'Yours is for shopping, theirs is for designing.'
- **Workspace tags:** `insight/pain-point`, `sentiment/negative`, `journey/design`, `market/industrial-automation`
- **Project tags:** `sharing/file-version-lock`, `selection/part-finder-stock`, `PROPOSED: workflow/tool-for-shopping-only`
- **Context:** [CONTEXT: Asked whether customers switch tools or use both. The part finder and first schematic are praised here; the loss is the design phase.]
- **Rationale:** RQ2's clearest answer about where the design goes after simulation (a different tool), with the qualifying evidence that the first ten minutes of FluxBench are genuinely liked, so the problem is retention, not acquisition.

### 15. Official tickets are a fifth of real cases

- **Block:** `^s0002-0102` · [00:44:08] · [[S-0002#^s0002-0102]]
- **Excerpt:**
  > Tool support measures tickets, but most of my cases never become tickets, because I resolve them by email. So the official number is maybe a fifth of the real number. The product team measures downloads and active users, which go up every quarter, so from their dashboard the tool is a success. And it is, in the sense that people open it. What's not measured is how many of those people finish a design in it. I'd love a single question in the tool: 'did this design go to a board?' Even if a third of people answered, it would be the most valuable number the product team has.
- **Workspace tags:** `insight/pain-point`, `functionality/new-feature-request`, `sentiment/neutral`, `journey/support`
- **Project tags:** none fitting (workspace tags only)
- **Context:** [CONTEXT: Asked whether anyone measures the outcomes he listed in `^s0002-0100` (tool-question share, hand rebuilds per month, first-try eval-kit matches).]
- **Rationale:** Changes how any recommendation should be received: the product team's dashboard cannot see the problem, and the proposed completion question is a cheap instrument for the study's core unknown, whether designs finish in the tool.

### 16. Cut news feed, 3D view, assistant, update nag

- **Block:** `^s0002-0104` · [00:45:01] · [[S-0002#^s0002-0104]]
- **Excerpt:**
  > The news feed on the start page. Nobody reads it and it delays the start by three seconds while it loads, which is three seconds of the customer watching me wait. The 3D board view, which looks good in the demo and I've never seen a customer use for anything. The assistant panel that pops up suggesting parts while you type, because it steals focus and it's wrong about half the time. And the update nag that appears every launch and can't be dismissed for more than a week. Every one of those was somebody's feature. None of them help the engineer finish a design. If cutting them bought the engineering time for a reset dialog, I'd cut them tomorrow.
- **Workspace tags:** `functionality/feature-removal-request`, `sentiment/negative`, `journey/design`
- **Project tags:** `tools/silent-parameter-reset`
- **Context:** [CONTEXT: Asked what he would cut. In `^s0002-0106` he qualifies the assistant: part finding is not the problem, so point the assistant at silent resets and it becomes "the best feature in the tool".]
- **Rationale:** The only explicit removal list in the study, framed as a trade for the top-priority fix, which gives the product owner a concrete reallocation to consider rather than only additions.

### 17. Shareable link: read-only, every value, comments

- **Block:** `^s0002-0108` · [00:46:54] · [[S-0002#^s0002-0108]]
- **Excerpt:**
  > A design has a link. The link opens in a browser, read-only, no install, no version. I send the link to the customer; the customer sends it to their colleague; the colleague opens it on their phone in a meeting. If they have the tool they click 'open in FluxBench' and get the full thing. If they don't, they see the schematic, the key numbers and the advanced panel values, all of them, in a list. And a comment thread, so I can say 'this value reset, change it back' on the line itself instead of describing it.
- **Workspace tags:** `functionality/new-feature-request`, `insight/desire`, `sentiment/neutral`, `journey/integrate`
- **Project tags:** `sharing/file-version-lock`, `sharing/screenshot-support`
- **Context:** [CONTEXT: Asked what "shared like silicon" (H-S0002-0010) would look like in practice. On confidentiality, `^s0002-0110`: defense-adjacent customers would keep the file; everyone else already emails screenshots, "the link is just a better screenshot".]
- **Rationale:** Turns the earlier abstract ask into a specification (read-only, phone-openable, all advanced values listed, line-level comments) and pre-empts the confidentiality objection with customer verbatims.

### 18. Conservative models shown with false precision

- **Block:** `^s0002-0112` · [00:48:48] · [[S-0002#^s0002-0112]]
- **Excerpt:**
  > But the tool presents every number with the same confidence, two decimal places, no indication. So a customer in battery storage sees eighty-nine point four percent, measures ninety-one, and concludes the tool is wrong, when actually the tool was deliberately pessimistic. If the number came with a note, 'this model is conservative by design, expect measured efficiency one to two points higher', the mismatch becomes reassurance instead of doubt. The information exists. The model team knows which models are which. It just never reaches the screen.
- **Workspace tags:** `insight/pain-point`, `functionality/new-feature-request`, `sentiment/negative`, `journey/validate`, `market/energy`
- **Project tags:** `correlation/accuracy-statement-missing`, `correlation/sim-vs-bench-gap`
- **Context:** [CONTEXT: Expanding on the third cause from `^s0002-0012`, conservative models. In `^s0002-0114` he adds he would rather the tool said "about eighty-nine to ninety-one" than "eighty-nine point four"; engineers accept ranges, not false precision.]
- **Rationale:** RQ1 and RQ3 together: a measured result better than simulated still destroys trust when the tool hides its intent, and the fix is a label the model team can already supply.

### 19. QR code loads the board's real parts

- **Block:** `^s0002-0116` · [00:50:30] · [[S-0002#^s0002-0116]]
- **Excerpt:**
  > That spreadsheet is not public. So the customer has no way to know their board differs from the model except through me. My proposal, which I've made twice, is a QR code on the board that opens the exact bill of materials and a button that says 'load this board's parts into FluxBench'. Then the simulation starts from the actual board. The one in four mismatch would go to zero overnight.
- **Workspace tags:** `functionality/new-feature-request`, `insight/pain-point`, `sentiment/neutral`, `journey/evaluate`
- **Project tags:** `correlation/kit-model-drift`
- **Context:** [CONTEXT: Asked how he tracks a customer's eval-kit revision: a tiny code under the inductor checked against a non-public kit-team spreadsheet. The "one in four" is from H-S0002-0009.]
- **Rationale:** A specific, twice-proposed fix for the third-ranked RQ3 cause, with the organisational reason it has stalled given in `^s0002-0118` (it falls between two teams).

### 20. Nobody owns "the number was wrong"

- **Block:** `^s0002-0118` · [00:51:23] · [[S-0002#^s0002-0118]]
- **Excerpt:**
  > The silent reset is a tool problem. The model version is a model team problem. The eval kit mismatch is a kit team problem. The file format is a tool problem. But the customer sees one thing: 'the number was wrong'. There's nobody whose job is 'the number was wrong'. I've sort of become that person by default, and I'm not sure that's the right place for it to live.
- **Workspace tags:** `insight/pain-point`, `sentiment/negative`, `journey/support`
- **Project tags:** `PROPOSED: workflow/no-owner-for-wrong-number`
- **Context:** [CONTEXT: Asked about the response to the QR-code proposal: "positive and slow", because no team owns it. In `^s0002-0120` he would place the owner on the tool's product team with "measured matches simulated on first try" as their metric; in `^s0002-0136` he estimates the field engineers together spend two or three full-time people on undocumented tool support.]
- **Rationale:** Reframes RQ3 from a list of causes to a structural finding: every cause has a defensible owner and the customer-facing symptom has none, which is why the FAE view of causes differs from each team's.

### 21. Serious customers build rituals around the tool

- **Block:** `^s0002-0124` · [00:54:01] · [[S-0002#^s0002-0124]]
- **Excerpt:**
  > The serious ones build rituals. One keeps a wiki page of every design with the tool version used. One exports every result to PDF immediately and treats the PDF as the truth and the tool file as scratch. One keeps a VM, as I mentioned. One has a rule that any part change requires a second engineer to review the advanced panel, which is basically my checklist as a process. These are all costs we've exported to the customer. They're paying in their own engineers' time for problems we could fix once.
- **Workspace tags:** `functionality/workaround`, `insight/pain-point`, `sentiment/negative`, `journey/design`
- **Project tags:** `sharing/pdf-review-loop`, `tools/design-history-missing`, `PROPOSED: tools/result-reproducibility`
- **Context:** [CONTEXT: Asked whether teams build processes around the tool's limitations; he says this is how he identifies serious customers, since casual users give up. In `^s0002-0122` a medical-imaging team with five engineers on four versions made one person's machine "the one that opens things".]
- **Rationale:** Four customer workarounds in one block, each a direct map to a missing feature (version record, stable export, model pinning, reset visibility), which is RQ2's strongest statement of what breaks after simulation and who pays.

### 22. First hour sells, second hour unsells

- **Block:** `^s0002-0126` · [00:54:56] · [[S-0002#^s0002-0126]]
- **Excerpt:**
  > First-time users change parts a lot because they're exploring. Every change silently resets things, so by the tenth change their design is a mix of their intentions and the tool's defaults, and they don't know which is which. Then they measure, it doesn't match, and they conclude, often permanently, that the tool is approximate. The first hour sells the tool. The second hour unsells it. And the second hour is where nobody is watching.
- **Workspace tags:** `insight/pain-point`, `experience/beginner`, `sentiment/negative`, `journey/design`
- **Project tags:** `tools/silent-parameter-reset`, `tools/hidden-defaults`
- **Context:** [CONTEXT: Asked about the first-time user's experience; he calls the first hour good: quick part finder, schematic in ten minutes, confident numbers.]
- **Rationale:** Ties RQ1's trust loss to a moment in time and a behaviour (exploratory part changes), and explains why usage metrics miss it: the loss happens after the first session and is attributed to model accuracy.

### 23. No warning is read as approval

- **Block:** `^s0002-0128` · [00:55:50] · [[S-0002#^s0002-0128]]
- **Excerpt:**
  > There's an 'advanced' label on the panel, which has the opposite effect: beginners avoid it because it says advanced, so they never see the values. There's a 'reset to defaults' button, which is funny, because the tool resets to defaults on its own anyway. And there's a warning when a parameter is out of the part's range, which is good, but it's the only warning in the tool, so people learn that no warning means everything is fine. The absence of a warning is read as approval.
- **Workspace tags:** `insight/pain-point`, `experience/beginner`, `sentiment/negative`, `journey/design`
- **Project tags:** `tools/hidden-defaults`
- **Context:** [CONTEXT: Asked whether anything in the tool tries to prevent the second-hour problem from proposal 22.]
- **Rationale:** Explains the trust mechanism in RQ1 at the interface level: the one existing warning teaches users that silence means okay, so adding a reset notice is consistent with a pattern the tool already trained.

### 24. Near miss: corrected model, marginal inductor

- **Block:** `^s0002-0132` · [00:57:41] · [[S-0002#^s0002-0132]]
- **Excerpt:**
  > They reopened the design months later for a cost-down, saw the inductor running hotter in the new simulation, and assumed it was the cost-down change. They nearly shipped the original design with a marginal inductor because the old simulation said it was fine. What saved them was an engineer who didn't trust either number and measured it. So the tool didn't cause harm, a careful engineer prevented it, but the tool did nothing to help. A note on open would have said: this part's loss model was corrected, re-check the thermal margin.
- **Workspace tags:** `insight/pain-point`, `sentiment/negative`, `journey/validate`, `market/automotive`
- **Project tags:** `tools/model-version-drift`, `correlation/sim-vs-bench-gap`
- **Context:** [CONTEXT: Asked whether a model update ever caused real harm. The automotive-lighting customer had qualified the design with a model that underestimated inductor losses. In `^s0002-0134` he explains it never became a ticket because "silently applied a corrected model" is not a defect category.]
- **Rationale:** The highest-stakes story in the interview: a corrected model nearly caused a worse outcome than the wrong one because the change was silent, which makes the on-open note a safety argument rather than a convenience.

### 25. Three hygiene fixes, reset dialog first

- **Block:** `^s0002-0138` · [01:00:26] · [[S-0002#^s0002-0138]]
- **Excerpt:**
  > The reset dialog, the model version in the file, and the thirty-day grace. Those three. Not the link, even, though I want the link. Those three would take most of the recurring cases off my desk, and what's left would be real engineering questions, which I'm happy to answer forever. The link is the next level, it changes how we work with customers. But the three are hygiene. They're the tool telling the truth about what it did. I'd put the reset dialog first because it's the cheapest and it's the one I'd notice next week.
- **Workspace tags:** `functionality/new-feature-request`, `sentiment/neutral`, `journey/support`
- **Project tags:** `tools/silent-parameter-reset`, `tools/model-version-drift`, `licensing/offline-activation`
- **Context:** [CONTEXT: Asked what would make the checklist, second laptop and spreadsheet unnecessary. In `^s0002-0140` he specifies the dialog: five values from his checklist with old and new side by side, "a dialog that lists forty values is as useless as no dialog". Magic wand in `^s0002-0144`: the tool never changes a value without saying so.]
- **Rationale:** The participant's own prioritisation of everything above, separating hygiene (three fixes) from the step change (the link), which a recommendation can adopt or argue against directly.

## Considered, not proposed

Strong moments left out to stay within range; the researcher may pull any in. `^s0002-0036` (proving drift with the never-updated laptop, release notes written for the model team), `^s0002-0044` (the twenty-minute reset case is "describing a screen in words"), `^s0002-0046` (offline activation chain fails four in five), `^s0002-0050` (tickets take eight to ten days, so he messages two developers directly), `^s0002-0054` and `^s0002-0056` (checklist contents; taped to a bench wall; eight months waiting on technical publications; version seven), `^s0002-0058` ("the checklist shouldn't exist"), `^s0002-0066` (the personal 3.4 laptop opens more files than 3.6), `^s0002-0070` (paper loop at defense sites, version 2.9), `^s0002-0072` (counting users does not need a live check-in every forty-eight hours), `^s0002-0074` (undocumented lockout timing), `^s0002-0080` (three questions every training session asks), `^s0002-0086` (four missing documents), `^s0002-0090` (portal search buries tool help; a filter would fix it), `^s0002-0098` ("we win the demo and lose the design review"), `^s0002-0100` (first-try bench match as the unmeasured revenue metric), `^s0002-0106` (point the assistant at the reset), `^s0002-0110` ("the link is just a better screenshot"), `^s0002-0114` (ranges over false precision), `^s0002-0120` (owner on the tool's product team), `^s0002-0122` (human as file-format converter), `^s0002-0130` (separate app updates from model updates), `^s0002-0134` (no ticket category for lost trust), `^s0002-0136` (two or three hidden FTEs), `^s0002-0140` (five values, not forty), `^s0002-0142` (Monday inbox), `^s0002-0144` (magic wand), `^s0002-0146` ("the customer is almost never wrong about what they saw. They're wrong about why").

## Coverage summary

**RQ1. When do engineers trust a simulated result, and what makes them stop?** Strong. Proposals 8, 9, 11, 12, 18, 22, 23, 24 (and 1). The consistent answer is that trust is lost on silence, not error: a silently reset value (8, 22, 23), a silently corrected model (1, 24), or a deliberately conservative model presented with two-decimal confidence (18). Trust is gained by the one result that states its assumptions (12), by a bench match (24, by implication), and by training that teaches silent behaviour rather than features (11). The exit path when trust is lost is a fifteen-year-old spreadsheet or a competitor (9, 13, 14).

**RQ2. Where does a design go after simulation, and what breaks on the way?** Good on sharing, versions and licensing; weak on export and production handoff. Proposals 3, 5, 10, 13, 14, 17, 21. Designs go to a VM (3), a USB stick (5), paper (10), a competitor tool for the real design (14), a PDF treated as truth (21), or a colleague who cannot open the file (21 context). P-002 says nothing about BOM export, approved-parts lists, report retyping or layout handoff (`export/*` tags unused), so RQ2 coverage for those steps must come from P-001 and P-003.

**RQ3. What do field engineers see as the top causes of "wrong" results?** Strong, and this is the participant's home ground. Proposals 1, 4, 6, 7, 18, 19, 20, 25. Causes are ranked by frequency (4: resets 40%, licensing 20%, model-vs-bench 15%, file compatibility 10%), mapped mechanically (7), and traced to an organisational root: each cause has a defensible owner and the customer-facing symptom has none (6, 20). Proposal 25 is the participant's own fix ordering.

**Weak or absent coverage.** No evidence from P-002 on `tools/simulation-crash`, `tools/no-progress-feedback`, `correlation/loss-breakdown-missing`, or any `export/*` tag; he does not report crashes or performance complaints at all, which is mild counter-evidence if either was a hypothesis. Selection (`selection/part-finder-stock`) appears only as praise (14). Nothing on pricing or the web tools, which are out of scope anyway.

**Unexpected findings.** Checklist-based training halves cases and a feature tour changes nothing (11), which undercuts "more training" as stated. Some models are conservative by design and the mismatch is in the customer's favour, yet still reads as "wrong" (18). Official ticket counts are about a fifth of real volume and the product dashboard shows success (15). Half of site visits happen under network conditions the tool was not designed for, and those are the highest-volume accounts (10). A corrected model nearly caused a worse outcome than the wrong one (24). The organisational finding that nobody owns "the number was wrong" (20) was not in the discussion guide.

**Qualifying evidence against oversimplification.** The tool is genuinely liked for the first ten minutes: part finder, first schematic, stock levels (14, 16 context, 22 context) and is ahead of the named competitor on first impression (13 context). The thermal estimate is trusted fastest because it explains itself (12), so the pattern already exists in the product. The reset "by design" reasoning is acknowledged as technically sound by the participant (6). In the near miss, the tool did not cause harm; an engineer's measurement prevented it (24). Customers themselves accept the confidentiality trade-off of a shareable link, except defense-adjacent accounts (17 context). Everything is one internal participant's account from memory and a personal spreadsheet; the case percentages (4) and the training effect (11) are self-reported and should be marked as such in any insight.

**Total: 25 proposals** from blocks `^s0002-0034` to `^s0002-0138`, plus 3 proposed project tags. Not done, per instruction: no highlight notes created, `tags.yaml` and the source untouched, no provenance line appended.
