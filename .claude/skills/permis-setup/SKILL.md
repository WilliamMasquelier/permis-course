---
name: permis-setup
description: Verify prerequisites for the Permis Côtier course. Triggers on /permis-setup.
---

# permis-setup

First-run verification skill. Checks Python venv, dependencies, Playwright MCP, rendered HTML files, and student progress file.

## When to use

Trigger on /permis-setup, vérifier l’installation, setup check, check prerequisites.

## Workflow

Execute all five steps in order. Collect results, then produce the final status table.

### Step 1 - Check Python 3.13+ and virtual environment

Run these shell checks:

    python3 --version 2>&1
    ls .venv/bin/python 2>/dev/null || echo MISSING
    source .venv/bin/activate && python -c "import jinja2, markdown_it, fsrs; print(OK)" 2>&1

Results:
- python3 3.13+ -> OK
- MISSING -> run uv sync
- import fails -> run uv sync

### Step 2 - Check Playwright MCP

Call browser_navigate with URL about:blank.
- Succeeds -> Playwright OK
- Tool unavailable -> show in French:

Le MCP Playwright n’est pas configuré. Pour l’activer :
1. Ouvrez les paramètres de Claude Code
2. Ajoutez ce serveur MCP : npx @playwright/mcp@latest
3. Redémarrez Claude Code

Si vous préférez ne pas configurer Playwright, le cours fonctionne en mode texte uniquement.

Mark as warning (non-blocking) - course works without Playwright.

### Step 3 - Check rendered HTML files

Check that all 8 session HTML files exist in rendered/:
session-01-balisage.html, session-02-regles-barre.html, session-03-feux-signaux.html,
session-04-securite.html, session-05-navigation.html, session-06-pratique-reglementation.html,
session-07-radio-vhf.html, session-08-examen-blanc.html

If any missing: tell user to run /permis-render first.

### Step 4 - Check student-progress.json

Read Wiki/meta/student-progress.json.
- Missing -> offer to create default: {learner: local-user, current_lesson: session-01-balisage.md, completed_lessons: [], flashcards: {}, review_log: []}
- JSON corrupt -> offer to reset to default
- Valid -> OK

### Step 5 - Status report

Print in French using check/warn/cross emoji:

✅ Python 3.13 - OK
✅ Dépendances Python (jinja2, markdown_it, fsrs) - OK
⚠️ Playwright MCP - Non configuré (mode texte uniquement)
✅ Fichiers HTML pré-rendus - 8 sessions présentes
✅ Progression étudiant - Prêt (session 1)

If all OK or only Playwright warning:
  Tout est en ordre ! Tapez /permis-tutor pour commencer votre première leçon.
If any blocking failure: walk through fixes first.

## Notes

- Idempotent - safe to run multiple times.
- Playwright warning is expected. Never block on it.
- Do not modify lesson content or progress unless user asks to reset.
