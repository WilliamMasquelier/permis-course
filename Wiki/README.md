# Permis Bateau — Obsidian LLM Wiki

LLM-maintained knowledge base for the French *Permis Plaisance Option
Côtière* + CRR radio certificate.

## Open in Obsidian
Open `Wiki/` as a vault. Obsidian will create `.obsidian/` on first launch.
Recommended community plugins (none required, all optional):

- **Smart Connections** — semantic search over notes (offline, fast).
- **Copilot for Obsidian** (logancyang) — chat with vault, point at any
  OpenAI/Anthropic/Ollama model.
- **Dataview** — query frontmatter (e.g. all `status: stub` notes).
- **Templater** — bind concept/entity templates to hotkeys.

## Layout

```
Wiki/
├── SCHEMA.md              # operating contract for the LLM
├── README.md              # this file
├── EDUCATIONAL-USE.md     # how to teach with this vault
├── meta/
│   ├── index.md           # entry point — start here
│   └── log.md             # ingest / lint history
├── raw/                   # read-only pointer to ../Cours 1, ../Cours 2
├── wiki/                  # LLM-curated knowledge
│   ├── themes/            # 9 MOCs (chapter overviews)
│   ├── concepts/          # atomic Zettelkasten notes (the why)
│   ├── entities/          # memorize-this items (the what)
│   └── questions/         # exam-style Q&A
└── output/                # generated artifacts (regenerable)
    ├── flashcards/
    ├── quizzes/
    └── study-guides/
```

## Design principles (from research)

1. **Three-folder pattern** (Karpathy / `obsidian-wiki`): `raw/` immutable
   sources, `wiki/` LLM-curated knowledge, `output/` regenerable artifacts.
2. **SCHEMA.md as contract**: a single file the LLM reads first, telling
   it folder roles, frontmatter conventions, and workflows.
3. **Frontmatter-first**: every note has `summary`, `tags`, `sources`,
   `status` so an agent can scan relevance without reading the body.
4. **Markdown + wikilinks**: vendor-free, future-proof, Git-diffable.
5. **Direct vault read until ~100 notes**: a 200K-token context handles
   the whole vault in one pass — no RAG plumbing needed yet. Add
   embeddings (Smart Connections) only when the vault outgrows context.
6. **Clean vault / messy vault separation**: `wiki/` is the trusted
   archive. If letting an agent free-roam, write to `output/` first,
   promote to `wiki/` on review.
7. **Educational layering**: theme → concept → entity → question is
   pedagogical, not arbitrary — see `EDUCATIONAL-USE.md`.

## Current state

- 9 theme MOCs (stubs, ready for ingest).
- 1 worked-example concept (`regle-de-barre-priorite`) demonstrating
  the full pattern.
- 1 sample question file showing the Q/A/Why/Source format.
- 1 sample flashcard set in `output/`.

## Next steps for a full build

1. Pass each `Cours 2/*RECTO/VERSO*.pdf` through an LLM with `SCHEMA.md`
   in context → produces ~10 concepts and ~5 entities per theme.
2. Transcribe `Cours 2/*.mp3` (139 files) → ingest into `questions/`.
3. Run a lint pass (find `status: stub` notes older than 7 days).
4. Promote stable concepts from `draft` to `reviewed`.
5. Build the tutor skill (see `EDUCATIONAL-USE.md` §5).

## Sources informing this design

Key references that shaped the structure:

- Karpathy's `llm-wiki` gist and the `obsidian-wiki` framework.
- "Karpathy's Obsidian RAG Killed My Vector Database" (Mejba Ahmed).
- "Scaling LLM Knowledge Bases" (devjournal — when RAG becomes necessary).
- Obsidian's own guidance on PARA / Zettelkasten + AI plugins
  (Smart Connections, Copilot for Obsidian, InsightA).
