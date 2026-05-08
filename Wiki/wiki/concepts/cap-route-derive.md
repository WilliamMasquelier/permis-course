---
title: Cap, route, dérive et relèvement
type: concept
tags: [navigation]
sources: [raw/course-2/6-La_navigation-RECTO.pdf]
related: [[carte-marine]], [[latitude-longitude]]
status: draft
updated: 2026-05-01
---

**Summary:** Le cap (direction de la proue) diffère de la route surface (trajet réel) à cause de la dérive (vent) et du courant ; les relèvements se convertissent entre compas, magnétique et vrai.

## Terminologie

| Terme | Définition |
|-------|-----------|
| **Cap vrai (Cv)** | Direction du navire tracée sur la carte (référence Nord vrai) |
| **Cap compas (Cc)** | Cap lu sur le compas de bord |
| **Cap magnétique (Cm)** | Cap corrigé de la déviation (d) du compas |
| **Dérive** | Angle entre le cap vrai et la route surface (dû au vent) |
| **Route surface (Rs)** | Rs = Cv + dérive (trajet réel de la surface) |
| **Route fond (Rf)** | Trajet réel par rapport au fond, tenant compte du courant |

## Dérive due au vent

- Vent sur le travers **tribord** → pousse sur **bâbord** → dérive **négative**
- Vent sur le travers **bâbord** → pousse sur **tribord** → dérive **positive**
- **Rs = Cap vrai + dérive** (ex : Cv 40° + dérive −40° = Rs 0° = Nord)

## Effet du courant

- Le courant modifie la route surface pour donner la **route fond**
- Vecteur route fond = vecteur route surface + vecteur courant
- Pour tenir compte du courant, le navigateur ajuste son cap vrai en conséquence

## Relèvements : types et conversions

| Symbole | Type | Pris par |
|---------|------|---------|
| **Zc** | Relèvement compas | Compas de relèvement, depuis un navire |
| **Zm** | Relèvement magnétique | Compas de relèvement, depuis la terre |
| **Zv** | Relèvement vrai | Règle rapporteur sur la carte |

**Formules de conversion** :
```
Zc + d = Zm
Zm + D = Zv
D + d = W (variation totale)

Zv − D = Zm − d = Zc  (conversion inverse)
```
- **d** = déviation (erreur propre au compas du bord)
- **D** = déclinaison magnétique (écart Nord magnétique / Nord vrai, lu sur la carte)
- **W** = variation totale = D + d

> Un Zc se convertit en Zv pour pouvoir reporter le relèvement sur une carte.

## Relèvement (définition)

Le **relèvement (Z)** est l'angle formé par la direction d'un point (amer, alignement) avec le **Nord**. Symbole Z. Se prend avec un **compas de relèvement** ; se reporte sur la carte avec une **règle rapporteur**.

## Alignement

Deux amers vus l'un par l'autre forment un alignement (ligne imaginaire AB, ex : Zv 100°). L'alignement permet de :
- Suivre une route précise sans compas
- Identifier sa position sur la carte (intersection de deux alignements)
- Éviter les hauts-fonds marqués par un alignement répertorié
