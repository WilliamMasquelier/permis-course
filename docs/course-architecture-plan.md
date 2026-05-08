# Interactive Course Material — End-to-End Plan

How to build an interactive course from raw source material, leveraging
the stromy-org skill ecosystem, Obsidian, and adjacent tooling. Topic-
agnostic; the running example is *Permis Bateau* (`/Users/williammasquelier/Documents/Permis Bateau/`).

> Status: planning document. Not implementation. Read together with the
> existing `wiki-builder` skill (`.claude/skills/wiki-builder/SKILL.md`)
> and the experimental vault at `~/Documents/Permis Bateau/Wiki/`.

## TL;DR

```
SOURCE FOLDER ──► [wiki-builder skill]    ──► OBSIDIAN VAULT (knowledge layer)
                  Karpathy 3-folder pattern    raw/ + wiki/ + output/
                                                       │
                  ┌────────────────────────────────────┼────────────────────────────────────┐
                  │                                    │                                    │
            [<topic>-tutor skill]              [<topic>-content skill]               [Astro course site]
            Socratic exam loop                 Lecture / handout / video         (website-builder + brand)
                  │                                    │                                    │
            output/study-guides/              output/lectures/, scenarios/         /Users/.../course-site/
                  │                                    │                                    │
                  └─────────────► PROGRESS LEDGER (meta/progress.md) ◄────────────────────┘
                                  + spaced repetition export to Anki
```

Five layers, each one a step the student or instructor can stop at.

## Layer 0 — Source corpus

Where the user already is. A folder of PDFs, slides, recordings, web
archives, hand-written notes scanned to PDF. **Don't pre-process.**
Leave the source folder immutable; downstream pointers will reference
relative paths.

For *Permis Bateau*: `~/Documents/Permis Bateau/` with `raw/course-1/`,
`raw/course-2/`, plus loose admin PDFs (~70 PDFs + 139 MP3 oral drills + 1
PowerPoint).

## Layer 1 — Knowledge base (Obsidian vault)

**Skill:** `wiki-builder` (just authored, `.claude/skills/wiki-builder/`).

**Output:** `<source-folder>/Wiki/` containing the Karpathy three-folder
pattern (`raw/` pointers + `wiki/` curated atomic notes + `output/`
regenerable artifacts), plus `SCHEMA.md` and `meta/{index,log}.md`.

Build phases:
1. **Discovery** — inventory the folder, classify the corpus type.
2. **Scaffold** — generate empty vault with theme MOCs.
3. **Ingest** — turn each source PDF into atomic concept + entity notes.
4. **Question / procedure layer** — exam Q&A or runbook procedures
   depending on corpus type.
5. **Lint** — find stubs, orphans, broken links, uncovered sources.

The vault is **the durable artifact**. Everything below is regenerable
from it.

For *Permis Bateau*: 9 themes (balisage, règles de barre, signaux, feux,
sécurité, navigation, pratique, radio/CRR, réglementation), ~80–120
concept notes, ~40–60 entity notes, ~150 questions (from `Q-eval.pdf` +
audio drill transcriptions).

## Layer 2 — Tutor agent (interactive solo study)

**Skill (to author):** `<topic>-tutor` — e.g. `permis-bateau-tutor`.

A skill that turns the vault into a Socratic examiner. Loads
`SCHEMA.md` + `meta/index.md` (cheap), then progressively reads the
theme MOC and concept notes relevant to the current question.

Loop:
1. Pick an unmastered tag from `meta/progress.md`.
2. Generate one question (variant of an existing `wiki/questions/`
   item, or freshly composed from concepts).
3. **Withhold** the answer until the student commits.
4. Evaluate against the linked concept note. Cite both the concept and
   the underlying source PDF.
5. Update `meta/progress.md` (per-tag mastery score).
6. After N rounds, write a personalized study guide to
   `output/study-guides/`.

Triggers: *"quiz me on permis"*, *"explain règle de barre"*, *"weak
spots"*, *"mock exam"*.

## Layer 3 — Content generation (instructor-facing)

**Skill (to author):** `<topic>-content` — e.g. `permis-bateau-content`.

Generates lecture material from the vault for instructors or for the
student who wants alternative formats:

| Output | From | To |
|--------|------|-----|
| Lecture outlines | theme MOCs | `output/lectures/<theme>.md` |
| Speaker notes | concept summaries | embedded in lectures |
| Slide decks | lectures | `duke-strategies:pptx` skill |
| Handouts | concept + entity notes | `duke-strategies:docx` skill |
| Visual cheat sheets | entities | `duke-strategies:pdf` skill |
| Explainer videos | scenarios | `duke-strategies:remotion-video` |
| Flashcards (Anki) | questions | `output/flashcards/<theme>.md` |
| Mock exams | questions, stratified by tag | `output/quizzes/mock-<n>.md` |
| Worked scenarios | concept combinations | `output/scenarios/<n>.md` |

The `duke-strategies:*` skills already exist in the org and produce
production-quality DOCX/PPTX/PDF/video. The content skill orchestrates
them — it doesn't reimplement.

## Layer 4 — Course website (public-facing)

**Skill:** `website-builder` (already exists).

Build a course-site Astro repo at `clients/<learner>/<topic>-course/`:
- Per-theme pages generated from theme MOCs.
- Per-concept pages from concept notes.
- Embedded interactive quiz widgets backed by `wiki/questions/`.
- Search across the vault.
- Brand-driven via `client-data` charter (use `brand-builder` /
  `brand-artifact-builder`).

Hosting: Cloudflare Pages or Vercel. The site is a *read view* into the
vault — Obsidian remains the authoring tool.

