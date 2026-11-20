## User Stories — Rolliste

> **Version 0.2 (2026-11-20)** : alignée sur les diagrammes de cas d'utilisation v0.2
> ([cas-utilisation/](cas-utilisation/)). Les ajouts et modifications sont marqués 🆕 et ✏️ (voir le
> journal en bas de page).
> Prochaine étape (issue #13) : identifiants `US-xxx`, critères d'acceptation (Given / When / Then)
> et priorité MoSCoW.

Acteurs : **Visiteur** (non connecté) · **Utilisateur** (tout compte connecté) · **Joueur** et
**Meneur** (rôles portés *dans une session*) · **Administrateur**.

### Compte & accès

| En tant que | Je veux | Afin de |
| - | - | - |
| Visiteur | M'inscrire | Créer mon compte |
| Visiteur ✏️ | Me connecter | Accéder à mon compte |
| Visiteur ✏️ | Réinitialiser mon mot de passe | Récupérer l'accès à mon compte en cas d'oubli |
| Utilisateur | Me déconnecter | Sécuriser mon compte sur un appareil partagé |
| Utilisateur 🆕 | Supprimer mon compte et mes données | Exercer mon droit à l'effacement (RGPD) |
| Utilisateur 🆕 | Signaler un problème depuis l'application | Aider l'équipe à corriger les anomalies |

### Personnages joueurs (PJ)

| En tant que | Je veux | Afin de |
| - | - | - |
| Utilisateur | Créer un personnage joueur | Être prêt pour une future session ou en rejoindre une en cours |
| Utilisateur ✏️ | Consulter la fiche de mes PJ, avec les valeurs calculées automatiquement | Visualiser mes caractéristiques, mon inventaire et mes états sans faire de calculs |
| Utilisateur | Modifier la fiche de mon PJ lors d'événements précis (montée de niveau, choix à faire) | Faire évoluer mon personnage de façon encadrée |
| Utilisateur | Conserver l'expérience et l'inventaire d'un PJ entre les sessions | Rejouer un même personnage d'une aventure à l'autre |
| Utilisateur | Supprimer un de mes PJ | Nettoyer ma liste de personnages |

### Sessions de jeu

| En tant que | Je veux | Afin de |
| - | - | - |
| Utilisateur | Accéder à la liste de mes sessions de jeu | Retrouver et reprendre mes parties |
| Utilisateur ✏️ | Créer une session, et en devenir le meneur | Mener une partie en tant que MJ |
| Utilisateur | Parcourir une page recensant les sessions ouvertes | Trouver une session à rejoindre |
| Utilisateur | Rejoindre une session via un code d'invitation | Intégrer rapidement la table d'un meneur |
| Utilisateur | Envoyer une demande pour rejoindre une session listée | Demander l'accès à une partie qui m'intéresse |
| Joueur ✏️ | Choisir avec quel PJ je participe à une session | Engager le bon personnage dans l'aventure |
| Joueur ✏️ | Retirer mon PJ d'une aventure sans le supprimer | Le mettre de côté tout en gardant sa progression |
| Joueur ✏️ | Quitter une session | Me retirer d'une partie à laquelle je ne participe plus |
| Meneur | Générer un code d'invitation pour ma session | Permettre à des joueurs de me rejoindre |
| Meneur | Accepter ou refuser les demandes des joueurs | Contrôler qui rejoint ma table |

### Jeu en session (dés, verdicts, combat)

| En tant que | Je veux | Afin de |
| - | - | - |
| Joueur ✏️ | Lancer les dés depuis ma fiche | Résoudre une action de jeu |
| Joueur ✏️ | Voir les jets des autres PJ | Suivre les résolutions d'actions de la table |
| Joueur ✏️ | Être notifié quand le meneur rend un verdict ou m'applique un état | Suivre en temps réel ce qui arrive à mon personnage |
| Joueur ✏️ | Agir à mon tour pendant un combat | Participer aux affrontements |
| Meneur 🆕 | Rendre un verdict sur le jet d'un joueur (confirmer, maquiller ou modifier le résultat) | Garder la main sur la narration, quel que soit le résultat calculé |
| Meneur | Lancer des dés cachés et en modifier le résultat | Garder la main sur la dramaturgie sans révéler mes jets |
| Meneur ✏️ | Surcharger n'importe quelle valeur de la fiche d'un PJ (bonus, malus, score) | Appliquer les conséquences du jeu et improviser librement |
| Meneur 🆕 | Appliquer un état à un personnage (empoisonné, à terre…) | Traduire les effets du jeu sur la fiche |
| Meneur 🆕 | Consulter l'historique de mes actions et annuler la dernière | Corriger une erreur sans casser la partie |
| Meneur | Lancer un combat et gérer l'initiative et les tours | Démarrer et rythmer un affrontement |
| Meneur 🆕 | Ajouter un ennemi du bestiaire au combat | Préparer un affrontement rapidement |
| Meneur | Gérer des PNJ | Animer les personnages non-joueurs de l'aventure |
| Meneur | Faire monter un PJ de niveau | Offrir une progression agréable et non frustrante |
| Meneur | Lancer un événement aléatoire | Animer la partie avec de l'imprévu |

### Compendium 🆕

| En tant que | Je veux | Afin de |
| - | - | - |
| Utilisateur | Consulter le compendium (bestiaire, sorts, objets, règles) | Trouver une information de jeu sans ouvrir les livres |
| Meneur | Créer mon contenu maison (créatures, objets), visible seulement à mes tables | Adapter le jeu à mon aventure |

### Administration

| En tant que | Je veux | Afin de |
| - | - | - |
| Administrateur | Gérer les utilisateurs | Modérer les comptes de la plateforme |
| Administrateur ✏️ | Modérer les sessions et les PJ | Maintenir une plateforme saine |
| Administrateur 🆕 | Importer les données du compendium | Alimenter le référentiel de jeu sans les versionner dans le dépôt public |

---

### Journal des modifications (v0.1 → v0.2)

| Modification | Raison |
| - | - |
| « Se connecter » et « Réinitialiser mon mot de passe » portés par le **Visiteur** | On réinitialise son mot de passe justement quand on ne peut pas se connecter |
| Stories de jeu portées par **Joueur** au lieu d'Utilisateur | Le rôle de joueur n'existe qu'au sein d'une session |
| « Devenir meneur » fusionnée avec « Créer une session » | Les deux décrivaient la même action |
| « Modifier la feuille d'un PJ (bonus / malus) » devient « Surcharger une valeur » | Alignement avec le principe « calcul automatique, surcharge libre » |
| Notification reformulée | Préciser ce qui déclenche une notification (verdict, état) |
| Ajouts : verdict, état, historique et annulation, ennemi du bestiaire, compendium, contenu maison, suppression de compte, signalement, import | Principes métier (§4 du cahier des charges), RGPD, besoins de maintenance (BC04) |
| « Gérer les sessions » et « Gérer les PJ » (administration) fusionnées en « Modérer » | Même finalité |
