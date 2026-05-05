# Permis Course — research sandbox

Isolated exploration of the LLM-wiki + interactive-course pattern, using
the *Permis Bateau* corpus at `~/Documents/Permis Bateau/` as the test
case. **Not committed** (this folder is gitignored via `research/`).

## Contents

```
permis-course/
└── PLAN.md              # end-to-end course plan, generic + Permis example
```

The `wiki-builder` skill itself lives at `.claude/skills/wiki-builder/`
(committed, org-level — not Permis-specific). This folder only holds
the Permis-flavored exploration of how to use it.

## Status

- **Test vault** lives at `/Users/williammasquelier/Documents/Permis Bateau/Wiki/`
  (outside this repo, scaffolded with 9 theme MOCs + 1 worked-example
  concept + sample questions + flashcards).
- **`PLAN.md`** sketches a five-layer stack (vault → tutor → content
  → website → multi-modal) using *Permis Bateau* as the running
  example. Generalizes to any course/curriculum.

## What to decide later

- Promote `wiki-builder` to `.claude/skills/` (org-level) vs.
  `~/.claude/skills/` (user-level personal tool).
- Whether to author the `<topic>-tutor` companion skill before or after
  the wiki-builder eval.
- Whether *Permis Bateau* warrants a dedicated `permis-bateau-tutor`
  user-level skill or stays an ad-hoc study aid.
- Whether to package the pattern (wiki-builder + tutor + content
  template) as a reusable "course-kit" plugin alongside the existing
  client plugins.

## Promotion path (when ready)

1. Run `wiki-builder` on the *Permis Bateau* folder to completion
   (full ingest of all PDFs + audio transcription).
2. Author `permis-bateau-tutor` skill at `~/.claude/skills/`.
3. First study sessions; iterate on both skills based on real use.
4. If the pattern proves out: `git mv research/permis-course/wiki-builder .claude/skills/`,
   add a catalog.json entry if applicable, link from `CLAUDE.md`.
5. Move `PLAN.md` to `infra-docs/ai/` if it becomes org-level guidance,
   or discard if superseded by the skill itself.
