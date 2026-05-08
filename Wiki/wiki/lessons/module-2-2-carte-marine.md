---
title: "La Carte Marine — Lecture et Symboles"
module: 2
module_title: "Lire la Mer"
session_in_module: 2
duration_min: 40
type: lesson
status: draft
updated: 2026-05-07
---

> [SCENE]
> **Mardi midi, ancré dans la baie de Fethiye. À table.**
>
> William a étalé la carte Imray T1 sur la table du cockpit — *Turkish Waters & Cyprus Pilot* côté golfe de Fethiye. Christelle regarde les chiffres partout sur la mer. "C'est quoi tous ces nombres ?"
>
> "Les profondeurs. En mètres."
>
> "Et les 5.5 là-bas entre les deux rochers ?"
>
> "5,5 mètres à marée basse. On a 1,8m de tirant d'eau, donc on passe."
>
> Emmanuel se penche. "Et là, le symbole avec des petits points ?"
>
> William cherche dans la légende. La carte marine est un monde entier à apprendre à lire.

## La carte marine — votre contrat avec la réalité

Contrairement à une carte routière qui montre ce qui est à la surface, la carte marine montre avant tout ce qui est **en dessous** : les profondeurs, les rochers submergés, les hauts-fonds, les épaves. C'est votre contrat avec la réalité sous-marine — une réalité que vous ne pourrez jamais vérifier à l'œil, sauf quand il est trop tard.

En France, les cartes marines officielles sont publiées par le **SHOM** (Service Hydrographique et Océanographique de la Marine). Imray, l'éditeur britannique, publie des séries régionales très utilisées en Méditerranée (dont la T1 pour les eaux turques). Toutes les cartes sérieuses partagent les mêmes conventions IALA et les mêmes symboles internationaux du SHOM/IHO.

Les profondeurs sont données par rapport au **zéro hydrographique** (*lowest astronomical tide*, LAT) — le niveau le plus bas que la mer peut théoriquement atteindre. Cela signifie que les sondes imprimées sur la carte sont des **minimums garantis** : la profondeur réelle sera toujours égale ou supérieure à la sonde, sauf en cas d'erreur de sondage. Les hauteurs à terre (falaises, phares) sont mesurées par rapport au niveau moyen de la mer ou à la pleine mer de vive-eau.

L'**échelle** d'une carte exprime le rapport entre la distance sur la carte et la distance réelle. Une carte à 1:50 000 signifie que 1 cm sur la carte représente 50 000 cm = 500 m dans la réalité. Retenez : grande échelle = grande précision = petite zone couverte. Il ne faut **jamais utiliser une carte de petite échelle** (1:200 000 ou moins) pour naviguer en eaux côtières étroites.

Les cartes doivent être **tenues à jour** par les avis aux navigateurs publiés par le SHOM. Une carte obsolète peut ne pas mentionner une nouvelle épave, un chantier naval, ou un changement de balisage. Vérifiez toujours la date d'édition avant un passage délicat.

La carte marine est votre source de vérité sur le terrain sous-marin et les dangers. Avant toute navigation, elle doit être consultée. Elle montre :

- Les **fonds** (sondes) — en mètres par rapport au zéro hydrographique (MLWS)
- Les **dangers** — roches, épaves, bancs
- Les **balises et phares** — avec leurs caractéristiques
- Les **zones réglementées** — réserves, chenaux, zones militaires
- Les **amers** — points de repère à terre

## Lire les sondes

Les sondes imprimées sur la carte représentent la profondeur d'eau au zéro hydrographique. Il ne s'agit pas d'une mesure prise à un moment donné, mais d'une valeur normalisée pour permettre la comparaison universelle. La profondeur réelle à l'instant t vaut : **profondeur réelle = sonde + hauteur de marée actuelle**.

En Méditerranée orientale où la marée est quasi-nulle, la profondeur réelle est pratiquement identique à la sonde. Sur les côtes atlantiques françaises, cette addition peut faire varier la profondeur réelle de plusieurs mètres entre basse mer et haute mer.

Les sondes sont données par rapport au **zéro hydrographique** (MLWS = Lowest Astronomical Tide). C'est le niveau le plus bas possible — les profondeurs réelles sont donc toujours **supérieures ou égales** à la sonde carte.

