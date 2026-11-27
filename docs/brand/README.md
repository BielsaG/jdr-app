# Identité visuelle — Rolliste

## Logo

| Fichier | Usage |
| - | - |
| [logo-rolliste.svg](logo-rolliste.svg) | Logo complet : README, écrans de connexion, supports de présentation |
| [icone-rolliste.svg](icone-rolliste.svg) | d20 seul : favicon, icône d'application, avatar |

Le nom mêle *roll* (lancer de dés) et *rôliste* (joueur de jeu de rôle). Le « O » est remplacé par
un **d20 vu de face**, le dé emblématique des règles 5e. Le premier « L » et le « E » sont volontairement
sans ornement ; seuls le « R » et le second « L » gardent le jambage décoratif de Cinzel Decorative.

Les SVG s'adaptent au **thème sombre** du système (`prefers-color-scheme`).

## Typographie

| Usage | Police | Licence |
| - | - | - |
| Logo et titres | **Cinzel Decorative**, graisse Bold (700) | SIL Open Font License 1.1 (© 2012 Natanael Gama) |
| Texte courant des applications | À définir avec les maquettes (P0, #43) | — |

Dans le logo, les lettres sont **vectorisées** : la police n'a pas besoin d'être installée pour
l'afficher. Dans les applications, elle sera chargée via `@expo-google-fonts/cinzel-decorative`
(mobile) et `next/font/google` (web).

## Couleurs

| Rôle | Thème clair | Thème sombre |
| - | - | - |
| Encre (lettres) | `#1F1A24` | `#EDE6F2` |
| Dé (accent) | `#B3261E` | `#E5534B` |
| Face du dé | accent, opacité 10 % | accent, opacité 16 % |

La palette complète des interfaces sera définie avec les maquettes (P0, #43, Amara). Elle devra respecter
les contrastes RGAA et privilégier un thème sombre pour les salles peu éclairées (besoin B-18).

## Régénérer le logo

```bash
pip install fonttools
python docs/brand/source/generate-logo.py CinzelDecorative-Bold.ttf \
  docs/brand/logo-rolliste.svg docs/brand/icone-rolliste.svg
```

Le fichier de police n'est pas versionné. Il se télécharge depuis
[Google Fonts](https://github.com/google/fonts/tree/main/ofl/cinzeldecorative).
