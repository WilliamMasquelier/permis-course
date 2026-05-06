---
title: Procédures PAN PAN et SECURITE — urgence et sécurité radio
type: concept
tags: [radio, crr, urgence, securite]
sources: [../../raw/../Cours 1/anfr-manuel_crr.pdf]
related: [[../themes/08-radio-crr]], [[procedure-mayday]], [[asn-dsc]], [[canaux-vhf]], [[securite-vhf-et-cross]]
status: draft
updated: 2026-05-06
---

**Summary:** PAN PAN signale une urgence (sécurité du navire ou d'une personne, sans péril de mort imminent). SECURITE signale un danger de navigation ou météorologique. Les deux se diffusent sur la voie 16. Les communications d'urgence ont priorité sur tout sauf la détresse.

## Tableau récapitulatif des trois niveaux

| Niveau | Signal | Priorité | Cas typiques |
|--------|--------|----------|--------------|
| Détresse | MAYDAY (× 3) | 1 — absolue | Naufrage, incendie grave, voie d'eau majeure |
| Urgence | PAN PAN (× 3) | 2 | Panne moteur, man overboard, urgence médicale |
| Sécurité | SECURITE (× 3) | 3 | Épave dérivante, phare éteint, coup de vent |

---

## PAN PAN — Urgence

### Quand ?

Situation concernant la **sécurité du navire** (remorquage, avarie) ou d'**une personne** (blessé, malade), sans péril de mort immédiate.

Prononciation : « panne, panne ».

### Appel sur la voie 16

```
PAN PAN  PAN PAN  PAN PAN
[Station appelée × 3, ou A TOUS × 3]
ICI
[Nom du navire × 3]
[Indicatif × 1]
```

### Texte du message

```
Position du navire (absolue ou relative)
Nature de l'urgence
Secours demandés
Intentions du responsable du navire
Tout renseignement utile
```

### Exemple

```
PAN PAN, PAN PAN, PAN PAN
A TOUS, A TOUS, A TOUS
ICI NEPTUNE, NEPTUNE, NEPTUNE  FP4624
Position 20 milles Nord Ouest de Cherbourg
Gouvernail cassé, partons à la dérive
Demandons remorquage
Voilier coque blanche, 3 personnes à bord
A vous
```

### Consultation radiomédicale

Lorsqu'une personne à bord est malade : émettre un PAN PAN, la station côtière ou le MRCC met le navire en liaison avec le **CCMM (Centre de Consultation Médicale Maritime)** de Toulouse ou de Rome.

### ASN (voie 70)

L'annonce d'urgence est transmise par ASN sur la voie 70, puis l'appel vocal suit sur la voie 16.

---

## SECURITE — Sécurité maritime

### Quand ?

Pour signaler :
- un danger de navigation (épave, objet flottant, phare défaillant)
- un avertissement météorologique (coup de vent > 7 Beaufort non prévu)

Ce signal précède tout **BMS (Bulletin Météorologique Spécial)** et tout **AVURNAV (AVis URgent aux NAVigateurs)**.

### Appel sur la voie 16

```
SECURITE  SECURITE  SECURITE
ICI
[Nom du navire × 3]
[Indicatif × 1]
```

### Texte du message

Si bref : diffusé directement sur la voie 16.
Si long : annoncer une voie de travail et diffuser sur cette voie.

Répéter jusqu'à accusé de réception d'une station côtière qui se chargera de diffuser un AVURNAV.

### Exemple

```
SECURITE, SECURITE, SECURITE
(A TOUS)
ICI RACHEL, RACHEL, RACHEL  FO8810
Épave à la dérive un mille au large du Cap Corse
```

### Diffusion météo CROSS en France

En France, les CROSS diffusent les bulletins météo plusieurs fois par jour sur les **voies 79 ou 80** selon la zone. Les BMS sont diffusés dès réception et répétés **toutes les heures** tant qu'ils sont valables.

### ASN (voie 70)

L'annonce de sécurité est transmise par ASN sur la voie 70, puis l'appel vocal suit sur la voie associée.
