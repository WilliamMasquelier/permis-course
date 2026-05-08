---
title: "VHF Marine — MAYDAY, PAN PAN et Canal 16"
module: 6
module_title: "Radio et Réglementation"
session_in_module: 1
duration_min: 40
type: lesson
status: draft
updated: 2026-05-07
---

> [SCENE]
> **Mardi matin, 8h45. À bord, avant l'appareillage pour Fethiye.**
>
> William décroche le combiné VHF. Canal 16. Il hésite.
>
> "Je veux appeler la capitainerie de Fethiye pour confirmer notre poste à quai. Quel canal ?"
>
> Mehmet : "Canal 16, c'est le canal de veille et d'appel. Tu les appelles sur le 16, ils te disent de passer sur un canal de travail — souvent le 9, 11, ou 12 ici en Turquie."
>
> William appuie sur le micro. Sa main tremble légèrement. Derrière lui, Emmanuel observe — silencieux, pour une fois. Rebecca est dans la descente, à portée d'oreille. Premier appel radio officiel.
>
> "Fethiye Liman, Fethiye Liman, ici voilier Deniz Rüzgarı, à l'écoute sur le seize, terminé."
>
> Grésillements. Puis une voix turque accueillante : "Deniz Rüzgarı, passez sur le canal onze." William pousse un long soupir. Emmanuel lui tape sur l'épaule.

## Le VHF maritime — fonctionnement

Le **VHF maritime** (Very High Frequency, 156–174 MHz) est le moyen de communication principal en navigation côtière. Sa portée est de l'ordre de **20–40 milles** entre deux bateaux, et plus grande vers les stations côtières en hauteur.

**Principe de propagation :** Le VHF se propage en ligne droite (*ligne de visée*). La portée dépend de la hauteur des antennes — une antenne montée en tête de mât à 15 m offre une portée de 20–25 milles vers une station côtière en hauteur, et 10–15 milles vers un autre bateau à flottaison. Les obstacles (collines, falaises) coupent la propagation.

**Puissance :**
- **VHF fixe (25W)** : portée maximale, antenne déportée en hauteur, DSC intégré. L'équipement de référence pour la navigation en mer.
- **VHF portatif (5–6W)** : portée 5–10 milles. Portable sur soi, résistant à l'eau, indispensable comme backup ou pour communiquer depuis l'annexe. En cas d'abandon du navire, emportez le portatif dans le gilet.

**Pourquoi 25W vs 5W compte en détresse :** Si votre bateau est en train de couler et que vous utilisez le VHF fixe, vous portez à 30 milles. Avec le portatif seul dans l'eau, vous portez à 5 milles. Toujours utiliser le fixe pour le MAYDAY initial.

**Le DSC (Digital Selective Calling / ASN) :** Fonctionnalité de votre VHF fixe qui envoie automatiquement un message numérique structuré sur la voie 70 : votre MMSI, votre position GPS (si le VHF est couplé au GPS), et la nature de la détresse. Ce message est reçu simultanément par toutes les stations VHF DSC à portée. Les secours savent qui vous êtes et où vous êtes en quelques secondes, *sans que vous ayez à parler*.

**Le MMSI (Maritime Mobile Service Identity)** : numéro à 9 chiffres qui identifie votre bateau de façon unique dans le monde. Il est enregistré auprès de l'ANFR (France) et lié aux données de votre bateau (nom, port d'attache, coordonnées du propriétaire). Sans MMSI enregistré, une alerte DSC génère une fausse alarme sans information utile.

Voir [[concepts/canaux-vhf]], [[concepts/mmsi]].

**Équipements :**
- **VHF fixe** : plus puissant (25W), antenne haute, DSC intégré
- **VHF portatif** : 5–6W, autonome, à avoir en cas d'urgence

## Les canaux principaux

**Le canal 16 est le canal universel de détresse et d'appel.** Toute radio maritime doit y maintenir une veille permanente. On appelle sur le 16 pour initier tout contact, puis on bascule immédiatement sur un canal de travail pour la conversation. Le canal 16 doit rester libre pour les appels de détresse.

**Le canal 70 est UNIQUEMENT pour les données DSC** — les signaux numériques automatiques. Ne jamais émettre vocalement dessus. C'est une infraction et cela brouille les alertes de détresse automatiques.

| Canal | Usage |
|-------|-------|
| **16** | Veille obligatoire, appels d'urgence, appels initiaux |
| **9** | Canal de travail plaisance (France) |
| **67** | Canal SAR (France) |
| **70** | DSC (Appel Sélectif Numérique — données uniquement, ne pas vocaliser) |
| 12, 14 | Ports (VTS) |
| 68–72, 77 | Canaux de travail plaisance |

