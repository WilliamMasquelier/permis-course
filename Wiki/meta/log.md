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
- `Cours 1/anfr-manuel_crr.pdf` → `anfr-manuel_crr.txt` (131 747 chars extracted successfully)
- `Cours 1/anfr-licence.pdf` → `anfr-licence.txt` (10 664 chars extracted successfully)

### Image-based PDFs (OCR needed — not extracted)
- `Cours 2/1-Les balises_RECTO.pdf` → 0 chars (image-based, pdfplumber returned empty)
- `Cours 2/1-Les_balises-VERSO.pdf` → 0 chars (image-based, pdfplumber returned empty)
- `Cours 2/identification_balises.pdf` → 0 chars (image-based, pdfplumber returned empty)

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
