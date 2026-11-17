---
type: highlight
highlight_id: H-S0003-0024
aliases: [H-S0003-0024]
title: Archived installers are the only way to reproduce a number
project: 2026_demo-fluxbench
source: '[[S-0003]]'
block: s0003-0094
participant: P-003
quote: 'If quality asks me to reproduce a result from a report, I need the tool version on page one of that report, not the one on my laptop. We had a case: re-ran a thermal from a report that was eight months old, got four degrees different, and it took a day to work out it was a model update, not the board, not the chamber. Now the version is recorded on page one, and the installer is archived with the report. It is the only way I can promise to reproduce a number.'
context: '[CONTEXT: In ^s0003-0144 they were twice asked to re-run a simulation in front of an auditor; the archived installer "saved me the second time". In ^s0003-0142 the parameters the tool defaulted are written nowhere, so a run is "reproducible in practice, usually, and not provably". In ^s0003-0156 release notes saying "improved models" give no way to size the risk of an update, so updates are delayed.]'
tags: [functionality/workaround, insight/pain-point, sentiment/neutral, journey/validate, tools/model-version-drift]
review: accepted
created_by: ai
model: claude-fable-5-1
skill_version: 0.3.0
created: 2026-11-17
reviewed_by: P-000
reviewed: 2026-11-17
---

> [!info]- Context
> [CONTEXT: In ^s0003-0144 they were twice asked to re-run a simulation in front of an auditor; the archived installer "saved me the second time". In ^s0003-0142 the parameters the tool defaulted are written nowhere, so a run is "reproducible in practice, usually, and not provably". In ^s0003-0156 release notes saying "improved models" give no way to size the risk of an update, so updates are delayed.]

![[S-0003#^s0003-0094]]
[[S-0003#^s0003-0094|Open in transcript · S-0003 @ 00:34:05]]

**Rationale:** Silent model updates force a regulated customer to archive installers (against IT's wishes) to keep results reproducible under audit; strong evidence for model versioning and change notification, the follow-up the project note already flags (RQ1, RQ2).
