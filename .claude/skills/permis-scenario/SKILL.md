---
name: permis-scenario
description: Generate a French coastal navigation scenario combining concepts from chosen thematic areas, with real-world incident research and YouTube resources. Conducts a branching Socratic dialogue then debriefs with COLREGs citations. Triggers on /permis-scenario, "un scénario", "exercice navigation".
---

# permis-scenario

Creates an immersive French-language coastal navigation scenario for a **voilier classique** (sailing vessel only — never a motor boat). The student freely chooses the thematic area(s) they want to practise. The skill researches the wiki for relevant concepts, searches online (prioritising French-language sources) for a real-world incident and a YouTube video to ground the scenario, then runs a branching Socratic dialogue (4–6 exchanges) before debriefing with exact wikilink citations and curated resources.

**No dependency on student-progress.json** — topic selection is entirely driven by the student's choice in the session.

## When to use

Trigger when the student types `/permis-scenario`, asks for "un scénario", "exercice navigation", or otherwise requests a practical scenario exercise. All student-facing output must be in French. Internal reasoning may be in English. Do not use HTML or browser automation — text-only in chat.

## Tools needed

- **Read / Bash (glob)** — read wiki concept files
- **WebSearch** — find a real incident + a YouTube video relevant to the scenario (always prefer French-language sources and results)
- **WebFetch** — fetch article text if needed to verify incident details

---

## Workflow

Execute these steps in order. Never skip a step.

---

### Step 1 — Offer thematic areas

Present the following menu to the student in French and ask them to choose **1 to 3 areas** (or describe a specific situation they want to practise):

```
🗺️ Choisissez 1 à 3 thématiques pour votre scénario :

1. Règles de barre       — priorités, croisements, voilier vs voilier, voilier vs moteur
2. Feux & signaux        — identification de nuit, feux de route, brume, signaux sonores
3. Balisage & pilotage   — IALA, entrée de port, chenal, amers, lecture de carte
4. Navigation            — point estimé, courants de marée, GPS, routage
5. Météo & gros temps    — fronts, prise de ris, tactique par mauvais temps, équipement
6. Manœuvres & mouillage — approche au port, mouillage, homme à la mer
7. Urgences & radio VHF  — MAYDAY, PAN-PAN, CROSS, DSC, procédures de détresse
8. Réglementation        — zones de navigation, bande des 300 m, pollution, infractions

(Vous pouvez aussi décrire librement : « je veux m'entraîner sur les manœuvres de nuit » etc.)
```

Wait for the student's answer before proceeding.

---

### Step 2 — Read relevant wiki concepts

Based on the chosen thematic area(s), read the most relevant concept files from `Wiki/wiki/concepts/`. Read **at minimum 3 and at most 6** concept files per chosen area. Use the mapping below as a guide — supplement with any other concept file whose name is clearly relevant.

| Thematic area | Key concept files to read |
|---|---|
| Règles de barre | `regles-de-barre-priorites-voiliers.md`, `regles-de-barre-priorites-moteur.md`, `voilier-vs-voilier.md`, `voilier-vs-moteur.md`, `rattrapage.md`, `route-directe-croisement.md` |
| Feux & signaux | `feux-base.md`, `feux-de-route.md`, `feux-voilier.md`, `feux-mouillage.md`, `signaux-sonores-brume.md`, `signaux-sonores-manoeuvre.md` |
| Balisage & pilotage | `balisage-iala-region-a.md`, `marques-laterales.md`, `marques-cardinales.md`, `marques-danger-isole.md`, `aide-navigation-phares.md`, `pilotage-cotier.md` |
| Navigation | `navigation-estime.md`, `cap-route-derive.md`, `courants-de-maree.md`, `gps-cartographie-electronique.md`, `routage-navigation.md`, `planification-traversee.md` |
| Météo & gros temps | `meteorologie-marine.md`, `securite-meteo-et-pression.md`, `gros-temps-tactique.md`, `signaux-meteo.md`, `veille-quart.md` |
| Manœuvres & mouillage | `manoeuvre-voile-base.md`, `mouillage-technique.md`, `homme-a-la-mer-manoeuvres.md`, `accostage-amarrage.md`, `pratique-mouillage.md` |
| Urgences & radio VHF | `procedure-mayday.md`, `procedure-pan-pan.md`, `cross-sauvetage.md`, `asn-dsc.md`, `signaux-detresse.md`, `canaux-vhf.md` |
| Réglementation | `zones-navigation.md`, `bande-300m.md`, `pollution-dechets.md`, `infractions.md`, `documents-bord.md`, `regles-de-barre-distances.md` |

Extract and note:
- The **exact rules** (COLREGs articles, French regulations, distances, procedures)
- The **common errors** and traps mentioned in the concepts
- Specific **vocabulary** to use naturally in the scenario

---

### Step 3 — Online research

**Always prefer French-language sources and results.** Use French search terms. Prioritise sites like voiles-et-voiliers.fr, lemarin.fr, mer-agitee.com, cross-med.fr, cross-etel.fr, brest.fr/mer, journal-de-la-voile.fr.

#### A — Real-world incident

Search for a real incident or official accident report related to the chosen theme. Use queries like:

- Règles de barre: `"abordage voilier" côte française règles barre collision mer site:lemarin.fr OR site:mer-agitee.com OR site:voiles-et-voiliers.fr`
- Feux: `"voilier sans feux" nuit abordage collision france`
- Météo/gros temps: `"chavirage voilier" tempête atlantique bretagne france`
- Homme à la mer: `"homme à la mer voilier" france CROSS sauvetage`
- MAYDAY/radio: `"appel MAYDAY voilier" CROSS france intervention mer`
- Balisage: `"voilier échoué" chenal balisage france côte`
- Navigation: `"voilier échoué" courant marée erreur navigation france`
- Réglementation: `voilier infraction bande 300m france amende gendarmerie maritime`

Use WebFetch to retrieve a brief summary if the article is accessible. Extract:
- What happened (vessel type, location, date if available)
- What rule or error was involved
- Outcome (rescue, damage, fine, etc.)

If no real incident is found after 2 searches, fall back to an official statistic or report (e.g. bilan annuel CROSS, rapport BEAmer) — but always label it as such.

#### B — YouTube video (educational, in French)

Search for a relevant French-language educational video:

`site:youtube.com [thème] voilier navigation côtière tutoriel explication français`

Examples by theme:
- `site:youtube.com règles de barre voilier COLREGs animation explication français`
- `site:youtube.com feux navigation voilier nuit identification français`
- `site:youtube.com météo marine voilier gros temps français`
- `site:youtube.com homme à la mer manoeuvre voilier français`
- `site:youtube.com MAYDAY VHF procédure voilier français`
- `site:youtube.com balisage IALA voilier chenal français`

Prefer: sailing schools, CROSS, SHOM, official channels, major French sailing YouTube channels (e.g. Yvan Bourgnon, ActuNautique, Ecole de Voile). Note the title, channel, and URL.

---

### Step 4 — Build the scenario

Construct a realistic coastal navigation scenario. Requirements:

- **Vessel**: always a voilier classique (monohull sailing boat) — give it a name, length (9–12 m), and typical equipment. Never use a motor boat as the protagonist vessel.
- **Setting**: French coastal waters — choose a specific, named location (e.g. Rade de Brest, Golfe du Lion, Côte d'Azur, Pertuis Charentais, Archipel des Glénan, Côte Basque, Baie de la Seine)
- **Weather and time**: be specific — time of day, wind force and direction (Beaufort scale), visibility, sea state
- **Crew**: 2–3 persons including the student (skipper or crew member)
- **Situation arc**: a developing situation that builds tension naturally over 4–6 exchanges, with at minimum one clear decision point where the correct rule/procedure must be applied
- **Real incident echo**: the scenario should echo (not copy verbatim) the real incident found in Step 3 — reference it briefly as inspiration without naming the actual people involved

**Before presenting the scenario**, share this brief context block in French:

```
📡 Contexte réel — [one-line summary of the real incident or statistic found]
Exemple : « En 2021, un voilier de 10 m a été abordé de nuit au large de Marseille suite à un défaut de veille. Cet incident inspire notre scénario. »

🎬 Ressource à garder sous la main : [Titre de la vidéo] — [URL]
(Nous y reviendrons en débriefing.)
```

Then begin the scenario immediately.

---

### Step 5 — Conduct the Socratic dialogue

Run 4–6 exchanges:

- Present each situation beat concisely (2–4 sentences, present tense, immersive)
- End each beat with a specific open question: what do you do? what rule applies? what do you observe?
- Wait for the student's response before continuing
- React in character to their choice — if clearly wrong, show a natural consequence (the other vessel alters course abruptly, the harbour entrance becomes confusing, the situation worsens), but **do not correct mid-scenario**
- Weave in 2–3 pieces of nautical vocabulary naturally; **bold** each term on first use (e.g. **tribord amures**, **feu de tête de mât**, **veille**)

Maintain tension and immersion throughout. Write like a sailing instructor narrating a real situation.

---

### Step 6 — Debrief

After the final exchange, signal the switch clearly:

```
--- Fin du scénario — Débriefing ---
```

Structure the debrief as follows:

**1. Résumé des décisions** — for each decision point, state what the correct action was

**2. Règles et références** — for each concept domain tested:
- Name the specific rule (COLREGs article, French regulation, or SHOM procedure)
- Cite the wiki: `[[concepts/<slug>]]`
- One sentence explaining why this rule exists (the underlying maritime safety logic)
- Whether the student applied it correctly

**3. L'incident réel** — expand on the real-world parallel: what happened, what went wrong, what the crew should have done

**4. Ressources pour aller plus loin**
- 🎬 **Vidéo** : [title] — [URL]
- Additional concept files worth reading: `[[concepts/<slug>]]`
- If relevant: the type of exam question this scenario maps to

**5. Verdict** — one of:
- ✅ **Réussi** — la décision clé était correcte
- 〰️ **Partiel** — bonne intuition mais la règle précise était manquante
- ❌ **À retravailler** — la décision principale était incorrecte (suggest which concept to review)

---

## Rules

- All student-facing text in French throughout
- **Always a voilier** — never a motor boat as the protagonist vessel
- Text-only: no HTML rendering, no Playwright, no browser automation
- **Do not read or write `student-progress.json`** — no progress tracking in this skill
- **Always prefer French-language sources** for web searches — French sites, French YouTube channels, French official reports
- Never reveal correct/incorrect during the scenario exchanges — debrief only
- Never invent regulations: if uncertain, read the wiki concept file; if still uncertain, note the uncertainty explicitly
- Keep the scenario grounded in specific, named French coastal waters
- The real incident must be real or clearly labelled as a statistical composite — never fabricate a named event
