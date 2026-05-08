# Ingest & Lint Log

Tracks the growth and health of the Permis Bateau wiki.

## Ingest History

- **2026-05-04**: Session 1 — Initial setup, storage cleanup, and asset directory creation.
- **2026-05-04**: Session 2 — Selected definitive buoy images from PDF scans; created and visually wired concept notes for 'plage', 'musoir', 'chenal-préféré'.
- **2026-05-05**: Session 3 — Extracted text via macOS Vision OCR for 'Règles de barre' and 'Signaux'. Authored atomic concept notes and 10+ questions. Populated theme index files.
- **2026-05-05**: Session 4 — Extracted text via macOS Vision OCR for 'Feux' and 'Sécurité'. Authored 10 concept notes covering lighting patterns and safety regulations. Generated 10 flashcards and linked them to their respective theme index files.
- **2026-05-05**: Session 5 — Extracted text via macOS Vision OCR for 'La_navigation' and 'La_pratique'. Authored 7 concept notes and 10 flashcards. Completed all theme index files.

## Lint History

- **2026-05-05**: Final Lint Pass — Checked all files for formatting and schema alignment. Project successfully ingested.

## INGEST 2026-05-06 (Phase 0.5)

### Files processed
- `raw/course-1/anfr-manuel_crr.pdf` → `anfr-manuel_crr.txt` (131 747 chars extracted successfully)
- `raw/course-1/anfr-licence.pdf` → `anfr-licence.txt` (10 664 chars extracted successfully)

### Image-based PDFs (OCR needed — not extracted)
- `raw/course-2/1-Les balises_RECTO.pdf` → 0 chars (image-based, pdfplumber returned empty)
- `raw/course-2/1-Les_balises-VERSO.pdf` → 0 chars (image-based, pdfplumber returned empty)
- `raw/course-2/identification_balises.pdf` → 0 chars (image-based, pdfplumber returned empty)

### Concept files created (7 new stubs → draft)
- `Wiki/wiki/concepts/canaux-vhf.md` — VHF channels, frequencies, simplex/duplex, veille
- `Wiki/wiki/concepts/procedure-mayday.md` — MAYDAY distress procedure (ASN + voice), relay, false alert cancellation
- `Wiki/wiki/concepts/procedure-pan-pan.md` — PAN PAN urgency + SECURITE safety procedures
- `Wiki/wiki/concepts/asn-dsc.md` — ASN/DSC digital selective calling, voie 70, distress natures, equipment classes
- `Wiki/wiki/concepts/alphabet-oaci.md` — Full ICAO phonetic alphabet table with pronunciations
- `Wiki/wiki/concepts/mmsi.md` — MMSI structure, MID codes, categories (navire/côtière/groupe), French MIDs
- `Wiki/wiki/concepts/licence-anfr.md` — Station licence (ANFR), CRR certificate, required documents, equipment conformance

### Concept files updated
- `Wiki/wiki/themes/08-radio-crr.md` — Updated status stub → draft, added coverage note

### Concept count: 59 → 66
### Entity count: 6 (unchanged)
### Question count: 44 (unchanged)

## LINT 2026-05-06 (Phase 1)
- Concept files: 66
- Entity files: 18 (was 6 — 13 new entities created)
- Question files: 44
- Stub concepts remaining: 0
- Draft concepts: 39

### Entity files created
- `bouee-danger-isole.md` — Marque de danger isolé (Fl(2), 2 sphères noires)
- `bouee-eaux-saines.md` — Marque d'eaux saines (Iso/Oc/LFl/Morse A, 1 sphère rouge)
- `bouee-speciales.md` — Marque spéciale (Fl.Y, croix jaune)
- `bouee-chenal-prefere-bb.md` — Chenal préféré passage bâbord (Fl(2+1)R)
- `bouee-chenal-prefere-tb.md` — Chenal préféré passage tribord (Fl(2+1)G)
- `feu-mat-tete.md` — Feu blanc de tête de mât, 225°
- `feu-cote-babord.md` — Feu rouge bâbord, 112,5°
- `feu-cote-tribord.md` — Feu vert tribord, 112,5°
- `feu-poupe.md` — Feu blanc de poupe, 135°
- `equipement-gilet.md` — Gilet 150N, EN ISO 12402-3
- `equipement-vhf.md` — VHF portative, canaux 16/70
- `equipement-feux-detresse.md` — Pyrotechnie, validité 3 ans

