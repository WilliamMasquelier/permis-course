---
title: "Point Estimé et GPS — Savoir Où Vous Êtes"
module: 3
module_title: "Naviguer"
session_in_module: 3
duration_min: 40
type: lesson
status: draft
updated: 2026-05-07
---

> [SCENE]
> **Mercredi 13h00. Au large d'Ölüdeniz, lagune bleue.**
>
> Le GPS indique : 36°33.8'N 29°06.5'E. La bouée d'entrée est à 0,4 NM au 270°. Parfait.
>
> "Et si le GPS tombe en panne ?" demande Emmanuel, l'œil malicieux — il connaît déjà la réponse.
>
> William réfléchit. Il ne connaît pas la réponse.
>
> "C'est pour ça qu'on apprend le point estimé," dit Mehmet depuis la plage arrière. "Le GPS, c'est magnifique jusqu'au jour où ce n'est plus là. Un marin qui ne sait pas naviguer sans GPS n'est pas un marin — il est passager d'un appareil électronique." Rebecca, depuis le bain de soleil : "Sur le catamaran en charter aux Bahamas, le capitaine avait deux GPS et un iPad." Mehmet : "Et s'ils tombent tous en panne en même temps ?" Silence de Rebecca.

## Le point estimé (Dead Reckoning / DR)

Le **point estimé** (PE) est la position calculée à partir d'une position connue, en appliquant les caps tenus et les distances parcourues. C'est la méthode de navigation qui existait avant le GPS — et qui reste indispensable dès que le GPS disparaît, s'éteint, ou donne une information erronée.

**Principe :** Vous êtes à la position A (connue, vérifiée). Vous barez un cap de 245° pendant 2 heures à 6 nœuds. Vous avez donc parcouru 12 milles dans la direction 245°. Tracez cette ligne sur la carte : son extrémité est votre point estimé.

Mais le PE seul est insuffisant car il ignore deux perturbateurs : la **dérive au vent** (leeway) et le **courant**. La méthode complète comporte trois étapes vectorielles :

1. **Route à l'estime (DR pur)** : cap barré × distance parcourue → une ligne avec une croix (+) au bout.
2. **Appliquer la dérive** : écarter légèrement vers le côté sous-le-vent de quelques degrés → on obtient la route dans l'eau (une flèche sur la ligne).
3. **Appliquer le courant** : depuis l'extrémité de la route dans l'eau, tracer le vecteur courant (direction + distance parcourue pendant la même période, trois flèches) → l'extrémité est le PE (symbolisé par un triangle avec l'heure).

**L'erreur s'accumule** : chaque PE repose sur le précédent. Une petite erreur de cap ou de vitesse sur la première heure se retrouve amplifiée après 6 heures. C'est pourquoi le PE doit être mis à jour régulièrement par des observations extérieures : relèvement d'un phare, transit visuel, ou fix GPS.

**Bonnes pratiques :** Tenir un carnet de bord avec position, cap, vitesse, heure à chaque changement significatif. En navigation côtière : toutes les 30 minutes près des dangers, toutes les heures au large.

Voir [[concepts/navigation-estime]], [[concepts/routage-navigation]].

## Les vecteurs de navigation

La route fond résulte de la combinaison de trois vecteurs, que l'on trace graphiquement sur la carte :

