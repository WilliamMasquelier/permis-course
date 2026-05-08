---
title: Position par relèvements et lignes de position
type: concept
tags: [navigation]
sources: [raw/books/complete-yachtmaster-cunliffe.pdf]
related: [[navigation-relevements-et-caps]], [[carte-marine]], [[aide-navigation-phares]]
status: draft
updated: 2026-05-07
---

**Summary:** Obtenir un point constaté par lignes de position (transit, relèvement compas, sonde, distance) ; évaluer la qualité du point (chapeau triangulaire).

> Ce fichier enrichit [[navigation-relevements-et-caps]] (compas, variation, déviation pour le permis côtier) avec les méthodes classiques de point constaté.

## Principe de la ligne de position (LOP)

Une **ligne de position (LDP)** est une ligne sur laquelle le navire se trouve à un instant donné. Elle est labellisée avec **une flèche** à l'extrémité éloignée de l'objet. L'intersection de **trois LDP** donne le point constaté.

## Sources de lignes de position

### 1. Transit (alignement)
Deux objets repérés à la carte alignés visuellement : la ligne qui les relie, prolongée vers la mer, est une LDP **exacte** (plus précise que le GPS ou un relèvement compas).

- Transits officiels (ferons, balises de chenal) : le cap est imprimé sur la carte
- Transits naturels : clocher aligné avec pointe de quai, falaise alignée avec bouée, etc.
- **Règle d'or** : toujours utiliser les transits en priorité quand ils existent

### 2. Relèvement compas (compass bearing)
Relever un amer avec le compas à main (bearing compass). Convertir en degrés vrais si la carte est en degrés vrais. La LDP est tracée depuis l'objet vers le navire.

Précision : 3° d'erreur → 90 m de déplacement latéral à 1 mille ; 450 m à 10 milles.

### 3. Sonde de profondeur (depth sounding)
La sonde de l'écho-sondeur, corrigée pour la hauteur de marée, donne une LDP = l'isobathe correspondante sur la carte. Utile comme deuxième LDP quand les relèvements visuels sont limités.

### 4. Distance angulaire (cercle de position)
- Distance à la levée d'un phare (rising/dipping distance) calculée depuis l'almanach + hauteur d'œil → LDP circulaire
- Angle vertical au sextant sur un phare de hauteur connue → distance précise

### 5. Secteurs et limites de feux
L'entrée ou la sortie d'un secteur coloré d'un phare fournit une LDP tracée sur la carte.

## Le point à trois relèvements — chapeau triangulaire

Trois LDP forment rarement un point unique → elles délimitent un **chapeau triangulaire** (cocked hat).

**Règle de sécurité** : si un coin du chapeau est plus proche d'un danger que les autres, se placer dans ce coin pour les calculs — toujours adopter le pire cas.

| Qualité du chapeau | Interprétation |
|-------------------|----------------|
| Très petit | Point de bonne qualité |
| Moyen | Acceptable si loin des dangers |
| Grand | Reprendre les relèvements — vérifier la variation, l'identification des amers |

## Point par relèvement progressif (running fix)

Quand un seul amer est disponible :
1. Relever l'amer à ~45° sur l'avant (noter heure, loch)
2. Attendre un bon angle de coupure (l'amer est à ~90°), relever à nouveau
3. **Transporter** la première LDP : partir d'un point estimé sur la première LDP, tracer le PE depuis ce point, puis déplacer la première LDP parallèlement pour couper le PE
4. Intersection de la LDP transportée avec la deuxième LDP = running fix
5. Vérifier la sonde

## Évaluation de la qualité d'un point

La précision d'un point dépend de :
- La distance à l'amer (plus c'est proche, mieux c'est)
- L'angle de coupure entre les LDP (idéalement 60°–120°)
- La qualité de l'identification des amers
- L'état de la mer (plate = meilleure précision)

**Même le GPS n'est fiable que si la carte est exacte.** Vérifier le datum (WGS84 pour la plupart des cartes modernes).

## Termes français / anglais

| Terme français | Terme anglais |
|----------------|---------------|
| Ligne de position (LDP) | Position line (PL) |
| Transit / alignement | Transit / range |
| Relèvement | Bearing |
| Chapeau triangulaire | Cocked hat |
| Point constaté | Fix |
| Angle de coupure | Angle of cut |
| Point par relèvement progressif | Running fix |
| LDP transportée | Transferred position line (TPL) |

## Voir aussi
- [[navigation-relevements-et-caps]] — Compas, variation et déviation (niveau permis côtier)
- [[navigation-estime]] — PE comme base avant le point constaté
- [[aide-navigation-phares]] — Identification des phares et secteurs
