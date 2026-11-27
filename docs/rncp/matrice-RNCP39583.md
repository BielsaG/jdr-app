# Matrice compétences ↔ preuves — RNCP39583 Expert en développement logiciel

Source : [fiche France compétences RNCP39583](https://www.francecompetences.fr/recherche/rncp/39583/)
(certificateur YNOV, niveau 7). Les intitulés ci-dessous sont **reformulés** : se référer au
référentiel officiel pour le libellé exact dans les dossiers.

Statuts : ⬜ à faire · 🟨 en cours · ✅ preuve disponible.

## BC01 — Cadrer un projet de développement d'applications logicielles (oral, devant un client)

| Code | Compétence (reformulée) | Preuve prévue | Phase | Statut |
| - | - | - | - | - |
| BC01.1 | Cartographier les acteurs et parties prenantes | [Cartographie des parties prenantes](../cadrage/01-besoin/parties-prenantes.md) (matrice pouvoir/intérêt, stratégie de communication) | P0 | ✅ |
| BC01.2 | Analyser la demande via un entretien d'explicitation et un état des lieux de l'existant | Compte rendu d'entretien (confidentiel), [guides d'entretien](../cadrage/01-besoin/README.md), [état de l'existant et comparatif](../cadrage/01-besoin/existant.md) | P0 | ✅ |
| BC01.3 | Cartographier opportunités et menaces, dont l'impact environnemental et les dépendances | [SWOT, impact environnemental et dépendances](../cadrage/02-analyse/swot.md) | P0 | ✅ |
| BC01.4 | Évaluer la faisabilité technique (environnement, contraintes, budget) | [Étude de faisabilité](../cadrage/02-analyse/faisabilite.md) (technique, humaine, financière, juridique ; go sous conditions) | P0 | ✅ |
| BC01.5 | Cartographier les risques techniques et fonctionnels avec indicateurs de contrôle | Matrice des risques (criticité), référentiel, indicateurs | P0 | ⬜ |
| BC01.6 | Réaliser une veille technique, technologique et réglementaire, dont l'écoconception | Processus et sources de veille, fiches de veille | P0 → continu | ⬜ |
| BC01.7 | Sélectionner l'architecture par étude comparative, sécurité incluse | Étude monolithe / microservices, ORM, GraphQL, front, hébergeurs ; [ADR 0001 à 0005](../adr/README.md) (proposées, à valider) | P0 | 🟨 |
| BC01.8 | Évaluer la charge de travail | Backlog estimé (points et heures), méthode d'estimation | P0 | ⬜ |
| BC01.9 | Estimer le coût et un budget prévisionnel | Budget à partir des TJM fictifs de l'équipe et des coûts d'infrastructure | P0 | ⬜ |
| BC01.10 | Modéliser l'architecture logicielle (spécifications, sécurité, écoconception) | Diagrammes C4, UML (cas d'utilisation ✅, séquences du MVP ✅, classes), modèle de données (porté par le diagramme de classes) | P0 | 🟨 |
| BC01.11 | Proposer les décisions au client et obtenir sa validation | Support de présentation du cadrage, PV de validation | Fin P0 | ⬜ |

## BC02 — Concevoir et développer des applications logicielles (dossier et code)

| Code | Compétence (reformulée) | Preuve prévue | Phase | Statut |
| - | - | - | - | - |
| BC02.1 | Mettre en œuvre les environnements de déploiement et de test, avec suivi de la qualité et de la performance | docker-compose, environnement de test, Sentry, rapports de qualité | P1 | ⬜ |
| BC02.2 | Configurer l'intégration continue | Workflows GitHub Actions (lint, typecheck, tests, frontières, scans) | P1 | ⬜ |
| BC02.3 | Concevoir un prototype selon l'ergonomie et les supports ciblés, sécurité incluse | Maquettes mobile (joueur) et web (MJ) | P1 | ⬜ |
| BC02.4 | Développer un harnais de tests unitaires | Tests de `domain/`, `application/`, `dice-engine`, `rules-dragons` et rapport de couverture | P2 | ⬜ |
| BC02.5 | Développer le logiciel (évolutivité, sécurité, accessibilité, spécifications) | Code des modules, mesures OWASP, audit RGAA | P2 | ⬜ |
| BC02.6 | Déployer en continu et progressivement, en vérifiant auprès des utilisateurs | Pipeline de déploiement continu, déploiement progressif (bêta-testeurs), retours | P2–P3 | ⬜ |
| BC02.7 | Élaborer le cahier de recettes | Cahier de recettes (scénarios, résultats attendus et obtenus) | P3 | ⬜ |
| BC02.8 | Élaborer un plan de correction des bogues | Plan de correction priorisé | P3 | ⬜ |
| BC02.9 | Rédiger la documentation technique d'exploitation | Manuels de déploiement, d'utilisation et de mise à jour | P3 | ⬜ |

## BC03 — Coordonner et piloter un projet de développement (oral et démonstration)

| Code | Compétence (reformulée) | Preuve prévue | Phase | Statut |
| - | - | - | - | - |
| BC03.1 | Planifier l'exécution (méthode, ordonnancement, ressources) | Choix de méthode : [méthode v1](../agile/methode.md), Scrum + Kanban, validée par la PO le 26/11/2026 ; planning, roadmap, affectation | P0 | 🟨 |
| BC03.2 | Piloter l'avancement avec des indicateurs | [GitHub Projects « Rolliste »](https://github.com/users/BielsaG/projects/3) (vue Board validée le 26/11/2026), burndown, vélocité, tableau de bord | Continu | 🟨 |
| BC03.3 | Arbitrer à partir de l'analyse des écarts | Cas d'arbitrage documenté avec logigramme ; [arbitrage n°1](../agile/sprints/sprint-01.md) (écart de périmètre, sprint 1) | Continu | 🟨 |
| BC03.4 | Piloter l'équipe (handicap, multiculturel, management, communication) | Matrice d'affectation, styles managériaux, plan de communication | Continu | 🟨 |
| BC03.5 | Évaluer les besoins en compétences (recrutement, formation) | Grille de compétences, plan de développement, fiche de poste | P0 → continu | 🟨 |
| BC03.6 | Rendre compte au client | Comptes rendus, points de validation, indicateurs de satisfaction | Continu | ⬜ |
| BC03.7 | Faire la démonstration de la dernière version | Scénario de démonstration et démonstration en direct | P6 | ⬜ |

## BC04 — Maintenir l'application en condition opérationnelle (dossier)

| Code | Compétence (reformulée) | Preuve prévue | Phase | Statut |
| - | - | - | - | - |
| BC04.1 | Gérer les mises à jour des dépendances | Renovate, politique de mise à jour, évaluation des impacts | P1 → P4 | ⬜ |
| BC04.2 | Concevoir un système de supervision et d'alerte | Sentry, endpoint `/health`, sonde externe, alertes, indicateurs | P1 → P4 | ⬜ |
| BC04.3 | Consigner les anomalies | Processus de collecte, modèle de fiche d'anomalie (GitHub Issues) | P3 → P4 | ⬜ |
| BC04.4 | Créer et déployer un correctif via la CI/CD | Exemple de correctif de bout en bout (issue → PR → release) | P4 | ⬜ |
| BC04.5 | Proposer des axes d'amélioration (indicateurs et retours) | Rapport d'amélioration argumenté | P4 | ⬜ |
| BC04.6 | Tenir un journal des versions | CHANGELOG (release-please, SemVer) | P2 → P4 | ⬜ |
| BC04.7 | Collaborer avec le support | Exemple de problème résolu avec le support (réel ou fictif) | P4 | ⬜ |
