---
name: permis-author
description: Expert teacher/author tool for the Permis Côtier course — add new lessons, redesign existing sessions, reorganize modules, update wiki notes, and incorporate new source material. Triggers on /permis-author, "ajouter une leçon", "modifier la leçon", "réorganiser le cours", "teacher mode", "mode auteur".
---

# permis-author

Expert authoring skill for the Permis Côtier course. Gives the teacher full write access to lesson markdown, wiki notes, and module structure. Draws on existing wiki knowledge, can do web research, and can process user-provided documents. Always triggers a render + QA pass after substantive changes.

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
- `Wiki/meta/student-progress.json` — student state (only the tutor skill owns this)
- `BACKLOG.md`

## Workflow

### 1. Establish intent

Ask the teacher (if not already clear) which of these modes applies:

| Mode | What it means |
|------|--------------|
| **Add** | Create a brand-new lesson session |
| **Redesign** | Rewrite or substantially restructure an existing session |
| **Reorganize** | Move sessions between modules, split/merge sessions, renumber |
| **Update wiki** | Add or update concept/entity/question notes |
| **Incorporate source** | Process a user-provided document or URL and extract new content |

A single invocation may cover multiple modes (e.g. "add a lesson and update the wiki notes it depends on").

### 2. Load context

Before writing anything:

- Read `Wiki/meta/student-progress.json` to know which lessons are already completed by the student — avoid restructuring completed lessons unless the teacher explicitly accepts the risk.
- Read the relevant existing lesson files (if redesigning or reorganizing).
- Read directly linked wiki concept/entity files.
- Run `ls Wiki/wiki/lessons/module-*.md | sort` to see the current module structure.

### 3. Source material

The teacher may provide additional source material in any of these ways:

- **Pasted text** — extract and incorporate inline.
- **File path** — read the file directly (PDF, text, markdown).
- **URL** — fetch the page content with WebFetch; summarize and extract relevant facts.
- **Web research request** — use WebSearch to find authoritative sources (official SHOM publications, legifrance.gouv.fr for regulations, météo-France for weather content). Always cite sources in wiki notes (`sources:` frontmatter field).

**Never invent regulations, distances, or signal specifications.** If uncertain, mark the note `status: stub` and add a gap note to `Wiki/meta/log.md`.

#### 3a. Finding diagrams and illustrations

When a lesson would benefit from a visual aid (buoy shapes, light sectors, tacking diagram, tide curve, etc.):

1. Use `WebSearch` with terms like `"IALA lateral marks diagram site:shom.fr"` or `"règles de barre COLREGs schéma"`. Prefer official sources (SHOM, IALA, legifrance, Météo-France, recognised navigation publishers).
2. Fetch the page with `WebFetch` to confirm the image is publicly accessible and correctly described.
3. **If a suitable freely-licensed or official image is found:** embed it as a markdown link in the lesson body (do not copy the binary into the repo unless it is clearly public domain):
   ```markdown
   [![Description de l'image](URL_de_l_image)](URL_de_la_page_source)
   *Source : [Nom de la source](URL_de_la_page_source)*
   ```
4. **If no suitable image is found online:** create an SVG diagram in `Wiki/assets/images/` using standard shapes and embed with `![[image-name.svg|Alt text]]`.

Never hotlink images from sources that forbid it. When in doubt, link to the page rather than the image directly.

#### 3b. Finding and embedding YouTube videos

When a short video could reinforce a concept (e.g. a knot tutorial, a marina manoeuvre demonstration, a meteorology explainer):

1. Use `WebSearch` to find candidate videos: e.g. `"site:youtube.com permis côtier balises IALA"` or `"youtube.com/watch matelotage nœud de cabestan"`.
2. **Relevance check — all three criteria must pass before embedding:**
   - The video is in French (or clearly subtitled) and at the appropriate level (recreational sailor, not professional mariner).
   - The video content directly covers the lesson concept — not just tangentially related.
   - The channel is credible: official maritime authority, recognised sailing school, or established sailing/navigation publisher. Avoid anonymous uploads with no description.
3. Fetch the YouTube page with `WebFetch` to confirm the title, channel, and approximate duration.
4. **If the video passes all three checks:** embed a clearly labelled markdown link in the lesson body inside a `> [SCENE]` or dedicated callout, e.g.:
   ```markdown
   > [VIDÉO] **Comprendre le balisage IALA en 5 minutes**
   > [▶ Regarder sur YouTube](https://www.youtube.com/watch?v=XXXXXX) — *Chaîne : École de voile XYZ (5 min)*
   ```
5. **If no video passes the relevance check:** skip the embed. Never embed a video just because it vaguely matches the topic.

Limit to **one YouTube embed per lesson section** to avoid cluttering the lesson flow.

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
- Use regular `##` sections for content — no special CONCEPT/TASK/HINT/SOLUTION markers needed (the tutor skill derives these from content organically).
- Use `> [ATTENTION]` callouts for safety-critical warnings.
- Use `> [MINI-QUIZ]` callouts for embedded self-check questions (optional, used sparingly).
- Use `[[concepts/slug]]` and `[[entities/slug]]` wikilinks throughout — these become FSRS flashcard seeds.
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

### 5. After writing

After any substantive changes to lesson files:

1. Run the renderer to verify the new/modified lesson renders cleanly:
   ```bash
   uv run python scripts/render_course.py
   ```
   For a single session (e.g. module 1, session 2):
   ```bash
   uv run python scripts/render_course.py 1-2
   ```
2. If the render fails, fix the issue (usually frontmatter or broken wikilink syntax) before reporting done.
3. Optionally open the rendered page via Playwright to visually confirm layout — especially for lessons with complex callouts, tables, or image embeds.
4. Append an entry to `Wiki/meta/log.md`:
   ```
   YYYY-MM-DD — [Author] — Added/revised module-N-M-slug: brief summary of what changed and why.
   ```
5. **Commit and push all changes** (mandatory — do this automatically, no user action required):

   ```bash
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
   git pull --rebase origin main && git push origin main
   ```

   Report the pushed commit SHA to the user so they know the content is live.
   **Never leave content changes uncommitted or unpushed.** The author should not need to run any git command manually.

### 6. Reorganization checklist

When moving or renumbering sessions:

- [ ] Rename source files
- [ ] Update `module`, `session_in_module` frontmatter in moved files
- [ ] Update `prev`/`next` references if any exist in the lesson body
- [ ] Run full render: `uv run python scripts/render_course.py`
- [ ] Verify `output/lessons/index.html` reflects the new order
- [ ] Check `Wiki/meta/student-progress.json` — if the student has completed moved lessons, the slugs in `completed_lessons` will need updating

## Error handling

- **Render fails after edit** — diagnose from the renderer output; most common causes are malformed frontmatter YAML, unmatched callout markers (`> [ATTENTION]` without closing), or missing image files.
- **Wiki link target missing** — create a stub note for the missing concept/entity rather than leaving a broken link.
- **Source document is a PDF** — use the Read tool to extract text; for scanned PDFs (image-only), note the limitation and ask the teacher to paste the relevant text.
- **Regulatory uncertainty** — always err on the side of `status: stub` + log entry rather than guessing.

## Boundaries

- Never modify `raw/` files.
- Never modify `Wiki/meta/student-progress.json`.
- Never invent regulations, distances, or signal specifications.
- Never delete wiki notes — deprecate instead.
- French technical terms must stay in French in all lesson and wiki content.
