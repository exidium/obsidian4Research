---
type: project
project_id: 2026_demo-fluxbench
title: 2026-10 Discovery - FluxBench Designer Trust (fictional demo)
phase: discovery
status: analysis
owner: P-000
domain: product-tools/fluxbench
rally_study: DEMO-0001
date_range: [2026-10-14, 2026-10-16]
product_space: [software/fluxbench-designer]
published_to: https://analog.atlassian.net/wiki/spaces/SDPUXR/pages/388542371
---

## Contents

1. [[10 Projects/2026_demo-fluxbench/01 project#Study overview|Study overview]]  
    1.1. [[10 Projects/2026_demo-fluxbench/01 project#Introduction|Introduction]]  
    1.2. [[10 Projects/2026_demo-fluxbench/01 project#Research questions and methodology|Research questions and methodology]]  
    1.3. [[10 Projects/2026_demo-fluxbench/01 project#Study participants|Study participants]]  
2. [[10 Projects/2026_demo-fluxbench/01 project#Findings|Findings]]  
    2.1. [[10 Projects/2026_demo-fluxbench/01 project#Reports|Reports]]  
    2.2. [[10 Projects/2026_demo-fluxbench/01 project#Insights|Insights]]  
3. [[10 Projects/2026_demo-fluxbench/01 project#Operations & data|Operations & data]]  
    3.1. [[10 Projects/2026_demo-fluxbench/02 insights review|Insights Review]]  
    3.2. [[10 Projects/2026_demo-fluxbench/03 tag board|Tag board]]  

# Study overview

> [!warning] Fictional demo project
> The product, the vendor, the participants and every quote are invented to exercise the pipeline. The recordings are text-to-speech over authored transcripts. Safe for a public repo.

## Introduction

FluxBench Designer is a desktop simulation tool for switching power stages, sold by a fictional semiconductor vendor alongside its regulator families. An engineer picks a part, enters the input range, output voltage and load current, and gets a starting schematic, component values and simulated results for ripple, efficiency, transients and temperature rise. For a growing number of new part families the simulation models exist only inside FluxBench, so the tool is becoming a required step rather than an optional one. That is the setting for a recurring complaint: engineers tell the field team that the tool is "wrong", stop using it after one bad result, or keep it only for the one output they have managed to check on the bench.

The product team asked for a discovery study before committing roadmap time to the obvious answers, which were better models or more training. The question underneath the complaint is one of trust: how an engineer decides a simulated number can be relied on, what it costs them when the tool and their own reference disagree, and what happens to a design after the simulation, when it has to be reviewed, laid out, validated and shipped by people who never open the tool. The field applications engineers see the aggregate of these failures as support load, and their view of the causes was treated as a third source of evidence rather than as an explanation to confirm.

The study covers FluxBench Designer itself, its evaluation kits and their simulation models, licensing and activation, exports and reports, and the documentation and support portal around it. It does not cover pricing, the vendor's web tools, or the accuracy of any specific model, which would need bench data rather than interviews. The audience for the findings is the FluxBench product owner, the FAE lead and the UX research sponsor, all referred to by role. No participant is named anywhere in the vault; consent is tracked in the Rally study `DEMO-0001` and participants appear only as `P-###`.

Three interviews are a small base. With this many participants an insight can reach at most the *emerging* evidence level, and the recommendations are framed as hypotheses to test in a wider study, not as decisions. There is no related project in the vault yet; a follow-up on model versioning and change notification is the natural next step, see the open questions in each insight.

## Research questions and methodology

1. When do engineers trust a simulated result, and what makes them stop?
2. Where does a design go after simulation, and what breaks on the way?
3. What do field engineers see as the top causes of "wrong" results?

Three hour-long semi-structured interviews over video call, 14 to 16 October 2026, following the [[10 Projects/2026_demo-fluxbench/a_setup/SETUP Discussion Guide|discussion guide]] in `a_setup/`. One external hardware design engineer who had just finished a first design in the tool, one internal field applications engineer who supports about forty accounts using it, and one external validation engineer whose job is to compare simulated and measured results. Each recording was transcribed, pseudonymised at ingest, and taken through review-first highlighting: the AI proposed highlights with tags and rationale, the researcher accepted or rejected each one, and only accepted highlights fed the synthesis. Evidence levels follow the vault rule: strong needs four or more participants, emerging two or three, and a single-participant pattern stays as tagged highlights without an insight.

## Study participants

| ID | Type | Role / context | Persona | Date | Status |
|---|---|---|---|---|---|
| [[20 Participants/P-001\|P-001]] | external-customer | Hardware design engineer, industrial robotics, first-time tool user | [[30 Personas/PE-01 Design engineer who trusts a result only after it matched the bench\|PE-01 Design engineer who trusts a result only after it matched the bench]] | 2026-10-14 | Complete |
| [[20 Participants/P-002\|P-002]] | internal-engineer | Field applications engineer, ~40 accounts | [[30 Personas/PE-02 Field engineer who patches the tool's gaps for forty accounts\|PE-02 Field engineer who patches the tool's gaps for forty accounts]] | 2026-10-15 | Complete |
| [[20 Participants/P-003\|P-003]] | external-customer | Validation engineer, medical devices | [[30 Personas/PE-03 Validation engineer who must prove every simulated number\|PE-03 Validation engineer who must prove every simulated number]] | 2026-10-16 | Complete |

# Findings

## Reports

| Report | Audience | Date | Where |
|---|---|---|---|
| [[10 Projects/2026_demo-fluxbench/f_deliverables/Readout - FluxBench Designer Trust\|Readout: why engineers stop trusting FluxBench Designer]] (draft v1.0) | Product owner, FAE lead, UX research sponsor | 2026-11-17 | `f_deliverables/` · [Confluence](https://analog.atlassian.net/wiki/spaces/SDPUXR/pages/388542423) |

## Insights

Engineers grant trust per result, only after it has matched the bench, and the tool gives them no other basis. Most "wrong" results trace to parameters the tool changed silently rather than to model error. Designs cannot leave the machine they were made on, so review, support, and hand-back all run on screenshots and PDFs.

![[_system/bases/insights.base]]

# Operations & data

- [[10 Projects/2026_demo-fluxbench/02 insights review|Insights Review]]: the highlights the AI proposed, waiting for a researcher to accept or reject them on the board.
- [[10 Projects/2026_demo-fluxbench/03 tag board|Tag board]]: tag groups and tags with definitions and counts, and one Kanban of highlights per tag group.
