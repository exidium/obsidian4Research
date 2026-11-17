---
type: hub
hub: insights-review
project: {{project_id}}
---

# Insights Review

Tagging is automatic: every highlight the AI wrote waits here as **proposed**, with its confidence. Review by exception: read the low-confidence cards, skim the high ones, drag to **accepted** or **rejected**, or run `uv run _system/scripts/review.py accept --source S-#### --min-confidence high`. Only accepted highlights feed the insights. You can also tell Claude: "accept H-S0001-0004 and H-S0001-0006, reject H-S0001-0011". Back to [[10 Projects/{{project_id}}/01 project|Study overview]].

## Review board

![[_system/bases/highlights-review.base#Review board]]

## Pending, as a table

![[_system/bases/highlights-review.base#Pending review]]

## Reviewed

![[_system/bases/highlights-review.base#Reviewed]]
