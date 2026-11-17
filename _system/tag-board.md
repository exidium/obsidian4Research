---
type: overview
project: all
generated: 2026-11-17
---

# Tag board (all projects)

Every board reads the highlight notes live. Structure generated 2026-11-17 by `python3 _system/scripts/tag_board.py --all`; re-run when a tag group is added.

## Tag board
Lanes are tag groups, cards are tags (with definition and counts). Click a tag to open its page with the live list of its highlights. Native Bases, no plugin.
![[_system/bases/tags-all.base#Tag board]]

## Highlights · one board per group
Lanes are the group's tags. Native Bases, no plugin needed. To re-tag by dragging, use the canvas. Expand a group:

> [!abstract]- Experience level · The experience level being described in the moment, not the participant's profile.
> ![[_system/bases/highlights-all.base#Experience level]]
>
> - `experience/beginner` · Participant's words indicate newness to the domain or tool (learning, first encounter, unfamiliarity).
> - `experience/intermediate` · Participant's words indicate working knowledge (competent use, some years of practice).
> - `experience/advanced` · Participant's words indicate expert depth (teaches others, deep domain reasoning, edge-case fluency).

> [!abstract]- Functionality · Separates missing from broken from unnecessary. Product managers filter by this first.
> ![[_system/bases/highlights-all.base#Functionality]]
>
> - `functionality/new-feature-request` · Participant explicitly asks for something that does not exist.
> - `functionality/existing-feature` · Participant references something that already exists (use to validate awareness).
> - `functionality/feature-removal-request` · Participant wants something taken away or simplified.
> - `functionality/bug` · Participant describes broken behaviour (not a gap; actually broken).
> - `functionality/workaround` · Participant describes a hack or alternative path to achieve their goal. Direct evidence of unmet need.

> [!abstract]- Insight · High-level buckets for quick scanning. Usually paired with a functionality tag.
> ![[_system/bases/highlights-all.base#Insight]]
>
> - `insight/pain-point` · Any moment of frustration, friction, or failure.
> - `insight/desire` · Aspiration or wish; softer and more emotional than a feature request.

> [!abstract]- Sentiment · Enables positive vs negative counts per topic across projects.
> ![[_system/bases/highlights-all.base#Sentiment]]
>
> - `sentiment/positive` · Clear satisfaction, praise, or delight expressed.
> - `sentiment/neutral` · Factual statement with no emotional charge (typical for workflow descriptions).
> - `sentiment/negative` · Frustration, disappointment, or criticism expressed.
> - `sentiment/confused` · Participant is uncertain, misunderstanding, or lost.

> [!abstract]- Research ops · Action tracking for the research team. Not for analysis; hidden from stakeholder views.
> ![[_system/bases/highlights-all.base#Research ops]]
>
> - `ops/follow-up-depth` · This topic needs deeper probing in a future session.
> - `ops/follow-up-clarification` · Something was unclear; verify with the participant.
> - `ops/follow-up-referral` · Participant mentioned someone else we should talk to.

> [!abstract]- Journey stage · Where in the engineer's workflow the moment happens. UNVERIFIED LIST - confirm against the *Journey Stage board in Dovetail before relying on it.
> ![[_system/bases/highlights-all.base#Journey stage]]
>
> - `journey/discover` · Finding out what exists; requirements, feasibility, first contact with a product or tool.
> - `journey/evaluate` · Comparing options, reading datasheets, trying eval boards, deciding what to adopt.
> - `journey/design` · Active design work; architecture, selection, configuration, simulation.
> - `journey/integrate` · Moving work between tools or into the production flow; exports, handoffs.
> - `journey/validate` · Testing on hardware, correlating, signing off.
> - `journey/support` · Getting help; documentation, FAEs, portals, reporting problems.

> [!abstract]- Software · Which ADI product is being discussed in the highlight. Apply on every relevant mention.
> ![[_system/bases/highlights-all.base#Software]]
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
> ![[_system/bases/highlights-all.base#Market]]
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

