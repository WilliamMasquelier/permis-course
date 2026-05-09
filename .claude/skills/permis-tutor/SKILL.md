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
    "current_lesson": "module-0-0-prologue.md",
    "completed_lessons": [],
    "flashcards": { "concepts/marques-cardinales": { "due": "2026-05-06T00:00:00Z", "stability": 1, "difficulty": 5, "reps": 0 } },
    "review_log": []
  }
  ```
- `Wiki/wiki/lessons/<slug>.md` — current lesson source (read into context before teaching).
- `output/permis-cours-complet.html` — monolithic SPA with all 21 lessons (Cowork mode, created by `scripts/render_complete.py`).
- `output/lessons/<module-N>/session-N-M-slug.html` — per-lesson rendered page (CLI fallback, created by `scripts/render_course.py`).
- `.claude/skills/permis-tutor/prompts/tutor-system-prompt.md` — RTRI system prompt template.

## Slug conventions

Lesson source files follow the pattern `module-{N}-{M}-{slug}.md` (e.g. `module-1-1-vocabulaire-bateau.md`).

To derive the HTML URL from a source filename:
1. Strip `.md` → `module-1-1-vocabulaire-bateau`
2. Extract N (first digit after `module-`) → `1`
3. Replace `module-` prefix with `session-` → `session-1-1-vocabulaire-bateau`
4. URL path: `module-1/session-1-1-vocabulaire-bateau.html`

Full URL example: `http://localhost:8080/module-1/session-1-1-vocabulaire-bateau.html`

## Workflow

Execute these steps in order. Do not skip steps; do not reorder.

### 1. Load progress and resolve current lesson

- Read `Wiki/meta/student-progress.json`.
- If the file is missing, create it with the default state:
  ```json
  { "learner": "local-user", "current_lesson": "module-0-0-prologue.md", "completed_lessons": [], "flashcards": {}, "review_log": [] }
  ```
- Identify `current_lesson` (e.g. `module-0-0-prologue.md`).
- Confirm the lesson file exists at `Wiki/wiki/lessons/<current_lesson>`. If not, halt and report.

### 2. Run a quick FSRS review round (max 10 cards)

