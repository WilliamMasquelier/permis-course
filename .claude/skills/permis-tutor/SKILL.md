---
name: permis-tutor
description: Run a Socratic Permis Côtier teaching session — opens the rendered HTML course as an artifact, lets the student pick a lesson, then teaches it using the RTRI prompt. Triggers on /permis-tutor, "tuteur permis", "lance la leçon", "next lesson permis course".
---

# permis-tutor

Drives a Permis Côtier de Plaisance teaching session. Opens the compiled course SPA as a clickable artifact, lets the student choose which lesson to cover, then teaches Socratically in chat.

## When to use

Trigger when the student types `/permis-tutor`, asks to "start the lesson", "lance la prochaine leçon", or otherwise opens a teaching session. Do not run for read-only questions about the wiki — teaching mode owns the chat once started.

## Source files this skill reads

- `Wiki/wiki/lessons/<slug>.md` — lesson source (read into context before teaching).
- `output/permis-cours-complet.html` — compiled SPA with all lessons (Cowork mode).
- `output/lessons/<module-N>/session-N-M-slug.html` — per-lesson HTML (CLI fallback).
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

### 0. Sync latest course content

Before doing anything else, clear any stale git lock files then pull the latest content:

```bash
rm -f .git/index.lock .git/ORIG_HEAD.lock 2>/dev/null || true
git pull --ff-only origin main 2>&1
```

- **If it succeeds:** proceed silently.
- **If it fails with "not possible to fast-forward"**: run `git pull --rebase origin main` instead. If that also fails, warn once ("Contenu local modifié — utilisation de la version locale") and continue.
- **If it fails for any other reason** (no network, remote unreachable): warn once in French ("Impossible de synchroniser le contenu — session en mode hors-ligne") and continue.

Never block the session because of a sync failure.

### 1. Open the course as an artifact

**Step 1a — resolve the repo root:**
```bash
pwd
```
Store the result as `$REPO_ROOT`.

**Step 1b — ensure the compiled SPA exists:**
```bash
ls output/permis-cours-complet.html
```
If missing, build it once:
```bash
uv run python scripts/render_complete.py
```

**Step 1c — present in two ways (both, every session):**
1. Read `output/permis-cours-complet.html` and output its full contents as a Cowork **HTML artifact** so the course opens automatically in the side panel.
2. In the same response, output a clickable file link for opening in the system browser:
   ```
   [📖 Ouvrir dans le navigateur](file://$REPO_ROOT/output/permis-cours-complet.html)
   ```
   Replace `$REPO_ROOT` with the actual path from step 1a.

Output the artifact only once per session (at start or on explicit student request). The clickable link may be repeated whenever useful.

**CLI fallback (terminal-only sessions — no Cowork artifact panel):**
Derive the per-lesson HTML path from `current_lesson` using the slug convention above. Start a local HTTP server:
```bash
python -m http.server 8080 --directory output/lessons/ > /tmp/permis-server.log 2>&1 &
echo $! > /tmp/permis-server.pid
for i in $(seq 1 10); do nc -z localhost 8080 && break || sleep 0.5; done
```
Then open via Playwright MCP: `browser_navigate` to `http://localhost:8080/<module-N>/session-N-M-slug.html`. If Playwright is unavailable, print the URL and continue chat-only.

### 2. Ask the student which lesson to cover

List the available lessons in French order:
```bash
ls Wiki/wiki/lessons/module-*.md | sort
```

Ask the student: **"Quelle leçon souhaitez-vous travailler aujourd'hui ?"** and show the list (just the slugs formatted as lesson titles — read the frontmatter `title` field from each file if you want to display French titles). Let the student pick by name, number, or slug. If the student asks for a recommendation, suggest starting from the beginning (module-0-0) or the first lesson they haven't mentioned covering yet.

Confirm the chosen lesson slug (e.g. `module-1-2-regles-de-barre.md`) before proceeding.

### 3. Load lesson content + linked concepts + RTRI prompt

- Read the full content of `Wiki/wiki/lessons/<chosen_lesson>` into context.
- Extract all wikilinks of the form `[[concepts/<slug>]]` and `[[entities/<slug>]]` from the lesson file.
- For each linked slug, read the corresponding file from `Wiki/wiki/concepts/<slug>.md` or `Wiki/wiki/entities/<slug>.md` if it exists. **Do not load the entire wiki** — only directly-linked files.
- Read `.claude/skills/permis-tutor/prompts/tutor-system-prompt.md`.
- Substitute placeholders:
  - `{lesson_title}` ← title from frontmatter.
  - `{lesson_file_contents}` ← entire markdown file (including frontmatter).
- Adopt the substituted prompt as your operating instructions for the rest of the chat.

### 4. Teach the lesson (Socratic mode)

You cannot "see" what the student is reading in the SPA. Your role is a knowledgeable Q&A companion: answer the student's questions about the current lesson using the wiki + web + lesson content already in your context. Drive 3–5 reflective questions per lesson but let the student lead the pace.

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
3. **Synthesise and cite** — write a comprehensive answer in French, then list the sources at the end as clickable markdown links.

Never answer from memory alone if a wiki note or credible web source can be checked. If sources contradict each other, report both and prefer the official regulation. If genuinely uncertain, say so explicitly rather than guessing.

### 5. Signal lesson completion (optional)

When you have verified that the student understands the 3–5 key concepts (correct answers, not just engagement), output the sentinel phrase on its own line:
```
Prêt pour la suite
```
Then ask if the student wants to continue to another lesson — loop back to step 2 if yes.

**Never output `Prêt pour la suite` prematurely.** The student must have correctly demonstrated understanding of the key concepts.

### 6. Cleanup on session end

On any user exit (`/exit`, "stop", "j'arrête"):
- If running an HTTP server (CLI fallback): `kill $(cat /tmp/permis-server.pid) 2>/dev/null; rm -f /tmp/permis-server.pid`

## Error handling

- **SPA missing** (`output/permis-cours-complet.html`) → run `uv run python scripts/render_complete.py` once, then output as artifact.
- **Per-lesson HTML missing** (CLI fallback) → run `uv run python scripts/render_course.py` automatically once, then retry.
- **Lesson file missing** → halt, report which slug failed, suggest verifying `Wiki/wiki/lessons/`.
- **CLI fallback: port busy** → try 8080, 8081, 8082 in order; if all busy, print `file://` URL.
- **CLI fallback: Playwright unavailable** → print the localhost URL and continue chat-only.

## Boundaries

- This skill **only teaches**. It does not write lesson markdown, edit the wiki, or track student progress.
- Never reveal answers outright — paraphrase only after hinting twice.
- Never modify `BACKLOG.md`.

## Files in this skill

- `SKILL.md` — this file.
- `prompts/tutor-system-prompt.md` — RTRI system prompt template (placeholders: `{lesson_title}`, `{lesson_file_contents}`).
