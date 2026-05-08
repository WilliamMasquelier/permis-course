---
title: Procédure MAYDAY — détresse absolue
type: concept
tags: [radio, crr, detresse, securite]
sources: [raw/course-1/anfr-manuel_crr.pdf]
related: [[../themes/08-radio-crr]], [[procedure-pan-pan]], [[asn-dsc]], [[canaux-vhf]], [[securite-vhf-et-cross]]
status: draft
updated: 2026-05-06
---

**Summary:** MAYDAY est le signal radio de détresse absolue (danger grave et imminent, vie en jeu). Il s'émet sur la voie 16, prononcé "m'aider". Depuis la voie 70 (ASN), une alerte numérique automatique précède l'appel vocal.

## Quand émettre un MAYDAY ?

Lorsqu'un navire ou une personne est sous la menace d'un **danger grave et imminent** et a besoin d'une aide immédiate. Exemples : voie d'eau majeure, incendie grave, naufrage imminent.

L'alerte est émise **sur ordre du commandant** (ou patron / chef de bord).

## Étape 1 — Alerte ASN (voie 70)

Si la VHF est équipée ASN :
1. Appuyer **≥ 5 secondes** sur le bouton rouge de détresse (sous le capot de protection).
2. La VHF transmet automatiquement **5 fois** sur la voie 70 : MMSI du navire + position GPS (si couplée) + nature de la détresse.
3. L'alerte est renouvelée automatiquement toutes les **4 minutes** jusqu'à accusé de réception.

## Étape 2 — Message vocal sur la voie 16

### Appel de détresse (qui identifie le navire)

```
MAYDAY  MAYDAY  MAYDAY
ICI
[Nom du navire × 3]
[Indicatif d'appel × 1]
```

### Message de détresse (après l'appel)

```
MAYDAY
[Nom du navire × 1]
[Indicatif d'appel × 1]
Position du navire (coordonnées absolues ou relative par rapport à point connu)
Nature de la détresse
Type d'assistance requise
Nombre de personnes à bord
Intentions du responsable du navire
Tout renseignement utile pour les secours
A vous
```

Le message est répété jusqu'à réception d'un accusé.

### Exemple complet

```
MAYDAY, MAYDAY, MAYDAY
ICI CORMORAN, CORMORAN, CORMORAN  FXFA
MAYDAY  CORMORAN  FXFA
Deux milles Ouest Quiberon
Feu à bord
Demandons assistance immédiate
5 personnes à bord
Quittons le navire
A vous
```

## Accusé de réception (par un autre navire)

Si aucune station côtière n'a répondu dans les **5 minutes**, un navire peut accuser réception :

```
MAYDAY  [nom et indicatif du navire en détresse]
ICI  [nom et indicatif du navire qui répond]
REÇU MAYDAY
[Délai d'arrivée si possible]
```

## Relais d'alerte de détresse

Si un navire doit retransmettre une détresse :

```
MAYDAY RELAY  MAYDAY RELAY  MAYDAY RELAY
A TOUS  A TOUS  A TOUS
ICI  [nom du retransmetteur × 3] [indicatif × 1]
MAYDAY  [nom et indicatif du navire en détresse]
[Répéter toutes les informations de la détresse]
```

## Contrôle du trafic de détresse

- **SILENCE MAYDAY** : imposé par la station coordinatrice pour dégager la voie 16.
- **SILENCE FINI** : signale la fin des opérations.

## Phases d'urgence SAR

| Phase | Déclencheur |
|-------|-------------|
| Incertitude | Navire non arrivé à destination ou n'a pas signalé sa position |
| Alerte | Tentatives de contact échouées ou navire en difficulté (sans péril immédiat) |
| Détresse | Navire clairement en détresse ou contact perdu |

## Annulation d'une fausse alerte

Sur la voie 16 (en radiotéléphonie, après annulation ASN si possible) :

```
A TOUS  A TOUS  A TOUS
ICI  [Nom × 3]  [Indicatif × 1]
Veuillez annuler mon alerte de détresse de [DATE/HEURE UTC]
```

Rester en veille sur la voie 16 pour répondre aux stations qui rappellent.
