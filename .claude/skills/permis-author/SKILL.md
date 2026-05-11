---
name: permis-author
description: Expert teacher/author tool for the Permis Côtier course — add new lessons, redesign existing sessions, reorganize modules, update wiki notes, and incorporate new source material. Triggers on /permis-author, "ajouter une leçon", "modifier la leçon", "réorganiser le cours", "teacher mode", "mode auteur".
---

# permis-author

Expert authoring skill for the Permis Côtier course. Gives the teacher full write access to lesson markdown, wiki notes, and module structure. Draws on existing wiki knowledge, can do web research, and can process user-provided documents. Performs proactive parallel research (French diagrams + YouTube videos) before authoring new content. Always shows the teacher the rendered result for validation before committing.

## Repo orientation (read this if unfamiliar with the codebase)

```
permis-course/
├── Wiki/wiki/lessons/       ← 21 lesson source files (module-N-M-slug.md)
│   ├── module-0-0-prologue.md
│   ├── module-1-1-vocabulaire-bateau.md
│   └── … (through module-7-0-epilogue.md)
├── Wiki/wiki/concepts/      ← Atomic concept notes (one idea per file)
├── Wiki/wiki/entities/      ← Buoys, lights, specific regulations, etc.
├── Wiki/wiki/questions/     ← Exam-style Q&A cards
├── Wiki/wiki/themes/        ← Map-of-Content index files
├── Wiki/assets/images/      ← Images and SVG diagrams
├── Wiki/meta/
│   └── log.md               ← Authoring log (append only)
├── templates/               ← Jinja2 HTML templates
├── scripts/render_course.py ← Main renderer (module-*.md → output/lessons/)
├── scripts/render_complete.py ← SPA renderer (→ output/permis-cours-complet.html)
├── output/lessons/          ← Rendered HTML (git-tracked, always rebuild after edits)
├── output/permis-cours-complet.html ← Compiled SPA (git-tracked, always rebuild after edits)
└── raw/                     ← Source PDFs — IMMUTABLE, never touch
```

The renderer reads `Wiki/wiki/lessons/module-*.md`, processes Obsidian-style `[[wikilinks]]` and `> [CALLOUT]` blocks, and writes per-session HTML to `output/lessons/`. The SPA renderer bundles all lessons into a single `output/permis-cours-complet.html`. Always re-render both after editing any lesson file.

## The Göcek storyline

Every lesson opens with a `> [SCENE]` callout that advances a continuous Mediterranean voyage narrative. **Canonical story elements** — all must stay consistent across all 21 lessons:

| Element | Canonical value |
|---------|----------------|
| Boat name | *Deniz Rüzgarı* (le Vent de Mer) |
| Boat type | Gulet 44 pieds, acajou verni, deux mâts, voile d'artimon crème |
| Departure marina | Marina de Fethiye, Turquie |
| Sailing area | Golfe de Göcek / Skopea Limanı |
| Voyage start | Samedi 4 juillet 2026, 14h30 |
| Characters | William (learner/narrator), Emmanuel, Christelle, Rebeca |

**Any change to a story element requires a cross-lesson search.** Before editing, run:

```bash
grep -rn "Deniz Rüzgarı\|Emmanuel\|Christelle\|Rebeca\|Fethiye\|Göcek" Wiki/wiki/lessons/module-*.md
```

Replace the search terms with whatever element is changing. Apply the change to **every match** across all lesson files. A partial update breaks narrative continuity and is worse than no update.

Also check wiki notes:
```bash
grep -rn "<element>" Wiki/wiki/concepts/ Wiki/wiki/entities/ Wiki/wiki/themes/
```

After updating, run a final grep to confirm zero remaining occurrences of the old value.

## When to use

Trigger on `/permis-author`, "ajouter une leçon", "modifier la leçon", "réorganiser le cours", "teacher mode", "mode auteur", or when the user explicitly asks to edit, redesign, or restructure course content. Do NOT trigger for read-only questions or student study sessions.

## Permissions

