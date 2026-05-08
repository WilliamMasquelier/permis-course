---
title: COLREGs — visibilité réduite et collision
type: concept
tags: [regles-de-barre, securite]
sources: [raw/books/complete-yachtmaster-cunliffe.pdf]
related: [[securite-vhf-et-cross]]
status: draft
updated: 2026-05-07
---

**Summary:** Règle 19 des COLREGs (visibilité réduite), obligation de veille (Règle 5), AIS et radar pour la prévention des abordages, signaux sonores par brume.

## Règle 5 — Veille (Lookout)

*Tout navire doit en permanence assurer une veille visuelle et auditive appropriée, en utilisant également tous les moyens disponibles (radar, AIS, GMDSS).*

En visibilité réduite, **tous les instruments doivent être utilisés**. Un navire en collision qui n'aurait pas utilisé son radar ou son AIS ne trouverait aucune indulgence devant un tribunal.

## Règle 19 — Comportement par visibilité réduite

En brouillard ou faible visibilité, **il n'y a plus de navire privilégié ni de navire manœuvrant** (les règles d'abordage normales ne s'appliquent plus).

**Obligations :**
- Naviguer à une vitesse de sécurité (*safe speed*)
- Radar en veille permanente si disponible
- À l'écoute des signaux sonores et de la VHF
- Stopper les machines ou réduire fortement si un signal sonore est entendu en avant du travers
- **Ne pas croiser la route d'un navire en avant du travers** sauf pour passer en arrière

**Règle 19(d) — Action radar :**
- Éviter de changer de cap à **bâbord** pour un contact en avant du travers (sauf si on le double)
- Éviter de changer de cap **vers** un navire par le travers ou par l'arrière

## AIS — Système d'identification automatique

**AIS** (Automatic Identification System) : système d'échange automatique de données entre navires et stations côtières.

### Obligations
- **Classe A** : obligatoire sur tout navire SOLAS > 300 tjb en voyage international, et tout navire > 500 tjb
- **Classe B** : non obligatoire pour les plaisanciers, mais recommandé

### Informations transmises
- Données dynamiques : position GPS, vitesse fond (SOG), cap fond (COG), vitesse de giration (ROT)
- Données statiques : nom du navire, indicatif, MMSI, dimensions, type

### Limitations de l'AIS — ne remplace pas la veille ni le radar
- Les navires de pêche, les voiliers et les militaires **ne transmettent pas toujours** leur AIS
- Un navire de commerce peut **filtrer les cibles Classe B** pour ne voir que les Class A
- L'AIS indique le cap sur le fond, non le cap vrai — en courant fort, le vecteur peut être trompeur
- **L'AIS ne remplace ni le radar ni la veille visuelle**

### CPA et TCPA (Closest Point of Approach / Time to CPA)
L'AIS (et le MARPA radar) calculent :
- **CPA** : distance minimale d'approche prévue
- **TCPA** : temps avant cette approche

Si le CPA est inférieur à 0,5 Mm et le TCPA < 6 min → agir immédiatement.

## Radar — prévention des abordages

### Modes d'affichage
| Mode | Description | Avantage |
|------|-------------|----------|
| Head-up | Nord de l'écran = étrave | Intuitif mais tourne à chaque changement de cap |
| North-up | Nord en haut, stabilisé au compas | Facile à comparer avec la carte |
| Course-up | Cap stabilisé en haut | Meilleur des deux mondes |

### MARPA (Mini Automatic Radar Plotting Aid)
- Calcule automatiquement le CPA, TCPA, vitesse et cap du contact
- En **True Motion** : les cibles se déplacent à leur vitesse réelle — plus intuitif
- En **Relative Motion** : les cibles se déplacent par rapport à votre bateau

### EBL et VRM
- **EBL** (Electronic Bearing Line) : ligne de relèvement depuis votre position — si la cible reste dessus ET se rapproche → risque de collision
- **VRM** (Variable Range Marker) : cercle de distance pour mesurer la portée d'une cible

## Signaux sonores par brume (Fog signals — Règle 35)

| Signal | Navire | Rythme |
|--------|--------|--------|
| 1 son long toutes les 2 min | Navire en marche, sous propulsion | — |
| 2 sons longs toutes les 2 min | Navire en marche, stoppé | — |
| 1 son long + 2 sons courts | Navire remorqueur, à voile, au mouillage | — |
| 1 coup de cloche rapide (1 min) | Navire au mouillage | — |

**Règle de conduite** : si vous entendez un signal sonore **en avant du travers** en visibilité réduite → réduire la vitesse ou stopper → **ne jamais accélérer vers le son**.

## Termes français / anglais

| Terme français | Terme anglais |
|----------------|---------------|
| Visibilité réduite | Restricted visibility |
| Brouillard | Fog |
| Veille | Lookout |
| Vitesse de sécurité | Safe speed |
| Radar | Radar |
| Feux de navigation | Navigation lights |
| Signaux sonores | Sound signals |
| CPA | Closest Point of Approach |
| TCPA | Time to CPA |
| MARPA | Mini Automatic Radar Plotting Aid |

## Voir aussi
- [[securite-vhf-et-cross]] — Communication en situation d'urgence
- [[regles-de-barre-navires-privilegies]] — Règles en visibilité normale