### Image refs fixed
- `bouee-cardinale-est.png` → `cardinal-marks-all.png` + caption note
- `bouee-cardinale-nord.png` → `cardinal-marks-all.png` + caption note
- `bouee-cardinale-ouest.png` → `cardinal-marks-all.png` + caption note
- `bouee-cardinale-sud.png` → `cardinal-marks-all.png` + caption note
- `bouee-laterale-babord.png` → placeholder warning (no replacement image available)
- `bouee-laterale-tribord.png` → placeholder warning (no replacement image available)

### Source paths fixed
- 62 files: removed `raw/../` pattern from `sources:` frontmatter fields

## INGEST 2026-05-07 (Books — Phase 1)

### Sources processed
- `raw/books/rya-competent-crew-extracted.txt` (OCR, référencé mais non utilisé directement pour cette session)
- `raw/books/yachtmaster-chapters/ch08-anchoring.txt`
- `raw/books/yachtmaster-chapters/ch13-aids-to-navigation.txt`
- `raw/books/yachtmaster-chapters/ch14-tidal-heights.txt`
- `raw/books/yachtmaster-chapters/ch15-tidal-streams.txt`
- `raw/books/yachtmaster-chapters/ch22-passage-planning.txt`
- `raw/books/yachtmaster-chapters/ch27-collision-avoidance.txt`
- `raw/books/yachtmaster-chapters/ch29-damage-control.txt`
- `raw/books/yachtmaster-chapters/ch30-emergencies.txt`
- `raw/books/yachtmaster-chapters/ch31-man-overboard.txt`
- `raw/books/yachtmaster-chapters/ch32-weather.txt`

### Concept files created (10 new)
- `Wiki/wiki/concepts/meteorologie-marine.md` — Dépressions frontales, fronts, brises, signes précurseurs
- `Wiki/wiki/concepts/marees-hauteurs.md` — Définitions MHWS/MHWN/MLWN/MLWS, tables, courbes, règle des douzièmes
- `Wiki/wiki/concepts/courants-de-maree.md` — Courants vs hauteurs, portes, losanges, atlas, étale
- `Wiki/wiki/concepts/mouillage-technique.md` — Types d'ancres, câbles, touée, fond, affourche, ancre embringuée
- `Wiki/wiki/concepts/planification-traversee.md` — SOLAS V, 10 étapes, DST/TSS, escales de secours
- `Wiki/wiki/concepts/aide-navigation-phares.md` — Caractéristiques des feux, secteurs, offshore/inshore
- `Wiki/wiki/concepts/securite-controle-avaries.md` — Incendie (classes A/B/C/E), jury rig, démâtage, gouvernail
- `Wiki/wiki/concepts/securite-urgences-bord.md` — Hélicoptère (Hi-line), radeau de survie, EPIRB, fusées
- `Wiki/wiki/concepts/homme-a-la-mer-manoeuvres.md` — Reach-Turn-Reach, Crash Stop, récupération à bord
- `Wiki/wiki/concepts/colreg-visibilite-reduite.md` — Règle 5 & 19, AIS, MARPA, signaux sonores brume

### Theme MOCs updated
- `Wiki/wiki/themes/06-navigation.md` — Ajout : marees-hauteurs, courants-de-maree, planification-traversee, aide-navigation-phares
- `Wiki/wiki/themes/05-securite.md` — Ajout : meteorologie-marine, securite-controle-avaries, securite-urgences-bord, homme-a-la-mer-manoeuvres
- `Wiki/wiki/themes/07-pratique.md` — Ajout : mouillage-technique, homme-a-la-mer-manoeuvres
- `Wiki/wiki/themes/02-regles-de-barre.md` — Ajout : colreg-visibilite-reduite

### Questions created (5 new)
- `Wiki/wiki/questions/navigation-06.md` — Hauteur d'eau à un port secondaire
- `Wiki/wiki/questions/navigation-07.md` — DST / Traffic Separation Scheme, Règle 10
- `Wiki/wiki/questions/securite-06.md` — Signaux sauvetage par hélicoptère
- `Wiki/wiki/questions/securite-07.md` — Touée minimale au mouillage
- `Wiki/wiki/questions/pratique-06.md` — Trois étapes immédiates homme à la mer

### Visual assets index created: Wiki/meta/visual-assets-needed.md
- 16 visuels prioritaires identifiés (diagrammes MOB, courbes de marée, dépression frontale, touée, feux phare, etc.)

## INGEST 2026-05-07 (Books — Phase 2 : ingestion complète)