| Symbole | Signification |
|---------|---------------|
| Nombre sous-marin simple (ex: 8) | Profondeur en mètres au zéro hydro |
| Nombre souligné ou barré (ex: ~~2~~) | Roche qui découvre à marée basse (hauteur en mètres au-dessus du zéro) |
| + (croix) | Roche couverte à moins de 2 m |
| Astérisque * | Roche couverte dangereuse (profondeur inconnue) |
| (entre parenthèses) | Sonde hors position (le long d'un quai, par exemple) |
| ED | Existence douteuse — le danger existe peut-être, prudence maximale |
| SD | Sonde douteuse — la profondeur indiquée est incertaine |

La **roche découvrante** (sonde soulignée) est particulièrement traître : elle est couverte à marée haute et visible à marée basse. Sur les côtes à forte amplitude comme la Bretagne, une roche à 1,2 m au-dessus du zéro peut être totalement submergée à 5 m de profondeur en pleine marée. Elle n'est donc pas sur la carte comme "danger immédiat" — mais elle le devient à marée basse.

Voir [[concepts/navigation-symboles-cartes]], [[concepts/carte-marine]].

## Coordonnées géographiques

La position d'un point en mer se donne par sa **latitude** et sa **longitude**. La latitude mesure la distance angulaire par rapport à l'équateur (0° à l'équateur, 90° aux pôles). La longitude mesure la distance angulaire par rapport au méridien de Greenwich (0° à Greenwich, jusqu'à 180° est et ouest).

![[navigation-carte-cap.svg]]

**Latitude** — lignes horizontales parallèles à l'équateur. Se lit sur les bords gauche et droit de la carte. Nord = positif.

**Longitude** — lignes verticales (méridiens). Se lit en haut et en bas de la carte. Est = positif.

**Format sur les cartes marines :** degrés, minutes, dixièmes de minute. Ex : 36°45.3'N, 28°57.6'E.

Pour lire une position sur la carte, placez vos compas de navigation (ou vos doigts) entre les graduations du bord. Chaque degré est divisé en 60 minutes sur l'échelle de latitude ; chaque graduation de 1 minute est souvent divisée en 6 ou 10 sous-graduations représentant des dixièmes ou des dixièmes de minutes.

**Accord de datum :** assurez-vous que votre GPS et votre carte utilisent le même système géodésique (datum). La plupart des cartes modernes et des GPS utilisent **WGS84**. Un datum incorrect peut décaler votre position indiquée de 100 à 500 mètres — suffisant pour vous placer sur une roche alors que le GPS affiche "eau libre".

Voir [[concepts/latitude-longitude]], [[concepts/navigation-coordonnees-et-distances]].

## Mesurer les distances

La clé pour mesurer des distances en milles nautiques tient en une phrase : la définition même du mille nautique est empruntée à la géographie terrestre. **Un mille nautique = une minute d'arc de latitude** = 1/60 de degré = 1852 mètres. Ce n'est pas une coïncidence pratique — c'est la définition.

En conséquence, l'échelle des latitudes (les graduations sur les bords verticaux de la carte) est littéralement une règle de mesure de distances, déjà étalonnée en milles nautiques. Posez vos compas sur la distance à mesurer, puis reportez-les sur le bord de la carte à la même latitude que la route — et lisez directement en minutes = en milles nautiques.

Pour mesurer des routes longues sur des cartes de petite échelle, mesurez en segments, car la projection Mercator introduit un léger étirement aux hautes latitudes.

> [ATTENTION]
> **Règle d'or : mesurez toujours les distances sur l'échelle des latitudes** (bords verticaux de la carte), jamais sur l'échelle des longitudes. Une minute d'arc de latitude = 1 mille nautique (1852 m). L'échelle des longitudes varie avec la latitude — elle est inutilisable pour les distances.

## Symboles essentiels à reconnaître

| Symbole | Signification |
|---------|---------------|
| Ancre entourée d'un cercle pointillé | Zone de mouillage recommandée |
| Ancre barrée | Mouillage interdit |
| PD | Position Douteuse — la position du danger est incertaine |
| ED | Existence Douteuse — le danger lui-même n'est pas confirmé |
| PA | Position Approchée — position approximative seulement |
| Obstn | Obstruction — obstacle submergé de nature indéterminée |
| Wr ou Wk | Épave (Wreck) — profondeur indiquée si connue |
| Côtés hachurés + profondeur | Épave partiellement visible à marée basse |
| R | Roche |
| S | Sable (Sand) — nature du fond |
| M | Vase (Mud) — nature du fond |
| Wd | Algues/Herbiers (Weed) |
| Teinte bleue claire | Profondeurs < 10 m (zone de danger côtier) |
| Teinte verte | Estran (zone découvrant à marée) |
| Câble avec tirets | Câble sous-marin — interdiction d'ancrer |
| Zone hachurée rouge | Zone réglementée ou interdite |
| Vitesse dans un cercle | Limite de vitesse |
| Flèche pointillée | Courant (avec force en nœuds) |
| Étoile avec liseré magenta | Feu de navigation (phare ou balise lumineuse) |

Voir [[concepts/navigation-symboles-cartes]], [[concepts/carte-marine]].

## Les projections et l'échelle

La quasi-totalité des cartes marines utilisent la **projection de Mercator**. Dans cette projection, les méridiens (longitudes) sont des lignes droites verticales et les parallèles (latitudes) sont des lignes horizontales — ce qui simplifie la navigation car les caps droits tracés sur la carte correspondent à des routes réelles droites (loxodromes).

L'inconvénient : les surfaces sont déformées. Un degré de latitude en haut d'une carte représente davantage de distance réelle qu'en bas. C'est pourquoi l'échelle des latitudes n'est pas uniforme sur les cartes de grande couverture — et pourquoi on mesure les distances au **bord de la carte, à la latitude de la route**, pas n'importe où sur le bord.

**Choisir la bonne échelle :**
- **1:50 000 ou plus grande** — entrée de port, rade, approach étroite. Chaque danger est visible.
- **1:200 000** — navigation côtière de passage. Vue d'ensemble du littoral.
- **1:1 000 000** — planification offshore. Jamais pour de la navigation côtière.

Utiliser une carte trop petite dans des eaux dangereuses est une faute professionnelle. Les échouages par carte inadaptée sont mentionnés dans les statistiques d'accidents de navigation de plaisance.

## La rose des vents et le compas

La rose des vents sur une carte marine comporte généralement **deux cercles concentriques**. Le cercle extérieur est orienté sur le **nord vrai** (Nord géographique, aligné avec les méridiens de la carte). Le cercle intérieur est orienté sur le **nord magnétique** de la zone, avec une notation indiquant la variation magnétique et son taux de changement annuel (ex : *Var 4°E (2024) diminuant 7' par an*).

Pour tracer ou lire un cap magnétique, utilisez le cercle intérieur. Pour un cap vrai (coordonné avec les méridiens de la carte), utilisez le cercle extérieur. En pratique sur un voilier moderne, votre compas lit le nord magnétique — donc les caps que vous tenez sont magnétiques, et doivent être convertis en vrais avant d'être tracés sur la carte (ou vice versa).

Voir [[concepts/navigation-relevements-et-caps]].

> [EXEMPLE GOLFE]
> **Carte Imray T1 (Turkish Waters), extrait zone Göcek :**
>
> Entre Göcek Marina (36°45.3'N 28°57.6'E) et Tersane Island (36°43.5'N 28°58.2'E), la route directe de **148°V** longe le bord ouest des Yassıca Adaları. Les sondes le long du passage varient de 12 à 30 m. Un banc côté est à 5 m est signalé à 36°44.0'N 28°58.8'E — à éviter si vous continuez vers les petites criques de l'est.
>
> Distance Göcek → Tersane : **2,8 NM** (mesurée sur l'échelle de latitude, soit ~3 minutes d'arc).

> [MINI-QUIZ]
> **Question 1 :** Sur quelle échelle mesurez-vous une distance en milles nautiques sur une carte marine ?
> **A)** Sur l'échelle des longitudes (axe horizontal)
> **B)** Sur l'échelle des latitudes (axe vertical)
> **C)** Indifféremment sur l'une ou l'autre
> **Réponse:** B — L'échelle des latitudes est la seule valide. 1 minute d'arc = 1 mille nautique. L'échelle des longitudes varie avec la latitude et ne peut pas être utilisée pour mesurer des distances.
>
> **Question 2 :** Une sonde notée "~~3~~" (3 barré) sur la carte signifie :
> **A)** Roche qui découvre à 3 mètres au-dessus du zéro hydrographique
> **B)** Profondeur de 3 mètres au zéro hydrographique
> **C)** Erreur de carte corrigée
> **Réponse:** A — Le nombre barré indique une roche qui *découvre* (emerge at low water), à cette hauteur en mètres au-dessus du zéro hydrographique. C'est un danger à marée haute dans cette zone.

> [TRANSITION]
> Depuis l'ancre, William regarde la baie de Fethiye. Les tombeaux lyciens sont découpés dans la falaise. Un phare clignote à l'entrée de la baie. "Comment on lit la caractéristique d'un phare ?" demande-t-il.
>
> **Session 2.3 — Phares et Aides à la Navigation : identifier et utiliser les amers lumineux.**