This skill has explicit write access to:
- `Wiki/wiki/lessons/module-*.md` — lesson source files
- `Wiki/wiki/concepts/*.md` — concept notes
- `Wiki/wiki/entities/*.md` — entity notes
- `Wiki/wiki/questions/*.md` — exam Q&A notes
- `Wiki/wiki/themes/*.md` — map-of-content files
- `Wiki/meta/log.md` — authoring log

It must NOT modify:
- `raw/` — source PDFs and extracted text are immutable
- `BACKLOG.md`

## Workflow

### 0. Sync and open the course

**Step 0a — clear stale git lock files, then pull:**
```bash
rm -f .git/index.lock .git/ORIG_HEAD.lock 2>/dev/null || true
git pull --rebase origin main 2>&1
```

If the pull reports conflicts, stop and tell the teacher before proceeding. If there are local uncommitted changes (`git status --short` is non-empty), ask the teacher whether to stash them or commit them first.

Report what was pulled (e.g. "Up to date" or "Pulled 3 commits").

**Step 0b — open the course as an artifact** so the teacher sees the current state before making changes:

```bash
pwd  # store as $REPO_ROOT
ls output/permis-cours-complet.html
```

If the SPA is missing, build it first: `uv run python scripts/render_complete.py`

Then:
1. Read `output/permis-cours-complet.html` and output its full contents as a Cowork **HTML artifact**.
2. Output a clickable link for the system browser:
   ```
   [📖 Ouvrir dans le navigateur](file://$REPO_ROOT/output/permis-cours-complet.html)
   ```

### 1. Establish intent

Ask the teacher (if not already clear) which of these modes applies:

| Mode | What it means |
|------|--------------|
| **Add** | Create a brand-new lesson session |
| **Redesign** | Rewrite or substantially restructure an existing session |
| **Reorganize** | Move sessions between modules, split/merge sessions, renumber |
| **Update wiki** | Add or update concept/entity/question notes |
| **Incorporate source** | Process a user-provided document or URL and extract new content |
| **Story change** | Modify a character name, boat name, location, or other storyline element |

A single invocation may cover multiple modes (e.g. "add a lesson and update the wiki notes it depends on").

### 2. Load context

Before writing anything:

- Read the relevant existing lesson files (if redesigning or reorganizing).
- Read directly linked wiki concept/entity files.
- Run `ls Wiki/wiki/lessons/module-*.md | sort` to see the current module structure.
- For story changes: run the cross-lesson grep described in the "Göcek storyline" section above before touching anything.

### 3. Source material and parallel research

The teacher may provide additional source material in any of these ways:

- **Pasted text** — extract and incorporate inline.
- **File path** — read the file directly (PDF, text, markdown).
- **URL** — fetch the page content with WebFetch; summarize and extract relevant facts.
- **Web research request** — use WebSearch to find authoritative sources (official SHOM publications, legifrance.gouv.fr for regulations, météo-France for weather content). Always cite sources in wiki notes (`sources:` frontmatter field).

**Never invent regulations, distances, or signal specifications.** If uncertain, mark the note `status: stub` and add a gap note to `Wiki/meta/log.md`.

#### 3a. Parallel concept research (mandatory when adding or redesigning a lesson)

Before writing any lesson content, launch **two parallel WebSearch calls** in the same response turn to find supporting resources. Do this in parallel — do not wait for one before starting the other.

**Search 1 — French diagrams and schemas:**
```
WebSearch: schéma {topic} navigation permis côtier site:shom.fr OR site:ffvoile.fr OR site:service-public.fr OR site:meteofrance.fr
```
Also try: `WebSearch: "{topic}" schéma navigation plaisance français filetype:svg OR filetype:png`

For each promising result: fetch the page with `WebFetch` to confirm the image is publicly accessible and correctly described. Prefer official sources (SHOM, IALA, legifrance, Météo-France, recognised navigation publishers).

- **If a freely-licensed or official image is found:** embed it as a markdown link in the lesson body (do not copy the binary into the repo unless it is clearly public domain):
  ```markdown
  [![Description de l'image](URL_de_l_image)](URL_de_la_page_source)
  *Source : [Nom de la source](URL_de_la_page_source)*
  ```
- **If no suitable image is found online:** create an SVG diagram in `Wiki/assets/images/` using standard shapes and embed with `![[image-name.svg|Alt text]]`.

