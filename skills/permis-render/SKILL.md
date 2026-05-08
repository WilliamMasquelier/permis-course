---
name: permis-render
description: Re-render all Permis Côtier lesson HTML files, start a local HTTP server, and run Playwright visual QA on each rendered page. Triggers on /permis-render, "re-render lessons", "rebuild HTML".
---

# permis-render

Renders the lesson markdown files to HTML, starts a local preview server, and verifies each page visually via Playwright. Reports file sizes, broken image references, and a per-session QA pass/fail summary.

## When to use

Trigger when the student or developer types `/permis-render`, asks to "re-render lessons", "rebuild HTML", or needs to preview the rendered lesson pages after editing source markdown or templates. Do NOT edit any lesson markdown or wiki content — this skill is read-and-render only.

## Inputs

- `Wiki/wiki/lessons/module-*.md` — lesson source files
- `scripts/render_course.py` — renderer script
- `templates/permis-course.html.j2` — Jinja2 lesson template
- `templates/permis-course-index.html.j2` — Jinja2 index template
- `Wiki/assets/images/` — image assets copied to `output/lessons/assets/`

## Outputs

- `output/lessons/index.html` — course index page
- `output/lessons/module-{N}/session-{N}-{M}-{slug}.html` — rendered HTML pages
- `output/lessons/assets/` — copied image assets
- Console report: file sizes, broken image refs, QA pass/fail per session

## Workflow

Execute these steps in order. Do not skip or reorder.

### 1. Run the renderer

Run the lesson renderer and capture its output:

```bash
uv run python scripts/render_course.py
```

Report the full output (file sizes, asset count). If the script exits non-zero, halt and display the error — do not proceed to QA.

To render a single session by slug (e.g. `1-2`):
```bash
uv run python scripts/render_course.py 1-2
```

### 2. Start the HTTP preview server

Start a background HTTP server with a PID file so it can be cleanly stopped:

```bash
python -m http.server 8080 --directory output/lessons/ > /tmp/permis-server.log 2>&1 &
echo $! > /tmp/permis-server.pid
for i in $(seq 1 10); do nc -z localhost 8080 && break || sleep 0.5; done
```

If port 8080 is already in use, kill the existing process first:
```bash
lsof -ti:8080 | xargs kill -9 2>/dev/null; sleep 0.5
```

### 3. Visual QA via Playwright

For each rendered HTML file in `output/lessons/module-*/session-*.html`, run the following checks using `browser_navigate` and `browser_take_screenshot`:

1. Navigate to `http://localhost:8080/<module-N>/session-N-M-slug.html`
2. Take a screenshot
3. Check:
   - **Nav/sidebar visible**: page contains a `<nav>` or sidebar element with course navigation links
   - **H1 present**: page contains at least one `<h1>` with non-empty text
   - **Prev/next links**: page has previous and/or next session links (except first and last)
   - **Dark mode on feux/signaux sessions**: `module-1-3-feux-signaux` must have `class="dark"` (or similar) on `<html>` or `<body>` — feux sessions use dark mode for light diagrams

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

| File | Size (bytes) | Nav | H1 | Prev/Next | Dark |
|------|-------------|-----|-----|-----------|------|
| module-0/session-0-0-prologue.html | ... | ✓/✗ | ✓/✗ | ✓/✗ | n/a |
| module-1/session-1-1-vocabulaire-bateau.html | ... | ✓/✗ | ✓/✗ | ✓/✗ | n/a |
| module-1/session-1-3-feux-signaux.html | ... | ✓/✗ | ✓/✗ | ✓/✗ | ✓/✗ |
...

### Broken image references
(list any <img src="assets/..."> where the referenced file does not exist in output/lessons/assets/)

### Overall: PASS / FAIL
```

If any check fails, describe what was found and suggest the fix (e.g. missing frontmatter field, broken image filename, template issue).

## Plugin note

All file paths (`Wiki/`, `output/`, `scripts/`, `templates/`) are relative to the plugin root. Prefix shell commands with `cd "${CLAUDE_SKILL_DIR}/../.." &&`.

## Boundaries

- Never edit lesson markdown files (`Wiki/wiki/lessons/`)
- Never edit wiki concept or question files
- Never modify templates unless explicitly asked
- Read-and-render only: if content issues are found, report them, do not fix them