En Turquie, les canaux de travail des ports varient : Fethiye utilise le canal 12 pour le VTS. En France, après l'appel sur le 16, le canal 9 est le plus courant pour la plaisance.

## Procédures radio — le bon langage

La discipline radio évite les confusions dans des situations où la clarté peut sauver des vies.

Voir [[concepts/alphabet-oaci]].

**Alphabet phonétique OACI :**
Alpha, Bravo, Charlie, Delta, Echo, Foxtrot, Golf, Hotel, India, Juliet, Kilo, Lima, Mike, November, Oscar, Papa, Quebec, Romeo, Sierra, Tango, Uniform, Victor, Whiskey, X-ray, Yankee, Zulu.

**Quand épeler :** Toujours pour les noms propres, immatriculations, MMSI. Utiles pour les lettres ambiguës en radio : B (Bravo, pas Sierra), D (Delta, pas Tango), M (Mike, pas November), P (Papa, pas Bravo).

**Terminologie standard :**
- "Ici" / "De" = identification de l'émetteur
- "À" = identification du destinataire
- "Terminé" / "À vous" = fin de transmission, réponse attendue
- "Reçu" = message bien reçu, pas de réponse nécessaire
- "Bien reçu cinq sur cinq" = réception excellente
- **"Silence"** = mot d'ordre du CROSS pour dégager le canal 16 pendant les opérations SAR — toutes les stations cessent immédiatement d'émettre
- **"Silence Fini"** = le CROSS annonce la fin de l'opération, le trafic normal peut reprendre

**Format d'un appel standard :**
```
[Destinataire], [Destinataire]
Ici [Votre nom], [Votre nom]
Terminé
```
Réponse attendue :
```
[Votre nom]
Ici [Destinataire]
Canal [X]
```

## MAYDAY — détresse grave

MAYDAY s'utilise en cas de **danger grave et imminent** pour le navire ou les personnes : naufrage en cours, incendie incontrôlable, blessé grave qui engage le pronostic vital, homme à la mer non récupéré.

Le mot "MAYDAY" vient du français "m'aidez" — il est reconnu dans toutes les langues maritimes.

![[vhf-mayday-flow.svg]]

**Procedure DSC d'abord (si disponible) :**
1. Ouvrir le capot rouge, appuyer ≥ 5 secondes → l'alerte numérique part automatiquement sur le canal 70 avec MMSI + position GPS.
2. La VHF passe automatiquement sur le canal 16 pour le message vocal.

**Structure du message vocal MAYDAY :**
```
MAYDAY MAYDAY MAYDAY
Ici [nom du bateau] [MMSI]
MAYDAY [nom du bateau]
Position : [lat/lon ou relèvement depuis un amer connu]
Nature du problème : [incendie/voie d'eau/etc.]
Type d'assistance requise : [remorquage/évacuation médicale/etc.]
Nombre de personnes à bord : [N]
Informations utiles : [couleur de la coque, type de bateau]
Terminé
```

**Exemple complet :**
```
MAYDAY MAYDAY MAYDAY
Ici voilier Deniz Rüzgarı, MMSI 271XXXXXX
MAYDAY Deniz Rüzgarı
Position : 36°43'N 29°02'E, 4 milles à l'ouest de Göcek
Incendie dans la salle des machines incontrôlable
Demandons assistance immédiate
4 personnes à bord
Voilier bois, coque blanche, 13 mètres
Terminé
```

**Relay MAYDAY :** Si vous captez un MAYDAY sans réponse : retransmettez en préfixant par "MAYDAY RELAY, MAYDAY RELAY, MAYDAY RELAY, à tous, ici [votre nom]..." suivi du message original.

Voir [[concepts/procedure-mayday]].

## PAN PAN — urgence non-mortelle

**PAN PAN** s'utilise pour une urgence sérieuse qui n'est pas encore une menace vitale immédiate : blessé qui nécessite des soins médicaux, homme à la mer récupéré mais inconscient, panne moteur avec dérive vers un danger dans les prochaines heures, avarie sérieuse sans naufrage imminent.

**PAN PAN** s'utilise pour une **urgence moins grave** mais nécessitant une assistance : blessé non vital, panne moteur en dérive vers un danger, bateau en difficulté sans risque immédiat.

Format similaire au MAYDAY : PAN PAN × 3, puis les mêmes éléments (identification, position, nature, assistance requise). L'appel se fait sur le canal 16.

**Annulation :** Quand l'assistance arrive ou que la situation se résout, annoncez sur le canal 16 : "À tous, ici [nom], annulation de mon PAN PAN de [heure UTC], tout est en ordre."

