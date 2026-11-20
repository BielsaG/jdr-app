# Spécifications fonctionnelles

| Contenu | Fichier | Issue |
| - | - | - |
| User stories | [userStories.md](userStories.md) | #13 |
| Diagrammes de cas d'utilisation | [cas-utilisation/](cas-utilisation/) | #14 |
| Descriptions textuelles des cas d'utilisation clés | `cas-utilisation/descriptions.md` (à venir) | #29 |
| Diagramme d'activité « jet → verdict » | à venir | #30 |
| Diagramme de fonctionnalités | à venir | #15 |

## Diagrammes de cas d'utilisation (v0.2)

| Diagramme | Contenu |
| - | - |
| [uc-00-vue-ensemble](cas-utilisation/uc-00-vue-ensemble.svg) | Acteurs, hiérarchie des acteurs, domaines fonctionnels |
| [uc-01-compte-administration](cas-utilisation/uc-01-compte-administration.svg) | Inscription, connexion, RGPD, signalement, administration |
| [uc-02-personnages-sessions](cas-utilisation/uc-02-personnages-sessions.svg) | Gestion des PJ, création et adhésion aux sessions |
| [uc-03-jeu-compendium](cas-utilisation/uc-03-jeu-compendium.svg) | Jets, verdicts, surcharges, combat, compendium |

**Génération** (PlantUML installé localement) :

```bash
cd docs/cadrage/03-specifications/cas-utilisation && plantuml -tsvg uc-*.puml
```

Les sources `.puml` font foi, et les `.svg` sont versionnés à côté. Le style commun est dans
`_style.puml`.

## Revue de l'ébauche v0.1 (2026-11-20)

L'ébauche réalisée avant le projet (un seul diagramme, sans fichier source) a été revue. Cette revue
sert aussi de preuve de démarche qualité.

| # | Constat dans la v0.1 | Règle UML ou métier | Correction en v0.2 |
| - | - | - | - |
| 1 | Les cas de l'« Espace Utilisateur » n'étaient reliés à **aucun acteur** | Un cas d'utilisation doit être déclenché par au moins un acteur | Chaque cas est associé à son acteur |
| 2 | Des « include » partaient de **cadres** vers « Se connecter » | `<<include>>` relie deux cas d'utilisation, jamais un cadre ou un paquetage | Relations supprimées |
| 3 | « Se connecter » était inclus partout | L'authentification est une **précondition**, pas une étape fonctionnelle incluse | Précondition indiquée en note |
| 4 | Plusieurs cadres « système » | Un diagramme a un seul sujet (le système), et les regroupements sont des paquetages | Un cadre « Rolliste » avec des paquetages |
| 5 | Administrateur spécialisait **Meneur** | L'héritage d'acteur signifie « peut faire tout ce que fait le parent » : un admin n'est pas un MJ | Administrateur spécialise Utilisateur |
| 6 | Acteur **Joueur** absent | Le rôle de joueur, porté dans une session, a des cas propres (lancer, choisir son PJ…) | Acteur Joueur ajouté |
| 7 | « Réinitialiser mon mot de passe » porté par l'Utilisateur connecté | On réinitialise quand on ne peut pas se connecter | Porté par le Visiteur |
| 8 | « Devenir meneur » distinct de « Créer une session » | Doublon | Fusionnés |
| 9 | « Recevoir une notification » modélisé comme un cas d'utilisation | Recevoir n'est pas un objectif de l'acteur ; c'est un effet d'un autre cas | Service de notifications en acteur secondaire, relié aux cas qui notifient |
| 10 | Cas manquants : verdict, surcharge, état, annulation, compendium, RGPD, signalement | Principes métier (§4 du cahier des charges), RGPD, BC04 | Ajoutés |
| 11 | Un seul diagramme dense | Lisibilité | Découpage : une vue d'ensemble et trois diagrammes détaillés |
