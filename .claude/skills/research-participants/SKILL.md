---
name: research-participants
description: Keep participant cards in step with Rally: sync the Rally export into 20 Participants/ (public card with role, experience, market, industry, region, consent state; identity kept local in _raw/), check that every source has a card and every card a persona, and hand new participants to research-persona. Use when the user says "sync participants", "update the participant cards", "who is P-004", "add a participant", "import from Rally", "consent status of P-…", or when research-ingest meets a participant without a card.
---

# research-participants

A participant is two halves. The **public card** (`20 Participants/P-###.md`) carries what research needs: role, seniority, experience band, market, industry, region, country, company size, tools, consent flags and retention date, projects and sources, persona. The **identity** (`_raw/participants/P-### identity.md` and `_raw/participants.csv`) carries name, employer and email, lives only on machines with the key (the SharePoint/OneDrive study folder in production), and is embedded by the card so people with the key see it inline. Rally is the source for both; the card never holds a name.

## Procedure

### sync

1. The Rally export must be at `_raw/rally/participants.json` (a Rally participant export, or the mock for the demo). **Never open it**; the script reads it. If it is missing or stale, ask the user to export from Rally (Study › Participants › Export) and drop it there.
2. `uv run _system/scripts/participants.py sync` writes every card, every identity note and `participants.csv`. `persona` on an existing card survives; everything else comes from Rally.
3. `uv run _system/scripts/participants.py check`: sources citing a participant without a card, cards without a persona.
4. For each card without a persona, run `research-persona` (match or propose). A participant is not done until it has one.
5. `bash _system/scripts/provenance.sh research-participants sync <project-or-all> $MODEL`. Report: cards written, new participants, consent states that block anything (expired retention, `video_clips: false` for someone with clips), cards still without a persona.

### a new participant during ingest

`research-ingest` needs a `P-###`. `uv run _system/scripts/next_id.py participant` gives the next ID; the user adds the person in Rally and re-exports, then `sync`. Until then the source note carries the ID and the card is missing; `check` will keep saying so.

### questions about a participant

Answer from the public card only: role, experience, market, industry, region, consent, which studies and highlights. Never look up or state a name. If the user asks "who is P-004" meaning the identity, point them at `_raw/participants/P-004 identity.md`, which they can open themselves.

### consent

The card's `consent_recording`, `consent_quotes`, `consent_video_clips` and `retention_until` gate what other skills may do: no quotes in an insight without `consent_quotes`, no clip without `consent_video_clips`, nothing after `retention_until`. When a participant withdraws, the user deletes the recording and clips from the study folder and the identity from the key, sets the card's `consent_status: withdrawn`, and `research-highlight` sets their highlights to `review: rejected` with a note. Git history keeps only pseudonymised text.

## Properties on the card (generated)

`participant_id`, `participant_type`, `role`, `seniority`, `experience` (band), `years_experience`, `market` (taxonomy ID), `industry`, `region`, `country`, `company_size`, `tools`, `persona`, `rally_id`, `consent_status`, `consent_recording`, `consent_quotes`, `consent_video_clips`, `retention_until`, `projects`, `sources`, `rally_synced`. Only `persona` is set by hand (by `research-persona`).

## Views

`_system/bases/participants.base` (table and cards) for the whole pool; each card has a live table of the participant's highlights; `01 project.md` lists the study's participants with their persona.

## Never

- Write a name, employer or email into any file outside `_raw/`.
- Open the Rally export or `participants.csv` in the conversation.
- Invent a participant field that Rally does not have; leave it empty and say so.
