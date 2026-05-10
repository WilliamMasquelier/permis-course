---
name: permis-setup
description: Verify prerequisites for the Permis Côtier course. Triggers on /permis-setup.
---

# permis-setup

First-run verification skill. Checks Python venv, dependencies, rendered HTML files, and student progress file.

## When to use

Trigger on /permis-setup, vérifier l'installation, setup check, check prerequisites.

## Workflow

Execute all steps in order. Collect results, then produce the final status table.

### Step 0 - Check git sync

```bash
git fetch origin main 2>&1
git status --short
git log --oneline origin/main..HEAD 2>/dev/null | wc -l   # commits ahead
git log --oneline HEAD..origin/main 2>/dev/null | wc -l   # commits behind
```

Results:
- Behind by 0 and ahead by 0 → pass (up to date)
- Behind by N → warn: "Le dépôt local a N commit(s) de retard sur la branche distante. Lancez `git pull --rebase origin main` pour synchroniser avant de commencer."
- Uncommitted local changes → warn: list the files with `git status --short` and suggest the teacher commits or stashes them before authoring.
- `git fetch` fails (no network / no remote) → note as warning (non-blocking for local-only use).

### Step 1 - Check Python venv and dependencies

```bash
.venv/bin/python --version 2>&1
.venv/bin/python -c "import jinja2, markdown_it; print('OK')" 2>&1
```

Results:
- Python 3.13+ and OK → pass
- MISSING or import fails → instruct user to run `bash install.sh` from the repo root (installs uv + Python 3.13 + deps automatically)

### Step 2 - Check Playwright MCP

Call `browser_navigate` with URL `about:blank`.
- Succeeds → Playwright OK
- Tool unavailable → show in French:

> Le MCP Playwright n'est pas configuré. Pour l'activer :
> 1. Ouvrez les paramètres de Claude Code
> 2. Ajoutez ce serveur MCP : `npx @playwright/mcp@latest`
> 3. Redémarrez Claude Code
>
> Si vous préférez ne pas configurer Playwright, le cours fonctionne en mode texte uniquement.

Mark as warning (non-blocking) — course works without Playwright.

### Step 3 - Check rendered HTML output

Check that the compiled SPA and per-lesson files exist:

```bash
ls output/permis-cours-complet.html 2>/dev/null && echo "SPA OK" || echo "SPA MISSING"
ls output/lessons/index.html 2>/dev/null && echo "INDEX OK" || echo "INDEX MISSING"
ls output/lessons/module-*/session-*.html 2>/dev/null | wc -l
```

Expected: `output/permis-cours-complet.html` exists, `output/lessons/index.html` exists, and at least 21 session HTML files present across all modules.

If SPA or sessions missing: tell user to run `/permis-render` first (which runs `.venv/bin/python scripts/render_complete.py` and `.venv/bin/python scripts/render_course.py`).

### Step 4 - Check student-progress.json

Read `Wiki/meta/student-progress.json`.
- Missing → offer to create default:
  ```json
  { "learner": "local-user", "current_lesson": "module-0-0-prologue.md", "completed_lessons": [], "flashcards": {}, "review_log": [] }
  ```
- JSON corrupt → offer to reset to default
- Valid → OK

### Step 5 - Status report

Print in French using check/warn/cross emoji:

```
✅ Git sync - À jour (ou ⚠️ N commit(s) de retard — lancez git pull --rebase)
✅ Python + dépendances (jinja2, markdown_it) - OK
⚠️  Playwright MCP - Non configuré (mode texte uniquement)
✅ SPA cours complet (output/permis-cours-complet.html) - OK
✅ Sessions HTML (21 sessions dans output/lessons/) - OK
✅ Progression étudiant - Prêt (module-0-0-prologue)
```

If all OK or only Playwright warning:
> Tout est en ordre ! Tapez `/permis-tutor` pour commencer votre première leçon.

If any blocking failure: walk through fixes before reporting done.

## Notes

- Idempotent — safe to run multiple times.
- Playwright warning is expected. Never block on it.
- Do not modify lesson content or progress unless user asks to reset.
