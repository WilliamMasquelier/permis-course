---
title: "Navigation Q10 — GPS : datum et erreur de position"
type: question
tags: [navigation, gps]
sources: [raw/books/complete-yachtmaster-cunliffe.pdf]
related: [[gps-cartographie-electronique]], [[carte-marine]]
status: draft
updated: 2026-05-07
---

**Q:** Votre GPS affiche une position mais le bateau semble systématiquement décalé par rapport aux repères visuels sur la carte. Quelle est la cause probable et comment la corriger ?

**A:** La cause probable est un **décalage de datum** : le GPS est configuré sur un datum différent de celui de la carte. La solution est de vérifier le coin de la carte pour identifier son datum (souvent WGS84 sur les cartes modernes), puis de configurer le GPS sur ce même datum.

**Why:** Un décalage de datum entre GPS et carte peut provoquer des erreurs de plusieurs centaines de mètres — potentiellement fatal en pilotage côtier. WGS84 est le standard mondial moderne. Cf. [[gps-cartographie-electronique]].

**Source:** raw/books/yachtmaster-chapters/ch19-satellites-radar.txt
