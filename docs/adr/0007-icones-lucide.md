# 0007 — Bibliothèque d'icônes : Lucide

- **Statut** : Acceptée (décision de la PO le 2026-11-27)
- **Date** : 2026-11-27
- **Décideurs** : Gaiane (PO), Amara (UX/UI), Karim (Tech Lead)
- **Issue** : #43

## Contexte

- La direction artistique « Grimoire nocturne » utilise des **icônes en contour**, plus lisibles
  sur fond sombre (thème par défaut).
- Les mêmes icônes doivent servir dans l'application joueur (**Expo**) et dans l'interface MJ
  (**Next.js**).
- Budget 0 € : la bibliothèque doit être gratuite, y compris pour les icônes en contour.
- Besoins concrets : épée, bouclier, cœur, éclair, botte, dés, baguette, parchemin, sac, crâne.

## Options envisagées

| Option | Avantages | Inconvénients |
| - | - | - |
| Font Awesome Free | Très connue | Peu d'icônes en contour (« regular ») dans l'offre gratuite ; les icônes fantasy n'existent qu'en plein |
| **Lucide** (ISC) | Gratuite, toute en contour, plus de 1 500 icônes dont les besoins JDR ; paquets `lucide-react` et `lucide-react-native` | Moins d'icônes très spécifiques au JDR |
| Phosphor (MIT) | Gratuite, plusieurs épaisseurs de trait, paquets React et React Native | Plus volumineuse ; style un peu plus arrondi |

## Décision

**Lucide**, via `lucide-react` (web MJ) et `lucide-react-native` (mobile joueur).

## Conséquences

- Les icônes ont le même dessin sur les deux applications.
- On n'importe que les icônes utilisées, une par une, pour garder un paquet léger (écoconception).
- Une icône absente de Lucide est dessinée à la main en SVG, dans le même style : trait de 2 px,
  coins arrondis.
- Les emblèmes de classe ne relèvent pas de cette bibliothèque. Ce sont des illustrations réalisées
  à part, par des connaissances de la PO ou libres de droits.
- La licence ISC est compatible avec la licence MIT proposée pour le code (ADR 0006).
