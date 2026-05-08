---
title: EPIRB — Balise de détresse 406 MHz
type: entity
tags: [securite, detresse]
sources: [raw/books/complete-yachtmaster-cunliffe.pdf]
related: [[securite-urgences-bord]], [[signaux-detresse], [[mmsi]]
status: draft
updated: 2026-05-07
---

**Summary:** Radiobalise de localisation d'urgence émettant sur 406 MHz vers les satellites COSPAS-SARSAT — dernier recours absolu.

## Caractéristiques techniques
- **Fréquence** : 406 MHz (satellite) + 121,5 MHz (guidage final des secours)
- **Système** : COSPAS-SARSAT (satellites géostationnaires + orbite basse)
- **Identification** : encode le MMSI du navire si enregistré auprès de l'ANFR
- **Précision** : quelques kilomètres (LEOSAR) à quelques dizaines de mètres (MEOSAR récent)

## Modes de déclenchement
1. **Manuel** : bouton d'activation direct
2. **Automatique / HRU** (Hydrostatic Release Unit) : libération automatique à ~1–4 m sous l'eau si le navire coule
3. Le dispositif **flotte** après libération automatique

## Obligations
- Enregistrement **obligatoire auprès de l'ANFR** (France) avec coordonnées du propriétaire
- Test autotest mensuel recommandé (sans émission satellite — mode test uniquement)
- Vérification de la date d'expiration de la batterie

## Voir aussi
- [[securite-urgences-bord]] — Utilisation de l'EPIRB dans le contexte d'abandon du navire
- [[mmsi]] — Numéro MMSI associé à l'EPIRB pour l'identification des secours
