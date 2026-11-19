---
name: research-synthesize
description: Turn a project's accepted highlights into evidence-linked insight notes with honest evidence levels and decision-forcing recommendations, following ADI's synthesis guide. Use when the user says "synthesize project X", "write the insights", "what are the themes", "update insight I-…", "re-assess evidence levels", or after highlight review is done. Reads highlight notes only, never transcripts; one project per run.
---

# research-synthesize

Insights are what stakeholders act on. Without them they interpret raw highlights themselves and get it wrong. One project per run. `MODEL` is the model you are running as.

```
accepted highlights  →  themes  →  e_insights/I-<project>-## <finding>.md  →  01 project.md summary
```

## Procedure

1. `uv run _system/scripts/audit.py`; don't synthesise over errors.
2. **Pull the evidence table. This is the only input; do not open transcripts.**
   ```bash
   uv run _system/scripts/highlights_table.py <project> --accepted-only
   uv run _system/scripts/highlights_table.py <project>                  # if review isn't finished: say so, mark insights draft
   ```
   Over about 150 rows, group by tag first (`--tag insight/pain-point` etc.) and synthesise per group. If you need more context for one highlight, open its single linked block, not the source.
3. **Review tag patterns**: clusters (tags with the highest counts across the most participants), co-occurring combinations, cross-participant versus single-person frustrations, gaps (what nobody mentioned), cross-source convergence (interview + workshop + reference material).
4. **Identify themes**: a pattern that tells a coherent story across highlights. Themes are not tags.
5. **Assess evidence** per theme: strong = 4+ participants with consistent language; emerging = 2 to 3; insufficient = 1. Insight notes for strong and emerging only. Insufficient stays as tagged highlights; mention it in the report and offer `ops/follow-up-depth` on the highlight.
6. **Write each insight** from `_system/templates/insight.md` (`uv run _system/scripts/next_id.py insight <project>`), file `e_insights/I-<project>-## <finding>.md`:
   - `title`: `Insight: <finding statement>`, a claim with a verb, not a topic.
   - **Finding**: one clear statement. **Severity and impact**: how many participants, how often, how strongly. **What this means**: interpretation for product, business, user. **Evidence**: embed every supporting highlight **by file name** (`![[H-S0001-0004 Part change silently reset switching frequency]]`; get names with `vaultlib.find_by_id`; a bare `![[H-S0001-0004]]` does not resolve), from different participants; say whether evidence is verbal, demonstrated or artifact-based. **Recommendations**: decision-forcing ("Prioritise X", not "consider X"). **Open questions**: what the next session should probe.
   - Frontmatter: `evidence_level`, `participants` (from the evidence), `research_question`, `highlights` as `[[<file name>|H-S####-####]]`, 2 to 3 `tags`, `status: draft`.
   - One highlight may serve several insights; link it in both.
7. **Update `01 project.md`**: `status: analysis`; under `# Findings → ## Insights` refresh the 2 to 3 sentence summary (the table beneath is live; don't list insights by hand). `uv run _system/scripts/personas.py refresh` so personas list the new insights. Audit again.
8. `bash _system/scripts/provenance.sh research-synthesize synthesize <project> $MODEL`. Report: insights by evidence level, research questions still unanswered, signals kept for later, highlights left unused and why.

## Updating an existing insight

Re-run steps 2 to 5 for that theme only. Keep the ID and file name unless the finding itself changed; then rename the file (ID stays), keep `aliases`, and fix links with a grep for the old name. Record `updated:` in frontmatter.

## Next steps the user may ask for

- A readout for stakeholders: `research-report`.
- A page in Confluence: `research-publish`.
- A reel of the evidence: `research-clip` (`media.py reel I-…`).

## Never

- Open a transcript to find "better" quotes; synthesis reads highlights only.
- Write an insight from one participant.
- Round an evidence level up.
