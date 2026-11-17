---
name: research-persona
description: Assign every participant a persona and keep the vault-wide persona set honest: match a participant to an existing persona in 30 Personas/ or propose a new one, build and revise personas from participant cards and accepted highlights (jobs to be done, behaviours, pain points, what earns their trust), refresh where each persona appears, merge or retire personas. Use when the user says "assign a persona", "which persona is P-…", "create a persona", "update the personas", "merge PE-02 into PE-04", "persona report", or when research-participants finds a card without a persona.
---

# research-persona

Personas are vault-wide, not per project. **Every participant card carries exactly one persona.** If no persona fits, propose a new one; never stretch an existing persona to make a participant fit. Personas are built from evidence in the vault (cards and accepted highlights), never from assumptions about a role. `MODEL` is the model you are running as.

## Naming

`PE-## <role> who <one defining behaviour>`, plain words: `PE-01 Design engineer who trusts a result only after it matched the bench`. No adjectives ("skeptical"), no metaphors, no archetype labels, no invented first names. The file name is the title; `aliases` holds the ID; `name` is the title without the ID.

## Procedure

### match P-###

1. Read the public card `20 Participants/P-###.md` (never the identity note). Read every note in `30 Personas/`: Who, Jobs to be done, Behaviours, Pain points.
2. Read the participant's accepted highlights (`grep -l "participant: P-###" "10 Projects/*/c_highlights/"*.md`, then the notes; `review != rejected`). Highlights are the behaviour evidence; the card is the profile.
3. Score each persona on four questions: same kind of job (what they are trying to get done)? same relationship to the product (designs with it, supports it, validates it, buys it)? shared pain points? would the persona's "how to research with them" work on this person? A persona fits when all four hold and nothing in the highlights contradicts it.
4. **Fits**: set `persona` on the card to `[[30 Personas/<file name>|<file name>]]` (ID and name as display text; a bare ID is not enough), add the participant to the persona's `participants`, and `uv run _system/scripts/personas.py refresh`.
5. **Doesn't fit**: `propose` below. Tell the user which personas were considered and the one fact that broke each match.

### propose (new persona)

1. Next ID: highest `PE-##` in `30 Personas/` plus one.
2. Write `30 Personas/PE-## <role> who <behaviour>.md` from `_system/templates/persona.md`, `status: proposed`:
   - **Who**: role, seniority, kind of company, how they meet the product. No names, no employer.
   - **Jobs to be done**: three statements, `When <situation>, I want <motivation>, so I can <outcome>`, each traceable to a highlight.
   - **Behaviours**, **Pain points**, **What earns their trust**, **How to research with them**: from the highlights, with the participant's own phrasing where it is strong.
   - A one-line opening quote with its highlight ID.
3. Set the card's `persona`, run `personas.py refresh` (fills Where they appear and the counts), `personas.py check`.
4. A persona with one participant stays `proposed` or `draft`. Tell the user it needs a second matching participant before it is `reviewed`.
5. `bash _system/scripts/provenance.sh research-persona propose PE-## $MODEL`.

### revise PE-##

After a new study adds participants or highlights to a persona: re-read its highlights, update the sections that changed, bump `updated`, `personas.py refresh`. Don't rewrite the voice for its own sake.

### merge PE-A into PE-B

When two personas describe the same job and relationship to the product: move PE-A's participants to PE-B (card `persona` links), fold any behaviour or pain point PE-B lacks, set PE-A `status: retired` with `merged_into: PE-B`, keep the file (links and history), `personas.py refresh`. Never delete a persona note.

### persona report

`_system/bases/personas.base` gives the set. Report: personas by status, participants per persona, personas with one participant (fragile), participants whose highlights contradict their persona (candidates for a split), markets and participant types not covered.

## Where they appear

`personas.py refresh` regenerates the section between the `appearances` markers in every persona: participants, projects, sources, every insight that uses their highlights (with how many), every highlight with its tags. Never edit that section by hand.

## Never

- Assign a persona because the role matches; the behaviour has to.
- Read `_raw/` or name a person.
- Write a persona from a single interview and call it reviewed.
