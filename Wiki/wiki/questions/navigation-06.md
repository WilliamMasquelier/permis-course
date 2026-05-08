---
title: "Navigation Q06 — Hauteur d'eau à un port secondaire"
type: question
tags: [navigation, marees]
sources: [raw/books/complete-yachtmaster-cunliffe.pdf]
related: [[marees-hauteurs]]
status: draft
updated: 2026-05-07
---

**Q : Comment calcule-t-on la hauteur d'eau disponible à un port secondaire à une heure donnée ?**

**R :** On utilise la méthode des courbes de marée : on calcule la hauteur à l'heure souhaitée en interpolant entre la pleine mer et la basse mer au port de référence, puis on applique la correction au port secondaire.

**Détail de la méthode :**
1. Trouver les heures et hauteurs de PM et BM au **port de référence** dans les tables de marée
2. Appliquer les **différences de temps et de hauteur** du port secondaire (annuaire) en interpolant si nécessaire selon le marnage du jour (vive-eau / morte-eau)
3. Obtenir PM et BM corrigées pour le **port secondaire**
4. Utiliser la **courbe de marée** du port de référence avec la "droite du jour" pour trouver la hauteur à l'heure désirée
5. Le résultat est directement en mètres au-dessus du **zéro hydrographique (ZH)**

**Point de vigilance :** les tables sont en UTC — ajouter +1 h (hiver) ou +2 h (été) pour l'heure locale française.
