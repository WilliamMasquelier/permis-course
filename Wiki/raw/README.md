---
title: Raw Sources
updated: 2026-05-01
---

# Raw sources (read-only)

Source material lives one level up to avoid duplicating large PDFs.
LLM and humans **read** these paths; **never modify** them.

## Course 1 — `raw/course-1/`
Theory PDFs for the *Permis Côtier* (chapters 1–7), plus annexes.

| File | Topic | Maps to theme |
|------|-------|---------------|
| `1-Permis_Cotier.pdf` … `7-Permis_Cotier.pdf` | Course chapters | Multiple — see [[../wiki/themes|themes]] |
| `1-PRATIQUE.pdf`, `Pratique_avantdépart.pdf`, `Pratique_navigation.pdf` | Practice | [[../wiki/themes/07-pratique]] |
| `7-dico_marine.pdf`, `vocabulaire.pdf` | Vocabulary | cross-cutting |
| `8-bande_300m_DK.pdf`, `zone_large.pdf` | Zones | [[../wiki/themes/09-reglementation]] |
| `Prevenir_Abordages.pdf` | COLREG | [[../wiki/themes/02-regles-de-barre]] |
| `gilet_sauvetage.pdf`, `sgmer.pdf`, `yd0532_*.pdf`, `yd0538_*.pdf` | Safety | [[../wiki/themes/05-securite]] |
| `yd-0526_*.pdf` | Buoyage | [[../wiki/themes/01-balisage]] |
| `yd0537_*.pdf` | Nautical documents | [[../wiki/themes/06-navigation]] |
| `yd-0525_*.pdf` | Recreational boating | [[../wiki/themes/09-reglementation]] |
| `Corrige_Moyens_individuels_de_reperage*.pdf` | Personal locator devices | [[../wiki/themes/05-securite]] |
| `1-Ex_candidat.pdf` | Sample exam | [[../wiki/questions]] |
| `anfr-licence.pdf`, `anfr-manuel_crr.pdf` | Radio / CRR | [[../wiki/themes/08-radio-crr]] |

## Course 2 — `raw/course-2/`
Same chapter PDFs + thematic RECTO/VERSO summary cards (most useful for
distilling) + `Q-eval.pdf` and extracted slide images for mock-exam practice.

| File | Maps to theme |
|------|---------------|
| `1-Les balises_*.pdf` | [[../wiki/themes/01-balisage]] |
| `2-regle_de_barre-*.pdf` | [[../wiki/themes/02-regles-de-barre]] |
| `3-Les_signaux-*.pdf` | [[../wiki/themes/03-signaux]] |
| `4-Feux-*.pdf` | [[../wiki/themes/04-feux]] |
| `5-securite-*.pdf` | [[../wiki/themes/05-securite]] |
| `6-La_navigation-*.pdf` | [[../wiki/themes/06-navigation]] |
| `7-La_pratique-*.pdf` | [[../wiki/themes/07-pratique]] |
| `Q-eval.pdf` | source for [[../wiki/questions]] |
| `RECTO-MER_COTIER.pdf`, `VERSO-MER_COTIER.pdf` | global cheat sheet |

## Ingest priority
1. `raw/course-2` RECTO/VERSO cards (highest signal-to-noise).
2. `raw/course-1` chapter PDFs (1–7) — fill in detail.
3. CRR manual (separate cert track).
4. Q-eval + audio drills → `questions/`.