### Phase A — Extraction PDF (21 chapitres restants Yachtmaster)
Tous les chapitres extraits via pdfplumber → `raw/books/yachtmaster-chapters/`:
- ch01, ch03, ch04, ch05, ch07, ch09, ch10, ch11, ch12, ch16, ch17, ch18, ch19, ch20, ch21, ch23, ch24, ch25, ch26, ch28, appendix1

### Phase B — Audit des doublons
4 paires vérifiées → décision CONSERVER (profondeurs complémentaires) :
- mouillage.md (cours) + mouillage-technique.md (Yachtmaster) → complémentaires
- pratique-homme-a-la-mer.md + homme-a-la-mer-manoeuvres.md → complémentaires
- securite-meteo-et-pression.md + meteorologie-marine.md → complémentaires
- signaux-sonores-brume.md + colreg-visibilite-reduite.md → complémentaires

### Phase C — RYA Competent Crew ingestion (3 nouveaux concepts)
- `Wiki/wiki/concepts/vocabulaire-nautique.md` — Glossaire bilingue parties du voilier
- `Wiki/wiki/concepts/veille-quart.md` — Quarts, Règle 5 COLREG, veille VHF 16
- `Wiki/wiki/concepts/accostage-amarrage.md` — Accostage, amarrage, corps-mort, mouillage

### Phase D — Yachtmaster navigation (5 nouveaux concepts)
- `Wiki/wiki/concepts/navigation-estime.md` — Point estimé, DR, dérive, vecteur courant
- `Wiki/wiki/concepts/navigation-relevements.md` — LDP, transits, chapeau triangulaire
- `Wiki/wiki/concepts/gps-cartographie-electronique.md` — GPS, datums, waypoints, charts élec.
- `Wiki/wiki/concepts/routage-navigation.md` — Cap à tenir, vecteur net, stratégie courant
- `Wiki/wiki/concepts/pilotage-cotier.md` — Route sûre, transits, clearing bearings

### Phase E — Yachtmaster seamanship (7 nouveaux concepts)
- `Wiki/wiki/concepts/voile-theorie-base.md` — Portance, vent apparent, allures
- `Wiki/wiki/concepts/voile-trim-efficace.md` — Cambrure, vrillage, pénons, prise de ris
- `Wiki/wiki/concepts/manoeuvre-voile-base.md` — Virement, empannage, mise en panne
- `Wiki/wiki/concepts/cordages-noeuds.md` — Types cordage, 7 nœuds essentiels, winch
- `Wiki/wiki/concepts/moteur-entretien.md` — Diesel, impulseur, purge, diagnostic
- `Wiki/wiki/concepts/gros-temps-tactique.md` — Préparation, mise en panne, fuite, survie
- `Wiki/wiki/concepts/brouillard-navigation.md` — Signaux Règle 35, tactiques brouillard

### Phase F — Questions (23 nouvelles questions)
- navigation-08 à navigation-12 (5 nouvelles)
- pratique-07 à pratique-11 (5 nouvelles)
- securite-08 à securite-12 (5 nouvelles)
- regles-barre-06 à regles-barre-08 (3 nouvelles)

### Phase G — Entités (8 nouvelles)
- ancre-cqr.md, ancre-bruce.md, ancre-delta.md
- extincteur-co2.md, extincteur-poudre.md
- epirb.md, balise-danbuoy.md, radeau-survie.md

### Phase H — SVGs (7 nouveaux visuels)
- mob-reach-turn-reach.svg, mob-crash-stop.svg
- marees-courbe-type.svg, marees-regle-douziemes.svg
- ancrage-touee.svg, meteo-depression-frontale.svg
- phare-secteurs-colores.svg

### Mise à jour MOCs
- 07-pratique : +14 concepts, +6 questions
- 06-navigation : +6 concepts, +7 questions
- 05-securite : +2 concepts, +7 questions
- 02-regles-de-barre : +3 questions

### Comptages finaux
- Concepts : 85 → 100
- Questions : 49 → 72 (avec sample-questions.md : 67 fichiers affichés)
- Entités : 18 → 26
- SVG : 5 → 12

## LINT 2026-05-07 (Phase 2)
- Tous les nouveaux fichiers : status draft (non stub)
- Tous les MOCs mis à jour avec liens vers nouveaux concepts
- Audit doublons effectué — aucune dépréciation requise
- 7 SVGs créés pour les visuels HIGH priority de visual-assets-needed.md
