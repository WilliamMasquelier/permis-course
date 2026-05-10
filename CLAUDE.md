# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Repo Is

An AI-assisted self-study system for the French **Permis Plaisance Option Côtière** (coastal boat licence). It combines a curated wiki, rendered HTML lessons, spaced-repetition tracking, scenario exercises, and a mock exam, all driven by Claude Code skills.

## Commands

All Python commands use `uv run` (venv at `.venv/`):

```bash
# Render all module-based lessons to output/lessons/
uv run python scripts/render_course.py

# Render one session (by slug or "N-M" code)
uv run python scripts/render_course.py 3-2

# Dry-run: list what would render
uv run python scripts/render_course.py --check

# Serve rendered output locally
python -m http.server 8080 --directory output/lessons

# Legacy session renderer (renders to rendered/ instead of output/lessons/)
uv run python scripts/render_lessons.py

# Validate the wiki (broken links, missing frontmatter, orphaned notes)
uv run python scripts/wiki_health.py

# Lint Python files
uv run ruff check scripts/ tests/

# Type-check
uv run pyright scripts/

# Run tests
uv run pytest
```

A `PostToolUse` hook runs `ruff check` automatically after every Python file edit and blocks writes that introduce lint errors.

## Architecture

### Two parallel renderers

| Script | Source | Output | Template |
|--------|--------|--------|----------|
| `scripts/render_course.py` | `Wiki/wiki/lessons/module-N-M-slug.md` | `output/lessons/module-N/session-N-M-slug.html` + `output/lessons/index.html` | `templates/permis-course.html.j2` + `templates/permis-course-index.html.j2` |
| `scripts/render_lessons.py` | `Wiki/wiki/lessons/session-*.md` | `rendered/session-*.html` | `templates/permis-lesson.html.j2` |

`render_course.py` is the **current system**: 8 modules, 21 sessions, with a sidebar course-nav and prev/next links. `render_lessons.py` is the legacy renderer for the older `session-*.md` files; both coexist in the wiki lessons folder.

### Lesson source files (`Wiki/wiki/lessons/`)

- **Module-based** (current): `module-{N}-{M}-{slug}.md` — N=module (0–7), M=session within module.
- **Legacy sessions**: `session-NN-slug.md` — used by the old renderer.
- All files use YAML frontmatter (`title`, `module_title`, `duration_min`, `status`).
- Obsidian-style `[[wikilinks]]` and `![[image.png]]` embeds are pre-processed into HTML spans/img tags before Markdown rendering.
- Custom callout blocks (`> [SCENE]`, `> [ATTENTION]`, `> [MINI-QUIZ]`, etc.) are transformed into styled `<div class="callout …">` elements.

### Wiki knowledge base (`Wiki/wiki/`)

Atomic notes following the **Karpathy "LLM Wiki" pattern**:

- `themes/` — Map-of-Content files, one per major topic.
- `concepts/` — Zettelkasten atomic notes (one concept per file, ≤150 lines).
- `entities/` — Concrete things: buoy types, light signals, specific regulations.
- `questions/` — Exam-style Q&A with `Q:`, `A:`, `Why:`, `Source:` fields.

Every `wiki/` note requires frontmatter: `title`, `type`, `tags`, `sources`, `related`, `status` (`stub | draft | reviewed`), `updated`.

### Learner state

`Wiki/meta/student-progress.json` tracks the current lesson, completed lessons, FSRS flashcard state, and review log. Skills read/write this file to implement spaced-repetition review.

### Plugin structure

This repo is a Claude Code plugin distributed via `WilliamMasquelier/permis-course-marketplace`.

| Location | Purpose |
|----------|---------|
| `.claude-plugin/plugin.json` | Plugin manifest — consumed by Claude Code's plugin system |
| `skills/permis-*/` | **Plugin skills** — loaded when the plugin is installed in Cowork |
| `.claude/skills/permis-*/` | **Dev skills** — loaded in local Claude Code CLI sessions |

**The two `SKILL.md` files for each skill are hardlinked** (same inode). Writing to either path updates both simultaneously. Never copy between them — `cp` will report "are identical". To add a new skill, create both paths and hardlink them:

```bash
mkdir -p skills/permis-newskill .claude/skills/permis-newskill
# write the file once, then hardlink:
ln .claude/skills/permis-newskill/SKILL.md skills/permis-newskill/SKILL.md
```

**Installing in Cowork:**
```
/plugin marketplace add WilliamMasquelier/permis-course-marketplace
/plugin install permis-course
cd ~/.claude/plugins/cache/permis-course && uv sync
```

**Skills:**

| Skill | Trigger | What it does |
|-------|---------|--------------|
| `permis-tutor` | `/permis-tutor` | Socratic teaching session with FSRS flashcard review |
| `permis-render` | `/permis-render` | Re-render all lessons and run Playwright visual QA |
| `permis-scenario` | `/permis-scenario` | Branching navigation scenario with COLREGs debrief |
| `permis-exam` | `/permis-exam` | 40-question mock exam (pass threshold: 35/40) |
| `permis-setup` | `/permis-setup` | Verify prerequisites |
| `permis-author` | `/permis-author` | Teacher/author mode — edit lessons and wiki |

### Module map

```
Module 0  Prologue — Le Départ
Module 1  Le Bateau et ses Règles      (vocabulaire, règles de barre, feux/signaux)
Module 2  Lire la Mer                  (balisage IALA, carte marine, phares/amers)
Module 3  Naviguer                     (compas, marées, point estimé/GPS, routage)
Module 4  Manœuvrer                    (voile théorie, manœuvres, mouillage)
Module 5  Sécurité                     (météo, équipement, urgences, visibilité réduite)
Module 6  Radio et Réglementation      (radio VHF, réglementation)
Module 7  Épilogue et Examen Blanc
```

## Key Constraints

- **Never modify files under `raw/`** — source PDFs and extracted text are immutable.
- **Never invent regulations or distances** — mark uncertain facts as `status: stub` and note the gap in `Wiki/meta/log.md`.
- Wiki notes are never deleted; mark as `status: deprecated` with a `superseded_by` field.
- French technical terms (`tribord`, `bâbord`, `feu de tête de mât`, etc.) must stay in French. Exam questions must be in French.
- The official exam is **40 questions, 5 errors admitted** (changed June 1, 2022). Mock-exam pass threshold is **35/40**.
- Assets live in `Wiki/assets/images/` and are copied to `output/lessons/assets/` by the renderer. Do not put assets elsewhere.
