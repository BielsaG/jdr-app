# CLAUDE.md — Instructions permanentes du projet

> Ce fichier est relu par Claude à chaque prompt. Il fixe le cadre ; le détail est dans
> [docs/cadrage/cahier-des-charges.md](docs/cadrage/cahier-des-charges.md).

## 1. Contexte

- **Produit** : **Rolliste** (logo : le « O » est un d20), application compagnon pour des parties de JDR sur table, en présentiel (IRL),
  compatible avec les règles de DRAGONS (5e). Les joueurs jouent sur **smartphone** (fiche de personnage, lancers de dés,
  notifications). Le MJ joue sur **ordinateur portable ou tablette** (tableau de bord de la table :
  joueurs, ennemis, combats).
- **Cadre** : projet de certification **RNCP39583 — Expert en développement logiciel (niveau 7,
  YNOV)**. Soutenance en août 2028. L'auteure travaille seule mais **simule une équipe fictive
  complète** (bloc BC03). **But : produire les preuves des 34 compétences**, pas forcément finir
  l'application. Suivi dans [docs/rncp/matrice-RNCP39583.md](docs/rncp/matrice-RNCP39583.md).
- **Rôle de l'auteure dans l'équipe fictive : Product Owner et cheffe de projet.** Équipe autonome
  de 9 personnes ([docs/agile/equipe.md](docs/agile/equipe.md)), sans pôle transverse. Le
  commanditaire est un persona distinct de la PO : ne jamais faire valider par la PO ce qui doit
  l'être par la cliente.
- **Principe métier n°1 : le MJ a toujours le dernier mot.** Le système calcule et propose ;
  le MJ valide, maquille ou modifie. Aucune règle ne doit empêcher l'improvisation. Toute
  modification faite par le MJ est tracée (journal d'événements) et peut être annulée.

## 2. Règles de travail pour Claude

1. **Langue** (l'auteure a un niveau d'anglais basique) :
   - réponses de Claude et documentation (cadrage, ADR, manuels) : **français** ;
   - code (identifiants, fichiers, routes, tables) : **anglais** ;
   - commentaires de code (TSDoc) et descriptions Swagger / OpenAPI : **français** ;
   - commits, titres et contenus d'issues et de PR : **anglais simple**. Claude fournit toujours le
     texte anglais prêt à l'emploi, avec la traduction française quand c'est utile ;
   - vocabulaire métier : traduit une seule fois dans le glossaire du cahier des charges, puis
     réutilisé tel quel.
2. **Ordre de priorité** : le *cahier des charges* l'emporte sur les *ADR* ([docs/adr/](docs/adr/)),
   qui l'emportent sur les habitudes. Si une demande contredit l'un d'eux, le signaler
   avant d'agir.
3. **Confidentialité** : les documents de la cliente (demande, entretiens, comptes rendus), les
   échanges juridiques (Studio Agate) et toute donnée personnelle vont dans `confidentiel/`
   (ignoré par Git). Ne jamais les copier dans `docs/`, dans une issue ou dans un message de commit.
   La documentation publique peut reprendre les besoins sous forme reformulée.
4. **Rangement strict** : chaque fichier a une place prévue (voir §4). Ne jamais créer de dossier
   « utils », « helpers » ou « misc » fourre-tout. En cas de doute sur l'emplacement, poser la
   question.
5. **Décision d'architecture = ADR.** Tout choix structurant (bibliothèque, pattern, découpage,
   service AWS) donne lieu à une ADR courte au format `docs/adr/NNNN-titre.md` (contexte,
   options, décision, conséquences). Proposer l'ADR, ne pas trancher en silence.
6. **Rôle d'équipe** : au début de chaque tâche importante, indiquer le persona porteur
   (voir `docs/agile/equipe.md`). Cela alimente les preuves
   du bloc BC03.
7. **Traçabilité RNCP** : lorsqu'un livrable couvre une compétence (ex. `BC02.4`), le signaler
   en fin de réponse et proposer de mettre à jour le statut dans la matrice RNCP. Les codes
   `BCxx.y` renvoient **uniquement** au RNCP39583.
8. **Poser des questions** plutôt que deviner sur : les règles du jeu, le périmètre du MVP, les
   coûts AWS, et tout ce qui touche aux données personnelles.
9. **Git** : ne jamais committer ni pousser sans demande explicite. Une branche par fonctionnalité
   (`feat/…`, `fix/…`, `docs/…`, `chore/…`), PR vers `main`. Commits au format **Conventional
   Commits** en anglais : `type(scope): message` (ex. `feat(table): add invite code generation`),
   compatible avec release-please.

## 3. Architecture (cible — voir cahier des charges §7 et §8)

