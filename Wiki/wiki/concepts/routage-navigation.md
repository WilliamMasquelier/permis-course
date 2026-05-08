---
title: Routage — cap à tenir et stratégie de courant
type: concept
tags: [navigation]
sources: [raw/books/complete-yachtmaster-cunliffe.pdf]
related: [[courants-de-maree]], [[cap-route-derive]], [[planification-traversee]]
status: draft
updated: 2026-05-07
---

**Summary:** Méthode vectorielle pour calculer le cap à tenir en présence d'un courant de traversée ; stratégie selon la durée du trajet et la rotation du courant.

## Principe — analogie du passeur

Imaginer une traversée à la rame sur une rivière en crue. Pour atteindre le bon point sur l'autre rive, il faut viser en amont : le bateau "ferryglide" en crabe, maintenant un transit avec la rive opposée.

En navigation hauturière, c'est identique : le courant de marée joue le rôle de la rivière.

## Méthode graphique (vecteur vitesse)

Sur la carte, pour une traversée du point **A** vers le point **B** :

1. **Tracer la route de fond** (ground track) de A vers B — deux flèches à mi-parcours
2. Depuis A, tracer le **vecteur courant** (trois flèches) : direction et distance parcourue par le courant pendant la durée estimée
3. Depuis l'extrémité du vecteur courant (**C**), ouvrir les pointes au compas à la **distance parcourue par le bateau** dans la même période
4. Pointer depuis C jusqu'à l'intersection sur la route de fond → le point **D**
5. La ligne CD = **cap à tenir** (une flèche)

> Attention : CD représente la vitesse du bateau, pas la distance au but. Ne jamais tracer la ligne de C vers B.

## Applications selon la durée du trajet

### Traversée ≤ 1 heure
Utiliser les données de courant pour l'heure en cours. Un seul vecteur courant.

### Traversée avec renverse de courant
Deux choix :
1. **Compensation heure par heure** : corriger le cap à chaque heure → on reste sur la route directe, mais on parcourt plus de distance
2. **Vecteur net** : laisser le courant emporter le bateau pendant la première moitié du trajet, il ramènera le bateau vers la route pendant la seconde moitié → **moins de distance**, plus efficace

> La stratégie du vecteur net est souvent la meilleure sur les traversées de plusieurs heures (ex. traversée de mer de 11 heures).

### Traversée longue (ex. 60 milles, 11 heures)
1. Relever les données de courant pour chaque heure de la traversée
2. Additionner les composantes nord-going et south-going séparément
3. Le **vecteur net** = différence entre les deux → tracer ce seul vecteur depuis A
4. Construire le triangle avec la distance totale à parcourir

## Dérive (leeway) — correction finale

Après avoir déterminé le cap à tenir par la méthode vectorielle, **ajouter la dérive** :
- Lofer (tourner vers le vent) du nombre de degrés de dérive estimés
- Cette correction finale n'est pas tracée sur la carte — noter dans le carnet de bord

## Navigation GPS en courant de traversée

Avec un GPS, deux méthodes :

| Méthode | Description |
|---------|-------------|
| Comparer cap barré et COG | Régler le cap jusqu'à ce que COG = bearing vers waypoint |
| Cross-track error (XTE) | Utiliser la fonction XTE du GPS pour rester sur la route |

**Mise en garde** : la fonction XTE peut conduire à sur-corriger sur une longue traversée avec courant tournant → préférer la méthode vectorielle pour les traversées de plusieurs heures.

## Termes français / anglais

| Terme français | Terme anglais |
|----------------|---------------|
| Cap à tenir | Course to steer |
| Route de fond | Ground track |
| Vecteur courant | Tide vector |
| Route dans l'eau | Water track |
| Vecteur net | Net vector |
| Vitesse fond | SOG (Speed over ground) |
| Route fond | COG (Course over ground) |
| Ferryglide | Ferryglide / crabe |

## Voir aussi
- [[courants-de-maree]] — Données courant (atlas, losanges cartographiques)
- [[cap-route-derive]] — Conversion cap compas ↔ cap vrai, dérive
- [[navigation-estime]] — Le même principe vectoriel appliqué au PE