Voir [[concepts/procedure-pan-pan]].

## SÉCURITÉ — avis de navigation

**SÉCURITÉ** est le préfixe pour les informations urgentes concernant la navigation ou la météo. Ce n'est pas un appel de détresse — c'est une information importante pour tous les navires dans le secteur.

Utilisé par :
- Le CROSS pour diffuser les bulletins météo spéciaux (BMS)
- Les navires qui signalent un danger flottant, une épave, une zone à éviter
- Les capitaineries pour les avis aux navigateurs urgents

Format : "Sécurité, Sécurité, Sécurité, à tous..." puis l'information.

Voir [[concepts/procedure-securite]].

## DSC — Appel Sélectif Numérique

Le **DSC** transforme votre VHF en système de détresse automatique. En cas d'urgence, vous n'avez pas à trouver les mots — un seul geste suffit.

**Comment fonctionne une alerte de détresse DSC :**
1. Appuyer ≥ 5 secondes sur le bouton rouge sous le capot protecteur
2. Votre VHF transmet automatiquement 5 fois sur le canal 70 : MMSI + position GPS (si couplée) + nature de la détresse
3. L'alerte se renouvelle toutes les 4 minutes jusqu'à accusé de réception
4. La VHF passe automatiquement sur le canal 16 pour le message vocal
5. Les stations côtières et navires DSC dans un rayon de 20–40 milles reçoivent l'alerte avec votre position

**Ce que les secours voient :** Votre MMSI → leur permet d'accéder immédiatement à la fiche de votre navire (nom, port, description, contacts d'urgence). Votre position GPS → ils savent où envoyer les secours avant même de vous avoir parlé.

**Programmation préalable obligatoire :** Le MMSI doit être programmé à l'avance dans la VHF par un professionnel. Une VHF DSC sans MMSI programmé ne peut pas envoyer d'alerte de détresse correcte. Priorité à faire avant de prendre la mer.

**Fausse alerte :** Annulez immédiatement sur le canal 70 (ASN) si votre VHF le permet, puis sur le canal 16 verbalement.

Voir [[concepts/asn-dsc]], [[concepts/mmsi]].

> [EXEMPLE GOLFE]
> **Contact avec les Gardes-Côtes turcs (Sahil Güvenlik) :**
>
> En Turquie, la veille du canal 16 est assurée par la **Sahil Güvenlik** (Garde Côtière turque). La procédure est identique aux COLREGs/SOLAS — même langage international.
>
> En entrant dans les ports turcs, certains requièrent un appel VHF préalable (Port Fethiye : canal 12 pour le VTS).
>
> Si vous avez un MMSI turc (ou français avec inscription ANFR), le DSC fonctionne également en eaux turques.

> [MINI-QUIZ]
> **Question 1 :** Dans quel ordre commencez-vous un appel MAYDAY ?
> **A)** Position, nom du bateau, MAYDAY
> **B)** MAYDAY MAYDAY MAYDAY, puis nom du bateau
> **C)** Canal 16, nature du problème, nom du bateau
> **Réponse:** B — Le mot MAYDAY est répété trois fois en premier, puis le nom du bateau. La position et la nature du problème suivent. La répétition de MAYDAY identifie immédiatement la nature de l'appel aux auditeurs.
>
> **Question 2 :** Vous êtes en panne moteur à 3 milles du port, sans vent, avec courant vous poussant vers des rochers à 30 minutes. Quel type d'appel radio faites-vous ?
> **A)** MAYDAY — danger grave et imminent
> **B)** PAN PAN — urgence sans danger immédiat de mort
> **C)** Appel ordinaire sur canal 9
> **Réponse:** A — Si les rochers sont à 30 minutes, vous avez peu de temps et le risque de naufrage est réel et imminent. MAYDAY est approprié. PAN PAN aurait été correct si vous étiez en dérive mais sans danger proche.

> [TRANSITION]
> À Fethiye, ils amarrent au quai de la douane. L'officier monte à bord pour vérifier les papiers. Il y a le "Carnet de Navigation" (le *Transit Log* en Turquie), le livre de bord, les licences radio. Tout est en ordre. Il signe, tamponne, sourit. Quand il repart, Emmanuel dit : "Donc même en vacances, la paperasse nous suit." Rebecca : "En Martinique, le gendarme maritime venait à bord avec un café." Emmanuel, amusé. "Et pour naviguer en France ?" demande-t-il. "Quels papiers faut-il ?"
>
> **Session 6.2 — Documents, Licence et Réglementation.**
