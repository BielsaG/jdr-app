# Sprint SP-00.1 — du 23/11/2026 au 04/12/2026

> Phase P0 (cadrage), étapes 0 et 1. Méthode : [methode.md](../methode.md).
> Tableau : [GitHub Projects « Rolliste »](https://github.com/users/BielsaG/projects/3), filtre
> `sprint:"SP-00.1"`.

## Avant le sprint (préparation, 20/11/2026)

Travail réalisé avant le démarrage du premier sprint, hors vélocité :

- #1 Équipe fictive : terminée et validée.
- #14 Diagrammes de cas d'utilisation v0.2 : en relecture par la PO.
- Cahier des charges v0.6, plan de cadrage, matrice RNCP, logo (première ébauche).

## Planification (20/11/2026)

**Participants** : Gaiane (PO), Thomas (Scrum Master), Amara, Karim. Jonas était excusé ; un résumé
en anglais lui est transmis.

**Objectif de sprint** : *la cliente a exprimé son besoin, et l'existant est analysé.*

**Capacité** :

| Scénario | Capacité | Base |
| - | - | - |
| Réel | ~8 h | 4 h par semaine sur 2 semaines |
| Équipe fictive | Non contraignante pour ce sprint | Livrables de cadrage, portés surtout par la PO |

**Périmètre retenu** :

| Issue | Livrable | Persona | Points | Estimate (h) |
| - | - | - | - | - |
| #2 | Méthode de travail (relecture et validation) | Thomas | 2 | 1,5 |
| #3 | Tableau GitHub Projects (vue Board, limites WIP) | Thomas | 1 | 0,5 |
| #4 | Demande initiale de la cliente | Gaiane, dans le rôle de Marion | 2 | 1 |
| #5 | Cartographie des parties prenantes | Gaiane | 2 | 1,5 |
| #6 | Guide d'entretien et compte rendu | Gaiane | 3 | 2 |
| #7 | État de l'existant et benchmark | Amara | 3 | 1,5 |
| | **Total** | | **13** | **8** |

**Ordre de réalisation** : #4 → #6 (l'entretien s'appuie sur la demande) → #5 → #7. #2 et #3 sont
traités au fil de l'eau.

**Risques identifiés** : la cliente et la PO sont jouées par la même personne. Parade : rédiger #4
avant de préparer l'entretien, sans relire la documentation de l'équipe.

## Journal

> Trois lignes par séance de travail : fait / à faire / blocages.

| Date | Fait | À faire | Blocages |
| - | - | - | - |
| 26/11/2026 | **6 à 8 h, hors périmètre du sprint** : cas d'utilisation v0.3 (#14), 10 séquences du MVP (#19, #32), diagramme de classes (#16), MCD remis en place et complété (#20) | Revenir aux issues du sprint (#5, #7) | Écart de périmètre : voir l'arbitrage ci-dessous |
| 26/11/2026 | #5 cartographie des parties prenantes et #7 état de l'existant (comparatif vérifié sur les sites officiels) : **objectif du sprint atteint** | Objectif atteint avant la fin du sprint : #8 (SWOT, étape 2) est tiré du backlog avec l'accord de la PO, dans l'ordre du cadrage | — |
| 26/11/2026 | La PO valide la méthode v1 (#2) : Scrum + tableau Kanban, sprints de 2 semaines, rituels, convention de branche `type/rl-<n°>-description`. Vue Board validée (#3) | Fermer #2 par PR ; revoir la méthode après les cours de gestion de projet | — |
| 27/11/2026 | Décision de la PO : branche de sprint `feat/SP-00` (conception) entre les branches d'issue et `main` ; sprints de la conception renommés `SP-00.<n>` ; la mise en place du cadre de travail passe au SP-01 | Renommer l'itération sur le board | — |
| 27/11/2026 | Affinage du backlog : 29 issues ouvertes ramenées à 10 (voir l'arbitrage n°2) | Fermer les issues fusionnées ou abandonnées | — |

### Arbitrage n°1 — Travail de conception réalisé hors du périmètre du sprint (26/11/2026)

> Preuve BC03.3. Décideurs : Gaiane (PO), Thomas (Scrum Master) ; avis de Karim (Tech Lead).

| Élément | Contenu |
| - | - |
| **Constat** | L'objectif du sprint porte sur le **besoin** (#2 à #7). Le 26/11, la séance a été consacrée à la **conception** (étapes 3 et 4 du cadrage), prévue plus tard. |
| **Cause** | Les diagrammes de cas d'utilisation en relecture (#14) ont fait apparaître des incohérences ; leur correction a entraîné les séquences, puis le modèle de données. |
| **Impact** | 6 à 8 h passées hors périmètre, soit l'équivalent de presque toute la capacité du sprint (~8 h). Risque de ne pas finir #5 et #7 avant le 04/12. En contrepartie, la modélisation UML (BC01.10) est presque terminée. |
| **Options** | A. Garder les livrables de conception, les rattacher au sprint et reporter #7 au sprint 2.<br>B. Garder les livrables, les compter hors vélocité (comme la préparation du 20/11) et maintenir le périmètre.<br>C. Mettre la conception en pause et revenir strictement au périmètre. |
| **Décision** | **Option B** (décision de la PO le 26/11/2026) : le travail fait n'est pas perdu, et l'objectif du sprint reste lisible. |
| **Action** | Rappel en planification du sprint 2 : vérifier que les issues entrant dans le sprint respectent l'ordre du cadrage, ou justifier l'écart. |

### Arbitrage n°2 — Simplification du backlog de cadrage (27/11/2026)

> Preuve BC03.3. Décideurs : Gaiane (PO), Thomas (Scrum Master).

| Élément | Contenu |
| - | - |
| **Constat** | 29 issues ouvertes pour le cadrage, découpées plus finement que nécessaire. Plusieurs outils (diagrammes d'activité, d'états, de paquetages, de fonctionnalités) ne sont pas exigés par le référentiel. |
| **Analyse** | La fiche RNCP39583 évalue 11 compétences au bloc BC01 sans imposer d'outil (ni SWOT, ni UML, ni C4). Elle accepte un « diagramme de fonctionnalités **ou** cahier des charges ». |
| **Options** | A. Garder les 29 issues.<br>B. Une issue par compétence ou par livrable, et abandonner les outils facultatifs. |
| **Décision** | **Option B** (décision de la PO le 27/11/2026) : 10 issues ouvertes. Fusions : #12 → #10 ; #14, #29 → #13 ; #18, #19, #20, #32, #33 → #16 ; #35 → #17 ; #22 → #21 ; #24, #25 → #23 ; #27, #28 → #26. Abandon : #15, #30, #31, #34. Déjà faites : #5, #7, #8, #9. |
| **Action** | Fermer les issues fusionnées (« merged into #X ») sans les supprimer, pour garder la trace. |

## Revue (04/12/2026)

> Démonstration des livrables à la cliente, retours et décisions.

- Livrables présentés :
- Retours de la cliente :
- Objectif de sprint atteint : oui / non

**Indicateurs** :

| Indicateur | Valeur |
| - | - |
| Points terminés / engagés | / 13 |
| Heures réelles / estimées | / 8 h |
| Compétences RNCP passées à ✅ | |

## Rétrospective (04/12/2026)

| Continuer | Arrêter | Commencer |
| - | - | - |
| | | |

**Action d'amélioration retenue pour le sprint 2** :

---

*Summary for Jonas (EN): Sprint SP-00.1 goal is "the client has expressed her need and the existing
situation is analysed". Scope: #2, #3, #4, #5, #6, #7 (13 points, about 8 hours).*
