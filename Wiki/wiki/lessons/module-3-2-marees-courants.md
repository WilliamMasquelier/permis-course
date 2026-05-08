---
title: "Marées et Courants — La Méditerranée et l'Atlantique"
module: 3
module_title: "Naviguer"
session_in_module: 2
duration_min: 45
type: lesson
status: draft
updated: 2026-05-07
---

> [SCENE]
> **Mercredi matin, 9h30. En route vers Ölüdeniz.**
>
> Emmanuel est pensif. "En Bretagne, à Brest, il y a parfois 8 mètres de marée. On attendait des heures pour entrer dans certains ports. Je me souviens d'un matin où on était échoués sur la grève pendant six heures."
>
> Christelle rit. "C'était les vacances 1988. Tu avais mal lu le tableau des marées."
>
> Rebecca, qui a entendu depuis le cockpit, s'approche, intéressée. "Échoués six heures ? Vraiment ? Aux Bahamas, quand ça arrive, le bateau repart deux heures plus tard." William : "Parce qu'il y a quasiment pas de marée là-bas non plus, comme ici." Rebecca, soudain curieuse : "Alors pourquoi la Bretagne c'est différent ?"
>
> "Ici," dit William, "la Méditerranée a une marée de... 20 centimètres."
>
> Emmanuel se retourne, regard malicieux. "Vingt centimètres ? Pour quoi faire ?"
>
> "Pour apprendre le concept avant de le faire pour de vrai. L'examen pose des questions sur les marées atlantiques. Donc on va les apprendre — même si ici, la marée ne change rien à notre navigation."

## Pourquoi les marées existent

La marée est une conséquence directe de la gravitation. La **Lune** (principalement) et le **Soleil** (dans une moindre mesure) exercent une attraction sur les masses d'eau des océans. Cette force crée deux *renflements* de la surface de la mer : l'un du côté de la Terre tourné vers la Lune, l'autre du côté opposé (par effet centrifuge). Pendant que la Terre tourne sur elle-même en 24h, chaque point de la surface passe sous ces renflements — produisant **deux hautes mers et deux basses mers toutes les 24 heures et 50 minutes** (le cycle lunaire est légèrement plus long que le jour solaire).

**Vive-eau vs morte-eau :**
- **Vive-eau** (*spring tide*) : Lune et Soleil sont alignés (pleine lune ou nouvelle lune). Leurs attractions s'additionnent → marées de **grande amplitude**.
- **Morte-eau** (*neap tide*) : Lune et Soleil sont en quadrature (premier ou dernier quartier). Leurs attractions se contrarient partiellement → marées de **faible amplitude**.

Le **coefficient de marée** (système français, échelle 20–120) quantifie l'intensité de chaque marée : un coefficient 20 correspond à une morte-eau extrême, 120 à une grande vive-eau. En pratique, un coefficient inférieur à 40 indique une petite marée sans grande conséquence ; un coefficient supérieur à 90 correspond à une grande vive-eau où les hauteurs, les courants et les durées d'étale peuvent être extrêmes.

## Lire un annuaire de marées

Les **annuaires des marées** (publications du SHOM, Bloc Mémo Vagnon, annuaires Imray) donnent pour chaque jour de l'année les heures et hauteurs des pleines mers (PM) et basses mers (BM) aux **ports de référence** (*standard ports*) — une trentaine en France.

**Format typique d'une entrée :**
```
Lundi 14 juillet — Coeff. 95
BM  06h12  1,2 m
PM  12h45  6,3 m
BM  18h30  0,9 m
PM  01h02  5,8 m  (heure légale CEST = UTC+2)
```

**Attention aux heures :** les tables SHOM sont souvent en Temps Universel (UTC). En France, ajoutez +1 h en hiver et +2 h en été (CEST) pour obtenir l'heure légale.

Pour un **port secondaire** non listé, l'annuaire donne des *corrections* (différences de temps et de hauteur) à appliquer aux données du port de référence le plus proche. Ces corrections varient parfois selon le niveau de marée — une interpolation est nécessaire.

