# SWOT, impact environnemental et dépendances

> Phase P0, étape 2 — issue #8. Porteuse : Gaiane (PO), avec Karim (Tech Lead) pour les dépendances.
> Compétence : **BC01.3**. Version 1.0 du 2026-11-26.

## 1. Matrice SWOT

| | **Positif** | **Négatif** |
| - | - | - |
| **Interne** | **Forces**<br>• Positionnement sans équivalent : accompagner une table physique en laissant le dernier mot au Meneur ([comparatif](../01-besoin/existant.md))<br>• Accès direct au besoin : la cliente est une Meneuse expérimentée<br>• Coût nul : outils et hébergement gratuits ([ADR 0004](../../adr/0004-hebergement-gratuit.md))<br>• Architecture modulaire et logique partagée entre mobile et web ([ADR 0001](../../adr/0001-monolithe-modulaire.md), [ADR 0002](../../adr/0002-front-expo-nextjs.md)) | **Faiblesses**<br>• Une seule développeuse, environ 3 h par semaine<br>• Compétences à acquérir (React Native et Expo, temps réel)<br>• La même personne joue la PO et la cliente : risque de biais<br>• Démarrage à froid de l'API sur l'offre gratuite (~1 min après 15 min d'inactivité) |
| **Externe** | **Opportunités**<br>• Une association de joueurs disponible comme terrain de bêta-test<br>• Les règles de base 5e sont publiées sous licence libre (SRD 5.1, Creative Commons CC-BY-4.0, version française disponible) : les mécaniques peuvent être codées sans attendre Studio Agate<br>• Aucun outil identifié dédié à DRAGONS lors du comparatif | **Menaces**<br>• Refus ou absence de réponse de Studio Agate sur l'usage des contenus de DRAGONS<br>• Modification ou fin d'une offre gratuite (Render, Neon, Expo)<br>• Concurrents puissants et connus (D&D Beyond, Roll20, Foundry VTT)<br>• Adoption compromise si l'application ralentit le jeu au lieu de l'accélérer<br>• Obligations RGPD sur les comptes utilisateurs |

### Lecture croisée (stratégies)

| Croisement | Stratégie retenue |
| - | - |
| Forces × Opportunités | S'appuyer sur l'association pour valider tôt le positionnement « table physique » par des tests réels |
| Forces × Menaces | Mesurer le temps d'un tour de combat avec et sans l'application : c'est la preuve que Rolliste accélère le jeu |
| Faiblesses × Opportunités | Coder les mécaniques à partir du SRD 5.1 libre, sans dépendre de l'autorisation de Studio Agate ; garder un périmètre MVP réduit (tranche verticale) |
| Faiblesses × Menaces | Image Docker portable et configuration 12-factor pour changer d'hébergeur vite ; contenus de DRAGONS dans un fichier de données non versionné tant que l'autorisation n'est pas écrite |

## 2. Impact environnemental

Référentiel : **RGESN** (référentiel général d'écoconception de services numériques). Les mesures
détaillées sont l'objet de l'issue #22 ; cette section identifie les impacts.

| Poste | Impact | Niveau | Piste |
| - | - | - | - |
| **Terminaux** (fabrication) | Le premier impact du numérique. Rolliste utilise des appareils déjà présents à la table (smartphones, portable du Meneur) | Fort si l'application pousse à renouveler un appareil | Rester compatible avec des versions anciennes d'Android ; application légère |
| **Réseau** | Échanges en temps réel pendant toute la séance | Faible | Messages WebSocket courts, sans images ; pas de rafraîchissement inutile |
| **Serveurs** | Une API et une base mutualisées chez des hébergeurs gratuits | Faible | Monolithe unique (ADR 0001) ; la mise en veille réduit la consommation hors séance |
| **Données** | Fiches, jets et comptes : volumétrie faible | Faible | Minimisation des données (RGPD) ; pas de stockage d'images en V1 |
| **Usage** | Un écran de plus à la table, pendant plusieurs heures | Moyen | Mode sombre, peu d'animations ; l'application sert ponctuellement, pas en continu |

**Effet positif attendu** : moins de papier (fiches réimprimées, brouillons de calcul), mais l'effet
reste marginal comparé à la fabrication des terminaux.

## 3. Dépendances

| Dépendance | Usage | Criticité | Plan B |
| - | - | - | - |
| **Studio Agate** (ayant droit de DRAGONS) | Autorisation d'utiliser les contenus du jeu | Forte pour les contenus, nulle pour les mécaniques | Mécaniques issues du SRD 5.1 libre ; données inventées compatibles 5e |
| **Render** | Hébergement de l'API | Forte | Image Docker portable vers un autre hébergeur |
| **Neon** | Base PostgreSQL | Forte | PostgreSQL standard : migration par sauvegarde et restauration |
| **Expo et EAS** | Build de l'APK, tests avec Expo Go | Moyenne | Build local illimité |
| **Expo Push Service** (via Firebase Cloud Messaging) | Notifications push | Faible (extension hors MVP) | Notifications dans l'application seulement |
| **GitHub** (dépôt, Actions, Projects) | Code, intégration continue, suivi | Forte | Dépôt Git exportable ; CI à reproduire ailleurs |
| **Sentry** | Supervision des erreurs | Faible | Journaux de l'hébergeur |
| **Écosystème npm** (NestJS, Prisma, Next.js…) | Bibliothèques | Moyenne | Renovate pour suivre les mises à jour et les failles |

Les dépendances fortes sont reprises dans la matrice des risques (#10).

## Sources

- SRD 5.1 en français sous licence Creative Commons : [document officiel (PDF)](https://media.wizards.com/2023/downloads/dnd/SRD_CC_v5.1_FR.pdf)
- Limites des offres gratuites : cahier des charges §8 (vérifiées en novembre 2026)
