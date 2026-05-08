---
title: Marées — hauteurs et calculs
type: concept
tags: [navigation]
sources: [raw/books/complete-yachtmaster-cunliffe.pdf]
related: [[navigation-coordonnees-et-distances]]
status: draft
updated: 2026-05-07
---

**Summary:** Comprendre les définitions de la marée, lire les tables de marée, calculer les hauteurs intermédiaires par la méthode des courbes ou la règle des douzièmes.

## Pourquoi les hauteurs de marée sont importantes

- **Franchir une barre** (crossing a bar) : calculer la hauteur minimale nécessaire (tirant d'eau + garde sous la quille + hauteur d'assèchement)
- **Passer sous un pont** : la hauteur libre sous un pont est donnée à partir de la **PHMA** (Plus Haute Mer Astronomique / HAT)
- **Mouiller** : calculer la profondeur à basse mer pour ne pas s'échouer
- **Entrer dans un port à basse eau** : les ports peu profonds nécessitent d'attendre un certain niveau

## Définitions (Tidal definitions)

| Terme français | Terme anglais | Définition |
|----------------|---------------|------------|
| Zéro hydrographique (ZH) | Chart Datum (CD) | Niveau de référence des cartes — niveau de la Plus Basse Mer Astronomique |
| PBMA | LAT (Lowest Astronomical Tide) | Plus basse mer astronomique possible |
| PHMA | HAT (Highest Astronomical Tide) | Plus haute mer astronomique possible |
| Pleine mer | High Water (HW) | Niveau maximal d'une marée donnée |
| Basse mer | Low Water (LW) | Niveau minimal d'une marée donnée |
| Marnage | Tidal range | Différence entre PM et BM d'une même marée |
| PMVE | MHWS (Mean High Water Springs) | Hauteur moyenne de PM de vive-eau |
| PMME | MHWN (Mean High Water Neaps) | Hauteur moyenne de PM de morte-eau |
| BMME | MLWN (Mean Low Water Neaps) | Hauteur moyenne de BM de morte-eau |
| BMVE | MLWS (Mean Low Water Springs) | Hauteur moyenne de BM de vive-eau |
| Vive-eau | Spring tide | Grande marée (près de la pleine ou nouvelle lune) |
| Morte-eau | Neap tide | Petite marée (demi-lune) |
| Hauteur de marée | Height of tide | Hauteur au-dessus du ZH à un instant donné |

## Tables de marée (Tide tables)

Les annuaires nautiques (Bloc Mémo, Imray Almanach, SHOM) donnent pour chaque jour les **heures et hauteurs** des pleines mers et basses mers aux **ports de référence** (ports standards).

**Attention aux heures :** les tables sont souvent en Temps Universel (UTC/UT). En France, ajouter +1 h en heure d'hiver et +2 h en heure d'été (CEST).

### Ports secondaires (Secondary ports)

Un port secondaire est défini par rapport à un port de référence. Les annuaires donnent :
- **Différences de temps** : à ajouter ou soustraire à l'heure du port de référence
- **Différences de hauteur** : à ajouter ou soustraire à la hauteur du port de référence (en PM et BM de VE/ME)

Si le marnage du jour est entre vive-eau et morte-eau, il faut **interpoler** la correction.

## Méthode des courbes de marée (Tidal curves method)

Utilisée pour les ports où la marée ne suit pas la règle des douzièmes. Les annuaires fournissent une courbe pour chaque port standard.

**Procédure :**
1. Déterminer l'heure et la hauteur de PM et BM du jour
2. Calculer le marnage du jour (PM − BM)
3. Comparer avec les marnages de référence VE/ME pour choisir la courbe (ou interpoler)
4. Tracer la "droite du jour" sur la courbe reliant BM à PM
5. Pour trouver la **hauteur à une heure donnée** : remonter de l'heure vers la courbe, puis horizontalement jusqu'à la droite du jour, puis verticalement vers l'échelle des hauteurs
6. Pour trouver **l'heure pour une hauteur donnée** : partir de la hauteur sur l'échelle, aller horizontalement à la droite du jour, puis à la courbe, puis descendre vers l'axe des temps

## Règle des douzièmes (Rule of Twelfths)

Dans les ports où la marée suit une courbe sinusoïdale, la montée (et la descente) suit la progression suivante sur 6 heures :

| Heure | Fraction du marnage montant (ou descendant) |
|-------|---------------------------------------------|
| 1re heure | 1/12 |
| 2e heure | 2/12 |
| 3e heure | 3/12 |
| 4e heure | 3/12 |
| 5e heure | 2/12 |
| 6e heure | 1/12 |

Moyen mnémotechnique : **1-2-3-3-2-1**

**Exemple :** BM à 15h00 = 1,0 m, PM à 21h00 = 5,8 m (marnage = 4,8 m). À 17h00 (2 heures après BM) : hauteur = 1,0 + (1/12 + 2/12) × 4,8 = 1,0 + 1,2 = **2,2 m**

## Facteurs non astronomiques

La pression atmosphérique modifie les hauteurs :
- 34 hPa de plus que la pression standard → marée abaissée de 0,3 m
- Vents prolongés d'offshore → drainent la marée
- Vents d'onshore prolongés → surcote

## Voir aussi
- [[courants-de-maree]] — Courants de marée, losanges, portes