## Calculer une hauteur de marée — Courbe type et règle des douzièmes

![[marees-courbe-type.svg]]
![[marees-regle-douziemes.svg]]

La montée de la marée ne se fait pas à vitesse constante. Elle est lente au début, s'accélère, puis ralentit à l'approche de la pleine mer — suivant approximativement une courbe sinusoïdale. La **règle des douzièmes** simplifie ce calcul en 6 étapes mémorables :

| Heure après BM | Fraction du marnage montant |
|----------------|----------------------------|
| 1ère heure | 1/12 |
| 2ème heure | 2/12 |
| 3ème heure | 3/12 |
| 4ème heure | 3/12 |
| 5ème heure | 2/12 |
| 6ème heure | 1/12 |

Mnémotechnique : **1-2-3-3-2-1**. La marée monte d'abord lentement (1/12 puis 2/12), puis très vite à mi-marée (3/12 + 3/12 = la moitié du marnage en seulement 2 heures), puis ralentit de nouveau.

**Exemple avec les données Brest :** BM à 06h12 = 1,2 m, PM à 12h45 = 6,3 m. Marnage = 5,1 m. Quelle hauteur à 10h12 (4 heures après BM) ?

Cumul 1-2-3-3 = 9/12 du marnage = 9/12 × 5,1 = 3,83 m. Hauteur totale = 1,2 + 3,83 = **5,03 m**.

**Limite de la règle :** Elle suppose une marée semi-diurne régulière — valide en Manche et Atlantique. En Méditerranée, avec un marnage de 20 cm, ce calcul est purement théorique. En Méditerranée occidentale (golfe du Lion, côte Provence), la marée peut atteindre 0,3–0,5 m lors de grandes vive-eaux, mais les effets météorologiques (vent, pression) dépassent souvent l'amplitude astronomique.

Voir [[concepts/marees-hauteurs]].

## Les courants de marée

![[ancrage-touee.svg]]

Les **courants de marée** (ou *tidal streams*) sont les mouvements horizontaux de l'eau créés par le remplissage et la vidange des mers lors des marées. Ils sont distincts des hauteurs de marée : pendant que la mer monte, l'eau se déplace horizontalement vers la côte (**flot**) ; pendant qu'elle descend, elle s'en éloigne (**jusant**).

Ces courants peuvent atteindre 3 à 5 nœuds dans les passages étroits (Raz de Sein, Alderney Race, raz Blanchard), rendant la navigation extrêmement délicate. Un bateau à 6 nœuds contre 4 nœuds de courant n'avance qu'à 2 nœuds sur le fond — 12h pour 24 milles. Avec le courant, il file à 10 nœuds.

**Sources d'information sur les courants :**

Les **atlas de courants de marée** SHOM cartographient heure par heure la direction et la vitesse des courants. Les valeurs sont données pour deux situations : morte-eau (ME) et vive-eau (VE). La notation `12.24` signifie 1,2 nœud en ME et 2,4 nœuds en VE.

Les **losanges de courant** (◆ sur les cartes SHOM) renvoient à un tableau en marge de la carte. Pour chaque heure avant ou après la PM du port de référence, le tableau donne la direction en degrés vrais et la vitesse ME/VE en ce point précis. Pour utiliser un losange : (1) identifiez l'heure de PM du port de référence le jour de votre passage, (2) calculez combien d'heures avant ou après vous êtes, (3) lisez la direction et la vitesse dans le tableau.

**Portes de courant :** Les caps, goulets et chenaux étroits concentrent les courants. Ces points critiques s'appellent *portes de courant* (*tidal gates*) — il faut les franchir au bon moment (courant favorable) ou à l'étale. Manquer une porte peut signifier 6 heures à attendre.

Voir [[concepts/courants-de-maree]].

