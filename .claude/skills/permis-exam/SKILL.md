---
name: permis-exam
description: Run a full 40-question Permis Côtier blanc exam with Playwright browser display, per-theme scoring, and a rendered score report. Triggers on /permis-exam, "examen blanc", "mock exam".
---

# permis-exam

Conducts a complete simulated Permis Côtier de Plaisance written exam. Selects 40 questions from the local question bank, runs them in strict exam mode (no per-question feedback), calculates the score, writes and renders a score report, then updates student progress.

## When to use

Trigger when the student types `/permis-exam`, asks for "examen blanc", "mock exam", or otherwise requests a full practice exam. This skill takes over the full session until the score report is displayed.

## Question file format

Questions live in `Wiki/wiki/questions/<category>-NN.md`. Two format variants exist in the bank:

**Variant A** (older balisage files) — free-form markdown:
```markdown
---
title: QCM Balisage 01 — Feu isophase
type: question
tags: [balisage, feux]
related: [[../concepts/feux-base]]
---
**Q:** Question text
- A — option text
- **B — correct option** ✓
**A:** B — correct option.
**Why:** Explanation. Voir [[../concepts/feux-base]].
```

**Variant B** (structured, most categories) — section headings:
```markdown
---
id: feux-01
theme: "Feux"
type: question
---
# Question
Question text
## Options
A) ...
B) ...
## Answer
B
## Explanation
Explanation text (may contain [[concepts/slug]] wikilinks).
```

When parsing: detect variant by checking for `# Question` section heading. In Variant A, the correct answer is the bolded option with ✓. In Variant B, `## Answer` gives the letter. Extract the `Why:` / `## Explanation` text for the study plan.

## Inputs

- `Wiki/wiki/questions/` — question bank (read only)

**No dependency on student-progress.json** — the exam runs regardless of tracked progress, since students may have completed sessions in the HTML SPA without it being recorded.

## Exam theme distribution (40 questions)

| Category (file prefix) | Target count | Available |
|---|---|---|
| `balisage` | 9 | 13 |
| `regles-barre` | 6 | 5–8 |
| `feux` | 5 | 5 |
| `signaux` | 3 | 5 |
| `navigation` | 7 | 5+ |
| `securite` | 7 | 5 |
| `pratique` | 3 | 5 |
| **Total** | **40** | |

If a category has fewer files than the target, take all available and top up from the remaining categories proportionally until total = 40.

Exclude `sample-questions.md` — it is not a real question file.

## Workflow

Execute these steps in order. Do not skip or reorder.

### 1. Open the course SPA in Cowork

Resolve the absolute repo path with `pwd`. Then output the compiled SPA as a Cowork HTML artifact and a clickable link:

```
[📖 Cours complet — référence pendant l'examen]($REPO_ROOT/output/permis-cours-complet.html)
```

If `output/permis-cours-complet.html` is missing, run `.venv/bin/python scripts/render_complete.py` once to generate it. Do not start an HTTP server.

### 2. Build the question set

Read all files from `Wiki/wiki/questions/`, excluding `sample-questions.md`.

Group files by category prefix (the part before the first `-NN`). For each category, randomly select up to the target count from the table above. If the selected set has fewer than 40 questions, top up from all unused real question files. Shuffle the 40 selected questions into a random order.

Parse each question file to extract:
- Question text
- Options (A–D)
- Correct answer letter
- Explanation / Why text (for study plan)
- Concept wikilinks from explanation (for study plan)
- Theme name

Keep the correct answers and explanations internal — do not include them in what you display to the student.

### 3. Run the exam

Announce:

> « Examen blanc Permis Côtier — 40 questions. Réponds par la lettre (A, B, C ou D). Bonne chance ! »

For each question (1 to 40):
- Display: `**Question N/40**` followed by the question text and options
- Wait for the student's single-letter answer
- Record the answer internally (do not reveal correct/incorrect)
- Every 5 questions, display a progress marker: `— [N/40 répondues] —`

Do not provide any feedback, hints, or corrections during the exam. If the student asks for the answer, reply: « En mode examen, je ne peux pas te donner les réponses. Continue ! »

### 4. Calculate results

After question 40, calculate:
- Total score (N/40)
- Per-theme score: correct/total for each category
- Pass: score >= 35/40

Identify wrong answers: for each incorrect question, note the theme and the explanation/Why text with any `[[concepts/slug]]` wikilinks.

### 5. Generate score report

Write a markdown score report to `/tmp/permis-score-report.md`:

```markdown
---
title: Résultats Examen Blanc — <date>
---

# <REÇU ✓ / RECALÉ ✗> — Score : N/40

> Seuil de réussite : 35/40 (maximum 5 erreurs)

## Résultats par thème

| Thème | Score | Résultat |
|-------|-------|---------|
| Balisage | N/10 | ✓/✗ |
| Règles de barre | N/5 | ... |
| Feux | N/5 | ... |
| Sécurité | N/5 | ... |
| Navigation | N/5 | ... |
| Signaux | N/5 | ... |
| Pratique | N/5 | ... |

## Plan de révision

Pour chaque mauvaise réponse, liste :
- **Q<N>** — <Question text> — Bonne réponse : <letter>
  - <Explication>
  - Revoir : <[[concepts/slug]] wikilinks from explanation>

(If all correct in a theme, write: « Excellent ! Rien à réviser dans ce thème. »)
```

### 6. Display the score report

Output the score report markdown content as a Cowork artifact (type: `text/markdown`) so it displays cleanly in the side panel. No HTTP server or browser navigation needed.

Announce the final result to the student in French, with the pass/fail banner and a motivational closing line.

## Pass threshold

35/40. Five errors are tolerated; six or more errors means recalé.

## Rules

- Strict exam mode: no per-question feedback until step 5
- Questions must be randomly sampled and shuffled each run (no fixed order)
- Never reveal correct answers during the exam
- French throughout (skill instructions are in English for Claude's benefit)
