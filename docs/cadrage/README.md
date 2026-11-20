# Phase P0 — Cadrage

> **Objectif** : produire toutes les preuves du **bloc BC01** (oral devant le client), poser les bases
> de **BC03** (équipe, méthode, planning) et aboutir à un **cahier des charges v1.0 validé par le
> client**.
> **Cahier des charges** : [cahier-des-charges.md](cahier-des-charges.md). **Budget** : 35 h. **Sortie** : réunion de validation avec la cliente (PV signé).

## Principes

1. **On suit l'ordre d'un vrai projet** : comprendre → analyser → spécifier → concevoir → chiffrer →
   faire valider. Chaque étape s'appuie sur la précédente.
2. **Deux casquettes, toujours séparées.**
   - La **cliente** (Gaiane en tant que MJ commanditaire) exprime le besoin, arbitre et valide.
     Elle parle « usage », jamais « technique ».
   - L'**équipe** (personas fictifs) analyse, propose et chiffre.
   - Chaque échange entre les deux donne lieu à un **compte rendu daté**.
3. **Un livrable = un fichier = au moins une compétence.** Mettre à jour
   [la matrice RNCP](../rncp/matrice-RNCP39583.md) à chaque livrable terminé.
4. **Le cahier des charges est vivant** : chaque étape l'enrichit. Il passe en v1.0 à l'étape 6.
5. **Diagrammes en PlantUML** (déjà utilisé pour les cas d'utilisation), versionnés à côté de leur
   rendu PNG.

## Déroulé

| # | Étape | Livrables | Compétences | Rôle porteur | Charge |
| - | - | - | - | - | - |
| 0 | **Préparer** | Équipe fictive (personas, compétences, capacité, TJM), méthode et rituels, tableau GitHub Projects | BC03.1, BC03.4, BC03.5 | Scrum Master, Tech Lead | 4 h |
| 1 | **Comprendre le besoin** | Demande initiale de la cliente, cartographie des parties prenantes, guide puis compte rendu d'entretien, état des lieux de l'existant (papier et concurrents) | BC01.1, BC01.2 | PO | 6 h |
| 2 | **Analyser le contexte** | SWOT avec impact environnemental et dépendances, étude de faisabilité, matrice des risques, processus de veille | BC01.3 à BC01.6 | PO, Architecte | 6 h |
| 3 | **Spécifier** | User stories avec critères d'acceptation et MoSCoW, diagramme de cas d'utilisation, diagramme de fonctionnalités, modèle du domaine | BC01.2, BC01.10 | PO | 5 h |
| 4 | **Concevoir** | Étude comparative consolidée, ADR, diagrammes C4 (niveaux 1 et 2, niveau 3 pour `table`), séquence « jet → verdict », modèle de données, analyse de sécurité (STRIDE simplifié), mesures d'écoconception | BC01.7, BC01.10 | Architecte | 7 h |
| 5 | **Chiffrer et planifier** | Estimation du backlog, budget prévisionnel, roadmap et jalons | BC01.8, BC01.9, BC03.1 | Tech Lead, PO | 4 h |
| 6 | **Restituer et faire valider** | Cahier des charges v1.0, note de préconisations, support de présentation pour la cliente, PV de validation | BC01.11, BC03.6 | PO, Tech Lead | 3 h |
| | | | | **Total** | **35 h** |

## Détail des étapes

### Étape 0 — Préparer (avant tout, car l'équipe sert à chiffrer)

- [x] `docs/agile/equipe.md` : 8 à 10 personas, chacun avec son rôle, ses compétences (grille de 1 à
  4), sa capacité (h/sprint) et un TJM fictif. Prévoir un membre en télétravail à l'international et
  un membre en situation de handicap avec aménagement (BC03.4).
- [x] `docs/agile/methode.md` : pourquoi Scrum (comparé à Kanban et au cycle en V), durée des
  sprints, rituels, Definition of Ready et Definition of Done.
- [x] Tableau GitHub Projects « Rolliste » (https://github.com/users/BielsaG/projects/3) : une issue par livrable de cadrage (#1 à #28).

### Étape 1 — Comprendre le besoin

- [ ] `01-besoin/demande-client.md` : la demande telle que la cliente l'exprime, en une page et en
  langage d'usage. Elle est rédigée **avant** l'entretien, sous la casquette cliente.
- [ ] `01-besoin/parties-prenantes.md` : liste, rôles, matrice pouvoir/intérêt, stratégie de
  communication par acteur. Acteurs : cliente, joueurs, MJ, bêta-testeurs, Studio Agate, équipe,
  école et jury.
- [ ] `01-besoin/entretien-guide.md` puis `01-besoin/entretien-cr-AAAA-MM-JJ.md` : questions
  ouvertes de l'équipe, puis réponses de la cliente, besoins reformulés et points à arbitrer.
- [ ] `01-besoin/existant.md` : déroulement d'une partie aujourd'hui (irritants des fiches papier) et
  benchmark de 4 à 6 outils (applis de fiches, tables virtuelles, lanceurs de dés), avec un tableau
  « ce qu'ils font / ce qui manque pour une table en présentiel ».

### Étape 2 — Analyser le contexte

- [ ] `02-analyse/swot.md` : forces, faiblesses, opportunités, menaces, **impact environnemental**
  (RGESN) et **dépendances** (hébergeurs gratuits, Expo, Studio Agate).
- [ ] `02-analyse/faisabilite.md` : faisabilité technique, humaine (capacité réelle), financière
  (0 €) et juridique (droits). Conclusion : go, no go, ou go sous conditions.
- [ ] `02-analyse/risques.md` : matrice probabilité × impact, avec pour chaque risque un indicateur de
  contrôle, un seuil d'alerte et une parade. Exemples : refus de Studio Agate, fin d'une offre
  gratuite, dérive de charge, bêta-testeurs indisponibles.
- [ ] `02-analyse/veille.md` : méthode (sources, outils, fréquence, format des fiches) et premières
  fiches de veille (technique, réglementaire RGPD et RGAA, écoconception).

### Étape 3 — Spécifier

- [ ] Reprendre les user stories existantes ([03-specifications/userStories.md](03-specifications/userStories.md)) : critères d'acceptation (Given/When/Then), MoSCoW et
  numérotation `US-xxx`.
- [ ] Mettre à jour le diagramme de cas d'utilisation (le fichier `.plantUml` est vide pour l'instant).
- [ ] Diagramme de fonctionnalités (arborescence des fonctionnalités par module).
- [ ] Modèle du domaine : diagramme de classes conceptuel par contexte, aligné sur le glossaire.

### Étape 4 — Concevoir

- [ ] `docs/adr/0001-monolithe-modulaire.md`, `0002-front-expo-nextjs.md`, `0003-orm-prisma.md`,
  `0004-hebergement-gratuit.md`, `0005-authentification-maison.md`.
- [ ] `docs/architecture/` : C4 contexte et conteneurs, composants du module `table`, séquence
  « jet → verdict », modèle de données par schéma.
- [ ] `docs/architecture/securite.md` : menaces (STRIDE simplifié) et mesures OWASP correspondantes.
- [ ] `docs/architecture/ecoconception.md` : mesures retenues (référentiel RGESN).

### Étape 5 — Chiffrer et planifier

- [ ] `05-chiffrage/estimation.md` : méthode (points de complexité calibrés sur une story de
  référence, conversion en heures) et backlog estimé.
- [ ] `05-chiffrage/budget.md` : charge × TJM des personas, infrastructure (0 € puis jour de la
  soutenance), outillage, et marge de risque. Présenter aussi un scénario « production réelle »
  (AWS) pour comparaison.
- [ ] `05-chiffrage/roadmap.md` : phases P1 à P6, jalons et plan de livraison.

### Étape 6 — Restituer et faire valider

- [ ] `06-validation/preconisations.md` : décisions recommandées, argumentées « bénéfice client »
  (BC01.11).
- [ ] Support de présentation (10 à 15 diapositives), vocabulaire client. Il sert de **répétition de
  l'oral BC01**.
- [ ] `06-validation/pv-validation-AAAA-MM-JJ.md` : décisions validées, réserves et prochaines
  étapes.
- [ ] Cahier des charges passé en **v1.0**.

## Critère de fin de phase

- Chaque compétence **BC01.1 à BC01.11** a au moins une preuve ✅ dans la matrice.
- Le PV de validation est signé par la cliente.
- Le backlog de P1 et P2 est estimé et priorisé.
