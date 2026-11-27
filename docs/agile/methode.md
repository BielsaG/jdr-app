# Méthode de travail — Rolliste

> **Statut : v1 validée par la PO le 26/11/2026.** Susceptible d'évoluer après les cours de gestion
> de projet. Livrable de l'étape 0 du cadrage (issue #2).
> Compétences visées : BC03.1 (cadre méthodologique), BC03.2 (outils de suivi et indicateurs).

## 1. Choix de la méthode

| Critère | Cycle en V | Kanban seul | Scrum seul | **Scrum + tableau Kanban (retenu)** |
| - | - | - | - | - |
| Besoin qui évolue (retours des bêta-testeurs, réponse de Studio Agate) | Mal adapté | Adapté | Adapté | **Adapté** |
| Rythme et jalons pour piloter et rendre compte au client | Fort, mais rigide | Faible (flux continu) | Fort (sprints) | **Fort** |
| Visualisation du flux et des goulots | Faible | Fort | Moyen | **Fort** |
| Traitement des anomalies en production (non planifiables) | Faible | **Fort** | Moyen | Fort, en passant en Kanban pur |
| Rôles et rituels attendus en BC03 | Partiel | Partiel | Complet | **Complet** |

**Décision.** Le **cadre Scrum** (rôles, sprints, rituels) donne le rythme et les points de
validation avec la cliente. Le **tableau Kanban** (colonnes, limites de travail en cours) rend le
flux visible. La méthode évolue avec les phases :

| Phases | Mode | Pourquoi |
| - | - | - |
| P0 à P3 (cadrage, socle, MVP, recette) | **Scrum**, sprints de 2 semaines | Travail planifiable, besoin de jalons et de démonstrations |
| P4 (exploitation de la bêta) | **Kanban pur** | Les anomalies et les retours arrivent en continu ; on priorise au fil de l'eau |

## 2. Rôles

Voir [equipe.md](equipe.md). En résumé :

- **Product Owner** : Gaiane, qui est aussi cheffe de projet ;
- **Scrum Master** : Thomas ;
- **Developers** : Karim (Tech Lead), Jonas, Sarah, Hugo, Amara, Paul et Yuki.

La **cliente** (Marion Leclerc) ne fait pas partie de l'équipe Scrum. Elle participe aux revues de
sprint et valide les jalons.

## 3. Sprint

- **Durée** : 2 semaines, du lundi au vendredi de la semaine suivante. Itérations dans le champ « Sprint »
  de GitHub Projects.
- **Nommage** : `SP-00.<n>` pour les sprints de la conception (SP-00.1 : du 23/11/2026 au
  04/12/2026), puis `SP-01`, `SP-02`… pour le développement. SP-01 commence par la mise en place
  du cadre de travail (monorepo, outillage).
