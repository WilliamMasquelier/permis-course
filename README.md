# Permis Côtier Course

Local AI-assisted course for the French **Permis Plaisance Option Côtière**.
The repo combines a structured Obsidian-style wiki, rendered HTML lessons,
Claude Code skills, spaced-repetition state, scenarios, and a mock exam flow.

## What It Does

- Teaches the course through `/permis-tutor`.
- Opens rendered lesson pages from `rendered/`.
- Tracks learner progress in `Wiki/meta/student-progress.json`.
- Generates scenario exercises with `/permis-scenario`.
- Runs a 40-question mock exam with `/permis-exam`.
- Maintains the underlying curriculum in `Wiki/wiki/`.

## Quick Start

```text
/permis-setup
/permis-tutor
```

If lesson HTML is missing or stale:

```text
/permis-render
```

## Repository Layout

```text
raw/                  Original course inputs and extracted text
Wiki/                 Curated learning wiki and learner state
Wiki/wiki/lessons/    Source Markdown for learner-facing lessons
Wiki/assets/images/   Visual assets copied into rendered HTML
rendered/             Generated HTML lesson pages
scripts/              Renderers, validators, and legacy extraction helpers
templates/            HTML templates
docs/                 Maintainer and source-freshness documentation
.claude/skills/       Claude Code slash-command skills
```

## Current Exam Model

The official theory exam changed on **June 1, 2022** from 30 to 40 questions.
Current official guidance says the exam has **40 questions** and **5 errors
are admitted**. This repo therefore uses **35/40** as the mock-exam pass
threshold.

See [docs/source-freshness.md](docs/source-freshness.md) for the official
sources and last verification date.

## Intended Use

Use this as a study companion, not as a legal source. The tutor and lessons
should always cite or trace back to wiki notes and raw source material. For
exam registration, eligibility, fees, and regulatory changes, rely on current
official sources from the French Ministry of the Sea and ANFR.

## Maintenance

- Keep raw material under `raw/`; do not put course inputs at repo root.
- Update `docs/source-freshness.md` when checking official rules.
- Run the wiki health check before trusting new generated content.
- Promote wiki notes from `draft` to `reviewed` only after human/source review.
