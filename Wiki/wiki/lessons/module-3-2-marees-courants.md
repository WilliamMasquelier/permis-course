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
> Rebeca, qui a entendu depuis le cockpit, s'approche, intéressée. "Échoués six heures ? Vraiment ? Aux Bahamas, quand ça arrive, le bateau repart deux heures plus tard." William : "Parce qu'il y a quasiment pas de marée là-bas non plus, comme ici." Rebeca, soudain curieuse : "Alors pourquoi la Bretagne c'est différent ?"
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

La courbe ci-dessous illustre la variation de la hauteur d'eau au cours d'un cycle de marée. Entre la basse mer (BM) et la pleine mer (PM), le niveau monte selon une forme approximativement sinusoïdale : lente au début, rapide au milieu, puis lente à nouveau à l'approche du sommet. Le **marnage** est la différence de hauteur entre PM et BM — c'est l'amplitude totale du cycle. Plus le coefficient de marée est élevé, plus le marnage est grand et plus la courbe est "étirée" verticalement.

![[marees-courbe-type.svg|Courbe de marée — variation sinusoïdale de la hauteur d'eau sur un cycle]]

*La forme sinusoïdale de la marée semi-diurne : la montée est symétrique à la descente. PM = pleine mer (sommet), BM = basse mer (creux). Le marnage est la différence verticale entre les deux.*

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

Le schéma suivant visualise cette distribution heure par heure. Remarquez que les heures centrales (3e et 4e) cumulent à elles seules 6/12 — soit la moitié du marnage total. C'est pendant ces deux heures que le niveau change le plus vite, que les courants sont les plus forts, et que les erreurs de timing coûtent le plus cher.

![[marees-regle-douziemes.svg|Règle des douzièmes — répartition du marnage par heure]]

*La règle des douzièmes : 1/12, 2/12, 3/12, 3/12, 2/12, 1/12 du marnage à chaque heure successive. Retenir "1-2-3-3-2-1" suffit pour calculer la hauteur d'eau à n'importe quel moment du cycle.*

**Exemple avec les données Brest :** BM à 06h12 = 1,2 m, PM à 12h45 = 6,3 m. Marnage = 5,1 m. Quelle hauteur à 10h12 (4 heures après BM) ?

Cumul 1-2-3-3 = 9/12 du marnage = 9/12 × 5,1 = 3,83 m. Hauteur totale = 1,2 + 3,83 = **5,03 m**.

**Limite de la règle :** Elle suppose une marée semi-diurne régulière — valide en Manche et Atlantique. En Méditerranée, avec un marnage de 20 cm, ce calcul est purement théorique. En Méditerranée occidentale (golfe du Lion, côte Provence), la marée peut atteindre 0,3–0,5 m lors de grandes vive-eaux, mais les effets météorologiques (vent, pression) dépassent souvent l'amplitude astronomique.

Voir [[concepts/marees-hauteurs]].

## Les courants de marée

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
> **Question 1 :** À Brest : BM = 1,2 m, PM = 6,8 m. En utilisant la règle des douzièmes, quelle hauteur d'eau (au-dessus du zéro) y a-t-il à la 3ème heure après la BM ?
> **A)** 2,4 m au-dessus du zéro hydrographique
> **B)** 3,0 m au-dessus du zéro hydrographique
> **C)** 4,0 m au-dessus du zéro hydrographique
> **Réponse:** C — Marnage = 6,8 − 1,2 = 5,6 m. Règle des douzièmes : cumul à la 3ème heure = (1+2+3)/12 = 6/12 = 1/2 du marnage = 2,8 m au-dessus de la BM. Hauteur d'eau totale = BM + 2,8 = 1,2 + 2,8 = **4,0 m**. A correspond à la hauteur à la 2ème heure ; B n'est pas une valeur de douzièmes correcte.
>
> **Question 2 :** Sonde sur la carte : 2,5 m. Annuaire des marées : hauteur de marée 3,8 m. Quel est le fond réel ?
> **A)** 1,3 m — tirant d'eau maximum pour ce point
> **B)** 3,8 m — la sonde est relative à la hauteur actuelle
> **C)** 6,3 m — profondeur réelle sous la quille
> **Réponse:** C — Profondeur réelle = Sonde (au-dessus du zéro hydrographique) + Hauteur de marée = 2,5 + 3,8 = 6,3 m. La sonde carte représente la hauteur d'eau au zéro hydrographique (marée basse de référence) ; la hauteur de marée s'additionne. A serait la réponse si on soustrayait par erreur.
>
> **Question 3 :** Le golfe de Göcek a une marée de 0,2–0,3 m maximum. Pour un bateau de 1,5 m de tirant d'eau mouillant par sonde 2 m, la marée est-elle un facteur limitant au lever du jour (BM) ?
> **A)** Non — la différence de 0,3 m est négligeable, on dispose encore de 0,2 m de marge au moins
> **B)** Oui — avec 0,3 m de marée, le fond en BM = 2,0 − 0,3 = 1,7 m, moins que le tirant d'eau
> **C)** Oui — il faut toujours utiliser l'annuaire des marées en Méditerranée
> **Réponse:** A — En Méditerranée, avec un marnage de seulement 0,2–0,3 m, la variation du niveau est quasi négligeable. Avec sonde 2,0 m et tirant 1,5 m, on dispose de 0,5 m de marge ; même en BM (−0,3 m), il reste 0,2 m. En revanche, en Manche ou Atlantique (marnage 4–9 m), ce calcul est critique.
>
> **Question 4 :** Emmanuel dit : "En Bretagne, à coefficient 45, le marnage est bien inférieur à coefficient 100." Qu'est-ce que le "coefficient" de marée indique ?
> **A)** La vitesse du courant de marée en nœuds
> **B)** L'intensité de la marée (marnage) par rapport à une marée de référence — 120 = grande vive-eau, 20 = morte-eau faible
> **C)** Le nombre d'heures entre la BM et la PM
> **Réponse:** B — Le coefficient de marée est un nombre sans unité (0–120) qui quantifie l'intensité : 95–120 = grande vive-eau, 70–95 = vive-eau, 45–70 = intermédiaire, 20–45 = morte-eau. Il est publié dans l'annuaire des marées et permet d'interpoler les hauteurs pour des ports secondaires.

> [TRANSITION]
> Ölüdeniz se dessine à l'horizon — la lagune bleue, les falaises blanches, les parachutes ascensionnels qui décollent du mont Babadağ. William prend son GPS. "On est à 36°34'N, 29°05'E. La bouée d'entrée devrait être à..."
>
> **Session 3.3 — Point Estimé et GPS : savoir où vous êtes à tout moment.**
