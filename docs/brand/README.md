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
| Titres de section, noms de personnage | **Cinzel**, graisse SemiBold (600), petites capitales espacées | SIL Open Font License 1.1 |
| Texte courant et chiffres des applications | **Atkinson Hyperlegible**, Regular (400) et Bold (700) : conçue pour la lisibilité (RGAA) | SIL Open Font License 1.1 |

Dans le logo, les lettres sont **vectorisées** : la police n'a pas besoin d'être installée pour
l'afficher. Dans les applications, elle sera chargée via `@expo-google-fonts/cinzel-decorative`
(mobile) et `next/font/google` (web).

## Direction artistique : « Grimoire nocturne »

Validée par la PO le 27/11/2026. La fantasy passe par des **détails** (typographie, filets dorés,
motif du d20) ; la structure reste **moderne** (espace, cartes, aucune texture lourde). Deux thèmes
validés : l'application suit la **préférence de l'utilisateur** (réglage du système, modifiable
dans l'application). Sans préférence, le thème **sombre** s'applique, pour les salles peu éclairées
(besoin B-18).

Aperçu de référence : [apercu-direction-artistique.html](apercu-direction-artistique.html), à
ouvrir dans un navigateur. Sa capture sert de référence visuelle aux prompts Figma.

### Couleurs

| Rôle | Thème sombre (défaut) | Thème clair |
| - | - | - |
| Fond | `#15111A` | `#F6F1E9` |
| Surface (cartes) | `#221C29` | `#FFFFFF` |
| Surface surélevée | `#2E2636` | `#EFE8DC` |
| Bordures | `#3D3347` | `#DDD3C4` |
| Texte (encre du logo) | `#EDE6F2` | `#1F1A24` |
| Texte secondaire | `#B8AEC2` | `#5A5163` |
| Accent d'action (dé du logo) | `#E5534B` | `#B3261E` |
| Or (niveau, badges, ornements, « modifié par le MJ ») | `#C9A55C` | `#7A5C22` |
| Réussite | `#6BBF8A` | `#2E7D4F` |
| Information | `#7FA7E0` | `#2F5FA8` |

Logo : lettres en couleur « Texte », dé en couleur « Accent », face du dé en accent à 10 %
d'opacité (clair) ou 16 % (sombre).

Contrastes vérifiés au niveau AA (WCAG 2.1) pour le texte, l'accent et l'or sur le fond. Une
information n'est jamais portée par la couleur seule : toujours une icône ou un libellé en plus.

### Formes et ornements

- **Coins arrondis : 6 px** partout (cartes, boutons, tuiles, badges). Seuls les avatars sont ronds.
  Valeur paire, pour un rendu net sur les écrans à densité 1,5× et 3× (5 px donnerait des demi-pixels).
- Filets dorés fins (1 px, opacité 50 %) avec un petit losange au centre pour séparer les sections.
- d20 du logo en filigrane (opacité ~6 %) et léger dégradé violet dans l'en-tête de fiche.
- Ombres très douces ; aucune texture (parchemin, bois) : plus élégant et plus léger (écoconception).
- Courte animation de dé au lancer.

### Icônes et illustrations

- Icônes d'interface : **Lucide**, en contour ([ADR 0007](../adr/0007-icones-lucide.md)).
- Emblèmes de classe : illustrations simples réalisées à part (artistes bénévoles ou images libres
  de droits), remplaçables par une image choisie par le joueur.

## Régénérer le logo

```bash
pip install fonttools
python docs/brand/source/generate-logo.py CinzelDecorative-Bold.ttf \
  docs/brand/logo-rolliste.svg docs/brand/icone-rolliste.svg
```

Le fichier de police n'est pas versionné. Il se télécharge depuis
[Google Fonts](https://github.com/google/fonts/tree/main/ofl/cinzeldecorative).
