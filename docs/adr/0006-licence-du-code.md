# 0006 — Licence du code

- **Statut** : Proposée (en attente de la décision de la PO)
- **Date** : 2026-11-20
- **Décideurs** : Gaiane (PO), Karim (Tech Lead)
- **Issue** : #35

## Contexte

- Le dépôt sera **public**, car le jury doit pouvoir consulter le code. Sans licence, un dépôt
  public reste « tous droits réservés » : on peut le lire et le forker sur GitHub, mais pas
  réutiliser le code.
- Le projet est **non commercial**. C'est aussi la condition de l'autorisation demandée à Studio
  Agate. Cette condition porte sur l'**univers DRAGONS**, pas sur le code écrit pour le projet.
- Le dépôt contient trois types d'éléments, à traiter séparément :
  1. le **code** de l'application ;
  2. l'**identité** Rolliste (nom, logo), qu'on ne veut pas voir réutilisée par d'autres ;
  3. les **contenus de jeu**. Les données DRAGONS ne sont pas dans le dépôt (§9 du cahier des
     charges) ; les données inventées pour la démo y sont.

## Options envisagées

| Option | Avantages | Inconvénients |
| - | - | - |
| Aucune licence | Simple, protège tout | Personne ne peut réutiliser le code légalement ; peu valorisant pour un projet public |
| **MIT** | Standard, simple, reconnue par les recruteurs ; montre une culture open source | Autorise la réutilisation commerciale du code |
| AGPL-3.0 | Toute version modifiée mise en ligne doit publier son code (empêche un clone fermé) | Plus contraignante, moins courante, moins lisible pour un portfolio |
| PolyForm Noncommercial | Interdit l'usage commercial, cohérente avec l'esprit du projet | Pas une licence open source reconnue (OSI) ; peu connue |

## Proposition

**MIT pour le code, avec des exclusions explicites** dans le fichier `LICENSE` et le README :

- le **nom et le logo Rolliste** restent « tous droits réservés » ;
- l'**univers DRAGONS** et ses marques appartiennent à Studio Agate et ne sont **pas** couverts par
  la licence ;
- la police Cinzel Decorative reste sous sa propre licence (SIL OFL 1.1).

**Justification** : le code d'une application compagnon n'a pas de valeur commerciale propre sans
les contenus de jeu, qui eux restent protégés. MIT valorise le projet sans exposer ni l'identité ni
les droits de Studio Agate.

## Conséquences

- Ajouter un fichier `LICENSE` (texte MIT avec les exclusions) et mettre à jour la section
  « Mentions » du README.
- Vérifier la compatibilité des licences des dépendances avec MIT (contrôle automatisé en CI en
  phase P1).
- Si la PO préfère interdire tout usage commercial, l'alternative est PolyForm Noncommercial. Dans ce
  cas, le projet ne peut plus être présenté comme « open source ».
