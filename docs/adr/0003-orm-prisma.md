# 0003 — ORM : Prisma

- **Statut** : Proposée (en attente de la décision de la PO)
- **Date** : 2026-11-26
- **Décideurs** : Karim (Tech Lead), Jonas (Dev Back)
- **Issue** : #17

## Contexte

- **Base** : PostgreSQL, **un schéma par module** et aucune jointure entre schémas (ADR 0001).
- **Clean Architecture** : le domaine ne doit dépendre d'aucun framework ni ORM. L'accès aux données
  est confiné à `infrastructure/`, derrière des ports (interfaces) définis dans `domain/`.
- **Données** : volumétrie faible ; blocs de statistiques hétérogènes stockés en JSONB ; recherche
  plein texte PostgreSQL (`french`, `unaccent`).
- **Qualité** : TypeScript strict, pas de `any` ; migrations versionnées et rejouables en CI.

## Options envisagées

| Option | Avantages | Inconvénients |
| - | - | - |
| A. TypeORM | Intégration NestJS historique ; décorateurs | Les entités portent des décorateurs d'ORM : le domaine se couple à l'ORM, contraire à la Clean Architecture ; typage des requêtes partiel |
| B. Sequelize | Mature, très répandu | Typage TypeScript faible ; même couplage des modèles |
| C. **Prisma** | Client entièrement typé, généré depuis le schéma ; migrations intégrées ; support multi-schémas PostgreSQL ; TypedSQL pour les requêtes complexes | Modèles Prisma distincts des entités du domaine : il faut écrire des *mappers* ; requêtes très spécifiques (plein texte) en SQL |
| D. SQL brut ou constructeur de requêtes (Kysely) | Contrôle total ; aucun couplage | Plus de code à écrire et à tester ; migrations à outiller à part |

## Décision

**Option C : Prisma, confiné à `infrastructure/`.** Le typage complet et les migrations intégrées
réduisent le travail d'une développeuse seule. Le surcoût des *mappers* est en réalité un avantage :
il garantit que les entités du domaine restent indépendantes de l'ORM.

## Conséquences

- **Plus facile** : requêtes typées, migrations versionnées, tests d'intégration des repositories
  avec Testcontainers.
- **Plus difficile** : écrire un *mapper* par agrégat (modèle Prisma ↔ entité du domaine) ; les
  requêtes plein texte passent par TypedSQL.
- **Règle** : aucun import de `@prisma/client` hors de `infrastructure/`. Contrôle par les règles
  de frontières (tags Nx, dependency-cruiser).
- **Actions** : un fichier de schéma Prisma organisé par schéma PostgreSQL (`identity`, `character`,
  `table`, `compendium`) ; le modèle de données suit le MCD.
