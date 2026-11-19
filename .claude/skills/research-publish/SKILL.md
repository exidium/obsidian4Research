---
name: research-publish
description: Publish a study page, insight or readout from the vault to Confluence (ADI SDP UX Research space) and record the page URL back on the note. Use when the user says "publish to Confluence", "sync the study", "push insight I-… to Confluence", "update the Confluence page", or "where is this published". Renders bodies with publish.py, creates or updates pages through the atlassian-main connector with a preview first, writes published_to back. Never publishes names, media or anything from _raw/.
---

# research-publish

Confluence is where stakeholders and Rovo find findings; the vault stays the system of record. Every published page is generated from a note, so re-publishing is a re-render, never a hand edit. `MODEL` is the model you are running as.

```
01 project.md / e_insights/*.md / f_deliverables/*.md  →  publish.py render  →  HTML bodies
HTML body  →  atlassian-main createConfluencePage / updateConfluencePage  →  URL
URL  →  publish.py record  →  published_to on the note
```

## Where pages go

Space **SDPUXR** (SDP UX Research), under **Projects › <year>**. The study page is the parent; readouts and insights are its children. Insights are titled `Insight: <finding>`, matching the space's "Writing Insights and Synthesis" page. Ask once if the user wants another parent and remember it for the session.

## Procedure

1. **Readiness.** `uv run _system/scripts/audit.py` clean for the project. An insight should be `status: reviewed`; if `draft`, say so and ask (the fictional demo publishes drafts). `redacted: true` on every source behind the evidence.
2. **Render.** `uv run _system/scripts/publish.py render <project>` writes one HTML body per page to `_system/publish/<project>/` plus `manifest.json`. Evidence in insight pages becomes quotes with their trace (`P-001 · S-0001 @ 00:04:09 · H-S0001-0005`) and tags; Bases views and media are dropped; wikilinks to notes that already have `published_to` become Confluence links, others become plain text with the ID. **Render insights before the study page**, so the study page links to them.
3. **Preview gate** (from the `atlassian-docs` skill): show the target (space › parent), the page tree, and the body as rendered text for each page; wait for an explicit yes. Load the `atlassian-docs` skill for the connection rules.
4. **Create or update.** `searchConfluenceUsingCql` with `title = "<title>" AND space = "SDPUXR"`; if the page exists, `updateConfluencePage` with a version message, otherwise `createConfluencePage` with `contentFormat: html` and the parent ID. Order: study page, then insights, then readouts, then update the study page once more so its lists are links.
5. **Record.** `uv run _system/scripts/publish.py record <project> <note-id-or-file> <url>` for every page (`study` for the study page). Set `status: published` on an insight the user approved for publishing. Add a published readout to the Reports table in `01 project.md` with its URL.
6. `bash _system/scripts/provenance.sh research-publish publish <target> $MODEL` per page. Report every page as `title — url (created | updated)`.

## Re-publishing after changes

Same procedure; `publish.py render` picks up the current notes, and `updateConfluencePage` replaces the body. Never edit a published page by hand in Confluence; the next render would overwrite it.

## Video

Clips and reels are not uploaded by this skill. If the user wants a reel on a page, it goes to the study's SharePoint folder (the `_raw/<project>/reels/` sync) and is linked from the page as a smart link; internal-participant video is never shared.

## Never

- Publish a name, an employer, a recording, a clip, or anything from `_raw/`.
- Publish without the preview gate.
- Write to any Atlassian site other than ADI Main, or any space the user did not name.
