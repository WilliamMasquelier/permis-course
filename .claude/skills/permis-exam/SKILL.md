---
name: permis-exam
description: Run a full 30-question Permis Côtier blanc exam with Playwright browser display, per-theme scoring, and a rendered score report. Triggers on /permis-exam, "examen blanc", "mock exam".
---

# permis-exam

Conducts a complete simulated Permis Côtier de Plaisance written exam. Selects 30 questions from the question bank following the official theme distribution, runs them in strict exam mode (no per-question feedback), calculates the score, writes and renders a score report, then updates student progress.

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

## Inputs (state files read/written)

- `Wiki/meta/student-progress.json` — read `completed_lessons`, write `exam_results`
- `Wiki/wiki/questions/` — question bank

## Exam theme distribution (30 questions)

| Category (file prefix) | Target count | Available |
|---|---|---|
| `balisage` | 6 | 13 |
| `regles-barre` | 5 | 5 |
| `feux` | 4 | 5 |
| `securite` | 4 | 5 |
| `navigation` | 4 | 5 |
| `signaux` | 4 | 5 |
| `pratique` | 3 | 5 |

If a category has fewer files than the target, use all available files from that category (adjust total accordingly — still report out of 30 in the final score).

Exclude `sample-questions.md` — it is not a real question file.

## Workflow

Execute these steps in order. Do not skip or reorder.

### 1. Check prerequisites and confirm

Read `Wiki/meta/student-progress.json`. Count `completed_lessons`.

If fewer than 4 sessions completed, warn the student:

> « Attention : tu n'as complété que N/4 sessions. L'examen blanc couvre toutes les matières. Veux-tu continuer quand même ? (oui/non) »

Wait for confirmation. If "non", stop.

### 2. Open exam page in browser

Start the HTTP server and open the exam session page:

```bash
python -m http.server 8080 --directory rendered/ > /tmp/permis-server.log 2>&1 &
echo $! > /tmp/permis-server.pid
for i in $(seq 1 10); do nc -z localhost 8080 && break || sleep 0.5; done
```

Navigate to `http://localhost:8080/session-05-examen-blanc.html` with `browser_navigate`. Take a screenshot to confirm the timer/exam page is visible.

### 3. Build the question set

Read all files from `Wiki/wiki/questions/`, excluding `sample-questions.md`.

Group files by category prefix (the part before the first `-NN`). For each category, randomly select up to the target count from the table above. Shuffle the 30 selected questions into a random order.

Parse each question file to extract:
- Question text
- Options (A–D)
- Correct answer letter
- Explanation / Why text (for study plan)
- Concept wikilinks from explanation (for study plan)
- Theme name

Keep the correct answers and explanations internal — do not include them in what you display to the student.

### 4. Run the exam

Announce:

> « Examen blanc Permis Côtier — 30 questions. Réponds par la lettre (A, B, C ou D). Bonne chance ! »

For each question (1 to 30):
- Display: `**Question N/30**` followed by the question text and options
- Wait for the student's single-letter answer
- Record the answer internally (do not reveal correct/incorrect)
- Every 5 questions, display a progress marker: `— [N/30 répondues] —`

Do not provide any feedback, hints, or corrections during the exam. If the student asks for the answer, reply: « En mode examen, je ne peux pas te donner les réponses. Continue ! »

### 5. Calculate results

After question 30:

Kill the server:
```bash
kill $(cat /tmp/permis-server.pid) 2>/dev/null; rm -f /tmp/permis-server.pid
```

Calculate:
- Total score (N/30)
- Per-theme score: correct/total for each category
- Pass: score >= 18/30

Identify wrong answers: for each incorrect question, note the theme and the explanation/Why text with any `[[concepts/slug]]` wikilinks.

### 6. Generate score report

Write a markdown score report to `/tmp/permis-score-report.md`:

```markdown
---
title: Résultats Examen Blanc — <date>
---

# <REÇU ✓ / RECALÉ ✗> — Score : N/30

> Seuil de réussite : 18/30

## Résultats par thème

| Thème | Score | Résultat |
|-------|-------|---------|
| Balisage | N/6 | ✓/✗ |
| Règles de barre | N/5 | ... |
| Feux | N/4 | ... |
| Sécurité | N/4 | ... |
| Navigation | N/4 | ... |
| Signaux | N/4 | ... |
| Pratique | N/3 | ... |

## Plan de révision

Pour chaque mauvaise réponse, liste :
- **Q<N>** — <Question text> — Bonne réponse : <letter>
  - <Explication>
  - Revoir : <[[concepts/slug]] wikilinks from explanation>

(If all correct in a theme, write: « Excellent ! Rien à réviser dans ce thème. »)
```

### 7. Render and display the score report

Render the score report to HTML:

```bash
source .venv/bin/activate && python -c "
import sys; sys.path.insert(0,'scripts')
from render_lessons import render_lesson
from pathlib import Path
render_lesson(Path('/tmp/permis-score-report.md'), Path('rendered'))
"
```

Start the server again briefly:
```bash
python -m http.server 8080 --directory rendered/ > /tmp/permis-server.log 2>&1 &
echo $! > /tmp/permis-server.pid
for i in $(seq 1 10); do nc -z localhost 8080 && break || sleep 0.5; done
```

Navigate to `http://localhost:8080/permis-score-report.html` with `browser_navigate`. Take a screenshot. Then kill the server:
```bash
kill $(cat /tmp/permis-server.pid) 2>/dev/null; rm -f /tmp/permis-server.pid
```

### 8. Update progress

Append to `exam_results` in `Wiki/meta/student-progress.json` (create the key as empty array if absent):

```json
{
  "date": "<ISO 8601 UTC timestamp>",
  "score": N,
  "total": 30,
  "passed": true|false,
  "theme_scores": {
    "balisage": "N/6",
    "regles-barre": "N/5",
    "feux": "N/4",
    "securite": "N/4",
    "navigation": "N/4",
    "signaux": "N/4",
    "pratique": "N/3"
  }
}
```

Announce the final result to the student in French, with the pass/fail banner and a motivational closing line.

## Pass threshold

18/30 (60%). Below 18: recalé. 18 or above: reçu.

## Rules

- Strict exam mode: no per-question feedback until step 5
- Questions must be randomly sampled and shuffled each run (no fixed order)
- Never reveal correct answers during the exam
- French throughout (skill instructions are in English for Claude's benefit)