> [ATTENTION]
> **La marée en Méditerranée.** En Méditerranée orientale (Turquie, Grèce, Italie), la marée est quasi-inexistante : 0,2–0,4 mètre maximum. Elle ne pose aucun problème pratique de navigation. MAIS l'examen du permis côtier français teste les marées atlantiques — apprenez-les même si vous naviguez en Méditerranée. Le golfe de Gascogne, Brest, Saint-Malo, Arcachon : là, les marées sont réelles et dangereuses.

## Vocabulaire essentiel des marées

| Terme | Définition |
|-------|-----------|
| Marnage | Différence de hauteur entre PM et BM |
| Coefficient | Intensité de la marée (20 = morte-eau, 120 = grande vive-eau) |
| Zéro hydrographique | Référence des sondes carte = niveau BM le plus bas |
| Hauteur d'eau | Profondeur réelle = Sonde carte + Hauteur marée |
| Estran | Zone entre le niveau des plus basses et plus hautes mers |

Le **marnage** varie énormément selon la géographie. En Méditerranée : 0,2–0,5 m. En Bretagne nord (Brest) : 4–8 m selon les coefficients. À Saint-Malo (baie du Mont-Saint-Michel) : jusqu'à 13 m — l'un des plus grands marnages du monde.

Le **coefficient** renseigne sur l'amplitude relative : un coefficient 95 (grande vive-eau) à Brest peut signifier un marnage de 6 m et des courants de 4 nœuds dans les goulets. Le même coefficient en Méditerranée correspond à... 0,28 m de marnage et des courants de 0,1 nœud.

Le **zéro hydrographique** est le niveau de référence de toutes les sondes sur les cartes marines — il correspond à la Plus Basse Mer Astronomique, soit le niveau le plus bas possible. C'est une garantie de sécurité : la hauteur d'eau réelle est toujours *au moins* égale à la sonde de la carte (on y ajoute la hauteur de marée du moment).

> [EXEMPLE GOLFE]
> **La marée à Göcek (juillet 2026) :**
>
> BM : 0,05 m. PM : 0,28 m. Marnage : 0,23 m. Coefficient équivalent : ~15 (morte-eau extrême).
>
> **Impact pratique :** Nul. Un tirant d'eau de 1,8 m peut entrer dans n'importe quelle crique dont la sonde carte est ≥ 2,0 m à n'importe quelle heure.
>
> **Contraste pédagogique :** À Brest (même semaine), PM : 7,1 m, BM : 1,0 m. Marnage : 6,1 m. Coefficient : 95 (grande vive-eau). Le *Deniz Rüzgarı* serait échoué dans plusieurs mouillages bretons à marée basse si le skipper ne vérifiait pas l'annuaire.

> [MINI-QUIZ]
> **Question 1 :** À Brest, la BM est à 1,2 m et la PM est à 6,8 m. Le coefficient est 95. Quelle est la hauteur de marée à la 3ème heure après la BM ?
> **A)** 1 m au-dessus de la BM
> **B)** 1,8 m au-dessus de la BM
> **C)** 2,8 m au-dessus de la BM
> **Réponse:** C — Marnage = 6,8 – 1,2 = 5,6 m. À la 3ème heure : cumul = 1/12 + 2/12 + 3/12 = 6/12 = 1/2 du marnage = 2,8 m au-dessus de la BM. Hauteur d'eau totale = 1,2 + 2,8 = 4,0 m.
>
> **Question 2 :** Vous lisez sur votre carte : sonde 3m, et l'annuaire indique une hauteur de marée de 4,5m. Quelle est la profondeur réelle à cet endroit ?
> **A)** 1,5 m
> **B)** 3,0 m
> **C)** 7,5 m
> **Réponse:** C — Profondeur réelle = Sonde + Hauteur de marée = 3 + 4,5 = 7,5 m.

> [TRANSITION]
> Ölüdeniz se dessine à l'horizon — la lagune bleue, les falaises blanches, les parachutes ascensionnels qui décollent du mont Babadağ. William prend son GPS. "On est à 36°34'N, 29°05'E. La bouée d'entrée devrait être à..."
>
> **Session 3.3 — Point Estimé et GPS : savoir où vous êtes à tout moment.**
