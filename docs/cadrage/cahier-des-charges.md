# Cahier des charges — Rolliste, application compagnon JDR (règles DRAGONS)

| Version | Date | Statut | Auteure |
| - | - | - | - |
| 0.1 | 2026-11-20 | Premier brouillon (sur la base erronée du RNCP38822) | Gaiane |
| 0.2 | 2026-11-20 | Contraintes de budget (0 €), de temps et de mobile intégrées | Gaiane |
| 0.3 | 2026-11-20 | **Recalage sur le bon titre : RNCP39583**. Planning piloté par les blocs | Gaiane |
| 0.4 | 2026-11-20 | Front B validé ; commanditaire fictif ; évaluations en août 2028 ; demande d'autorisation à Studio Agate (§9) | Gaiane |
| 0.5 | 2026-11-20 | Nom « Rolliste » ; données de jeu inventées en attendant Studio Agate (§9.1) ; plan de cadrage ; documents déplacés dans `docs/cadrage/` | Gaiane |
| 0.6 | 2026-11-20 | Équipe fictive validée (Gaiane PO et cheffe de projet) ; commanditaire Marion Leclerc ; règles de langue ; GitHub Projects | Gaiane |
| 0.7 | 2026-11-24 | Glossaire : partie et séance (au lieu de « session / salon »), demande d'adhésion, entrée du journal, peuple, classe, maîtrise. Vocabulaire aligné dans tout le document | Gaiane |
| 0.8 | 2026-11-24 | Principe n°4 : pas d'annulation en V1, actions du MJ datées et visibles | Gaiane |

Les éléments marqués **[PROPOSÉ]** sont des recommandations qui attendent une validation. Une fois
validés, ils deviennent des ADR dans `docs/adr/`. La correspondance détaillée entre compétences et
preuves est dans [docs/rncp/matrice-RNCP39583.md](../rncp/matrice-RNCP39583.md).

---

## 1. Contexte

Le jeu de rôle sur table se pratique autour d'une table, avec des fiches papier, des dés et un
écran de MJ. Plusieurs tâches y restent fastidieuses :

- tenir à jour les fiches (PV, états, inventaire, expérience) ;
- suivre l'initiative et les PV des ennemis pendant un combat ;
- garder ses personnages d'une campagne à l'autre.

L'application **n'a pas vocation à remplacer la table**. Elle l'accompagne : le jeu reste
présentiel, l'application s'occupe des chiffres.

Le projet sert de support au titre **RNCP39583 — Expert en développement logiciel** (niveau 7,
certificateur YNOV). Soutenance en **août 2028**. Les 4 blocs sont évalués sur une mise en
situation réelle ou fictive :

| Bloc | Intitulé | Évaluation |
| - | - | - |
| BC01 | Cadrer un projet de développement d'applications logicielles | **Soutenance orale** devant un client (fictif ou réel) |
| BC02 | Concevoir et développer des applications logicielles | **Dossier écrit** et code source |
| BC03 | Coordonner et piloter un projet de développement | **Soutenance orale** et démonstration |
| BC04 | Maintenir l'application en condition opérationnelle | **Dossier écrit** |

**Objectif du projet : produire les preuves des 34 compétences.** Terminer l'application n'est pas
un but en soi. Le périmètre et le planning sont pilotés par la couverture du référentiel (§13).

## 2. Contraintes du projet