Never hotlink images from sources that forbid it. When in doubt, link to the page rather than the image directly.

**Search 2 — French YouTube educational videos:**
```
WebSearch: site:youtube.com "{topic}" permis côtier navigation français
```
Also try: `WebSearch: youtube.com "{topic}" plaisance côtière explication français`

For each candidate video, **all three criteria must pass before embedding:**
- The video is in French (or clearly subtitled) and pitched at recreational sailors, not professional mariners.
- The content directly covers the lesson concept — not just tangentially related.
- The channel is credible: official maritime authority, recognised sailing school, or established navigation publisher. Avoid anonymous uploads with no description or low production quality.

Fetch the YouTube page with `WebFetch` to confirm the title, channel name, and approximate duration.

- **If a video passes all three checks:** embed a clearly labelled callout in the lesson body:
  ```markdown
  > [VIDÉO] **{Title}**
  > [▶ Regarder sur YouTube](https://www.youtube.com/watch?v=XXXXXX) — *Chaîne : {Channel} ({duration} min)*
  ```
- **If no video passes:** skip the embed. Never embed a video just because it vaguely matches the topic.

Limit to **one YouTube embed per lesson section** to avoid cluttering the lesson flow.

**After both searches complete:** present findings to the teacher in a short summary:
- Diagrams found: list titles and source URLs, or note "aucun schéma libre trouvé → création SVG prévue".
- Videos found: list title / channel / duration for each passing candidate, or note "aucune vidéo retenue".

**Wait for the teacher's confirmation** on which resources to include before writing lesson content. The teacher may approve all, select specific items, or ask for further research.

### 4. Authoring rules

#### Lesson file format (`Wiki/wiki/lessons/module-N-M-slug.md`)

All lesson files require this frontmatter:
```yaml
---
title: "Title in French"
module: N
module_title: "Module Title"
session_in_module: M
duration_min: 30
type: lesson
status: draft
updated: YYYY-MM-DD
---
```

Lesson body structure:
- Open with a `> [SCENE]` callout establishing the Göcek/Mediterranean storyline context.
- Use regular `##` sections for content — no special CONCEPT/TASK/HINT/SOLUTION markers needed.
- Use `> [ATTENTION]` callouts for safety-critical warnings.
- Use `> [MINI-QUIZ]` callouts for embedded self-check questions (optional, used sparingly).
- Use `[[concepts/slug]]` and `[[entities/slug]]` wikilinks throughout.
- Use `![[image-name.svg|Alt text]]` for image embeds (assets in `Wiki/assets/images/`).
- French technical terms must stay in French throughout.
- Exam-relevant facts should be bolded.

#### Numbering when adding sessions

- `module-N-M-slug.md` where N = module number (0–7), M = session within module (1-based, 0 only for module 0 prologue and module 7 epilogue).
- If inserting between existing sessions, renumber subsequent sessions and update all inter-lesson references.
- After renumbering, re-derive HTML filenames (`session-N-M-slug.html`) — the renderer uses the frontmatter `module` and `session_in_module` fields, not just the filename.

#### Wiki note format (`Wiki/wiki/concepts/slug.md`, etc.)

```yaml
---
title: "Concept Title"
type: concept          # or entity, question, theme
tags: [tag1, tag2]
sources: ["source citation"]
related: ["concepts/other-slug"]
status: draft          # stub | draft | reviewed
updated: YYYY-MM-DD
---
```

Notes must be ≤ 150 lines. If longer, split into multiple atomic notes.

Never delete wiki notes — if a note is superseded, add:
```yaml
status: deprecated
superseded_by: concepts/new-slug
```

#### Exam question format (`Wiki/wiki/questions/slug.md`)

```
Q: The question text in French?
A: The answer in French.
Why: Explanation of the underlying rule or reasoning.
Source: Official source citation.
```

### 5. After writing — validate with teacher before committing

After any substantive changes to lesson files:

