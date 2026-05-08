---
title: GPS et cartographie électronique
type: concept
tags: [navigation]
sources: [raw/books/complete-yachtmaster-cunliffe.pdf]
related: [[aide-navigation-phares]], [[carte-marine]], [[colreg-visibilite-reduite]]
status: draft
updated: 2026-05-07
---

**Summary:** Principes du GPS, datums cartographiques, waypoints et routes, limites de la navigation électronique et recoupement indispensable des sources.

## Principes du GPS

Le **GPS (Global Positioning System)** fournit des points en 3D, 24h/24, partout dans le monde. Principes :

1. Une constellation de satellites émet des signaux radio avec timestamps de haute précision
2. Le récepteur calcule sa distance à chaque satellite (sphère de position)
3. L'intersection de 4+ sphères donne la position 3D

Précision civile théorique : **±5 m**. En pratique : rarement plus de 2 longueurs de bateau.

**Galileo** : système européen parallèle au GPS, complémentaire. Pratiquement interchangeable pour l'utilisateur.

### Limites du GPS
- Fiable uniquement si la carte sous-jacente est exacte
- L'antenne est vulnérable aux dommages physiques
- Les satellites peuvent être dégradés ou coupés dans des zones sensibles
- Ne jamais utiliser comme **seule** source — toujours recouper (sonde, visuel, radar)

## Datum cartographique — problème critique

Le **datum** est le modèle mathématique de la forme de la Terre utilisé pour la carte.

- **WGS84** : datum GPS standard mondial — utilisé par la plupart des cartes modernes
- Certaines cartes anciennes utilisent des datums locaux (ex. OSGB 1936 au Royaume-Uni)
- Un décalage de datum peut provoquer une erreur de **plusieurs centaines de mètres** sur la carte

**Vérification obligatoire** : lire le coin de la carte (mention du datum). Configurer le GPS au même datum que la carte.

> En pilotage côtier, une erreur de datum est potentiellement fatale.

## Fonctions essentielles du GPS de bord

### COG / SOG
- **COG (Course Over Ground)** : route réelle par rapport au fond (intègre le courant et la dérive)
- **SOG (Speed Over Ground)** : vitesse réelle par rapport au fond
- À ne pas confondre avec le cap compas (cap barré) ni la vitesse loch (vitesse dans l'eau)

### Waypoints
Un **waypoint** est une position géographique préprogrammée. Le GPS indique en permanence :
- Distance restante
- Relèvement vers le waypoint
- ETA (heure d'arrivée estimée)
- Heure restante (TTG — Time To Go)

### GoTo / Route
- Activation **GoTo** : le GPS guide vers un waypoint unique
- **Route** : succession de waypoints reliés automatiquement
- **Cross-track error (XTE)** : écart latéral par rapport à la route prévue

## Carte électronique (chart plotter)

### Types de cartes électroniques
- **Raster (ARCS)** : scan numérique d'une carte papier Amirauté → aspect identique, zoom limité
- **Vectorielle (C-MAP, Navionics)** : base de données d'objets → zoom illimité, infobulles

**Risque du zoom excessif** : une carte vectorielle sur-zoomée peut paraître plus précise qu'elle ne l'est réellement. Le fond sous-marin peut avoir été levé avec une précision bien inférieure à la résolution affichée.

### AIS sur le traceur
Le traceur peut afficher les navires AIS avec leur route et vitesse. Complémentaire du radar, utile pour identifier les cibles.

## Recoupement des sources — règle d'or

> « Soyez toujours mal à l'aise si vous n'utilisez qu'une seule source d'information. »

| Situation | Sources à recouper |
|-----------|-------------------|
| Navigation au large | GPS + PE à l'estime + sonde |
| Approche côtière | GPS + transits visuels + sonde |
| Pilotage | Visuel (transits) + GPS comme vérification |
| Brouillard | Radar + GPS + sonde |

## Termes clés

| Terme français | Terme anglais |
|----------------|---------------|
| Traceur (traceur de cap) | Chart plotter |
| Carte électronique | Electronic chart |
| Carte raster | Raster chart |
| Carte vectorielle | Vector chart |
| Point par satellite | GPS fix |
| Datum cartographique | Chart datum (positional) |
| Route fond / cap fond | COG |
| Vitesse fond | SOG |
| Écart de route | Cross-track error (XTE) |

## Voir aussi
- [[carte-marine]] — Lecture des cartes papier, symboles, échelles
- [[navigation-estime]] — PE à l'estime en complément du GPS
- [[colreg-visibilite-reduite]] — AIS et MARPA pour la collision en brume
