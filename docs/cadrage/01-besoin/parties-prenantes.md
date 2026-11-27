# Cartographie des parties prenantes

> Phase P0, étape 1 — issue #5. Porteuse : Gaiane (PO et cheffe de projet).
> Compétence : **BC01.1**. Version 1.0 du 2026-11-26.

Une partie prenante est une personne ou une organisation qui **influence** le projet ou qui est
**touchée** par son résultat. La cartographie sert à décider avec qui communiquer, comment et à
quelle fréquence.

## 1. Liste des parties prenantes

| # | Partie prenante | Type | Rôle dans le projet | Implication attendue |
| - | - | - | - | - |
| P1 | **Commanditaire** : Marion Leclerc, présidente de *La Guilde du Dé* (association fictive) | Externe, cliente | Exprime le besoin, arbitre le périmètre, valide les livrables | Entretiens, revues de sprint, validation du cadrage (PV) |
| P2 | **Meneurs (MJ)** de l'association | Externe, utilisateurs clés | Utilisent le tableau de bord ; prescripteurs auprès des joueurs | Retours sur les maquettes, tests du parcours Meneur |
| P3 | **Joueurs** de l'association | Externe, utilisateurs finaux | Utilisent l'application mobile en partie | Tests d'utilisabilité, questionnaire de satisfaction |
| P4 | **Bêta-testeurs** (MJ et joueurs volontaires) | Externe, utilisateurs | Testent la bêta en conditions réelles (P4) | Remontée d'anomalies, satisfaction après chaque séance |
| P5 | **Équipe Forge & Pixel** (9 personas, voir [equipe.md](../../agile/equipe.md)) | Interne | Analyse, conçoit, réalise, teste et exploite | Rituels Scrum, tableau GitHub Projects |
| P6 | **Studio Agate** | Externe, ayant droit de DRAGONS | Autorise ou non l'usage des contenus du jeu | Réponse écrite à la demande d'autorisation |
| P7 | **École YNOV et jury** | Externe, certificateur | Évaluent les preuves des 34 compétences (RNCP39583) | Dossiers BC02 et BC04, oraux BC01 et BC03 (août 2028) |
| P8 | **Fournisseurs de services gratuits** (GitHub, Render, Neon, Expo, Sentry) | Externe, fournisseurs | Hébergent le code, l'API, la base, les builds et la supervision | Aucune relation directe : leurs conditions d'offre s'imposent |
| P9 | **CNIL** (cadre RGPD) | Externe, régulateur | Contrôle le respect du RGPD (données personnelles des comptes) | Aucune relation directe : conformité par conception |

**Point de vigilance** : la commanditaire (P1) et la PO sont jouées par la même personne. Les
échanges avec la cliente sont toujours tracés par un compte rendu daté, et la PO ne valide jamais à
la place de la cliente.

## 2. Matrice pouvoir / intérêt

- **Pouvoir** : capacité à influencer ou à bloquer le projet (décision, autorisation, évaluation).
- **Intérêt** : degré auquel la partie prenante est concernée par le résultat.

| | **Intérêt faible** | **Intérêt fort** |
| - | - | - |
| **Pouvoir fort** | **Satisfaire** : P6 Studio Agate, P7 École et jury, P9 CNIL | **Gérer étroitement** : P1 Commanditaire |
| **Pouvoir faible** | **Surveiller** : P8 Fournisseurs | **Tenir informé et impliquer** : P2 Meneurs, P3 Joueurs, P4 Bêta-testeurs, P5 Équipe |

Justification des placements discutables :

- **P5 Équipe** : intérêt fort, mais le pouvoir de décision sur le périmètre appartient à la
  commanditaire et à la PO.
- **P7 École et jury** : pouvoir décisif sur la certification, mais aucun intérêt pour le produit
  lui-même, seulement pour les preuves.
- **P2 Meneurs** : pouvoir faible sur les décisions, mais leur adhésion conditionne l'adoption ; à
  surveiller pour une éventuelle montée vers « gérer étroitement ».

## 3. Stratégie de communication

| Partie prenante | Objectif | Canal | Fréquence | Responsable |
| - | - | - | - | - |
| P1 Commanditaire | Valider le besoin et les décisions, garder sa confiance | Entretiens, revues de sprint, comptes rendus datés | Toutes les 2 semaines (revue) et à chaque décision | Gaiane (PO) |
| P2 Meneurs | Recueillir leurs besoins d'usage, les associer aux choix d'interface | Ateliers sur maquettes, tests du parcours Meneur | À chaque prototype | Amara (UX/UI) |
| P3 Joueurs | Vérifier l'utilisabilité sur téléphone | Tests d'utilisabilité, questionnaire | À chaque prototype, puis en bêta | Amara (UX/UI) |
| P4 Bêta-testeurs | Remonter les anomalies, mesurer la satisfaction | Formulaire « signaler un bug », questionnaire après chaque séance | Pendant toute la bêta (P4) | Paul (QA et support N1) |
| P5 Équipe | Partager l'objectif, l'avancement et les obstacles | Rituels Scrum, GitHub Projects ; résumé en anglais pour Jonas ; écrit systématique pour Sarah | Rituels du sprint | Thomas (Scrum Master) |
| P6 Studio Agate | Obtenir puis respecter l'autorisation d'usage | Courrier électronique formel, archivé dans `confidentiel/` | À la demande, puis à chaque changement d'usage des contenus | Gaiane (PO) |
| P7 École et jury | Démontrer chaque compétence par une preuve | Matrice RNCP, dossiers, oraux | À chaque jalon de certification | Gaiane (PO) |
| P8 Fournisseurs | Anticiper un changement d'offre gratuite | Veille sur les conditions et quotas | Avant chaque jalon | Yuki (DevOps) |
| P9 CNIL | Rester conforme au RGPD | Registre des traitements, minimisation des données | À chaque nouvelle donnée personnelle | Karim (Tech Lead) et Gaiane (PO) |

## 4. Suites

- Les risques liés aux parties prenantes (refus de Studio Agate, fin d'une offre gratuite,
  indisponibilité des bêta-testeurs) sont repris dans la matrice des risques (étape 2).
- La cartographie est revue à chaque fin de phase.