**Step 5.1 — render both outputs:**
```bash
uv run python scripts/render_course.py
uv run python scripts/render_complete.py
```
For a single session only (faster, use when touching one session):
```bash
uv run python scripts/render_course.py N-M  # e.g. 1-2
```
Then still run the full SPA rebuild so the artifact reflects the change:
```bash
uv run python scripts/render_complete.py
```

If the render fails, fix the issue (usually frontmatter or broken wikilink syntax) before proceeding.

**Step 5.2 — show the teacher for validation:**

Read `output/permis-cours-complet.html` and output it as a Cowork **HTML artifact**, plus the browser link:
```
[📖 Ouvrir dans le navigateur](file://$REPO_ROOT/output/permis-cours-complet.html)
```

Then ask the teacher:

> **"Les modifications ci-dessus vous conviennent-elles ? Répondez oui pour publier, ou indiquez ce qui doit changer."**

- If the teacher requests changes: loop back to step 4, apply changes, re-render, re-show.
- If the teacher approves: proceed to step 5.3.

*For trivial edits (log entry, typo fix with no layout impact): skip the validation loop and go straight to 5.3.*

**Step 5.3 — log the change:**

Append an entry to `Wiki/meta/log.md`:
```
YYYY-MM-DD — [Author] — Added/revised module-N-M-slug: brief summary of what changed and why.
```

**Step 5.4 — commit and push:**

```bash
# Clear stale lock files before staging
rm -f .git/index.lock .git/ORIG_HEAD.lock 2>/dev/null || true

# Stage only course content and rendered output — never secrets or runtime files
git add Wiki/wiki/ Wiki/meta/log.md Wiki/assets/ output/lessons/ output/permis-cours-complet.html
git status --short
```

Build the commit message from what was actually changed, then commit:
```bash
git commit -m "$(cat <<'EOF'
feat(lessons): ✨ <one-line summary of what was added/changed>

<Optional 2-3 sentence body: what changed and why, in English.>

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>
EOF
)"
```

Push immediately:
```bash
git push origin main
```

If `git push` is rejected (diverged remote), pull first then push:
```bash
rm -f .git/index.lock .git/ORIG_HEAD.lock 2>/dev/null || true
git pull --rebase origin main && git push origin main
```

Report the pushed commit SHA to the teacher so they know the content is live.
**Never leave content changes uncommitted or unpushed.** The teacher should not need to run any git command manually.

**Step 5.5 — show updated course as artifact:**

After the successful push, re-open the course as artifact so the teacher sees the published state:

1. Read `output/permis-cours-complet.html` and output as HTML artifact.
2. Output the browser link: `[📖 Ouvrir dans le navigateur](file://$REPO_ROOT/output/permis-cours-complet.html)`

### 6. Reorganization checklist

When moving or renumbering sessions:

- [ ] Rename source files
- [ ] Update `module`, `session_in_module` frontmatter in moved files
- [ ] Update `prev`/`next` references if any exist in the lesson body
- [ ] Run full render: `uv run python scripts/render_course.py && uv run python scripts/render_complete.py`
- [ ] Verify `output/lessons/index.html` reflects the new order
- [ ] Show the teacher the artifact and confirm before committing

## Error handling

- **Render fails after edit** — diagnose from the renderer output; most common causes are malformed frontmatter YAML, unmatched callout markers (`> [ATTENTION]` without closing), or missing image files.
- **Wiki link target missing** — create a stub note for the missing concept/entity rather than leaving a broken link.
- **Source document is a PDF** — use the Read tool to extract text; for scanned PDFs (image-only), note the limitation and ask the teacher to paste the relevant text.
- **Regulatory uncertainty** — always err on the side of `status: stub` + log entry rather than guessing.
- **Push rejected** — run `rm -f .git/index.lock .git/ORIG_HEAD.lock 2>/dev/null || true && git pull --rebase origin main` then retry push. If rebase conflicts appear, resolve them before pushing.
- **Git lock files** — if any git command errors with "index.lock exists", run `rm -f .git/index.lock .git/ORIG_HEAD.lock 2>/dev/null || true` and retry.

## Boundaries

- Never modify `raw/` files.
- Never invent regulations, distances, or signal specifications.
- Never delete wiki notes — deprecate instead.
- French technical terms must stay in French in all lesson and wiki content.
