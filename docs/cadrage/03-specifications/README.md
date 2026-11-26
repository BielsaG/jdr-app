# Spécifications fonctionnelles

| Contenu | Fichier | Issue |
| - | - | - |
| User stories | [userStories.md](userStories.md) | #13 |
| Diagrammes de cas d'utilisation | [cas-utilisation/](cas-utilisation/) | #14 |
| Diagrammes de séquence (MVP) | [sequences/](sequences/) | — |
| Modèle conceptuel de données (MCD, Mocodo) : référence détaillée | [MCD/](MCD/) | #20 |
| Diagramme de classes : entités principales (attributs, méthodes) | [classes/](classes/) | #20 |
| Descriptions textuelles des cas d'utilisation clés | `cas-utilisation/descriptions.md` (à venir) | #29 |
| Diagramme d'activité « jet → verdict » | à venir | #30 |
| Diagramme de fonctionnalités | à venir | #15 |

## Diagrammes de cas d'utilisation (v0.3)

| Diagramme | Contenu |
| - | - |
| [uc-00-vue-ensemble](cas-utilisation/uc-00-vue-ensemble.puml) | Acteurs, hiérarchie des acteurs, domaines fonctionnels |
| [uc-01-compte-administration](cas-utilisation/uc-01-compte-administration.puml) | Inscription, connexion, RGPD, signalement, administration |
| [uc-02-personnages-parties](cas-utilisation/uc-02-personnages-parties.puml) | Gestion des PJ, parties, adhésion, séances, mode de verdict, PJ géré par le MJ |
| [uc-03-jeu-compendium](cas-utilisation/uc-03-jeu-compendium.puml) | Jets, verdicts, surcharges, combat, compendium |

Les sources `.puml` font foi. Le style commun est dans `_style.puml`. Les images sont produites
à part par la PO.

**v0.3 (2026-11-24)** : « session » devient **partie** et **séance** (glossaire du cahier des
charges v0.7). Ajouts issus de l'entretien du 20/11 : ouvrir et clôturer une séance, rejoindre la
séance en cours, régler le mode de verdict, gérer le PJ d'un joueur sans téléphone.

## Diagrammes de séquence du MVP (v0.1)

Un diagramme par cas d'utilisation de la tranche verticale (cahier des charges §12, P2). Lignes de
vie génériques : application (mobile ou web), backend en trois couches (contrôleur, service,
repository), base de données. Le temps réel n'apparaît que dans le jet → verdict.

| Diagramme | Cas d'utilisation |
| - | - |
| [seq-01-inscription](sequences/seq-01-inscription.puml) | S'inscrire (uc-01) |
| [seq-02-connexion](sequences/seq-02-connexion.puml) | Se connecter (uc-01) |
| [seq-03-creer-pj](sequences/seq-03-creer-pj.puml) | Créer un PJ avec calcul automatique (uc-02) |
| [seq-04-creer-partie](sequences/seq-04-creer-partie.puml) | Créer une partie (uc-02) |
| [seq-05-generer-code](sequences/seq-05-generer-code.puml) | Générer un code d'invitation (uc-02) |
| [seq-06-rejoindre-partie-code](sequences/seq-06-rejoindre-partie-code.puml) | Rejoindre une partie par code (uc-02) |
| [seq-07-ouvrir-seance](sequences/seq-07-ouvrir-seance.puml) | Ouvrir une séance (uc-02) |
| [seq-08-rejoindre-seance](sequences/seq-08-rejoindre-seance.puml) | Rejoindre la séance en cours (uc-02) |
| [seq-09-jet-verdict](sequences/seq-09-jet-verdict.puml) | Lancer un jet et rendre un verdict (uc-03) |
| [seq-10-surcharger-valeur](sequences/seq-10-surcharger-valeur.puml) | Surcharger une valeur de la fiche d'un PJ (uc-03) |

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