- Compute `now = current ISO 8601 UTC timestamp`.
- Filter `flashcards` for entries where `due <= now`.
- Take **at most 10** due cards (oldest `due` first). If none, skip to step 3.
- Tell the student: « Avant de commencer, petite révision rapide — N carte(s) à revoir. »
- For each card:
  1. Ask the question (the card's slug labels the concept; pose a recall question on it).
  2. Wait for the student's answer.
  3. **You (Claude) rate the answer** — do not ask the student to rate it:
     - **4 (Easy)** — correct, immediate recall, confident
     - **3 (Good)** — correct with normal effort
     - **2 (Hard)** — partially correct or hesitated significantly
     - **1 (Again)** — wrong or blank
     Give brief encouraging feedback, then move to the next card.
  4. Update the card in `student-progress.json`:
     - Increment `reps`.
     - Apply a simple FSRS-lite update: `stability *= {0.5, 1.0, 1.5, 2.5}[rating-1]`; clamp ≥ 0.5.
     - Set `due = now + stability days`.
     - Append a row to `review_log`: `{ "concept": "<slug>", "rating": <n>, "ts": "<now>" }`.
- Save `student-progress.json` after each card (resilient to crashes).
- Cap the round at 10 cards even if more are due.

### 3. Present the lesson visually

**Cowork is the primary tutor environment.** Always open the compiled SPA here first.

**Step 3a — resolve the absolute path of the repo root:**
```bash
pwd
```
Store the result as `$REPO_ROOT` for use in links below.

**Step 3b — check for the compiled SPA:**
```bash
ls output/permis-cours-complet.html
```
- **If it exists:** use it as-is. **Do NOT re-run any render script** — the file is already compiled.
- **If missing:** run once: `uv run python scripts/render_complete.py`, then proceed.

**Step 3c — present it in two ways (both every time):**
1. Output the full file contents as a Cowork **HTML artifact** so the lesson panel opens automatically.
2. In the same response, output a clickable markdown link in chat:
   ```
   [📖 Ouvrir le cours complet]($REPO_ROOT/output/permis-cours-complet.html)
   ```
   Replace `$REPO_ROOT` with the actual absolute path obtained in step 3a.

Output the artifact only once per session (at lesson start or on explicit student request). Do not re-output it when advancing to the next lesson — the SPA stays open in the artifact panel. The clickable link may be repeated whenever useful.

Do not start an HTTP server or use Playwright in Cowork mode.

**CLI fallback (terminal-only sessions):**
Derive the per-lesson HTML path from `current_lesson` using the slug convention above.
Build the full filesystem path: `output/lessons/<module-N>/session-N-M-slug.html`.
If the HTML file does not exist, run `uv run python scripts/render_course.py` once to generate it.
Start a local HTTP server:
```bash
python -m http.server 8080 --directory output/lessons/ > /tmp/permis-server.log 2>&1 &
echo $! > /tmp/permis-server.pid
for i in $(seq 1 10); do nc -z localhost 8080 && break || sleep 0.5; done
```
Then open via Playwright MCP: `browser_navigate` to `http://localhost:8080/<module-N>/session-N-M-slug.html`.
If Playwright is unavailable, print the URL and continue chat-only.

### 5. Load lesson content + linked concepts + RTRI prompt

- Read the full content of `Wiki/wiki/lessons/<current_lesson>` into context.
- Extract all wikilinks of the form `[[concepts/<slug>]]` and `[[entities/<slug>]]` from anywhere in the lesson file.
- For each linked slug, read the corresponding file from `Wiki/wiki/concepts/<slug>.md` or `Wiki/wiki/entities/<slug>.md` if it exists. Load each into context. **Do not load the entire wiki** — only directly-linked files.
- Read `.claude/skills/permis-tutor/prompts/tutor-system-prompt.md`.
- Substitute placeholders:
  - `{lesson_title}` ← title from frontmatter.
  - `{lesson_file_contents}` ← entire markdown file (including frontmatter).
- Adopt the substituted prompt as your operating instructions for the rest of the chat.

### 6. Teach the lesson (Socratic mode)

- Greet the student in French. Confirm the lesson title.
- Walk through the lesson content section by section using questions — never lecturing outright. Reference wikilinks with `[[concepts/<slug>]]` notation when explaining why an answer is correct.
- Derive 3–5 key concepts from the lesson content to probe: use section headings and bolded terms as your guide.
- When the student struggles, offer a hint framed as a narrower question. After a second failed exchange, paraphrase the answer as a statement and ask a follow-up question to confirm understanding.
- Watch for common misconceptions (e.g. inverting bâbord/tribord, confusing cardinal and lateral marks) and redirect proactively.
- End **every** response with exactly one reflective question.

#### Answering student questions comprehensively

Whenever the student asks a factual, regulatory, or conceptual question (outside the main Socratic flow), apply this **three-source protocol** before answering:

1. **Wiki first** — search `Wiki/wiki/concepts/`, `Wiki/wiki/entities/`, and `Wiki/wiki/themes/` for relevant notes. Read every file that could bear on the question.
2. **Online research** — use `WebSearch` to find authoritative sources (SHOM, legifrance.gouv.fr, météo-France, official IALA documents, recognised sailing/navigation publishers). Fetch the most relevant page with `WebFetch` to extract precise wording.
3. **Synthesise and cite** — write a comprehensive answer in French, then list the sources at the end as clickable markdown links (e.g. `[legifrance.gouv.fr – Arrêté du …](https://…)`).

Never answer from memory alone if a wiki note or credible web source can be checked. If sources contradict each other, report both and prefer the official regulation. If genuinely uncertain, say so explicitly rather than guessing.

### 7. Advance the lesson when mastery is demonstrated

When you have verified that the student understands the 3–5 key concepts you identified (correct answers, not just engagement), execute the following sequence **all in the same response turn**:

1. Output the sentinel phrase on its own line:
   ```
   Prêt pour la suite
   ```
2. Immediately — in the same turn, without waiting — call Bash to update `Wiki/meta/student-progress.json`:
   - Append `current_lesson` slug (without `.md`) to `completed_lessons`.
   - Create FSRS flashcards for every `concepts/...` or `entities/...` wikilink found in the lesson. For each not already in `flashcards`:
     ```json
     { "due": "<now_iso_utc>", "stability": 1, "difficulty": 5, "reps": 0 }
     ```
   - Set `current_lesson` to the next `module-*.md` in alphabetical order from `Wiki/wiki/lessons/`, or `null` if all lessons are done.
   - Save the file.
3. If running an HTTP server (CLI fallback): `kill $(cat /tmp/permis-server.pid) 2>/dev/null; rm -f /tmp/permis-server.pid`
4. If a next lesson exists:
   - Announce: « Session terminée — on enchaîne sur la suivante. »
   - Present the next lesson visually (step 3 — artifact or HTTP server depending on mode).
5. If no lessons remain:
   - Congratulate the student in French.
   - Suggest `/permis-exam` for the mock exam.

**Never output `Prêt pour la suite` prematurely.** The student must have correctly demonstrated understanding of the key concepts. "I think I understand" does not qualify.

### 8. Cleanup on session end

On any user exit (`/exit`, "stop", "j'arrête"), or abnormal termination:
- If running an HTTP server (CLI fallback): `kill $(cat /tmp/permis-server.pid) 2>/dev/null; rm -f /tmp/permis-server.pid`
- Save `student-progress.json` one final time.

## Error handling

- **SPA missing** (`output/permis-cours-complet.html`) → run `uv run python scripts/render_complete.py` once, then output as artifact.
- **Per-lesson HTML missing** (CLI fallback) → run `uv run python scripts/render_course.py` automatically once, then retry.
- **`student-progress.json` missing** → create it with the default state shown in step 1.
- **Lesson file missing** → halt, report which slug failed, suggest running `uv run python scripts/render_course.py` and verifying `Wiki/wiki/lessons/`.
- **CLI fallback: port busy** → try 8080, 8081, 8082 in order; if all busy, print `file://` URL.
- **CLI fallback: Playwright unavailable** → print the localhost URL and continue chat-only.

## Boundaries

- This skill **only teaches**. It does not write lesson markdown, edit the wiki, or grade beyond the chat session.
- Never reveal answers outright — paraphrase only after hinting twice.
- Never advance to the next lesson without the sentinel — the student must demonstrate mastery.
- Never modify `BACKLOG.md` (org rule).

## Files in this skill

- `SKILL.md` — this file.
- `prompts/tutor-system-prompt.md` — RTRI system prompt template (placeholders: `{lesson_title}`, `{lesson_file_contents}`).
