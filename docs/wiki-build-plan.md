# Permis Bateau Wiki — Master Plan & Progress

This document tracks the phased ingestion and construction of the boat license wiki.

## Phased Implementation Plan

- [x] **Phase 1: Housekeeping & Infrastructure**
  - [x] Delete all audio `.mp3` files to free space.
  - [x] Create `Wiki/assets/images/` directory.
  - [x] Initialize `Wiki/meta/log.md`.
  - [x] Set up this wiki build plan.
- [x] **Phase 2: Visual Wiring POC & Balisage Ingestion**
  - [x] Extract key images from `1-Les balises_RECTO.pdf` (Fragments extracted to `Wiki/assets/images/`).
  - [x] Wire images into `bouee-cardinale-*` entities and `balisage` questions (Placeholders ready).
  - [x] Process `1-Les balises_VERSO.pdf` into concepts/entities (Needs OCR pass).
  - [x] Extracted definitive buoy icons and cleared raw fragment pile.
- [x] **Phase 3: Text & Visual Ingestion (Règles de Barre & Signaux)**
  - [x] Ingest `2-regle_de_barre` RECTO/VERSO.
  - [x] Ingest `3-Les_signaux` RECTO/VERSO.
  - [x] Extract and wire visual diagrams for signals.
- [x] **Phase 4: Text & Visual Ingestion (Feux & Sécurité)**
  - [x] Ingest `4-Feux` RECTO/VERSO.
  - [x] Ingest `5-securite` RECTO/VERSO.
  - [x] Extract and wire night light (feux) patterns.
- [x] **Phase 5: Remaining Text Ingestion & Final Lint**
  - [x] Ingest `6-La_navigation` and `7-La_pratique` RECTO/VERSO.
  - [x] Final wiki lint pass and health check.

## Session Log

### 2026-05-04 — Session 1
- **Status:** Completed.
- **Actions:** Initialized master plan, cleaned up storage, and set up asset infrastructure.
- **Next:** Start visual extraction POC in Session 2.

### 2026-05-04 — Session 2
- **Status:** Completed.
- **Actions:** Cropped definitive buoy icons from PDF pages (eaux saines, danger isolé, spéciales, cardinales). Wired these images into existing concept notes. Authored new concept notes from `1-Les_balises_VERSO.pdf` (plage, musoir, chenal préféré). Cleared 14,000 raw image fragments to save space.
- **Next:** Proceed to Phase 3 (Règles de Barre & Signaux).
