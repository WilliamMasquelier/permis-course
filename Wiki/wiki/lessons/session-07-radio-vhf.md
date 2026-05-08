---
title: "Session 7 : VHF, CROSS et Alertes"
type: lesson
lesson_order: 7
prerequisites: ["session-06-pratique-reglementation"]
difficulty: intermediate
dark_mode: false
exam_mode: false
sources: []
related: []
status: draft
updated: 2026-05-07
---

## CONCEPT

La VHF est un outil de sécurité, pas un téléphone de confort. Le permis plaisance permet l'usage d'une VHF dans les eaux territoriales françaises ; le CRR reste le cadre radio plus large, notamment hors de ce périmètre. Voir [[concepts/canaux-vhf]], [[concepts/securite-vhf-et-cross]], [[concepts/asn-dsc]], [[concepts/mmsi]], [[concepts/procedure-mayday]] et [[concepts/procedure-pan-pan]].

![[vhf-mayday-flow.svg]]

### Les canaux à connaître

- **16** : veille, appel et détresse en phonie.
- **70** : ASN/DSC, appels numériques de détresse ou sélectifs.
- **6, 8, 72, 77** : communications inter-navires selon usage.
- **13** : sécurité de navigation dans certains contextes.

Voir [[concepts/canaux-vhf]].

### MAYDAY, PAN-PAN, SÉCURITÉ

**MAYDAY** : danger grave et imminent, vie en jeu.  
**PAN-PAN** : urgence réelle sans péril vital immédiat.  
**SÉCURITÉ** : message concernant la sécurité de navigation ou la météo.

Un MAYDAY commence strictement :

```
MAYDAY MAYDAY MAYDAY
ICI
[Nom du navire]
```

Puis : position, nature de la détresse, assistance demandée, nombre de personnes, intentions, informations utiles, « À vous ».

### ASN, MMSI et position

L'ASN sur canal 70 transmet une alerte numérique. Si la VHF est reliée au GPS, l'alerte contient l'identité MMSI et la position. Le bouton rouge ne remplace pas la phonie : après l'alerte, il faut parler sur le canal 16 si possible.

### Le CROSS

Le CROSS coordonne les secours en mer en France. Il écoute, qualifie la situation et engage les moyens adaptés. Voir [[concepts/cross-sauvetage]].

## TASK

Expliquez la différence entre MAYDAY et PAN-PAN, citez les canaux 16 et 70, puis donnez les trois premières informations à transmettre après l'identification du navire.

## HINT_1

MAYDAY = vie en danger. PAN-PAN = urgence sans péril vital immédiat. Les canaux se répartissent entre voix et numérique.

## HINT_2

Après le nom du navire, le sauveteur a besoin de savoir où aller, ce qui se passe, et quel type d'aide envoyer.

## MISCONCEPTION

- Appuyer sur le bouton ASN puis se taire : l'alerte numérique doit être complétée par un message vocal si possible.
- Utiliser le canal 16 pour discuter après contact : on bascule sur un canal de travail.
- Confondre urgence et détresse : PAN-PAN n'est pas banal, MAYDAY est vital.

## SOLUTION

MAYDAY signale un danger grave et imminent avec vie en jeu. PAN-PAN signale une urgence sans péril vital immédiat. Le canal **16** sert à la veille, l'appel et la détresse en phonie ; le canal **70** sert à l'ASN/DSC.

Après l'identification, les premières informations utiles sont : **position**, **nature de la détresse ou de l'urgence**, **assistance demandée**. Viennent ensuite le nombre de personnes à bord, les intentions et toute information utile.

## MOTIVATION

La radio est l'un des rares outils qui transforment une situation isolée en secours coordonné. Bien choisir MAYDAY ou PAN-PAN, donner une position claire, et garder le canal 16 propre peut changer l'issue d'un incident.

## PREREQUISITES

- [[lessons/session-06-pratique-reglementation]]
