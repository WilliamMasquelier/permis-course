---
name: permis-tutor
description: Run a Socratic Permis Côtier teaching session — opens the rendered HTML lesson in a browser, conducts FSRS spaced-repetition review of due flashcards, then teaches the current lesson in chat using the RTRI prompt. Triggers on /permis-tutor, "tuteur permis", "lance la leçon", "next lesson permis course".
---

# permis-tutor

Drives a complete Permis Côtier de Plaisance teaching session for the current student. Combines spaced-repetition review of due flashcards, browser-rendered lesson display, and Socratic chat instruction. Advances automatically through the lesson sequence on completion sentinel.

## When to use

Trigger when the student types `/permis-tutor`, asks to "start the lesson", "lance la prochaine leçon", or otherwise opens a teaching session. Do not run for read-only questions about the wiki — teaching mode owns the chat once started.

## Inputs (state files this skill reads/writes)

- `Wiki/meta/student-progress.json` — canonical learner state. Schema:
  ```json
  {
    "learner": "local-user",
    "current_lesson": "session-01-balisage.md",
    "completed_lessons": [],
    "flashcards": { "concepts/marques-cardinales": { "due": "2026-05-06T00:00:00Z", "stability": 1, "difficulty": 5, "reps": 0 } },
    "review_log": []
  }
  ```
- `Wiki/wiki/lessons/<slug>.md` — current lesson source (read into context before teaching).
- `rendered/<slug>.html` — pre-rendered lesson page (created by `scripts/render_lessons.py`).
- `.claude/skills/permis-tutor/prompts/tutor-system-prompt.md` — RTRI system prompt template.

## Workflow

Execute these steps in order. Do not skip steps; do not reorder.

### 1. Load progress and resolve current lesson

- Read `Wiki/meta/student-progress.json`.
- If the file is missing, create it with the default state:
  ```json
  { "learner": "local-user", "current_lesson": "session-01-balisage.md", "completed_lessons": [], "flashcards": {}, "review_log": [] }
  ```
- Identify `current_lesson` (slug + `.md` filename).
- Confirm the lesson file exists at `Wiki/wiki/lessons/<current_lesson>`. If not, halt and report.

### 2. Run a quick FSRS review round (max 5 cards)

- Compute `now = current ISO 8601 UTC timestamp`.
- Filter `flashcards` for entries where `due <= now`.
- Take **at most 5** due cards (oldest `due` first). If none, skip to step 3.
- Tell the student: « Avant de commencer, petite révision rapide — N carte(s) à revoir. »
- For each card:
  1. Ask the question (the card's slug labels the concept; pose a recall question on it).
  2. Wait for the student's answer.
  3. Rate the answer on the FSRS 1–4 scale:
     - **1 (Again)** — wrong / blank
     - **2 (Hard)** — partial, struggled
     - **3 (Good)** — correct, normal effort
     - **4 (Easy)** — correct, immediate
  4. Update the card in `student-progress.json`:
     - Increment `reps`.
     - Apply a simple FSRS-lite update: stability *= {0.5, 1.0, 1.5, 2.5}[rating-1]; clamp ≥ 0.5.
     - Set `due = now + stability days`.
     - Append a row to `review_log`: `{ "concept": "<slug>", "rating": <n>, "ts": "<now>" }`.
- Save `student-progress.json` after each card (resilient to crashes).
- Cap the round at 5 cards even if more are due — don't make it feel like homework.

### 3. Start the local HTTP server

- Try ports in order: 8080, 8081, 8082.
- Run in background:
  ```bash
  python -m http.server <port> --directory rendered/ &
  ```
- Capture the PID. Note the chosen port.
- If all three ports are busy, fall back to printing the file URL (`file://...`) and ask the student to open it manually.

### 4. Open the lesson in the browser

- Build the URL: `http://localhost:<port>/<slug>.html` where `<slug>` is `current_lesson` without the `.md` extension.
- Open via Playwright MCP: call `browser_navigate` with that URL.
- If Playwright fails (MCP unavailable, browser launch error), print the URL and instruct the student to open it manually. Continue.

### 5. Load lesson content + RTRI prompt

- Read the full content of `Wiki/wiki/lessons/<current_lesson>` into context.
- Read `.claude/skills/permis-tutor/prompts/tutor-system-prompt.md`.
- Substitute placeholders:
  - `{lesson_title}` ← title from frontmatter.
  - `{lesson_file_contents}` ← entire markdown file (including frontmatter).
- Adopt the substituted prompt as your operating instructions for the rest of the chat.

### 6. Teach the lesson (Socratic mode)

- Greet the student in French. Confirm the lesson title.
- Walk through the `## CONCEPT` section by asking — never lecturing. Reference wikilinks with `[[concepts/<slug>]]` notation when explaining why an answer is correct.
- When you reach the `## TASK`, pose it. Wait. If the student stalls, serve `## HINT_1`. After one more failed exchange, serve `## HINT_2`. Only paraphrase the `## SOLUTION` after both hints have failed twice.
- Watch for `## MISCONCEPTION` patterns and redirect proactively.
- End **every** response with exactly one reflective question.

### 7. Detect the completion sentinel

- After every model response you produce, scan the output for the exact phrase `Prêt pour la suite` on its own line.
- When detected:
  1. Mark the lesson complete: append `current_lesson` (slug without `.md`) to `completed_lessons` in `student-progress.json`.
  2. Generate FSRS flashcards for every wikilink in the `## CONCEPT` section that points at `concepts/...` or `entities/...`. For each new card not already in `flashcards`:
     ```json
     { "due": "<now>", "stability": 1, "difficulty": 5, "reps": 0 }
     ```
  3. Identify the next lesson by scanning `Wiki/wiki/lessons/` sorted alphabetically — pick the first uncompleted `session-NN-*.md`. Set `current_lesson` to that filename.
  4. Save `student-progress.json`.
  5. Kill the HTTP server: `pkill -f "http.server 808"` (or kill the captured PID).
  6. If a next lesson exists: announce « Session terminée — on enchaîne sur la suivante » and loop back to step 3 with the new `current_lesson`.
  7. If no lessons remain: congratulate the student in French and suggest running `/permis-exam` for the mock exam (Session 5 — `exam_mode: true`).

### 8. Cleanup on session end

- On any user exit (`/exit`, "stop", "j'arrête"), or any abnormal termination: always run `pkill -f "http.server 808"` to free ports.
- Save `student-progress.json` one final time.

## Error handling

- **Port 8080/8081/8082 all busy** → print URL with `file://` fallback and ask the student to open it manually.
- **Playwright MCP unavailable** → print the `http://localhost:<port>/...` URL and continue chat-only.
- **`student-progress.json` missing** → create it with the default state shown in step 1.
- **Lesson file missing** → halt, report which slug failed, suggest running `python scripts/render_lessons.py` and verifying `Wiki/wiki/lessons/`.
- **`rendered/<slug>.html` missing** → run `python scripts/render_lessons.py` automatically once before retrying step 4.

## Boundaries

- This skill **only teaches**. It does not write lesson markdown, edit the wiki, or grade beyond the chat session.
- Never reveal `## SOLUTION` verbatim. Paraphrase only after both hints have failed.
- Never advance to the next lesson without the sentinel — the student must demonstrate mastery.
- Never modify `BACKLOG.md` (org rule).

## Files in this skill

- `SKILL.md` — this file.
- `prompts/tutor-system-prompt.md` — RTRI system prompt template (placeholders: `{lesson_title}`, `{lesson_file_contents}`).