- **Objectif de sprint** : une phrase, fixée en planification (ex. « La cliente a exprimé son
  besoin et l'existant est analysé »).

### Rituels

La première colonne de durée correspond au Scrum Guide, pour l'équipe fictive. La deuxième indique
comment Gaiane le pratique réellement, seule, avec environ 8 h par sprint.

| Rituel | Équipe fictive | Pratique réelle | Trace |
| - | - | - | - |
| Planification de sprint | 4 h max | 20 min : objectif, choix des issues selon la capacité réelle, champ « Sprint » renseigné | `sprints/sprint-XX.md` § Planification |
| Daily | 15 min par jour (hybride écrit et oral, voir les aménagements) | Journal de bord : 3 lignes à chaque session de travail (fait, à faire, blocages) | `sprints/sprint-XX.md` § Journal |
| Affinage du backlog | ≤ 10 % du sprint | 15 min : préparer les issues du sprint suivant jusqu'à la Definition of Ready | Issues mises à jour |
| Revue de sprint | 2 h max, avec la cliente | 20 min : démonstration ou présentation des livrables à la cliente, avec ses retours | `sprints/sprint-XX.md` § Revue |
| Rétrospective | 1 h 30 max | 15 min : « Continuer / Arrêter / Commencer » et une action d'amélioration | `sprints/sprint-XX.md` § Rétrospective |

Les rituels avec Jonas se tiennent en anglais. Les comptes rendus sont en français, avec un résumé
en anglais.

## 4. Tableau Kanban et flux

Tableau : [GitHub Projects « Rolliste »](https://github.com/users/BielsaG/projects/3).

| Colonne | Signification | Limite (WIP) |
| - | - | - |
| Backlog | Identifié, pas encore prêt | — |
| Ready | Respecte la Definition of Ready | — |
| In progress | En cours de réalisation | **2** |
| In review | En relecture (PR) ou en attente de validation par la cliente | **3** |
| Done | Respecte la Definition of Done | — |

Règle : on **termine avant de commencer**. Si une colonne atteint sa limite, on aide à débloquer ce
qui est en relecture plutôt que d'ouvrir une nouvelle tâche.

### Definition of Ready (une issue peut entrer dans un sprint)

- [ ] Titre clair, en anglais
- [ ] Livrable attendu identifié (fichier ou fonctionnalité)
- [ ] Critères d'acceptation rédigés
- [ ] Estimation renseignée (Points et Estimate (h))
- [ ] Persona porteur et bloc RNCP renseignés (labels)
- [ ] Aucune dépendance bloquante

### Definition of Done

**Pour un livrable de documentation :**

- [ ] Tous les critères d'acceptation sont cochés
- [ ] Le livrable est relu (checklist de revue) et, si nécessaire, validé par la cliente (compte
  rendu)
- [ ] La matrice RNCP est mise à jour
- [ ] Le livrable est fusionné dans `main` via une PR qui ferme l'issue
- [ ] Le champ « Actual (h) » est renseigné

**Pour une fonctionnalité** (s'ajoute à la liste ci-dessus, à partir de P1) :

- [ ] Tests unitaires écrits et au vert ; couverture ≥ 80 % sur `domain/` et `application/`
- [ ] CI au vert (lint, typecheck, tests, frontières de modules, scans de sécurité)
- [ ] Critères d'accessibilité vérifiés (RGAA)
- [ ] Swagger à jour si l'API change
- [ ] Recette par la QA, validée par la PO

## 5. Estimation

- **Points de complexité**, en suite de Fibonacci : 1, 2, 3, 5, 8, 13. Au-delà de 13, on découpe
  l'issue.
- **Story de référence** : #5 « Map the project stakeholders » = **2 points**. Toute estimation se
  fait par comparaison avec elle.
- **Planning poker** fictif : on note la proposition de chaque persona concerné et l'écart discuté
  quand il est significatif. C'est une preuve d'animation d'équipe.
- Chaque issue a aussi une **estimation en heures** (Estimate (h)) et des **heures réelles**
  (Actual (h)), pour calibrer la conversion entre points et heures.

## 6. Flux Git (branche d'issue → branche de sprint → `main`)

| Branche | Rôle | Fusionnée dans |
| - | - | - |
| `main` | Version validée | — |
| `feat/SP-<nn>` | Branche de sprint. `feat/SP-00` : conception, c'est-à-dire tout ce qui précède le cadre de travail (cadrage complet, wireframes et maquettes). `feat/SP-01` : premier sprint, qui génère le cadre de travail ; créée une fois la conception validée | `main`, après validation |
| `type/rl-<n°>-description` | Branche d'issue | Branche de sprint en cours |

1. **Une branche par issue** : `type/rl-<n°>-description-courte`, où `rl` est le préfixe du
   projet Rolliste (ex. `docs/rl-4-client-request`, `feat/rl-42-invite-code`). La branche est
   créée **depuis l'issue** pour être reliée au ticket : bouton « Create a branch » (encart
   « Development ») ou `gh issue develop <n°> --name type/rl-<n°>-description --checkout`.
   Le numéro dans le nom ne suffit pas à créer le lien.
2. **Commits** en Conventional Commits, en anglais : `type(scope): message`.
3. **Pull request** vers la **branche de sprint en cours** (jamais directement vers `main`), avec
   `Closes #<n°>` dans la description pour relier la PR à l'issue. Relecture avec la checklist.
   GitHub ne ferme automatiquement l'issue que lors d'une fusion dans `main` : après la fusion dans
   la branche de sprint, fermer l'issue à la main (la carte passe alors en Done).
4. **Fusion en squash**, pour garder un historique lisible (un commit par livrable). La branche est
   supprimée après fusion.

Quand le dépôt sera public : protection de `main` (PR obligatoire, CI au vert). Les règles de
protection ne sont pas disponibles sur un dépôt privé avec l'offre gratuite.

## 7. Indicateurs de pilotage (BC03.2)

| Indicateur | Calcul | Source | Usage |
| - | - | - | - |
| Vélocité réelle | Points terminés par sprint | GitHub Projects (Insights, somme des Points par Sprint) | Prévision et recalage du planning |
| Burn-up | Points terminés cumulés, comparés au périmètre | GitHub Projects (Insights) | Suivi de l'avancement de la phase |
| Fiabilité des estimations | Actual (h) / Estimate (h) | Champs du tableau | Calibrage des estimations |
| Temps de cycle | Durée entre « In progress » et « Done » | Historique des issues | Détection des goulots |
| Couverture RNCP | Compétences avec une preuve ✅ / 34 | [Matrice RNCP](../rncp/matrice-RNCP39583.md) | Priorisation par rapport à l'objectif de certification |

Ces indicateurs sont relevés à chaque revue de sprint. Un écart significatif (par exemple, une
vélocité inférieure de plus de 30 % à la prévision pendant 2 sprints) déclenche un **arbitrage**
documenté (BC03.3).

## 8. Organisation des fichiers

```
docs/agile/
  equipe.md          # composition, compétences, RACI, management
  methode.md         # ce document
  sprints/
    sprint-00-1.md   # planification, journal, revue, rétrospective
  arbitrages/        # cas d'arbitrage documentés (BC03.3)
```
