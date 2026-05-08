---
title: Educational use cases
updated: 2026-05-01
---

# Leveraging this wiki for teaching

The vault was built so an LLM can use it as durable, structured
memory — but the same structure makes it a strong **teaching artifact**.
Here is how to use it in an educational context, ordered by leverage.

## 1. Personal study (the obvious one)

- **Read the theme MOC** to orient → drill into linked concepts → finish
  with `wiki/questions/`. The progressive disclosure (theme → concept →
  entity → question) mirrors how a teacher actually walks a student
  through a chapter.
- Ask the LLM: *"Quiz me on theme 04 (feux). 10 questions, increasing
  difficulty, French. After each answer, cite the concept note."* The
  citations let the student verify rather than trust.
- Spaced repetition: pipe `output/flashcards/*.md` into Anki / Mochi.

## 2. Tutor agent (highest leverage for solo learners)

Build a small Claude/Codex skill that:

1. Loads `SCHEMA.md` + `meta/index.md` as system context.
2. Picks an unmastered topic from a `meta/progress.md` ledger.
3. Runs a **Socratic loop**: ask, evaluate the student's answer against
   the linked concept note, give the citation, log the result.
4. After N rounds, generates a **personalized study guide** in
   `output/study-guides/` listing the student's weak spots with links
   into the wiki.

Why this works: the wiki is the *curriculum*; the agent is just a
patient examiner that always cites its source. No hallucinated rules.

## 3. Worked-example generator

Ask the LLM to generate **scenarios** from concept combinations:

> "Combine [[regle-de-barre-priorite]] + [[feux-base]] + [[zones-navigation]]
> into a night-time crossing scenario near a TSS, in French, with a
> branching decision tree."

These plug directly into theory + practical exam prep. The wiki provides
the constraints; the LLM provides the narrative. Save winners to
`output/scenarios/`.

## 4. Group teaching — instructor mode

For an instructor running a class:

- **Lecture outline**: open a theme MOC; the linked concept titles are
  the slide-by-slide structure.
- **Live cold-call**: ask the LLM to generate one question per concept,
  rotated per session — repeatable infinite, never stale.
- **Per-student dashboards**: maintain `meta/students/<name>.md` with
  weak-link tags; the LLM produces individualized homework from
  `wiki/questions/`.
- **Mock exam**: ask for "40 questions, strict exam mode, maximum 5
  errors." The wiki gives it the tag structure to sample deterministically
  from the local question bank.

## 5. Re-use as a downstream skill (Stromy/Cowork pattern)

This vault can graduate from a personal artifact to a **reusable Claude
Code skill**:

```
.claude/skills/permis-bateau-tutor/
├── SKILL.md              # how to invoke the tutor loop
├── references/
│   ├── schema.md         # copy of Wiki/SCHEMA.md
│   └── themes-index.md   # copy of meta/index.md
└── scripts/
    └── quiz.py           # picks question, tracks progress
```

Triggers: *"quiz me on permis", "explain règle de barre", "scenario MOB
night"*. The skill loads the relevant theme MOC into context (cheap),
not the whole vault. This is the same progressive-disclosure pattern
your repo already uses for `/m365-manager`, `/website-builder` etc.

Strong fit because:
- The wiki is **already structured** — no preprocessing required.
- Sources stay in `raw/`, so the skill can quote primary material
  without re-OCRing PDFs every call.
- The pattern transfers: any structured curriculum (driving theory,
  CFA prep, sailing logbook, language certifications) can use the same
  vault layout — fork this vault, swap `raw/`, regenerate `wiki/`.

## 6. Multi-modal extension

The `raw/course-2/Q-eval/` slide images and any future audio transcripts can
be turned into an oral/visual question bank. A natural pipeline:

1. OCR or transcribe each item → `raw/extracted-text/` or `raw/audio-transcripts/<n>.md`.
2. LLM ingests each transcript, classifies it by theme tag, writes one
   `questions/<theme>-<n>.md` per item.
3. Auto-link to the concept note that justifies the answer.

Result: a question bank cross-referenced to the wiki — the student can
practice oral, then click into the *why* without breaking flow.

## 7. Failure modes to design around

- **Stale wiki**: if the LLM updates concepts but the student never
  reviews, errors compound. Mitigation: `status: stub|draft|reviewed`
  field + a periodic lint pass surfacing un-reviewed notes.
- **Drift from official text**: regulations change (RIPAM amendments,
  ANFR procedures). Mitigation: keep `sources:` as exact paths, run a
  yearly diff against fresh source PDFs.
- **Over-helpful tutor**: an LLM that hands out answers undermines
  learning. Design the tutor agent to *withhold* the answer until the
  student commits — Socratic, not encyclopedic.
- **French/English mixing**: keep test questions purely in French to
  match exam phrasing; explanations can be bilingual.

## TL;DR

The wiki is curriculum-as-data. The most valuable downstream is a
**Socratic tutor skill** that draws all its content from the vault
(no hallucination, full citations) and tracks progress per student.
Everything else — flashcards, scenarios, lecture outlines, mock
exams — falls out of the same structure for free.