**Le triangle de navigation :**
1. **Vecteur cap/vitesse** (route dans l'eau) : direction que tient le bateau + distance parcourue dans l'eau pendant la période considérée. Une flèche simple.
2. **Vecteur courant** : direction et distance que l'eau a parcourue pendant la même période. Trois flèches.
3. **Vecteur résultant** (route fond / COG) : la ligne qui relie le point de départ à l'extrémité du vecteur courant. Deux flèches. C'est la vraie trajectoire sur le fond.

**Exemple pratique — traversée avec courant latéral :**
Objectif : aller droit vers la côte est. Courant : 1,5 nœud vers le nord. Si vous barez droit vers l'est, vous dériverez vers le nord et manquerez votre objectif.

Solution : calculez le cap à tenir (cap + courant = route fond souhaitée) en construisant le triangle. Résultat : barez légèrement vers le sud (lofer de quelques degrés) pour que le courant nord vous ramène exactement sur la route voulue — technique du *ferryglide*.

C'est identique à un piéton traversant une rue avec circulation dans le sens opposé : pour arriver face à la boutique d'en face, il marche légèrement en biais pour compenser.

## Les relèvements pour confirmer la position

Quand un amer reconnaissable est visible, un relèvement permet de vérifier ou corriger le PE. Trois relèvements simultanés sur des amers séparés donnent un **point constaté** — plus fiable que tout PE.

**Technique du point à trois relèvements :**
1. Choisissez trois amers clairement identifiés sur la carte, idéalement séparés d'environ 60° (entre 45° et 120° pour une bonne précision).
2. Prenez les trois relèvements aussi vite que possible — sur un bateau en mouvement, chaque minute de délai introduit une erreur.
3. Convertissez en relèvements vrais (Zv = Zc + d + D).
4. Tracez chaque LDP depuis l'amer vers votre position.

Le **chapeau triangulaire** (*cocked hat*) : les trois lignes forment rarement un point unique — elles délimitent un petit triangle. La règle de prudence est d'adopter le coin du triangle le **plus proche du danger identifié** : en cas d'incertitude, placez-vous toujours du côté pessimiste.

Un chapeau triangulaire de moins de 0,5 mm sur la carte est une bonne position. Plus grand : reprendre les relèvements, vérifier l'identification des amers.

Voir [[concepts/navigation-relevements]], [[concepts/pilotage-cotier]].

## Le GPS — outil essentiel, pas substitut

Le GPS fonctionne par **trilatération** : votre récepteur mesure le temps de transit des signaux radio venant d'au moins 4 satellites. Chaque mesure définit une sphère de position. L'intersection de ces sphères donne votre position en 3D avec une précision théorique de ±5 mètres.

En pratique, le GPS de bord donne :
- **COG** (Course Over Ground) — la direction réelle de votre déplacement par rapport au fond.
- **SOG** (Speed Over Ground) — votre vitesse réelle par rapport au fond.
- **Position** en lat/lon en temps réel.
- **Waypoints et routes** — navigation guidée vers des objectifs.

**Différence capitale :**
- Le **Heading** (cap compas) mesure la direction de votre *proue* — là où le bateau pointe.
- Le **COG** mesure la direction de votre *déplacement réel* — là où vous allez.

Ces deux valeurs peuvent différer de 10° à 20° en présence de courant ou de vent fort. Le GPS vous dit où vous allez réellement ; le compas vous dit où vous pointez.

**Le problème du datum :** Le GPS utilise le système géodésique WGS84. Si votre carte est en ED50 (datum européen ancien), il peut exister un écart de 100 à 200 mètres entre votre position GPS et votre position sur la carte. Toujours vérifier le datum de la carte et configurer le GPS en conséquence.

**Limites du GPS :** L'antenne peut être endommagée par la mer. Les satellites peuvent être indisponibles temporairement. Des interférences militaires peuvent dégrader le signal. Une carte électronique sur-zoomée donne une impression de précision qui n'existe pas si le levé hydrographique date des années 1950. Ne jamais en faire la seule source.

Voir [[concepts/gps-cartographie-electronique]], [[concepts/latitude-longitude]].

> [ATTENTION]
> **Ne pas naviguer au GPS seul.** L'examen et la pratique professionnelle requièrent que vous soyez capable de naviguer sans GPS. Tenez toujours un journal de bord avec vos positions et caps — il vous permettra de reconstruire votre route si nécessaire.

> [EXEMPLE GOLFE]
> **Point estimé Göcek → Ölüdeniz (si panne GPS hypothétique) :**
>
> Position de départ connue : Göcek Marina 36°45.3'N 28°57.6'E
>
> Cap tenu : 245°V, vitesse moyenne 7 nœuds, durée 2h24min
>
> Distance parcourue : 7 × 2.4 = 16.8 NM
>
> Courant estimé (quasi-nul en Méditerranée) : négligeable ici
>
> Point estimé : On trace le cap 245° depuis Göcek sur 16.8 NM → tombe à ~36°33.5'N 29°06.2'E — très proche de l'entrée d'Ölüdeniz. Sans GPS, on aurait la position correcte à ±0.5 NM près.

> [MINI-QUIZ]
> **Question 1 :** Quelle est la différence entre COG (Course Over Ground) et Heading (cap) ?
> **A)** COG est la direction de la proue ; Heading est la route fond réelle
> **B)** Heading est la direction de la proue ; COG est la route fond réelle après effet du courant et du vent
> **C)** Ce sont deux termes pour la même mesure
> **Réponse:** B — Le Heading est ce que vous tenez au compas (direction de la proue). Le COG est ce que le GPS mesure : la direction réelle du déplacement sur le fond, après que vent et courant ont agi.
>
> **Question 2 :** Vous prenez trois relèvements simultanés et tracez trois lignes de position. Elles forment un petit triangle. Comment déterminez-vous votre position ?
> **A)** Au centre géométrique du triangle
> **B)** Au sommet du triangle le plus proche du point de départ
> **C)** Au coin du triangle le plus proche du danger, par prudence
> **Réponse:** C — La méthode du "chapeau triangulaire" place votre position au coin le plus proche du danger. Principe de prudence nautique.

> [TRANSITION]
> Ölüdeniz est magnifique. La lagune bleue, les klipspringers sur les falaises, les voiles de parachute ascensionnel. Mais pour atteindre Butterfly Valley demain, il va falloir un vrai plan de route qui contourne les bas-fonds.
>
> **Session 3.4 — Routage et Pilotage Côtier : planifier une traversée, éviter les dangers.**
