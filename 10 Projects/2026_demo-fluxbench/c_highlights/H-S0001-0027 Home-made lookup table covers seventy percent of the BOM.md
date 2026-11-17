---
type: highlight
highlight_id: H-S0001-0027
aliases: [H-S0001-0027]
title: Home-made lookup table covers seventy percent of the BOM
project: 2026_demo-fluxbench
source: '[[S-0001]]'
block: s0001-0104
participant: P-001
quote: I built a lookup table. In the spreadsheet, naturally. It maps the tool's suggested part numbers to our approved equivalents, by value and voltage and package. So now I export the CSV, paste it into the sheet, and a formula fills in our part number where it has a match. It's about seventy percent coverage. The other thirty percent are parts I haven't seen before, which I look up by hand and then add to the table. So it's getting faster. But this is me building the feature the tool should have. If the tool let me import a preferred parts list, even just a CSV with their number and my number, it would do this itself. I'd happily give them my lookup table as a starting point.
context: '[CONTEXT: Blocks 0100 and 0102: half an hour of part-number search and replace per revision, four revisions so far; each revision cycle (change, re-run, export PDFs, paste, export BOM, fix BOM) is about an hour "of which the thinking was ten minutes".]'
tags: [functionality/workaround, functionality/new-feature-request, insight/pain-point, sentiment/neutral, journey/integrate, export/approved-parts-mismatch]
review: accepted
created_by: ai
model: claude-fable-5-1
skill_version: 0.3.0
created: 2026-11-17
reviewed_by: P-000
reviewed: 2026-11-17
---

> [!info]- Context
> [CONTEXT: Blocks 0100 and 0102: half an hour of part-number search and replace per revision, four revisions so far; each revision cycle (change, re-run, export PDFs, paste, export BOM, fix BOM) is about an hour "of which the thinking was ten minutes".]

![[S-0001#^s0001-0104]]
[[S-0001#^s0001-0104|Open in transcript · S-0001 @ 00:44:33]]

**Rationale:** Quantifies the workaround for the approved-vendor gap already highlighted (block 0018) and specifies the minimum feature (a two-column CSV import) that would retire it.
