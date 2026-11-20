<p align="center">
  <img src="docs/brand/logo-rolliste.svg" alt="Rolliste" width="420">
</p>

<p align="center">
  <strong>L'application compagnon des parties de jeu de rôle autour d'une vraie table.</strong>
</p>

<p align="center">
  <em>Statut : phase de cadrage (P0) · aucun code applicatif pour l'instant</em>
</p>

---

## Présentation

**Rolliste** accompagne les parties de jeu de rôle sur table **en présentiel**. Le jeu reste autour
de la table ; l'application s'occupe des chiffres.

- **Joueurs, sur smartphone** : leur fiche de personnage (calculée automatiquement), leurs lancers
  de dés, et des notifications quand le meneur agit sur leur personnage.
- **Meneur de jeu, sur ordinateur ou tablette** : une vue d'ensemble de la table (joueurs, ennemis,
  combat), avec la main sur **tous** les résultats.

> **Principe n°1 : le MJ a toujours le dernier mot.** L'application calcule et propose ; le meneur
> valide, maquille ou modifie. Aucune règle ne bloque l'improvisation.

L'application est pensée pour les règles de **DRAGONS** (compatibles 5e).

## Contexte

Ce projet sert de support à la certification **RNCP39583 — Expert en développement logiciel**
(niveau 7). Il simule un projet mené par une agence fictive, *Forge & Pixel*, pour une cliente
fictive, l'association *La Guilde du Dé*.

## Fonctionnalités visées (MVP)

| Domaine | Fonctionnalités |
| - | - |
| Compte | Inscription, connexion, réinitialisation du mot de passe, suppression du compte |
| Personnages | Création, fiche calculée automatiquement, conservation d'une partie à l'autre |
| Parties | Création d'une partie, invitation par code, ouverture de la séance du jour par le MJ |
| Jeu | Lancers de dés, verdict du MJ en temps réel, modification libre des fiches par le MJ |
| Combat | Initiative, tours, points de vie et états des ennemis et des PJ |

Le détail et les priorités sont dans le [cahier des charges](docs/cadrage/cahier-des-charges.md) et
les [user stories](docs/cadrage/03-specifications/userStories.md).

## Architecture et technologies (cible)

| Couche | Choix |
| - | - |
| Application joueur | **Expo** (React Native), livrée en APK Android et en version navigateur |
| Interface MJ | **Next.js** |
| API | **NestJS**, monolithe modulaire découpé par contexte métier, Clean Architecture |
| Temps réel | WebSocket (Socket.IO) |
| Données | **PostgreSQL** (un schéma par module) avec **Prisma** |
| Documentation de l'API | Swagger (OpenAPI) |
| Organisation du code | Monorepo **Nx**, TypeScript strict |
| Hébergement | Offres gratuites : Render (API), Neon (PostgreSQL) |

Les choix sont argumentés dans le cahier des charges (§7 et §8). Les décisions d'architecture
seront consignées dans [docs/adr/](docs/adr/).

## Organisation du dépôt

```
apps/            # applications : api, mobile, web (à partir de la phase P1)
libs/            # modules métier et bibliothèques partagées (à partir de P1)
docs/
  agile/         # équipe, méthode de travail, sprints
  brand/         # logo et charte graphique
  cadrage/       # cahier des charges, besoins, spécifications, diagrammes UML
  rncp/          # correspondance entre compétences et preuves
CLAUDE.md        # règles de travail du projet
```

## Documentation

| Document | Contenu |
| - | - |
| [Cahier des charges](docs/cadrage/cahier-des-charges.md) | Besoins, contraintes, architecture, planning |
| [Plan de cadrage](docs/cadrage/README.md) | Étapes, livrables et avancement de la phase P0 |
| [Spécifications](docs/cadrage/03-specifications/README.md) | User stories, diagrammes de cas d'utilisation |
| [Équipe](docs/agile/equipe.md) | Composition, compétences, responsabilités |
| [Méthode](docs/agile/methode.md) | Scrum, tableau Kanban, Definitions of Ready et Done, indicateurs |
| [Matrice RNCP](docs/rncp/matrice-RNCP39583.md) | Suivi des preuves pour les 34 compétences |

## Suivi du projet

- **Tableau** : [GitHub Projects « Rolliste »](https://github.com/users/BielsaG/projects/3)
  (sprints de 2 semaines).
- **Branches** : `type/<n° d'issue>-description` (ex. `docs/5-stakeholders`), puis une pull request
  vers `main`.
- **Commits** : [Conventional Commits](https://www.conventionalcommits.org/fr/), en anglais
  (ex. `feat(table): add invite code generation`).
- **Langues** : code, commits, issues et PR en anglais ; documentation et commentaires de code en
  français.

## Démarrage

L'installation et le lancement en local seront documentés à la fin de la phase P1 (socle
technique).

## Mentions

- *Rolliste* est un projet **non officiel et non commercial**. Il n'est **pas affilié à Studio
  Agate**. DRAGONS est une marque de Studio Agate, et tous les droits sur l'univers et ses contenus
  lui appartiennent.
- En attendant la réponse de Studio Agate, les données de jeu du dépôt sont **inventées** et
  compatibles avec les mécaniques 5e.
- Licence du code : à définir.

---

<details>
<summary>English summary</summary>

**Rolliste** is a companion app for in-person tabletop role-playing games. Players use their phone
as a character sheet and dice roller; the game master runs the table from a laptop or tablet and
always has the final say on every result. Built with Expo, Next.js, NestJS and PostgreSQL, as a
certification project (RNCP39583, *Expert en développement logiciel*). Currently in the framing
phase; no application code yet. Unofficial, non-commercial, not affiliated with Studio Agate.

</details>
