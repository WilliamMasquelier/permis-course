---
title: "Session 3 : La Nuit et la Brume"
type: lesson
lesson_order: 3
prerequisites: ["session-02-regles-barre"]
difficulty: intermediate
dark_mode: true
exam_mode: false
sources: []
related: []
status: draft
updated: 2026-05-07
---

## CONCEPT

Il fait nuit noire. Le bruit du moteur se mêle au clapot. Devant vous, dans le rideau d'obscurité, trois points lumineux se détachent : un feu blanc en hauteur, un feu rouge à gauche, un feu vert à droite. Ces trois feux racontent une histoire complète — vous voyez un navire à propulsion mécanique qui vient droit sur vous. Le langage des feux est précis : chaque couleur, chaque secteur angulaire, chaque combinaison décrit le type de navire et sa route.

### Les feux de route — la grammaire de base

Tout navire faisant route porte trois feux fondamentaux. Voir [[concepts/feux-base]].

![[feux-secteurs-route.svg]]

| Feu | Couleur | Secteur | Position |
|-----|---------|---------|----------|
| [[entities/feu-mat-tete]] | Blanc | 225° | Avant + côtés jusqu'à 22,5° derrière le travers |
| [[entities/feu-cote-babord]] | Rouge | 112,5° | Côté gauche |
| [[entities/feu-cote-tribord]] | Vert | 112,5° | Côté droit |
| [[entities/feu-poupe]] | Blanc | 135° | Arrière |

> **La règle de lecture nocturne :**
> - **Vert + blanc tête** → il se dirige vers ma droite, voie libre.
> - **Rouge + blanc tête** → il se dirige vers ma gauche, je dois manœuvrer.
> - **Rouge ET vert ensemble (+ blanc)** → il vient droit sur moi, face à face.
> - **Blanc seul de poupe** → il s'éloigne, je le rattrape.

Mnémonique : « Port wine is red » — Port (bâbord, gauche) = rouge.

### Les navires privilégiés — feux de travail 360°

Un navire qui ne peut pas manœuvrer normalement le signale par des feux **visibles tout autour** (360°), souvent disposés verticalement. Voir [[concepts/feux-peche]].

| Configuration verticale (360°) | Identité |
|-------------------------------|----------|
| **Rouge sur blanc** | Navire de pêche au filet |
| **Blanc sur rouge** | Navire pilote (« casquette blanche, nez rouge ») |
| **Rouge - blanc - rouge** | Capacité de manœuvre restreinte |
| **Rouge - rouge** | Non maître de sa manœuvre (avarie) |

Mnémonique : pêcheur = **rouge en haut** ; pilote = **blanc en haut**.

### Quand on n'y voit plus rien : la brume

Sans visibilité, les feux ne servent plus — il faut écouter. Voir [[concepts/sons-manoeuvre]].

| Situation | Signal sonore (toutes les 2 minutes) |
|-----------|--------------------------------------|
| Moteur ayant de l'erre | 1 son **prolongé** |
| Moteur sans erre | 2 sons **prolongés** |
| Voilier, navire de pêche, remorqué | 1 prolongé + 2 brefs |
| Au mouillage | Cloche rapide ≈ 5 s par minute |

> Bref ≈ 1 s. Prolongé = 4 à 6 s.

### Et les signaux de manœuvre (jour ou nuit)

| Signal | Sens |
|--------|------|
| 1 son bref | Je gouverne sur **bâbord** |
| 2 sons brefs | Je gouverne sur **tribord** |
| 3 sons brefs | Je bats en **arrière** |

## TASK

En voyant uniquement les feux d'un navire la nuit, identifiez son type et sa route : rouge à gauche, vert à droite, blanc à l'avant.

## HINT_1

Vous voyez **les trois feux à la fois** — ce qui signifie que vous êtes dans le secteur visible de chaque côté **et** de l'avant. Que peut-on en déduire de votre position relative à ce navire ?

## HINT_2

Les feux de côté sont étanches : le rouge n'est visible **que** depuis le côté bâbord du navire, jusqu'à 22,5° derrière le travers. Si vous voyez rouge ET vert simultanément, vous êtes forcément… où ?

## MISCONCEPTION

- « Vert à droite, donc le navire va à droite. » Faux : le vert est à **sa** droite, pas à la vôtre. Si vous voyez son vert, vous voyez son côté tribord — il vous croise par votre gauche.
- Confondre feu de pêche (rouge sur blanc) et feu de pilote (blanc sur rouge) : les deux ont les mêmes couleurs, l'ordre vertical change tout.
- Oublier qu'un voilier au moteur perd son statut et porte les feux d'un moteur — donc un feu de tête de mât blanc.

## SOLUTION

Si vous voyez **rouge à votre gauche, vert à votre droite, et blanc en hauteur**, le navire arrive **face à vous**, route opposée à la vôtre. C'est un navire à propulsion mécanique en route. Vous êtes dans une situation de **face-à-face** au sens RIPAM : les deux navires manœuvrent **chacun sur tribord** pour se croiser bâbord à bâbord. La règle est symétrique — personne n'a la priorité, les deux agissent.

Si le rouge et le vert sont visibles **sans** feu blanc de tête de mât → c'est un voilier de moins de 20 m (les voiliers ne portent pas de feu de tête de mât).

## MOTIVATION

Les feux et signaux se travaillent comme une langue visuelle : vous voyez une combinaison, vous traduisez immédiatement en type de navire, route probable et action à tenir. À 8 nœuds, on parcourt environ 4 mètres par seconde — il n'y a pas le temps de douter.

## PREREQUISITES

- [[lessons/session-02-regles-barre]]
