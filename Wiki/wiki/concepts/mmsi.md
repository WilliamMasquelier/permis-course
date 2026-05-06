---
title: MMSI — Maritime Mobile Service Identity
type: concept
tags: [radio, crr, mmsi, asn]
sources: [../../raw/../Cours 1/anfr-manuel_crr.pdf]
related: [[../themes/08-radio-crr]], [[asn-dsc]], [[licence-anfr]], [[canaux-vhf]]
status: draft
updated: 2026-05-06
---

**Summary:** Le MMSI est un code numérique unique de 9 chiffres identifiant chaque navire ou station côtière dans le cadre du SMDSM. Il est attribué par l'ANFR en France et doit être programmé dans tous les équipements ASN (VHF ASN, BLU ASN, balise COSPAS-SARSAT, Inmarsat).

## Structure du MMSI

Le MMSI est composé de :
- **MID (Maritime Identification Digit)** : 3 premiers chiffres indiquant la nationalité.
- 6 chiffres d'identification du navire.

### MID français

| Zone | MID |
|------|-----|
| France métropolitaine | 226, 227, 228 |
| DOM / COM / Collectivités territoriales | MID spécifiques |

### Catégories de MMSI

| Catégorie | Format | Exemple |
|-----------|--------|---------|
| Station de navire | MID XXX XXX | 227 132 120 |
| Appel de groupe de navires | 0 MID XXX XX | 0227 310 00 |
| Station côtière | 00 MID XXXX | 00227 5400 |
| Appel de groupe stations côtières | 00 MID XXXX | 00227 4000 |

### MMSI spéciaux

| Usage | Format |
|-------|--------|
| Aéronefs SAR | 111 MID XXX |
| Aides à la navigation | 99 MID XXXX |
| Embarcations rattachées à un navire | 98 MID XXXX |

Exemple MMSI du CROSS Gris-Nez : **00 227 5100** (commence par 00 = station côtière).

## Attributions et règles

- Attribué par l'**ANFR** (Agence Nationale des Fréquences) lors de la demande de licence.
- Un MMSI attribué à un navire **ne peut pas être réutilisé sur un autre navire**.
- Le MMSI doit être **programmé à l'avance** dans les équipements (de préférence par un professionnel).
- En cas de détresse, le MMSI est transmis automatiquement dans l'alerte ASN → identification rapide et sûre du navire.

## Équipements nécessitant un MMSI

- VHF avec ASN (classe A, B ou D)
- BLU MF/HF avec ASN
- Inmarsat (B, C ou M)
- Radiobalise COSPAS-SARSAT

## Données communiquées par le MMSI

L'ANFR communique à l'UIT et aux organismes de secours (CROSS, CNES) les informations liées au MMSI :
- Nom du navire
- Indicatif d'appel
- Immatriculation
- Matériel à bord
- Coordonnées du titulaire (sauf opposition)

Ces données facilitent l'identification lors d'un appel de détresse.

## Point d'examen

Le MMSI commence toujours par **00** pour une **station côtière** — cela permet de distinguer un MRCC ou un CROSS d'un navire dans les messages ASN reçus.