For *Permis Bateau*, this is overkill for a single learner; relevant if
the same vault is published as a public study aid.

## Layer 5 — Multi-modal extensions

Optional pipelines beyond text:

- **Audio drills** (already present for *Permis Bateau*) — Whisper-
  ingest `raw/course-2/Q-eval/` and any future audio transcripts into
  `wiki/questions/`.
- **Video lessons** — `duke-strategies:remotion-video` from scenario
  notes for animated explainers.
- **Voice tutor** — Realtime API + tutor skill = oral exam practice
  in the source language.
- **Spaced repetition** — `output/flashcards/*.md` → Anki / Mochi /
  RemNote import.

## Cross-cutting: progress + telemetry

A single ledger at `Wiki/meta/progress.md`:

```yaml
---
student: william
last_session: 2026-05-04
---

## Per-tag mastery
- balisage: 0.7 (14/20)
- regles-de-barre: 0.4 (8/20)  ← weakest, drill next
- feux: 0.6 (12/20)
- ...

## Sessions
- 2026-05-04 — 12 questions, 9 correct, weak: feux-mouillage
- 2026-05-03 — 15 questions, 11 correct, weak: voilier-vs-voilier
```

Read by the tutor skill at session start. Updated at session end.
Surfaces in the content skill ("generate flashcards for my weak tags").

## Implementation order (recommended)

1. **Vault scaffold** — `wiki-builder` invocation on the source folder.
   *Hours, not days.*
2. **Manual ingest of 1–2 themes** to validate the pattern. Author 1
   worked-example concept fully (the *why* template). *2–4 hours.*
3. **LLM-assisted ingest** of the remaining themes, RECTO/VERSO cards
   first (highest signal-to-noise). *1–2 days.*
4. **Question layer** — transcribe oral drills, transcribe Q-eval. *1 day.*
5. **Tutor skill** — author `<topic>-tutor`, point it at the vault.
   *Half a day; the skill is small once the vault exists.*
6. **First study sessions** — fix the things you didn't think of until
   you used it. *Ongoing.*
7. **Content skill** — only if instructor / publishing use case appears.
   *1–2 days when needed.*
8. **Course site** — only if going public. *2–3 days, mostly brand work.*

The vault + tutor skill is the **viable minimum**. Everything else is
optional and can be deferred until the use case appears.

## Failure modes & mitigations

| Risk | Mitigation |
|------|-----------|
| LLM hallucinates regulations / facts | Mandatory `sources:` frontmatter; tutor cites every answer; lint flags uncited claims |
| Vault rots — agent ingests new sources but never re-reads old ones | Periodic lint pass surfaces stub > 7d, draft > 30d, modified-source notes |
| Tutor over-explains, student doesn't internalize | Withhold-the-answer protocol; require commit before reveal |
| Vendor lock-in to Obsidian | Markdown + wikilinks only, no proprietary syntax; vault portable to Foam / Logseq / Quartz |
| Source language drift in translation | Keep regulatory / legal / technical terms in source language; translate explanations only |
| Vault outgrows context | At 100 notes, add Smart Connections (semantic search). At 500+, migrate to RAG with vault as canonical text |
| Multiple students sharing one vault | Per-student `meta/students/<name>.md` ledgers; tutor scopes progress reads |
| Content skill stamps over the wiki | `output/` is the only write target for generated artifacts; promotion to `wiki/` is human-reviewed |

## What this plan deliberately does NOT include

- **A custom LMS.** Use the vault + tutor + Anki. Course websites should
  be content-first, not platform-first.
- **A vector database.** Skip until vault > 500 notes. Direct context
  is cheaper, simpler, more accurate.
- **A monolithic "course skill."** Skills are layered — wiki-builder,
  tutor, content, website-builder are independent and composable.
- **Live class infrastructure.** Out of scope; if needed, layer Zoom /
  Discord on top of the vault output, don't bake it into the stack.
- **Grading / certification awarding.** The vault tracks mastery; the
  *real* certification (Permis Côtier, CRR, etc.) is a separate exam
  process and stays that way.

## Topics this plan generalizes to

| Domain | Source corpus | Layer 4 site? |
|--------|---------------|---------------|
| Permis Bateau (running example) | `~/Documents/Permis Bateau/` | No (solo) |
| Belgian self-employed tax | `infra-docs/saas/Odoo.md` + deductibles refs | Internal only |
| Stromy onboarding for new collaborators | `org-docs/` + selected `infra-docs/` | Internal portal |
| Client-specific compliance training | client SOPs in `client-data/` | Per-client website |
| Language certification (DELF, TEF) | textbook PDFs + audio | Public site, brand-driven |
| Driving theory | Code de la route PDFs | Maybe |
| CFA / professional certs | curriculum PDFs + practice exams | Maybe, paid |

The skill ecosystem (wiki-builder + topic-tutor + topic-content +
website-builder + duke-strategies:*) gives you the same five layers for
any of these. Only the source corpus and brand differ.

## Next concrete action

For *Permis Bateau* specifically (the test case already started):
1. Continue the ingest pass on the 8 RECTO/VERSO summary cards in
   `raw/course-2/` — they have the highest signal-to-noise.
2. Ingest `raw/course-2/Q-eval/` slide images and any future audio transcripts into `raw/audio-transcripts/`.
3. Author `permis-bateau-tutor` skill at `~/.claude/skills/` (user-level,
   since this is a personal study aid, not an org artifact).
4. First 30-minute study session as the system test.

For everything else: the plan is on disk; pick a topic when ready.
