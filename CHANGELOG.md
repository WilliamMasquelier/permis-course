# Changelog

All notable changes to the **permis-course** plugin are documented in this file.
Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and the project uses semantic versioning.

## [0.4.0] — 2026-05-10

Major content + character refresh based on a full pedagogical review.

### Added
- **Character bible** (Emmanuel, William, Christelle, Rebeca) — distinct voices, verbal tics, growth arcs documented in `docs/improvement-plan.md`.
- **Three narrative landmines** planted across Modules 2–4 and detonated in Modules 3, 4, and the epilogue (Trébeurden buoy mistake, GPS waypoint near-miss at Yassıca, dragged anchor at Hamam Koyu).
- **"Ce qui aurait pu mal tourner"** recap section in epilogue (`module-7-0-epilogue.md`).
- **Technical content depth**:
  - Compass deviation — *méthode du tour* swing procedure (`module-3-1`).
  - Heavy weather tactics — *mise à la cape* and *fuite devant* (`module-5-3`).
  - Tonnage rule beyond RIPAM (`module-1-2`).
  - Worked example — port secondaire de Roscoff (`module-3-2`).
- **Five new pedagogical SVGs** authored and embedded:
  - `prop-walk.svg` — propeller walk top-down (lesson 4-2).
  - `amarrage-spring-lines.svg` — six-line dock layout (lesson 4-2).
  - `feux-vue-skipper.svg` — 4-panel skipper POV at night with COLREGs verdict (lesson 1-3).
  - `synoptic-chart-fronts.svg` — simplified synoptic chart with warm + cold fronts (lesson 5-1).
  - `passage-plan-butterfly-valley.svg` — applied passage plan with waypoints, hazards, clearing bearing (lesson 3-4).
- **Animated Knots links** as `[VIDÉO]` callouts for the 5 essential knots in `module-1-1`.
- `[ATTENTION]` callouts added to `module-5-3-urgences.md` and `module-6-2-reglementation.md`.

### Changed
- **Mehmet removed** from the entire course — Emmanuel is now the sole expert sailor onboard.
- **Rebeca rewritten** in Painter / Crew / Swimmer rotation; Spanish + French-learning voice; positive vibrant tone replacing the prior deflating Caribbean comparisons.
- **Christelle** layered with intuitive sensory observations; pivotal weather-by-feel beat in `module-5-1`.
- **William** narrator voice tightened — analytical/quantitative modelling-aloud tic; explicit growth arc through the GPS error in 3-3.
- **Emmanuel** given an electronics-impatience flaw used twice (3-3 chartplotter freeze, 6-1 DSC admission).
- **Lesson 3-2** opening scene tightened from 14 lines to 8.
- **Lesson 3-4** opening scene expanded with the buoy-hesitation moment.
- **Lesson 4-3** restructured with arrival + night drag scene to anchor the touée 5:1 lesson.
- **`permis-tutor` skill** — clarified SPA-output once-per-session contract (no re-emit on lesson advance); Socratic mode reframed as Q&A companion since the tutor cannot see what the student is reading; step 5 re-execution required on lesson advance.
- **`permis-exam` skill** — theme distribution corrected to total 40 questions (was 35).
- **`permis-scenario` skill** — domain-mapping table updated from legacy `session-NN-*` slugs to current `module-N-M-*` slugs; previously broken silently for current students.

### Fixed
- **Critical: epilogue Mini-Quiz Q1** — IALA A vs IALA B inversion. The final wrap-up quiz was teaching the wrong rule for French waters. Now correctly tests *« rouge à gauche en entrant »*.
- **Lesson 3-2** — duplicate image embeds removed (`tidal-curve.svg` / `rule-of-twelfths.svg` were duplicates of French-named files; misplaced `ancrage-touee.svg` reference cleaned up).

### Documentation
- `docs/improvement-plan.md` — full implementation plan retained for reference.
- `Wiki/meta/visual-assets-needed.md` — V1, V2, V3, V5, V6 marked done.
- `Wiki/meta/log.md` — REWORK 2026-05-10 and REWORK 2026-05-10b entries.

## [0.3.0]

Initial public release — 21 sessions, 8 modules, Göcek storyline, FSRS tutor, scenario, mock exam.
