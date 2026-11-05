# Note schema

Every note in `10 Projects/` and `90 Archive/` has a `type` property. Properties are frontmatter only. Tags use the `dimension/tag` form from `_system/taxonomy.yaml`.

## project.md

```yaml
type: project
project_id: 2026_demo-fluxbench      # equals folder name
title: FluxBench Designer onboarding study
status: active                       # planning | active | synthesizing | closed
owner: P-000                         # researcher, by ID; names stay out of git
rally_study: ""                      # Rally reference for consent and recruitment
started: 2026-10-01
methods: [method/interview]
product: [product/fluxbench-designer]
```

Body: research questions, participant table (IDs and task-based segment only), embedded Bases views for sources, pending highlights, insights.

## sources/S-####.md

```yaml
type: source
source_id: S-0001
project: 2026_demo-fluxbench
title: Interview P-001
participant: P-001
rally_id: ""                         # consent record in Rally
method: method/interview
date: 2026-10-14
duration_min: 48
language: en
origin: _raw/2026_demo-fluxbench/P-001.mp4   # local path, never committed
transcriber: mlx-whisper/large-v3-turbo      # or teams | krisp | manual
speakers_inferred: false             # true when the AI assigned speakers
redacted: true                       # names replaced with IDs, checked by scan_pii
status: ingested                     # ingested | highlighted | archived
```

Body:

```
## Summary
- five bullets, written at ingest, no interpretation

## Transcript
[00:00:12] **Interviewer:** … ^s0001-0001

[00:00:40] **P-001:** … ^s0001-0002
```

One paragraph per speaker turn (or per ~60 s for monologues). The block ID is the last token of the paragraph. **Transcript paragraphs and IDs are immutable once `status` leaves `ingested`.**

## highlights/H-S####-####.md

```yaml
type: highlight
highlight_id: H-S0001-0003
project: 2026_demo-fluxbench
source: "[[S-0001]]"
block: s0001-0014                    # block id without the caret
participant: P-001
segment: segment/designing-power-stage
quote: "verbatim sentence or two, nothing paraphrased"
tags: [behavior/troubleshoot, theme/pain, topic/accuracy]
review: proposed                     # proposed | accepted | rejected
created_by: ai                       # ai | human
model: claude-fable-5-1
skill_version: 0.1.0
created: 2026-11-05
```

Body:

```
![[S-0001#^s0001-0014]]

**Why it matters:** one sentence, the researcher's reading, not a restatement of the quote.
```

One idea per highlight. Quote is verbatim from the block. Tags: at least one `theme/` and one `behavior/` or `topic/`. Never tag interviewer speech.

## insights/I-<project>-##.md

```yaml
type: insight
insight_id: I-2026_demo-fluxbench-01
project: 2026_demo-fluxbench
title: Engineers don't trust simulation results until they match the bench
status: draft                        # draft | reviewed | published
confidence: medium                   # low = 1 participant (call it a signal), medium = 2, high = 3+
participants: [P-001, P-003]
highlights: ["[[H-S0001-0003]]", "[[H-S0003-0007]]"]
tags: [theme/trust, topic/hardware-correlation]
published_to: ""                     # Confluence URL once published
created: 2026-11-05
```

Body:

```
## Insight
Two or three sentences. A claim, not a topic.

## Evidence
![[H-S0001-0003]]
![[H-S0003-0007]]

## Implications
- for product
- for research (what we still don't know)

## Open questions
-
```

## _system/taxonomy.yaml

```yaml
dimensions:
  theme:
    description: what kind of finding this is
    required: true
    tags:
      - id: theme/pain
        definition: …
        examples: […]
        status: active            # proposed | active | deprecated
        created: 2026-11-05
        proposed_by: ai|human
        evidence: [H-S0001-0003]  # for proposed tags
        merged_into: theme/other  # for deprecated tags
```

Only `research-organize` changes `status`. Any skill may append a `proposed` tag.

## _system/provenance.log

Tab-separated, append-only: `date  skill  action  target  model`.
