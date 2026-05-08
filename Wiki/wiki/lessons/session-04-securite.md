---
title: "Session 4 : La Sécurité et l'Équipement"
type: lesson
lesson_order: 4
prerequisites: ["session-03-feux-signaux"]
difficulty: intermediate
dark_mode: false
exam_mode: false
sources: []
related: []
status: draft
updated: 2026-05-07
---

## CONCEPT

La sécurité en mer ne se règle pas au moment du danger — elle se règle **au moment du largage**. L'équipement embarqué, la procédure radio, le réflexe MAYDAY : tout cela doit être su d'avance, parce que dans la panique on ne lit pas une notice.

### L'équipement obligatoire — un système cumulatif

L'arrêté divisé en trois zones définit ce que vous **devez** avoir à bord. Chaque zone supérieure ajoute, ne remplace pas. Voir [[concepts/equipement-obligatoire]].

![[securite-zones-armement.svg]]

**Zone Basique (≤ 2 milles d'un abri) — 5 catégories à retenir :**

1. **Flottabilité individuelle** — un [[entities/equipement-gilet]] par personne (ou combinaison portée).
2. **Repérage et signalisation** — moyen de repérage lumineux (collectif ou individuel).
3. **Lutte contre l'eau et le feu** — dispositif d'assèchement + extincteur.
4. **Mouillage et remorquage** — ligne de mouillage/ancre + dispositif de remorquage.
5. **Secours individuel** — moyen de remonter une personne tombée à l'eau, coupe-circuit pilote.

**Zone Côtière (≤ 6 milles) ajoute :**
- 3 [[entities/equipement-feux-detresse]] (feux rouges automatiques à main)
- Miroir de signalisation, signal sonore
- Compas magnétique, RIPAM, document balisage, **carte(s) de navigation**

**Zone Hauturière (> 6 milles) ajoute :**
- Harnais, radeau de survie
- Fusées à parachute + fumigènes (ou [[entities/equipement-vhf]] ASN qui les remplace)
- Moyens de point + météo + livre des feux + journal de bord

> Le permis côtier vous limite à **6 milles d'un abri** — la zone Hauturière est hors-permis.

### La radio VHF — pourquoi le canal 16

La VHF est l'outil de détresse de référence en mer. Le **canal 16** (156,800 MHz) est la voie internationale de **veille, appel et détresse**. Tout navire équipé doit y rester en écoute.

Une VHF moderne a deux canaux dédiés : **16** (vocal) et **70** (ASN — Appel Sélectif Numérique). L'ASN, si la VHF est couplée à un GPS, transmet **automatiquement** votre MMSI et votre position au CROSS quand vous appuyez 5 secondes sur le bouton rouge. Voir [[concepts/securite-vhf-et-cross]] et [[concepts/asn-dsc]].

### MAYDAY — la procédure absolue

Quand le danger est grave et imminent (vie en jeu) : **MAYDAY** sur voie 16. Le mot vient du français « m'aider ». Voir [[concepts/procedure-mayday]].

Les **5 premiers mots** d'un MAYDAY, dans l'ordre exact, sont :

```
MAYDAY  MAYDAY  MAYDAY
ICI
[Nom du navire]
```

Puis vient le contenu :
1. **Position** (coordonnées ou point connu)
2. **Nature** de la détresse
3. **Type d'assistance** demandée
4. **Nombre de personnes** à bord
5. **Intentions et infos utiles**, puis « **À vous** »

> Pour un danger **moins** grave (panne, urgence sans péril vital) : c'est **PAN-PAN** (3 fois), pas MAYDAY. Voir [[concepts/procedure-pan-pan]].

### Le CROSS — votre interlocuteur

Le **CROSS** (Centre Régional Opérationnel de Surveillance et de Sauvetage) coordonne tous les secours en mer en France. Un MAYDAY sur 16 ou une alerte ASN sur 70 lui parvient directement. Il décide des moyens (canot SNSM, hélicoptère, déroutement d'un navire commercial). Voir [[concepts/cross-sauvetage]].

## TASK

Citez les 5 catégories d'équipement obligatoire et énoncez les 5 premiers mots d'un appel MAYDAY sur VHF 16.

## HINT_1

Pour les 5 catégories : pensez aux 5 risques fondamentaux en mer — tomber à l'eau, ne pas être vu, prendre l'eau, brûler, dériver. Pour le MAYDAY : c'est un mot répété, suivi d'un seul mot français.

## HINT_2

Les 5 catégories répondent à : « Comment je flotte ? Comment on me trouve ? Comment je vide ou j'éteins ? Comment je m'arrête ou me fais tirer ? Comment je sauve quelqu'un ? » — les cinq mots du MAYDAY occupent **deux lignes** : trois fois un même mot, puis une formule de présentation, puis l'identité.

## MISCONCEPTION

- « PAN-PAN, c'est moins urgent que MAYDAY donc on s'en fiche. » Faux : PAN-PAN est une **urgence** réelle (panne, blessé léger). Mal classer son appel sature le réseau ou empêche les secours d'arriver à temps.
- Croire que les fusées sont **toujours** obligatoires en hauturier : la VHF/ASN les remplace si elle est embarquée et fonctionnelle.
- Oublier que le canal 16 est **réservé à l'appel et à la détresse** — on bascule sur un canal de travail dès qu'on a établi le contact.

## SOLUTION

**Les 5 catégories d'équipement Basique :**
1. Flottabilité individuelle (gilet ou combinaison)
2. Repérage lumineux
3. Assèchement + extincteur
4. Mouillage + remorquage
5. Coupe-circuit + dispositif homme à la mer

**Les 5 premiers mots d'un MAYDAY (énoncés dans l'ordre) :**

> **MAYDAY — MAYDAY — MAYDAY — ICI — [Nom du navire].**

Le mot « MAYDAY » est répété **trois fois** pour ne laisser aucun doute (interférences, fading). « ICI » introduit l'identification du navire émetteur. Le nom du navire est ensuite répété trois fois, suivi de l'indicatif d'appel.

## MOTIVATION

La sécurité est une matière de réflexes. Au-delà des points d'examen, un MAYDAY mal formulé en pleine détresse peut coûter des minutes irremplaçables. La procédure existe pour qu'en 30 secondes le sauveteur sache où venir, quoi apporter, et pour combien de personnes.

## PREREQUISITES

- [[lessons/session-03-feux-signaux]]
