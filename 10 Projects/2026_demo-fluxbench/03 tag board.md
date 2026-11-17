---
type: overview
project: 2026_demo-fluxbench
generated: 2026-11-17
---

# Tag board

Every board reads the highlight notes live. Structure generated 2026-11-17 by `python3 _system/scripts/tag_board.py 2026_demo-fluxbench`; re-run when a tag group is added.

## Tag board
Lanes are tag groups, cards are tags (with definition and counts). Click a tag to open its page with the live list of its highlights. Native Bases, no plugin.
![[10 Projects/2026_demo-fluxbench/a_setup/boards/tags.base#Tag board]]

## Highlights · one board per group
Lanes are the group's tags. Native Bases, no plugin needed. To re-tag by dragging, use the canvas. Expand a group:

> [!abstract]- Experience level · The experience level being described in the moment, not the participant's profile.
> ![[10 Projects/2026_demo-fluxbench/a_setup/boards/tag-board.base#Experience level]]
>
> - `experience/beginner` · Participant's words indicate newness to the domain or tool (learning, first encounter, unfamiliarity).
> - `experience/intermediate` · Participant's words indicate working knowledge (competent use, some years of practice).
> - `experience/advanced` · Participant's words indicate expert depth (teaches others, deep domain reasoning, edge-case fluency).

> [!abstract]- Functionality · Separates missing from broken from unnecessary. Product managers filter by this first.
> ![[10 Projects/2026_demo-fluxbench/a_setup/boards/tag-board.base#Functionality]]
>
> - `functionality/new-feature-request` · Participant explicitly asks for something that does not exist.
> - `functionality/existing-feature` · Participant references something that already exists (use to validate awareness).
> - `functionality/feature-removal-request` · Participant wants something taken away or simplified.
> - `functionality/bug` · Participant describes broken behaviour (not a gap; actually broken).
> - `functionality/workaround` · Participant describes a hack or alternative path to achieve their goal. Direct evidence of unmet need.

> [!abstract]- Insight · High-level buckets for quick scanning. Usually paired with a functionality tag.
> ![[10 Projects/2026_demo-fluxbench/a_setup/boards/tag-board.base#Insight]]
>
> - `insight/pain-point` · Any moment of frustration, friction, or failure.
> - `insight/desire` · Aspiration or wish; softer and more emotional than a feature request.

> [!abstract]- Sentiment · Enables positive vs negative counts per topic across projects.
> ![[10 Projects/2026_demo-fluxbench/a_setup/boards/tag-board.base#Sentiment]]
>
> - `sentiment/positive` · Clear satisfaction, praise, or delight expressed.
> - `sentiment/neutral` · Factual statement with no emotional charge (typical for workflow descriptions).
> - `sentiment/negative` · Frustration, disappointment, or criticism expressed.
> - `sentiment/confused` · Participant is uncertain, misunderstanding, or lost.

> [!abstract]- Research ops · Action tracking for the research team. Not for analysis; hidden from stakeholder views.
> ![[10 Projects/2026_demo-fluxbench/a_setup/boards/tag-board.base#Research ops]]
>
> - `ops/follow-up-depth` · This topic needs deeper probing in a future session.
> - `ops/follow-up-clarification` · Something was unclear; verify with the participant.
> - `ops/follow-up-referral` · Participant mentioned someone else we should talk to.

> [!abstract]- Journey stage · Where in the engineer's workflow the moment happens. UNVERIFIED LIST - confirm against the *Journey Stage board in Dovetail before relying on it.
> ![[10 Projects/2026_demo-fluxbench/a_setup/boards/tag-board.base#Journey stage]]
>
> - `journey/discover` · Finding out what exists; requirements, feasibility, first contact with a product or tool.
> - `journey/evaluate` · Comparing options, reading datasheets, trying eval boards, deciding what to adopt.
> - `journey/design` · Active design work; architecture, selection, configuration, simulation.
> - `journey/integrate` · Moving work between tools or into the production flow; exports, handoffs.
> - `journey/validate` · Testing on hardware, correlating, signing off.
> - `journey/support` · Getting help; documentation, FAEs, portals, reporting problems.

> [!abstract]- Software · Which ADI product is being discussed in the highlight. Apply on every relevant mention.
> ![[10 Projects/2026_demo-fluxbench/a_setup/boards/tag-board.base#Software]]
>
> - `software/ace` · ACE Analysis Control Evaluation platform.
> - `software/ace-dvd` · Device View Designer within ACE.
> - `software/a2b-bus-analyzer` · A2B audio bus tool.
> - `software/analog-com` · analog.com website experience.
> - `software/data-mesh` · ADI Data Mesh initiative.
> - `software/ee-sim` · EE-Sim simulation tool.
> - `software/harmonic-design-system` · Harmonic design system.
> - `software/interactive-engineering-solutions` · IES platform.
> - `software/ltpowercad` · LTpowerCAD tool.
> - `software/ltspice` · LTspice simulation tool.
> - `software/noise-tool` · Noise analysis tool.
> - `software/pdt` · Product Development Tools platform.
> - `software/fluxbench-designer` · FICTIONAL demo product; delete for real use.

> [!abstract]- Market · Which market is being discussed in the highlight, which may differ from the participant's own.
> ![[10 Projects/2026_demo-fluxbench/a_setup/boards/tag-board.base#Market]]
>
> - `market/aerospace-defence` · A&D context
> - `market/automotive` · Automotive context.
> - `market/broad-market` · General or non-specific market context.
> - `market/communications` · Comms
> - `market/consumer` · Consumer electronics context.
> - `market/data-center` · Data center or cloud infrastructure context.
> - `market/digital-healthcare` · Medical or healthcare tech context.
> - `market/energy` · Power generation
> - `market/industrial-automation` · Factory automation or IIoT context.
> - `market/instrumentation-measurement` · Test and measurement context.
> - `market/intelligent-buildings` · Smart building or BMS context.

> [!abstract]- 1. Workflow and Process
> ![[10 Projects/2026_demo-fluxbench/a_setup/boards/tag-board.base#1. Workflow and Process]]
>
> - `workflow/workflow-described` · Participant describes how they actually do a step of their work.
> - `workflow/review-loop-described` · Participant describes how a design gets reviewed and iterated with colleagues.

> [!abstract]- 2. Tool Behaviour
> ![[10 Projects/2026_demo-fluxbench/a_setup/boards/tag-board.base#2. Tool Behaviour]]
>
> - `tools/hidden-defaults` · A parameter or assumption the tool applies without showing it on the main screens.
> - `tools/silent-parameter-reset` · The tool changed a value the user had set
> - `tools/model-version-drift` · Results of an old design change because a part model was updated.
> - `tools/simulation-crash` · The application closes or fails during a run.
> - `tools/no-progress-feedback` · Long runs give no progress indication or block the interface.
> - `tools/design-history-missing` · No record inside the project of what changed and when.

> [!abstract]- 3. Simulation vs Bench
> ![[10 Projects/2026_demo-fluxbench/a_setup/boards/tag-board.base#3. Simulation vs Bench]]
>
> - `correlation/sim-vs-bench-gap` · Participant compares a simulated value with a measurement or a trusted calculation and reports a gap.
> - `correlation/kit-model-drift` · The evaluation kit's actual parts differ from the simulation model's defaults.
> - `correlation/accuracy-statement-missing` · Participant wants the vendor to state how accurate a result is meant to be.
> - `correlation/loss-breakdown-missing` · Results are aggregated in a way that blocks diagnosing which mechanism is off.
> - `correlation/thermal-correlated` · The thermal estimate matched hardware; apply to positive correlation moments.

> [!abstract]- 4. Sharing and Versions
> ![[10 Projects/2026_demo-fluxbench/a_setup/boards/tag-board.base#4. Sharing and Versions]]
>
> - `sharing/file-version-lock` · Project files cannot be opened across tool versions.
> - `sharing/screenshot-support` · Support happens via screenshots because the design itself cannot be shared.
> - `sharing/pdf-review-loop` · Design review runs on exported PDFs rather than the design.
> - `sharing/design-fork` · Two people hold divergent copies of a design with no way to tell which is current.

> [!abstract]- 5. Licensing and Offline
> ![[10 Projects/2026_demo-fluxbench/a_setup/boards/tag-board.base#5. Licensing and Offline]]
>
> - `licensing/offline-activation` · Activation or check-in needs network access the user does not have.
> - `licensing/license-lockout` · The tool locked the user out because a license check failed.

> [!abstract]- 6. Documentation and Support
> ![[10 Projects/2026_demo-fluxbench/a_setup/boards/tag-board.base#6. Documentation and Support]]
>
> - `docs/feature-vs-symptom-docs` · Documentation is organised by feature while users search by symptom.
> - `docs/shadow-docs` · Someone outside the product team wrote their own guide to compensate for the official docs.
> - `docs/no-defect-channel` · No practical way to report a bug from inside the tool.

> [!abstract]- 7. Export and Handoff
> ![[10 Projects/2026_demo-fluxbench/a_setup/boards/tag-board.base#7. Export and Handoff]]
>
> - `export/plot-data-not-exportable` · Plots export as images but the underlying numbers do not.
> - `export/report-retyping` · Numbers are retyped by hand into reports because no data export exists.
> - `export/approved-parts-mismatch` · BOM export suggests parts outside the company's approved vendor list.

> [!abstract]- 8. Part Selection
> ![[10 Projects/2026_demo-fluxbench/a_setup/boards/tag-board.base#8. Part Selection]]
>
> - `selection/part-finder-stock` · Part selection filtered by distributor stock; apply to selection moments.

## Other views
![[10 Projects/2026_demo-fluxbench/a_setup/boards/tag-board.base#By participant]]

![[10 Projects/2026_demo-fluxbench/a_setup/boards/tag-board.base#By review status]]

[[10 Projects/2026_demo-fluxbench/a_setup/boards/tag-board.canvas|tag-board.canvas]] · drag cards between lanes, then `python3 _system/scripts/canvas_sync.py 2026_demo-fluxbench`.

