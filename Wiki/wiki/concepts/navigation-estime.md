---
title: Navigation à l'estime — point estimé
type: concept
tags: [navigation]
sources: [raw/books/complete-yachtmaster-cunliffe.pdf]
related: [[cap-route-derive]], [[courants-de-maree]], [[carte-marine]]
status: draft
updated: 2026-05-07
---

**Summary:** Construire le point estimé (PE) par la méthode des vecteurs : route de l'eau (avec dérive), vecteur courant, et point estimé résultant.

## Point estimé vs point constaté

Le **point estimé (PE)** précède toujours le point constaté — c'est la base du raisonnement nautique. Un point GPS ne sort pas du néant : il confirme ou infirme le PE. Si les deux divergent, le navigateur doit comprendre pourquoi avant de continuer.

## Étape 1 — Point de navigation à l'estime (DR)

Le **Dead Reckoning (DR)** utilise uniquement :
- Le **cap compas** réellement barré (après correction variation/déviation)
- La **distance parcourue** depuis le dernier point connu (via le loch)

Tracé : une ligne au cap depuis le dernier point connu, d'une longueur proportionnelle à la distance parcourue. Symbole : une croix (+) avec un arrondi.

Le DR seul est insuffisant car il ignore la dérive et le courant.

## Étape 2 — Appliquer la dérive (leeway)

La dérive est l'angle entre le **cap barré** et la **route dans l'eau** réelle. Elle existe dès que le vent est sur le travers ou plus avant.

- Par force 4 au près : 2–3° pour un yacht de 12 m bien conçu
- Par force 6 au près serré : jusqu'à 20° pour un petit voilier à quilles bilatérales
- Par temps calme au portant : dérive négligeable

Pour estimer la dérive : observer le sillage par rapport à l'axe du bateau, ou comparer le relèvement du sillage avec le cap reciproque.

**Appliquer** : faire pivoter la route au cap barré vers le côté sous le vent du nombre de degrés estimés → on obtient la **route dans l'eau** (water track). Cette ligne porte **une flèche** à mi-longueur.

> En cas de doute par mer formée, ne jamais sous-estimer la dérive.

## Étape 3 — Vecteur courant (tide vector)

À l'extrémité de la route dans l'eau, tracer le **vecteur courant** :
- Direction = direction du courant (en degrés vrais)
- Longueur = distance qu'un objet flottant aurait parcourue dans la période considérée

Exemple : courant de 1,8 nd portant 250° → vecteur de 1,8 M dans la direction 250°.

Le vecteur courant porte **trois flèches**.

**Période standard** : calculer le PE à la fin d'une heure complète de marée — simplifie les calculs.

## Résultat — Le point estimé (PE)

Le PE se place à l'extrémité du vecteur courant. Il est symbolisé par un **triangle** avec l'heure notée.

En cas de navigation au près avec virements de bord, ne pas recalculer après chaque virement : noter les heures et distances, puis tracer un **PE composé** (compound EP) en une seule fois.

## Vérification au sondeur

Après tout PE, consulter le sondeur. Corriger la profondeur lue pour la hauteur de marée, puis comparer avec la sonde cartographiée au PE. Concordance = PE crédible ; écart important = suspecter une erreur.

## Carnet de bord (log book)

Le carnet de bord est le socle de la navigation. Entrées minimales :

| Colonne | Contenu |
|---------|---------|
| Heure | Heure du relevé |
| Loch | Distance parcourue |
| Cap barré / COG | Route réelle |
| Météo | Vent, pression |
| Position | PE ou point constaté |
| Remarques | Changements de cap, évènements notables |

En croisière : entrée toutes les heures près des dangers, toutes les 2 heures au large.

## Termes français / anglais

| Terme français | Terme anglais |
|----------------|---------------|
| Point estimé | Estimated position (EP) |
| Point de navigation à l'estime | Dead reckoning (DR) |
| Route dans l'eau | Water track |
| Dérive (par le vent) | Leeway |
| Vecteur courant | Tide vector |
| Angle de dérive | Leeway angle |
| Carnet de bord | Log book |

## Voir aussi
- [[cap-route-derive]] — Correction variation/déviation, cap vrai vs cap compas
- [[courants-de-maree]] — Données courant (losanges, atlas)
- [[navigation-relevements]] — Confirmer le PE par un point constaté
