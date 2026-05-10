---
name: permis-scenario
description: Generate a French coastal navigation scenario combining concepts from completed sessions. Conducts a branching Socratic dialogue then debriefs with COLREGs citations. Triggers on /permis-scenario, "un scénario", "exercice navigation".
---

# permis-scenario

Creates an immersive French-language coastal navigation scenario that combines 2–3 concept domains drawn from the student's completed sessions. Runs a branching Socratic dialogue (4–6 exchanges) with a decision point, evaluates the student's reasoning against COLREGs/French coastal rules, then debriefs with exact wikilink citations.

## When to use

Trigger when the student types `/permis-scenario`, asks for "un scénario", "exercice navigation", or otherwise requests a practical scenario exercise. All output must be in French. Do not use HTML or browser tools — text-only in chat throughout.

## Inputs (state files read/written)

- `Wiki/meta/student-progress.json` — read `completed_lessons`, write `scenarios_completed`

## Session → Domain mapping

| Lesson file | Concept domain slug |
|---|---|
| `module-1-1-vocabulaire-bateau.md` | `vocabulaire` |
| `module-1-2-regles-de-barre.md` | `regles-barre` |
| `module-1-3-feux-signaux.md` | `feux-signaux` |
| `module-2-1-balisage-iala.md` | `balisage` |
| `module-2-2-carte-marine.md` | `carte` |
| `module-2-3-phares-amers.md` | `phares` |
| `module-3-1-compas-cap-route.md` | `compas` |
| `module-3-2-marees-courants.md` | `marees` |
| `module-3-3-point-estime-gps.md` | `navigation-position` |
| `module-3-4-routage-pilotage.md` | `pilotage` |
| `module-4-1-voile-theorie.md` | `voile` |
| `module-4-2-manoeuvres.md` | `manoeuvres` |
| `module-4-3-mouillage.md` | `mouillage` |
| `module-5-1-meteo.md` | `meteo` |
| `module-5-2-securite-equipement.md` | `securite-equipement` |
| `module-5-3-urgences.md` | `urgences` |
| `module-5-4-visibilite-reduite.md` | `visibilite-reduite` |
| `module-6-1-radio-vhf.md` | `radio-vhf` |
| `module-6-2-reglementation.md` | `reglementation` |

## Workflow

Execute these steps in order.

### 1. Check prerequisites

Read `Wiki/meta/student-progress.json`. Extract the `completed_lessons` array.

If fewer than 2 sessions are completed, tell the student (in French):

> « Tu dois d'abord terminer au moins 2 sessions avant de faire un exercice de scénario. Continue avec `/permis-tutor` ! »

Then stop — do not proceed.

### 2. Select concept domains

Map each completed lesson filename or slug to its concept domain using the table above. Accept both filename forms (`module-1-1-vocabulaire-bateau.md` and `module-1-1-vocabulaire-bateau`) since progress ledgers may omit the `.md` extension. You now have a list of available domains.

Pick 2–3 concept slugs from **different** completed domains:
- If 2 domains available: use both
- If 3+ domains available: pick 3, weighting toward the most recently completed sessions (last in `completed_lessons`)
- Choose specific concepts within each domain that combine interestingly for a coastal navigation decision scenario

### 3. Generate the scenario

Write a realistic French coastal navigation scenario (Méditerranée or Atlantique context) that naturally requires applying all chosen concept domains. The scenario must have:

- **Setting**: location, weather, time of day, vessel type (voilier or moteur)
- **Situation**: a developing navigational situation with at least one clear decision point
- **Branching dialogue**: 4–6 exchanges. At each key moment, present the situation and ask the student what they would do or what rule applies. Do not reveal the correct answer yet.
- **COLREGs/règles côtières hook**: the decision point must involve a rule from COLREGs or French coastal regulations (e.g., bâbord/tribord, feux de route, priorité, signaux de brume)

Keep each exchange concise. Use nautical vocabulary naturally. Maintain tension and immersion.

### 4. Conduct the dialogue

Run the scenario interactively:

- Present each situation/question
- Wait for the student's answer
- React in character to their choice (but do not reveal correctness mid-scenario)
- Adapt slightly based on clearly wrong answers (give a gentle situational consequence, not a direct correction)

### 5. Debrief

After the final exchange, switch to debrief mode. Signal this clearly:

> « --- Fin du scénario — Débriefing --- »

For each concept domain tested:
- Name the relevant rule
- Cite the exact wikilink: `[[concepts/<slug>]]`
- Explain what the correct action was and why
- Note if the student answered correctly

Evaluate overall outcome: **pass** (got the key decision right), **partial** (partially correct), or **fail** (missed the main decision point).

### 6. Update progress

Write the scenario result to `Wiki/meta/student-progress.json`. Append to `scenarios_completed` (create the key as an empty array if it doesn't exist):

```json
{
  "date": "<ISO 8601 UTC timestamp>",
  "concepts_tested": ["<domain-slug-1>", "<domain-slug-2>"],
  "outcome": "pass|partial|fail"
}
```

Confirm to the student: « Résultat enregistré. »

## Rules

- All text in French throughout (skill instructions are in English for Claude's benefit)
- Text-only: no HTML, no browser, no screenshots
- Never test concepts from sessions the student has not completed
- Never reveal correct/incorrect per-exchange during the scenario (debrief only)
- Keep the scenario grounded in realistic French coastal waters
