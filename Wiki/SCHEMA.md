---
title: Wiki Schema
purpose: Operating instructions for any LLM working in this vault
updated: 2026-05-01
---

# Vault Schema — Permis Bateau (Permis Côtier + CRR)

This vault is an **LLM-maintained knowledge base** for studying the French
*Permis Plaisance Option Côtière* (coastal boat license) and the *CRR*
(radio operator certificate). It follows the Karpathy "LLM Wiki" pattern
adapted for educational use.

## Folder contract

| Folder | Who writes | What goes in |
|--------|-----------|--------------|
| `raw/` | **Human only** — LLM reads, never modifies | Source PDFs, extracted text, original course material. Immutable. Course packs live in `raw/course-1/` and `raw/course-2/`; extracted text lives in `raw/extracted-text/`. |
| `wiki/` | **LLM curated**, human-reviewed | Distilled atomic notes. The "clean" knowledge layer. |
| `wiki/themes/` | LLM | One MOC (Map of Content) per major topic (balisage, règle de barre, feux, signaux, sécurité, navigation, pratique, radio/CRR). |
| `wiki/concepts/` | LLM | Atomic Zettelkasten-style notes — one concept per file. |
| `wiki/entities/` | LLM | Concrete things: specific buoy types, light signals, equipment, regulations, distances. |
| `wiki/questions/` | LLM | Exam-style Q&A pairs derived from `raw/course-2` Q-eval material and course notes. |
| `output/` | LLM, ephemeral | Generated study artifacts (flashcards, quizzes, study guides). Safe to delete and regenerate. |
| `meta/` | LLM + human | `index.md`, `log.md`, this `SCHEMA.md`. |

## Note conventions

Every `wiki/` note MUST have:

```yaml
---
title: <human-readable title>
type: theme | concept | entity | question
tags: [<theme-slug>, ...]
sources: [<relative path to raw/ files used>]
related: [[<wikilink>]]
status: stub | draft | reviewed
updated: <YYYY-MM-DD>
---
```

Plus a one-line **Summary:** at the top of the body — this is what the LLM
reads first when scanning for relevance.

## Workflows

### 1. Ingest
When a new source lands in `raw/`:
1. Read it.
2. For each new concept → create a `concepts/<slug>.md` (or extend existing).
3. For each named entity (buoy type, signal, regulation article) → `entities/<slug>.md`.
4. Link back from the matching `themes/<theme>.md` MOC.
5. Append to `meta/log.md`: `INGEST <date> <file> → <notes touched>`.

### 2. Question generation
For exam prep, build `questions/<theme>-<NN>.md` items with:
- `Q:` the prompt
- `A:` the correct answer
- `Why:` the reasoning, with `[[wikilinks]]` to relevant concepts
- `Source:` exact citation in `raw/`

### 3. Health check (linting)
Run on demand. Look for:
- Stub notes older than 7 days
- Concepts with no inbound link from any theme MOC
- Entities not cited by any question
- Broken wikilinks
- Sources in `raw/` with zero coverage in `wiki/`

Append findings to `meta/log.md` under `LINT <date>`.

## Pedagogical layering (educational use)

The vault is structured for **progressive disclosure** mirroring how a
student learns:

1. **Themes** = chapter overviews (read first to orient).
2. **Concepts** = the *why* (rules, principles, mental models).
3. **Entities** = the *what* (memorize: specific buoys, lights, distances).
4. **Questions** = the *test* (active recall, exam simulation).

When generating study material, always traverse: theme → linked concepts →
linked entities → linked questions. Never jump straight to questions; the
LLM should reconstruct the conceptual chain so the student sees *why* each
answer is correct, not just *what* it is.

## Language

Source material is in **French** (legal/technical terms must stay in
French — `tribord`, `bâbord`, `feu de tête de mât`, etc.). Explanatory
prose may be bilingual French/English when it aids comprehension, but
exam-style questions must be in French to match the real test.

## What NOT to do

- Never modify files in `raw/`.
- Never invent regulations or distances — if uncertain, mark `status: stub`
  and note the gap in `log.md`.
- Never delete `wiki/` notes; mark as `status: deprecated` and keep a
  `superseded_by` field.
- Never write a `concepts/` note longer than ~150 lines — split it.
