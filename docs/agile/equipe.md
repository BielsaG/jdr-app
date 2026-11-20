# Équipe projet Rolliste (fictive)

> **Statut : v3, validée le 2026-11-20.** Livrable de l'étape 0 du cadrage. Compétences visées :
> BC03.1, BC03.4, BC03.5 (et BC01.9 via les coûts journaliers).
> Tous les personas sont **fictifs**, à l'exception de Gaiane Bielsa. Toute ressemblance avec des
> personnes réelles serait fortuite.

## 1. Cadre organisationnel

| Élément | Choix |
| - | - |
| Structure | **Forge & Pixel** (fictive), agence de développement, Lyon |
| Équipe | **Autonome et pluridisciplinaire** : toutes les compétences nécessaires (produit, design, développement, qualité, exploitation) sont dans l'équipe. Aucune dépendance à un pôle externe |
| Commanditaire | Persona fictif externe : **Marion Leclerc**, présidente de l'association fictive *La Guilde du Dé* (Lyon). Gaiane joue ce rôle pendant les échanges client, mais il reste distinct de celui de PO (voir §7) |
| Méthode | Scrum, avec un tableau Kanban pour visualiser le flux (détail dans `methode.md`) |
| Langue de travail | Français avec la cliente et dans la documentation ; **anglais** pour les commits, les issues, les PR et les rituels avec Jonas (voir §5) |

## 2. Composition (9 personnes, toutes à 100 % sauf l'alternant)