- **Contraintes structurantes** : budget **0 €**, une seule développeuse, quelques heures par
  semaine, soutenance en août 2028. Toute proposition doit être gratuite et sobre. Dire
  explicitement quand une solution coûte de l'argent ou du temps.
- **Monorepo Nx**, TypeScript strict partout.
- **Back** : NestJS en **monolithe modulaire, prêt pour les microservices**. Les modules sont
  découpés par contexte métier (DDD), et non par entité : `identity`, `character`, `table`,
  `compendium`, `realtime`.
  - Un module n'importe que l'API publique (`contracts`) d'un autre module, jamais ses entrailles.
    Contrôle par les tags Nx et dependency-cruiser.
  - Un **schéma PostgreSQL par module**, sans jointure entre schémas.
  - Communication entre modules par événements de domaine (bus `@nestjs/cqrs` et table outbox).
- **Dans chaque module : Clean Architecture / hexagonale.**
  - `domain/` : entités, value objects, événements de domaine, ports (interfaces). **Aucun import
    de framework** (ni Nest, ni Prisma).
  - `application/` : cas d'usage (commandes et requêtes). Dépend uniquement de `domain/`.
  - `infrastructure/` : adaptateurs (repositories Prisma, bus, clients externes).
  - `presentation/` : contrôleurs HTTP, gateways WebSocket, DTO et validation.
  - Les dépendances pointent **vers l'intérieur**. Ce sont les modules Nest qui câblent les ports
    aux adaptateurs.
- **Communication** : REST, documentée par Swagger (`@nestjs/swagger`, descriptions en français), WebSocket (Socket.IO) pour le temps réel. Pas de
  GraphQL en v1.
- **Front** : **Expo** pour les joueurs (APK Android, Expo Go, push natif) et **Next.js** pour le MJ
  (web ≥ 1024 px). Logique partagée via `libs/` (contracts, dice-engine, rules-dragons, client API).
- **Données** : PostgreSQL et Prisma (confiné à `infrastructure/`). L'autorisation de Studio Agate
  est **demandée, pas encore obtenue**. Tant qu'elle n'est pas confirmée par écrit : les mécaniques de jeu vont dans le code, mais les textes de contenu (bestiaire,
  encyclopédie) restent dans un fichier de données **non versionné**. En attendant, on
  utilise des **données de jeu inventées**, compatibles 5e et en petit volume (fixtures écrites à la
  main), plus `@faker-js/faker` avec une graine fixe pour les données de volume. Dépôt **public** : aucun
  secret, scan gitleaks.
- **Hébergement** : local (docker-compose) ; production bêta sur Render (API) + Neon (PostgreSQL) +
  hébergement web gratuit. Image Docker portable, configuration 12-factor.
- **Exploitation (BC04)** : Renovate, Sentry, sonde `/health`, fiches d'anomalie dans GitHub Issues,
  SemVer + Conventional Commits + release-please (CHANGELOG).
- **SOLID** appliqué sans dogmatisme : une abstraction doit répondre à un besoin réel
  (substitution, test). Pas d'interface « au cas où ».

## 4. Arborescence de référence

```
apps/
  api/                    # NestJS — point de composition du monolithe modulaire
  mobile/                 # Expo — APK Android (joueur)
  web/                    # Next.js — interface MJ
libs/
  backend/
    identity/             # chaque module : domain/ application/ infrastructure/ presentation/
    character/
    table/
    compendium/
    realtime/
  contracts/              # DTO et événements partagés, versionnés
  dice-engine/            # moteur de dés pur (aucune dépendance)
  rules-dragons/          # calcul automatique des fiches (règles DRAGONS / 5e, pur)
  shared-kernel/          # Result, erreurs de domaine, types de base
confidentiel/            # 🔒 ignoré par Git : documents client et juridiques
docs/
  adr/                    # Architecture Decision Records
  architecture/           # diagrammes C4, séquences, modèle de données
  agile/                  # équipe fictive, sprints, comptes rendus, arbitrages
  brand/                  # logo, charte graphique
  cadrage/                # cahier des charges + livrables du cadrage (P0), dont 03-specifications/
  rncp/                   # matrice compétences ↔ preuves
```

## 5. Qualité (Definition of Done)

- Tests unitaires sur `domain/` et `application/` ; tests d'intégration des repositories avec
  Testcontainers ; tests E2E des parcours critiques avec Playwright.
- Lint et formatage OK. Les règles Nx `enforce-module-boundaries` sont respectées.
- Pas de `any`, pas de secret dans le code, entrées validées en bordure (DTO).
- Accessibilité visée : RGAA / WCAG 2.1 AA. Données personnelles minimisées (RGPD).
- Documentation mise à jour (README du service, ADR, OpenAPI).