| Contrainte | Valeur | Conséquence |
| - | - | - |
| Budget | **0 €**, quelques euros possibles le jour de la soutenance | Développement en local ; production sur offres gratuites (§8) |
| Ressources | 1 personne, quelques heures par semaine. Premier budget : **~70 h** (dont ~50 h prévues par l'école) | MVP en tranche verticale ; planning par incréments (§12) |
| Équipe | **Équipe fictive complète** à simuler (BC03) | Personas, rôles, capacités, rituels (§11) |
| Client | **Commanditaire fictif : Marion Leclerc**, présidente de l'association fictive *La Guilde du Dé*, jouée par Gaiane | Distincte de la PO (Gaiane) : la cliente exprime le besoin et valide, l'équipe propose et réalise. Chaque échange client donne lieu à un compte rendu daté (BC01.2, BC01.11, BC03.6) |
| Évaluation | Les 4 blocs sont évalués à la même date, **au plus tard en août 2028** (date exacte inconnue) | Planning calé sur fin juin 2028 pour garder une marge |
| Bêta-testeurs | Joueurs réels disponibles | Retours, satisfaction et anomalies réels (BC02.6, BC04) |
| Production | BC04 exige une application **exploitée** : supervision, anomalies, correctifs, journal des versions | Mise en production avec de vrais utilisateurs **plusieurs mois avant** la soutenance |
| Dépôt | GitHub **public** | Aucun secret dans le code (scan en CI) ; contenus sous licence maîtrisés (§9) |
| Mobile | App Android installable en **.apk** (pas de store) ; tests via Expo Go | Choix du front (§7.6) |
| Réseau | Connexion obligatoire (authentification) | Pas de mode hors ligne en v1 |
| Droits | **Demande d'autorisation à Studio Agate en cours** | §9 |

## 3. Objectifs

| # | Objectif produit | Indicateur de réussite |
| - | - | - |
| O1 | Un joueur consulte et utilise sa fiche depuis son téléphone pendant la partie | Fiche affichée en < 2 s sur 4G, utilisable d'une main |
| O2 | Le MJ pilote la table depuis un seul écran | Joueurs, ennemis et combat visibles sans changer de page sur un écran ≥ 1024 px |
| O3 | Le MJ garde le contrôle narratif total | 100 % des jets passent par l'arbitrage du MJ ; tout score est modifiable par le MJ |
| O4 | Les actions sont visibles en temps réel | Jet du joueur affiché chez le MJ en < 500 ms (p95), serveur démarré |
| O5 | Un personnage est conservé d'une partie à l'autre | Expérience et inventaire conservés entre plusieurs parties |
| O6 | Les utilisateurs sont satisfaits | Indicateur de satisfaction mesuré après chaque séance de bêta-test (BC03.6) |

## 4. Principes métier (non négociables)

1. **Le MJ a le dernier mot.** Le système calcule un résultat ; le MJ rend un **verdict**
   (réussite, échec, valeur modifiée). Le joueur voit le verdict, jamais le calcul s'il est maquillé.
2. **Calcul automatique, surcharge libre.** Les valeurs de la fiche sont **calculées
   automatiquement** par défaut, et le MJ peut surcharger n'importe laquelle :
   `valeur effective = surcharge MJ ?? valeur calculée`. Une surcharge est visible, datée et
   révocable.
3. **Improvisation d'abord.** Aucune règle n'est bloquante. Les automatismes sont des **suggestions**.
4. **Traçabilité.** Chaque modification faite par le MJ (surcharge, verdict) est datée et visible.
   L'historique consultable et l'annulation sont prévus après la V1 (entretien du 24/11 : trop de
   complexité pour une première version).
5. **Un rôle par partie, pas par compte.** Un même utilisateur peut être MJ d'une partie et joueur
   dans une autre.

## 5. Acteurs et parties prenantes

| Acteur | Appareil principal | Description |
| - | - | - |
| Visiteur | — | Personne non connectée |
| Joueur | Smartphone Android (APK) ; navigateur sinon | Utilisateur participant à une partie avec un PJ |
| Meneur (MJ) | Portable ou tablette (web) | Utilisateur ayant créé la partie ; il arbitre tout |
| Administrateur | Ordinateur | Modération, support de niveau 2 |

Parties prenantes du projet (cartographie détaillée à produire en P0, BC01.1) : commanditaire,
utilisateurs bêta-testeurs, équipe fictive, Studio Agate (ayant droit), école et jury.

## 6. Glossaire

| Terme FR | Terme code (EN) | Définition |
| - | - | - |
| Personnage joueur (PJ) | `Character` | Fiche appartenant à un utilisateur, réutilisable entre parties |
| Personnage non joueur (PNJ) / ennemi | `NonPlayerCharacter` | Instance créée par le MJ dans une partie, souvent à partir d'une créature du bestiaire |
| Créature (bestiaire) | `Creature` | Entrée de référence du compendium (profil type) |
| Peuple | `Species` | Origine du personnage (donnée de référence du compendium) |
| Classe | `CharacterClass` | Classe du personnage (donnée de référence du compendium) ; indique notamment le type de magie |
| Maîtrise | `Proficiency` | Compétence maîtrisée par un PJ (maîtrise simple ou expertise) |
| Partie | `Table` | Aventure organisée par un MJ sur plusieurs séances, rejointe par des joueurs. Remplace « session / salon » |
| Séance | `GameSession` | Moment de jeu ouvert puis clôturé par le MJ ; les jets n'ont lieu que pendant une séance ouverte |
| Participation | `Seat` | Lien entre un utilisateur, une partie et le PJ engagé. Une **demande d'adhésion** est une participation au statut « demandée » |
| Code d'invitation | `InviteCode` | Code court permettant de rejoindre une partie |
| Jet de dés | `Roll` | Expression de dés (ex. `1d20+5`) et son résultat calculé |
| Verdict | `Ruling` | Décision du MJ sur un jet : validé, maquillé ou modifié, visible ou caché |
| Surcharge | `Override` | Valeur imposée par le MJ à la place d'une valeur calculée |
| Entrée du journal | `ActionLogEntry` | Action du MJ horodatée, consultable et annulable (journal d'actions de la partie) |
| Combat | `Encounter` | Affrontement avec ordre d'initiative et tours |
| État | `Condition` | Effet appliqué à un personnage (empoisonné, à terre…) |
| Compendium | `Compendium` | Données de référence : bestiaire, encyclopédie, sorts, objets, règles |

## 7. Architecture technique

### 7.1 Monolithe modulaire, prêt pour les microservices — **[VALIDÉ, ADR 0001 à rédiger]**

Les contextes métier ont des frontières aussi strictes que des services, mais ils sont déployés
dans **un seul processus**.

**Justification** (étude comparative, preuve BC01.7) :

- **Budget nul** : les offres gratuites hébergent un service sans difficulté. Plusieurs services
  en continu épuisent les quotas et multiplient les démarrages à froid.
- **Une personne, quelques heures par semaine** : des microservices imposent une messagerie, des
  transactions distribuées, du traçage, N déploiements et N pipelines. Ce coût fixe
  n'apporterait aucune preuve supplémentaire pour le référentiel.
- **Maintenance (BC04)** : une seule unité déployable simplifie la supervision, les correctifs et le
  journal des versions.
- **État de l'art** : *Monolith First* (Fowler) ; le monolithe modulaire est recommandé pour une
  petite équipe tant que les frontières du domaine ne sont pas éprouvées.

**Comment le projet reste « prêt pour les microservices » :**

1. **Un module = un contexte métier = une squad** de l'équipe fictive.
2. **Frontières vérifiées en CI** : un module n'importe que l'API publique (`contracts`) d'un autre.
   Contrôle par les tags Nx et dependency-cruiser.
3. **Un schéma PostgreSQL par module**, sans jointure entre schémas.
4. **Événements de domaine** entre modules (bus `@nestjs/cqrs` et table *outbox*). Brancher un
   broker plus tard ne touche que l'infrastructure.
5. **Critères de bascule documentés** : profil de charge, cycle de livraison ou équipe différents.
   `realtime` serait le premier candidat.

À éviter : un découpage par entité (personnage, monstre, combat), qui produit un « monolithe
distribué », et les « MVC qui se connectent » (MVC est un pattern de présentation ; chaque module
suit une Clean Architecture).

### 7.2 Modules (contextes métier)

| Module | Responsabilité | Schéma PostgreSQL |
| - | - | - |
| `identity` | Comptes, authentification, réinitialisation, rôles plateforme | `identity` |
| `character` | Fiches PJ, calcul automatique, surcharges, progression, inventaire | `character` |
| `table` (**cœur du domaine**) | Parties, séances, invitations, participations, PNJ, combats, jets et verdicts, journal d'actions | `table` |
| `compendium` | Bestiaire, sorts, objets, règles, encyclopédie ; recherche plein texte | `compendium` |
| `realtime` | WebSocket et notifications push ; **aucune logique métier** | — |

Bibliothèques pures, partagées entre le front et le back :

- `dice-engine` : parseur et lanceur de dés ;
- `rules-dragons` : calcul de la fiche selon les règles de DRAGONS, compatibles 5e ;
- `contracts` : DTO et événements versionnés ;
- `shared-kernel`.

### 7.3 Communication

- **Client → back** : REST (OpenAPI), JWT vérifié par un guard global.
- **Temps réel** : WebSocket (Socket.IO) via `realtime`, avec reconnexion automatique.
- **Module ↔ module** : événements (`RollRequested`, `RollRuled`, `ConditionApplied`,
  `CharacterUpdated`…) via le bus interne et l'outbox.

**Exemple de flux, un jet de dé :**

1. Le joueur lance `1d20+5` → le module `table` calcule le résultat avec `dice-engine`.
2. L'événement `RollRequested` est publié → `realtime` l'affiche chez le MJ.
3. Le MJ rend son verdict (« réussi », malgré une CA trop élevée) → `RollRuled`.
4. `realtime` notifie le joueur et la table, avec le verdict seulement.
5. Si le verdict inflige des dégâts ou un état → le module `character` met à jour la fiche.

### 7.4 GraphQL : non en v1

Il n'y a qu'un client par usage et des écrans bien connus. Le vrai besoin est le temps réel, que le
WebSocket couvre. GraphQL ajouterait un coût (N+1, cache HTTP perdu, autorisation par champ) pour un
gain faible.

### 7.5 Base de données et ORM

- **PostgreSQL**, avec un schéma par module. Volumétrie faible (quelques milliers d'entrées).
- Les blocs de statistiques hétérogènes sont stockés en **JSONB**, avec des colonnes typées pour les
  champs filtrables.
- Recherche en full-text PostgreSQL (configuration `french` et `unaccent`).
- **ORM : Prisma**, confiné à `infrastructure/`, avec des *mappers* vers les entités du domaine et
  TypedSQL pour les requêtes complexes. Écartés : TypeORM (couplage du domaine à l'ORM) et
  Sequelize (typage faible).

### 7.6 Front — **[VALIDÉ : option B, ADR 0002 à rédiger]**

Le besoin : un **APK Android** pour les joueurs (téléphone) et une **interface web dense** pour le
MJ (portable ou tablette).

| Critère | A. Expo seul (APK + web) | B. Expo (joueur) + Next.js (MJ) | C. Next.js seul (PWA empaquetée en APK via Capacitor) |
| - | - | - | - |
| Produit un APK | Oui, nativement (EAS) | Oui (côté joueur) | Oui, mais c'est une WebView qui embarque un export statique |
| Tests avec Expo Go | Oui | Oui (côté joueur) | Non |
| Push, vibration, secousse pour lancer les dés | Natif (Expo Push, Haptics, capteurs) | Natif côté joueur | Plugins Capacitor et FCM, plus de configuration |
| Interface MJ dense sur desktop | Moyenne (react-native-web, peu de composants desktop) | **Excellente** | **Excellente** |
| Accessibilité web (RGAA) | Moyenne (pas de HTML sémantique natif) | Bonne côté MJ | **Bonne** |
| Ta maîtrise de la stack | À apprendre | Partielle | **Maîtrisée** |
| Coût en temps | **Le plus faible** (une base de code) | Moyen : deux apps, mais les écrans joueur et MJ sont différents par nature ; seule la logique est partagée via `libs/` | Faible, mais rendu « appli web dans une coque » et SSR perdu dans l'APK |

**Décision : B (Expo pour les joueurs, Next.js pour le MJ).** Les interfaces joueur et MJ
n'ont presque aucun écran en commun. Deux apps ne doublent donc pas le travail : on partage
`contracts`, `dice-engine`, `rules-dragons` et un client d'API typé. Chaque support a l'outil le
plus adapté, et cela illustre directement BC02.3 (prototype multi-supports web et mobile).
**Repli** si le temps manque : A (critère et décision tracés par une ADR).

- **Notifications push** : Expo Push Service (gratuit, via Firebase Cloud Messaging).

### 7.7 Authentification

**Module `identity` maison** :

- mots de passe hachés en Argon2id ;
- JWT d'accès court et refresh token avec rotation (SecureStore sur mobile, cookie httpOnly sur le
  web) ;
- limitation de débit ;
- jeton de réinitialisation à usage unique.

Il suit l'OWASP ASVS niveau 1 (preuve BC02.5).

## 8. Environnements, hébergement et exploitation **[PROPOSÉ]**

| Environnement | Solution | Coût |
| - | - | - |
| Développement | docker-compose local (PostgreSQL), API Nest, Expo Go | 0 € |
| Production (bêta) | API : **Render** (web service gratuit, image Docker, WebSocket) · BDD : **Neon** (gratuit) · Web MJ : hébergement gratuit (Render static, Vercel Hobby ou Netlify) | 0 € |
| Jour de la soutenance | API temporairement sur une instance Render payante (pas de mise en veille) | Quelques € |
| CI/CD | GitHub Actions (illimité, dépôt public) ; EAS Build pour l'APK (~30 builds/mois, ou build local illimité) | 0 € |

**Exploitation et maintenance (BC04), outils gratuits :**

| Besoin | Outil | Compétence |
| - | - | - |
| Mises à jour des dépendances | Renovate ou Dependabot, avec politique de fusion documentée | BC04.1 |
| Supervision des erreurs | Sentry (offre gratuite) côté API et apps | BC04.2 |
| Disponibilité et alertes | Endpoint `/health` et sonde externe gratuite (UptimeRobot ou Better Stack) | BC04.2 |
| Consignation des anomalies | GitHub Issues avec modèle de fiche d'anomalie, labels de sévérité, et formulaire « signaler un bug » dans l'app | BC04.3 |
| Correctifs | Branche `fix/…` → CI → déploiement continu | BC04.4 |
| Journal des versions | SemVer, Conventional Commits et release-please (CHANGELOG généré) | BC04.6 |
| Retours utilisateurs | Questionnaire de satisfaction après chaque séance de bêta-test | BC04.5, BC03.6 |

**Limites des offres gratuites** (vérifiées en novembre 2026, à revérifier avant chaque jalon) :

- **Render** s'endort après 15 min d'inactivité et met environ 1 min à redémarrer. Sa base gratuite
  expire, d'où le choix de Neon.
- **Neon** offre 1 Go et 100 CU-heures par mois, sans expiration.

L'API est livrée en image Docker standard, configurée en 12-factor : elle est portable vers un autre
hébergeur.

## 9. Propriété intellectuelle

- **Statut** : demande d'autorisation écrite à Studio Agate (rédigée le 2026-11-20, à envoyer) (usage non commercial, dépôt
  GitHub public, APK distribué aux bêta-testeurs, démonstration devant le jury, nom de
  l'application). La réponse sera archivée **hors du dépôt public** et citée dans le dossier.
- **Tant que la réponse n'est pas reçue, ou si elle est restrictive :**
  - **les mécaniques de jeu** (formules, règles de calcul) peuvent être dans le code ;
  - **les textes et données de contenu** sont chargés depuis un fichier de données **non versionné**
    (import via un script d'administration), avec un jeu de démo minimal dans le dépôt ;
  - aucune illustration ni aucun logo de Studio Agate ;
  - mentions « projet non officiel, non affilié à Studio Agate » et crédits dans l'app et dans le
    README ;
  - aucune monétisation, ni publicité, ni don.
- Éviter un nom calqué sur « Donjons & Dragons » (marque de Wizards of the Coast).

### 9.1 Données de développement et de démonstration (en attendant la réponse)

- **Données de jeu inventées**, compatibles avec les mécaniques de DRAGONS (5e) : quelques peuples,
  classes, sorts, objets et créatures. Volume volontairement réduit (de l'ordre de 3 à 15 entrées par
  type), écrit à la main en fichiers de fixtures versionnés.
- **Données de volume** (utilisateurs, personnages, parties) générées par **@faker-js/faker**
  (maintenu, locale `fr`, graine fixe pour des jeux de données reproductibles).
- Écartés : `fantasy-content-generator` et `fantasy-name-generator` (non maintenus depuis 2022,
  contenus en anglais, sans lien avec les règles de DRAGONS).
- Toutes les fixtures passent par les **mêmes validations que le domaine** : une fixture invalide
  fait échouer le seed (et donc la CI).

## 10. Exigences non fonctionnelles

| Domaine | Exigence |
| - | - |
| Performance | Jet visible chez le MJ < 500 ms (p95) ; fiche chargée < 2 s en 4G (hors démarrage à froid) |
| Disponibilité | Reconnexion WebSocket automatique ; aucun état perdu en cas de mise en veille du téléphone ; sonde de disponibilité |
| Sécurité | OWASP Top 10 et ASVS niveau 1 ; autorisation par rôle **dans la partie** ; rate limiting ; scan des secrets (gitleaks) et des dépendances en CI |
| RGPD | Données minimales (e-mail, pseudo) ; droit à l'effacement ; registre des traitements ; hébergement en UE (Frankfurt) |
| Accessibilité | RGAA / WCAG 2.1 AA : contrastes, lecteurs d'écran (TalkBack, VoiceOver, NVDA), cibles tactiles, navigation clavier côté MJ |
| Éco-conception | Référentiel RGESN (exigé en BC01.3, BC01.6 et BC01.10) : payloads sobres, pas de polling, mise en veille hors usage, mesure (EcoIndex sur le web MJ) |
| Compatibilité | APK : Android 10 et plus ; web : navigateurs récents ; MJ ≥ 1024 px |
| Maintenabilité | Clean Architecture, frontières vérifiées en CI, couverture ≥ 80 % sur `domain/` et `application/`, ADR à jour |

## 11. Organisation du projet (équipe fictive complète)

- **Méthode** : Scrum, avec des sprints de 2 semaines, un Kanban dans GitHub Projects et des user
  stories estimées en points.
- **Équipe fictive** : 9 personas, équipe autonome sans pôle transverse. Gaiane y est **Product Owner
  et cheffe de projet**. Composition, compétences, RACI, styles managériaux, aménagements et
  contexte international (dev à Berlin) : voir [docs/agile/equipe.md](../agile/equipe.md).
- **Outil** : GitHub Projects (tableau Kanban, itérations pour les sprints, champ « points »,
  graphiques d'avancement). En phase d'exploitation (P4), passage en **Kanban pur**.
- **Langues** : documentation et commentaires en français ; code, commits, issues et PR en anglais.
- **Artefacts de pilotage (BC03)** :
  - planning et ordonnancement ;
  - tableau de bord d'indicateurs (vélocité, burndown, taux d'anomalies) ;
  - **un cas d'arbitrage documenté** avec logigramme ;
  - matrice d'affectation ;
  - styles managériaux appliqués selon les situations ;
  - plan de communication ;
  - grille de compétences et plan de développement ;
  - comptes rendus client ;
  - points de validation ;
  - indicateurs de satisfaction.
- **Rituels tracés** dans `docs/agile/` : planning, revue, rétrospective.
- **Revue de code** : checklist (qualité, sécurité, RGPD, accessibilité).

## 12. Planning prévisionnel piloté par les blocs **[PROPOSÉ]**

Horizon : décembre 2026 → août 2028, soit environ 88 semaines. Principe : **d'abord les preuves,
ensuite les fonctionnalités**. Le MVP est une **tranche verticale** qui suffit à alimenter les
4 blocs.

| Phase | Contenu | Blocs alimentés | Estimation |
| - | - | - | - |
| P0 — Cadrage | Commanditaire, parties prenantes, entretien de besoin, opportunités et menaces, faisabilité, risques, veille, étude comparative, équipe fictive, estimation de charge et budget, architecture et modélisation UML, wireframes et maquettes (prototype mobile joueur et web MJ), CDC v1, ADR | **BC01**, BC02, BC03 | 41,5 h |
| P1 — Socle | Monorepo, environnements de dev et de test, CI, déploiement continu, supervision, Renovate | BC02, BC04 | 25 h |
| P2 — Tranche verticale MVP | Authentification, PJ avec calcul automatique (sous-ensemble, dont les sorts : emplacements, DD de sauvegarde et bonus d'attaque), partie, séance et invitation, jet → verdict en temps réel, modification de fiche par le MJ ; combat simple : initiative, jets d'attaque et de dommages, PV ajustés par le MJ ; ennemis choisis dans le bestiaire (données inventées en attendant Studio Agate) ou saisis à la main ; états après la V1 ; tests unitaires | **BC02** | 80 h |
| P3 — Recette et mise en production | Cahier de recettes, plan de correction, manuels (déploiement, utilisation, mise à jour), bêta avec de vrais joueurs | BC02, BC03 | 25 h |
| P4 — Exploitation | Plusieurs mois de bêta : anomalies consignées, correctifs, mises à jour, journal des versions, support, satisfaction | **BC04**, BC03 | 20 h (étalées) |
| P5 — Pilotage continu | Tableaux de bord, comptes rendus, arbitrage, évaluation de l'équipe | **BC03** | 20 h (étalées) |
| P6 — Certification | Dossiers BC02 et BC04, supports oraux BC01 et BC03, répétitions | Tous | 40 h |
| Marge (≈ 15 %) | | | 35 h |
| **Socle certifiant** | | | **≈ 287 h, soit ≈ 3,3 h/semaine** |
| P7 — Extensions (optionnelles) | Combat, compendium, push, PNJ, montée de niveau | BC02 | 0 à 60 h |

**Jalons clés :**

- **Fin P0** : présentation du cadrage au commanditaire. C'est la répétition de l'oral BC01.
- **Mise en production de la bêta au plus tard début 2028**, pour accumuler des preuves
  d'exploitation (BC04).
- **Fin juin 2028** : dossiers BC02 et BC04 terminés, oraux BC01 et BC03 répétés (marge avant une
  évaluation au plus tard en août 2028).
- Le budget initial de 70 h couvre **P0, P1 et le début de P2**.
- Recalage à chaque sprint selon la vélocité réelle. Les écarts et arbitrages sont des preuves
  BC03.2 et BC03.3.

## 13. Couverture du référentiel RNCP39583

Synthèse ci-dessous ; le détail des 34 compétences, avec preuves et statut, est dans
[docs/rncp/matrice-RNCP39583.md](../rncp/matrice-RNCP39583.md).

| Bloc | Preuves principales |
| - | - |
| **BC01** Cadrer | Cartographie des parties prenantes, compte rendu d'entretien de besoin, SWOT et impact environnemental, faisabilité, matrice des risques, veille, étude comparative d'architecture, estimation de charge et budget, modèles C4 et UML, préconisations |
| **BC02** Concevoir et développer | Environnements, CI/CD, prototype, tests unitaires, code sécurisé et accessible, déploiement continu, cahier de recettes, plan de correction, documentation d'exploitation |
| **BC03** Piloter | Planning, suivi par indicateurs, cas d'arbitrage, affectation et management de l'équipe fictive, plan de compétences, comptes rendus client, démonstration |
| **BC04** Maintenir | Processus de mise à jour des dépendances, supervision et alertes, fiches d'anomalie, correctifs, journal des versions, recommandations, support |

## 14. Nom du produit — **[VALIDÉ]**

**Rolliste** : contraction de *roll* (lancer de dés) et de *rôliste* (joueur de jeu de rôle). Le
« O » du logo est un **d20 vectoriel**. Typographie : **Cinzel Decorative** Bold (licence SIL OFL),
lettres vectorisées. Logo, icône et charte : [docs/brand/](../brand/README.md).

Aucune application homonyme n'a été trouvée (recherche du 2026-11-20). Le nom proche le plus
connu est *Rolisteam*, une table virtuelle libre.

## 15. Questions ouvertes

1. **Premier oral** : l'école prévoit-elle un oral intermédiaire ? Si oui, porte-t-il sur ce projet ?
   Si c'est le cas, la présentation du cadrage (fin de P0) en fournit la matière.
2. **Réponse de Studio Agate** : à reporter au §9 dès réception.