| Persona | Rôle | Profil | Lieu | Alloc. | Coût jour. fictif |
| - | - | - | - | - | - |
| **Gaiane Bielsa** (réelle) | **Product Owner et cheffe de projet** | Vision produit, backlog, relation client, pilotage (planning, budget, staffing, montée en compétences) | Lyon | 100 % | 600 € |
| **Thomas Nguyen** | Scrum Master | Facilitation des rituels, levée des obstacles, amélioration continue | Lyon | 100 % | 550 € |
| **Karim Benali** | Tech Lead / Architecte, Dev Back senior | NestJS, PostgreSQL, 10 ans d'expérience. Garant de l'architecture, *owner* des modules `identity` et `character` | Lyon | 100 % | 650 € |
| **Jonas Weber** | Dev Back confirmé | Node.js et temps réel, 5 ans d'expérience. Germanophone, anglais courant ; **lit le français (B1), ne le parle pas**. *Owner* des modules `table` et `realtime` | **Berlin (télétravail)** | 100 % | 550 € |
| **Sarah Lefèvre** | Dev Front Web (Next.js) | 5 ans d'expérience, **référente accessibilité**. Malentendante appareillée (RQTH) | Lyon | 100 % | 500 € |
| **Hugo Petit** | Dev Mobile (Expo), **alternant** | 2ᵉ année de master, bases en React, découvre React Native | Lyon | 60 % (rythme d'alternance) | 250 € |
| **Amara Diallo** | UX/UI Designer | Prototypes, design system, tests utilisateurs | Lyon | 100 % | 500 € |
| **Paul Martin** | QA et support N1 | Cahiers de recette, Playwright ; premier contact des bêta-testeurs | Lyon | 100 % | 450 € |
| **Yuki Tanaka** | DevOps / SRE | CI/CD, Docker, supervision, gestion des mises à jour | Lyon | 100 % | 600 € |

Taille conforme au Scrum Guide (10 personnes au plus). Le support suit le principe « *you build
it, you run it* » : Paul assure le N1 et les développeurs assurent le N2 par rotation
hebdomadaire (BC04.7).

## 3. Cartographie des compétences (grille de 1 à 4)

1 = notions · 2 = autonome sur des tâches simples · 3 = autonome · 4 = expert, peut former.

| Compétence | Gaiane | Karim | Jonas | Sarah | Hugo | Amara | Paul | Yuki |
| - | - | - | - | - | - | - | - | - |
| NestJS / Node.js | 3 | 4 | 3 | 2 | 1 | – | 1 | 2 |
| PostgreSQL / Prisma | 3 | 4 | 3 | 1 | 1 | – | 2 | 2 |
| Temps réel (WebSocket) | 2 | 2 | 4 | 2 | 1 | – | 1 | 1 |
| React / Next.js | 3 | 1 | 2 | 4 | 2 | 2 | 1 | – |
| React Native / Expo | 2 | – | 1 | 2 | **1** | 1 | 1 | – |
| Tests automatisés | 3 | 3 | 3 | 3 | 1 | – | 4 | 2 |
| CI/CD, Docker | 3 | 2 | 2 | 1 | 1 | – | 2 | 4 |
| Sécurité (OWASP) | 3 | 3 | 2 | 2 | 1 | – | 2 | 3 |
| Accessibilité (RGAA) | 2 | 1 | 1 | **4** | 1 | 3 | 3 | – |
| UX / prototypage | 2 | – | – | 2 | 1 | 4 | 1 | – |
| Règles JDR / DRAGONS | 4 | 1 | 1 | 1 | 3 | 2 | 1 | – |
| Français | 4 | 4 | **2 (écrit)** | 4 | 4 | 4 | 4 | 4 |
| Anglais | **1** | 3 | 4 | 2 | 3 | 3 | 2 | 3 |

**Écarts identifiés**, qui alimentent le plan de compétences (§6) :

1. Personne n'atteint le niveau 3 en React Native / Expo.
2. La connaissance du domaine du JDR est faible chez la plupart des membres.
3. Jonas ne parle pas français, alors que la cliente communique en français.
4. La PO (Gaiane) a un niveau d'anglais basique, alors que l'anglais est la langue d'échange avec Jonas.

## 4. Responsabilités (RACI simplifié)

R = réalise · A = approuve (un seul par ligne) · C = consulté · I = informé.

| Activité | Cliente | PO (Gaiane) | SM | Tech Lead | Devs | UX | QA | DevOps |
| - | - | - | - | - | - | - | - | - |
| Expression et validation du besoin | A | R | I | C | I | C | I | – |
| Priorisation du backlog | C | A/R | C | C | I | C | I | I |
| Planning, budget, reporting client | I | A/R | C | C | – | – | – | – |
| Choix d'architecture (ADR) | – | C | – | A/R | C | – | C | C |
| Prototype et maquettes | C | A | – | C | C | R | C | – |
| Développement d'une story | – | C | – | A | R | C | C | – |
| Recette d'une story | C | A | – | C | C | C | R | – |
| Mise en production | I | A | I | C | C | – | C | R |
| Traitement d'une anomalie en production | I | A | – | C | R | – | R (N1) | R |
| Animation des rituels | – | C | A/R | C | C | C | C | C |

## 5. Management et communication

### Styles managériaux par situation (modèle situationnel de Hersey et Blanchard)

En tant que cheffe de projet, Gaiane adapte son style à la maturité de chacun sur la mission
confiée :

| Persona | Situation | Style | Concrètement |
| - | - | - | - |
| Hugo (alternant) | Débute en React Native | **Directif** | Tâches découpées finement, binôme avec Sarah, points courts fréquents |
| Jonas | Compétent, mais nouveau dans l'agence, à distance et étranger au domaine du JDR | **Persuasif** | Expliquer le pourquoi des règles métier, sessions de découverte du jeu, points individuels réguliers |
| Amara, Paul | Experts, mais leur adhésion à la démarche compte | **Participatif** | Co-construction du prototype et de la stratégie de test |
| Karim, Sarah, Yuki | Experts autonomes | **Délégatif** | Ownership (architecture, accessibilité, exploitation), objectifs fixés et moyens libres |

### Contexte international (Jonas, Berlin)

| Support | Langue | Justification |
| - | - | - |
| Code (identifiants) | Anglais | Standard du métier |
| Commits, issues, PR, revues de code | **Anglais** simple, avec des modèles d'issue et de PR | Langue commune avec Jonas |
| Rituels oraux avec Jonas | Anglais | Jonas ne parle pas français |
| Commentaires de code, Swagger | Français | Jonas lit le français écrit (B1) ; cela facilite la relecture par la cliente, la PO et le jury |
| Documentation, échanges client | Français | La cliente et le jury sont francophones |

- Même fuseau horaire (CET) ; venue à Lyon une semaine par trimestre (revue, rétrospective,
  atelier d'équipe).
- Attention aux différences culturelles : communication allemande plus directe ; accord de
  fonctionnement d'équipe co-écrit au sprint 0.

### Aménagements (Sarah, RQTH, malentendante)

- Sous-titrage automatique sur toutes les visios ;
- compte rendu écrit systématique ;
- daily hybride (tour de table écrit sur le canal d'équipe, puis échange oral court) ;
- casque adapté financé dans le cadre de la RQTH.

### Alternance (Hugo)

Planning calé sur son rythme d'école ; tuteur désigné (Karim). Les missions évaluées par son école
sont intégrées au backlog.

### Outils

GitHub (issues, PR, Projects) comme source de vérité ; canal d'équipe asynchrone ; visio pour les
rituels ; comptes rendus dans `docs/agile/`.

## 6. Plan de compétences et recrutement (amorce)

| Besoin | Réponse | Échéance |
| - | - | - |
| React Native / Expo (niveau 3 requis) | **Formation** d'Hugo (parcours en ligne, binôme avec Sarah) et **recrutement** d'un·e dev mobile confirmé·e en freelance pour 2 sprints au démarrage (fiche de poste à rédiger) | Avant P2 |
| Domaine du JDR | Atelier « découverte de DRAGONS » animé par la PO : une partie d'initiation | Sprint 0 |
| Accessibilité pour tous | Atelier RGAA animé par Sarah | Sprint 1 |
| Temps réel côté front | Transfert de compétences de Jonas vers Sarah et Hugo | P2 |
| Français pour Jonas (facultatif) | Cours financés par l'agence, à son initiative | Continu |
| **Anglais pour la PO (Gaiane)** | Modèles d'issue et de PR, glossaire technique FR/EN, cours d'anglais professionnel (CPF), pratique au quotidien | Continu |

## 7. Points de vigilance sur les rôles

- **PO ≠ cliente.** La PO représente la cliente dans l'équipe, mais ne valide pas à sa place.
  Les validations (cadrage, recettes, démonstrations) sont faites par le persona commanditaire et
  tracées dans un compte rendu.
- **PO et cheffe de projet.** En Scrum pur, le PO ne manage pas l'équipe, qui s'auto-organise. Le
  référentiel (BC03.4) demande pourtant de « piloter l'équipe ». D'où la double casquette PO et
  cheffe de projet, fréquente en entreprise : pilotage du planning, du budget, du staffing et des
  compétences. Les développeurs restent maîtres de la façon de réaliser.

## 8. Lien entre l'équipe fictive et la réalisation réelle

Toute la réalisation est faite par Gaiane, à raison de quelques heures par semaine. La simulation
porte sur l'**organisation**, pas sur le volume de travail.

- **On estime en points de complexité**, une unité indépendante de qui réalise.
- **Scénario « équipe »** : la vélocité théorique de l'équipe convertit les points en jours-homme,
  puis en coûts. Elle sert au budget (BC01.9) et au planning présenté à la cliente (BC03.1).
- **Scénario « réel »** : la vélocité mesurée sert au pilotage et aux arbitrages (BC03.2, BC03.3).
- Chaque issue est attribuée au **persona porteur** (label `persona:karim`, etc.).
