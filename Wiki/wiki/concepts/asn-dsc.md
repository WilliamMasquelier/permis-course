---
title: ASN / DSC — Appel Sélectif Numérique
type: concept
tags: [radio, crr, asn, dsc, vhf]
sources: [../../raw/../Cours 1/anfr-manuel_crr.pdf]
related: [[../themes/08-radio-crr]], [[mmsi]], [[canaux-vhf]], [[procedure-mayday]], [[procedure-pan-pan]]
status: draft
updated: 2026-05-06
---

**Summary:** L'ASN (en anglais DSC : Digital Selective Calling) est un système de communication numérique automatique sur la voie 70 (VHF). Il permet d'envoyer des alertes de détresse avec position GPS, MMSI et nature de la détresse sans parler — le message se transmet en quelques secondes à 1 200 bauds.

## Principe

L'ASN module l'onde radio avec des valeurs binaires "0" et "1" à **1 200 bauds**. Le message prédéfini est décodé et affiché sur l'écran du récepteur. Toutes les communications ASN passent sur la **voie 70** (156,525 MHz).

## La voie 70 — règles absolues

- **Jamais de radiotéléphonie** sur la voie 70 (uniquement signaux ASN).
- Interdiction d'émettre des tests sur la voie 70 — utiliser la **fonction test interne** du menu.
- L'équipement doit assurer une **veille efficace en permanence** sur la voie 70.
- Toute émission pouvant brouiller les voies 70 ou 16 est **interdite**.

## Catégories d'appel ASN

| Catégorie | Usage |
|-----------|-------|
| DISTRESS | Alerte de détresse |
| URGENCY | Urgence |
| SAFETY | Sécurité |
| ROUTINE | Communication de routine, correspondance publique |

## Types de formats d'appel

| Format | Description |
|--------|-------------|
| ALL SHIPS | Appel à tous les navires |
| INDIVIDUAL | Appel à un navire particulier (par MMSI) |
| GROUP | Appel à un groupe de navires |

## VHF ASN — équipements

- **Classe A/B** : deux antennes (VHF principale + récepteur de veille sur voie 70), clavier de saisie complet.
- **Classe D** : modèle simplifié pour navires non soumis aux règles internationales, souvent une seule antenne. C'est le modèle courant en plaisance.

## Alertes de détresse ASN — fonctionnement détaillé

### Contenu d'une alerte de détresse

Obligatoire :
- MMSI du navire
- Position (GPS si couplé, sinon saisie manuelle)

Optionnel :
- Nature de la détresse (voir liste ci-dessous)
- Heure UTC de la détresse
- Classe d'émission pour le trafic ultérieur

### Natures de détresse disponibles

| Français | Anglais |
|----------|---------|
| Indéterminée | UNDESIGNATED |
| Incendie / explosion | FIRE, EXPLOSION |
| Voie d'eau | FLOODING |
| Abordage | COLLISION |
| Échouement | GROUNDING |
| Gîte / danger de chavirement | LISTING, IN DANGER OF CAPSIZING |
| Navire coule | SINKING |
| Navire désemparé et à la dérive | DISABLE AND ADRIFT |
| Abandon de navire | ABANDONING SHIP |
| Homme à la mer | MAN OVERBOARD |
| Piraterie / agression armée | PIRACY/ARMED ROBBERY ATTACK |

### Méthode simple (bouton rouge)

Appuyer **≥ 5 secondes** sur le bouton rouge de détresse → l'alerte est transmise avec nature UNDESIGNATED et position GPS (si disponible).

### Méthode détaillée (menu)

1. Sélectionner CALL → DISTRESS
2. Choisir la nature de la détresse
3. Vérifier / corriger la position et l'heure
4. Confirmer SEND

### Après l'envoi

La VHF renvoie l'alerte automatiquement toutes les **4 minutes** jusqu'à accusé de réception. Dès réception d'un accusé (généralement de la station côtière en ASN sur la voie 70) : l'émission s'arrête, passer sur la voie 16 pour le message vocal de détresse.

## Accusé de réception d'une alerte de détresse

En général, c'est **la station côtière** qui accuse réception immédiatement, en ASN sur la voie 70, format ALL SHIPS.

- Si une station côtière accuse réception avant le renouvellement : passer à l'écoute de la voie 16.
- Si **aucune station** n'a accusé réception après la deuxième alerte :
  - Classe A/B : accuser réception sur la voie 70 en ASN.
  - Classe D : sélectionner la voie 16 et accuser réception en radiotéléphonie.

## Correspondance publique par ASN

La voie 70 peut aussi servir pour les communications de routine avec une station côtière (format INDIVIDUAL, catégorie ROUTINE, télécommande DUPLEX). La station côtière répond avec la voie de trafic à utiliser.

## Points d'examen

- Ne jamais émettre en radiotéléphonie sur la voie 70.
- Le MMSI doit être **programmé à l'avance** dans la VHF ASN (de préférence par un professionnel).
- La touche de détresse est protégée par un capot translucide pour éviter les fausses manœuvres.
- Toute fausse alerte doit être annulée par ASN (si possible) puis par radiotéléphonie sur la voie 16.
