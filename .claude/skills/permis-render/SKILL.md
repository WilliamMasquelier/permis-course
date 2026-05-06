---
name: permis-render
description: Re-render all Permis Côtier lesson HTML files, start a local HTTP server, and run Playwright visual QA on each rendered page. Triggers on /permis-render, "re-render lessons", "rebuild HTML".
---

# permis-render

Renders the lesson markdown files to HTML, starts a local preview server, and verifies each page visually via Playwright. Reports file sizes, broken image references, and a per-session QA pass/fail summary.

## When to use

Trigger when the student or developer types `/permis-render`, asks to "re-render lessons", "rebuild HTML", or needs to preview the rendered lesson pages after editing source markdown or templates. Do NOT edit any lesson markdown or wiki content — this skill is read-and-render only.

## Inputs

- `Wiki/wiki/lessons/session-*.md` — lesson source files
- `scripts/render_lessons.py` — renderer script
- `templates/permis-lesson.html.j2` — Jinja2 template
- `Wiki/assets/images/` — image assets copied to `rendered/assets/`

## Outputs

- `rendered/<slug>.html` — rendered HTML pages
- `rendered/assets/` — copied image assets
- Console report: file sizes, broken image refs, QA pass/fail per session

## Workflow

Execute these steps in order. Do not skip or reorder.

### 1. Run the renderer

Run the lesson renderer and capture its output:

```bash
source .venv/bin/activate && python scripts/render_lessons.py
```

Report the full output (file sizes, asset count). If the script exits non-zero, halt and display the error — do not proceed to QA.

### 2. Start the HTTP preview server

Start a background HTTP server with a PID file so it can be cleanly stopped:

```bash
python -m http.server 8080 --directory rendered/ > /tmp/permis-server.log 2>&1 &
echo $! > /tmp/permis-server.pid
for i in $(seq 1 10); do nc -z localhost 8080 && break || sleep 0.5; done
```

If port 8080 is already in use, kill the existing process first:
```bash
lsof -ti:8080 | xargs kill -9 2>/dev/null; sleep 0.5
```

### 3. Visual QA via Playwright

For each rendered HTML file in `rendered/session-*.html`, run the following checks using `browser_navigate` and `browser_take_screenshot`:

1. Navigate to `http://localhost:8080/<slug>.html`
2. Take a screenshot
3. Check the following (inspect page source or DOM as needed):
   - **Sidebar visible**: page contains a `<nav>` or sidebar element with lesson navigation links
   - **H1 present**: page contains at least one `<h1>` with non-empty text
   - **Dark mode on session-03**: `session-03-feux-signaux.html` must have `class="dark"` (or similar) on the `<html>` or `<body>` element — this session uses dark mode for feux/navigation light diagrams

Record pass/fail for each check per session.

### 4. Stop the HTTP server

Kill the preview server cleanly:

```bash
kill $(cat /tmp/permis-server.pid) 2>/dev/null; rm -f /tmp/permis-server.pid
```

### 5. Report findings

Output a structured report:

```
## Render Report

| File | Size (bytes) | Sidebar | H1 | Dark (s03) |
|------|-------------|---------|-----|------------|
| session-01-balisage.html | ... | ✓/✗ | ✓/✗ | n/a |
| session-02-regles-barre.html | ... | ✓/✗ | ✓/✗ | n/a |
| session-03-feux-signaux.html | ... | ✓/✗ | ✓/✗ | ✓/✗ |
| session-04-securite.html | ... | ✓/✗ | ✓/✗ | n/a |
| session-05-examen-blanc.html | ... | ✓/✗ | ✓/✗ | n/a |

### Broken image references
(list any `<img src="assets/...">` where the referenced file does not exist in `rendered/assets/`)

### Overall: PASS / FAIL
```

If any check fails, describe what was found and suggest the fix (e.g., missing frontmatter `dark_mode: true`, broken image filename).

## Boundaries

- Never edit lesson markdown files (`Wiki/wiki/lessons/`)
- Never edit wiki concept or question files
- Never modify templates unless explicitly asked
- Read-and-render only: if content issues are found, report them, do not fix them
