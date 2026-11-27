# État de l'existant et comparatif des outils

> Phase P0, étape 1 — issue #7. Porteuse : Amara (UX/UI Designer).
> Compétence : **BC01.2**. Version 1.0 du 2026-11-26.

## 1. Déroulement d'une partie aujourd'hui

Une partie se joue en présentiel, autour d'une table : chaque joueur a sa **fiche papier**, ses
**dés**, et le Meneur dispose de son **écran**, de ses notes et des livres de règles (dont
l'encyclopédie et le bestiaire).

| Moment | Ce qui se passe | Qui calcule |
| - | - | - |
| Action d'un joueur | Le joueur annonce son action, lance les dés, ajoute ses modificateurs lus sur sa fiche | Le joueur |
| Résolution | Le Meneur compare le total à une difficulté ou à la défense d'un ennemi, puis annonce le résultat | Le Meneur |
| Combat | Le Meneur gère l'ordre d'initiative, les points de vie des ennemis, et joue le tour de chaque ennemi | Le Meneur |
| Recherche d'une règle ou d'un ennemi | Le Meneur consulte l'encyclopédie ou le bestiaire | Le Meneur |
| Suites de l'action | Chacun met à jour sa fiche : PV, états, inventaire, expérience | Joueurs et Meneur |

### Irritants relevés auprès de la cliente

Recueillis auprès de la cliente le 26/11/2026, puis reformulés :

1. **Des temps morts à chaque calcul du Meneur.** Quand le Meneur fait les calculs pour le groupe,
   le jeu s'arrête : les joueurs attendent.
2. **Le tour des ennemis est le moment le plus lent.** Le Meneur doit jouer chaque ennemi, suivre
   ses valeurs, et souvent **vérifier une information dans l'encyclopédie** ou le bestiaire.
3. **L'ampleur des « blancs » dépend de l'expérience du Meneur.** Un Meneur débutant subit plus
   ces interruptions, alors qu'il a déjà le plus de choses à gérer.

S'y ajoutent les tâches fastidieuses identifiées dans le cahier des charges (§1) : tenir les fiches
à jour (PV, états, inventaire, expérience), suivre l'initiative et les PV des ennemis, et conserver
ses personnages d'une campagne à l'autre.

**Conséquence pour le produit** : la valeur de Rolliste se mesure à la **réduction des temps
morts**. L'application doit calculer à la place du Meneur, et lui apporter l'information au bon
moment, sans retirer son pouvoir de décision (principe n°1 : le MJ a le dernier mot).

## 2. Comparatif des outils existants

> Informations vérifiées sur les sites officiels le 2026-11-26 (sources en fin de document). Les
> tarifs et les fonctionnalités évoluent : à revérifier avant chaque présentation.

| Outil | Type | Ce qu'il fait | Ce qui manque pour une table en présentiel |
| - | - | - | - |
| **D&D Beyond** | Fiches et contenus en ligne (web, mobile) | Fiches avec calcul automatique ; *Game Log* : jets partagés avec la campagne, jets secrets du Meneur ; règles et bestiaire officiels de D&D | Contenus D&D uniquement (pas DRAGONS) ; livres payants et abonnement (formules Hero et Master) ; le Meneur voit les jets mais ne rend pas de verdict |
| **Roll20** | Table virtuelle (navigateur) | Cartes, jetons, fiches de plus de 1 200 systèmes, jets de dés, initiative ; offre gratuite (avec publicité), Plus à 5,99 $/mois, Pro à 10,99 $/mois | Conçu pour le jeu à distance ; interface lourde sur smartphone ; remplace la table au lieu de l'accompagner |
| **Foundry VTT** | Table virtuelle auto-hébergée | Très complet grâce aux modules : fiches, combat, automatisations ; modules pour modifier les jets en secret, ou pour saisir des dés physiques à table (*Onsite Play*) | Licence unique à 50 $ ; installation et hébergement à la charge du Meneur ; pensé pour l'ordinateur ; aucun module trouvé pour valider un jet avant de le révéler |
| **Owlbear Rodeo** | Table virtuelle légère (navigateur) | Cartes et dés partagés, simple ; offre gratuite limitée (nombre de salles et stockage), formules payantes ; fiches et combat via des extensions | Pas de fiches calculées en natif ; dépend d'extensions tierces ; pas de lien avec les règles |
| **Fight Club 5e** | Application mobile de fiches 5e (iOS, Android) | Fiche de personnage sur téléphone, export PDF ; gratuite avec publicité et un seul personnage, version Premium payante (2,99 $ sur iOS) | Chaque joueur est isolé : aucun lien en temps réel avec le Meneur ; l'outil du Meneur est une application séparée |
| **AideDD** | Site de référence en français | Règles, sorts, créatures et objets magiques de D&D 5 en français, en grande partie gratuits ; créateur de personnage en ligne | Simple consultation : aucun lien avec la partie, les fiches ou les jets ; contenus D&D, pas DRAGONS |

### Synthèse

| Besoin de la table en présentiel | D&D Beyond | Roll20 | Foundry VTT | Owlbear Rodeo | Fight Club 5e | AideDD | **Rolliste** |
| - | - | - | - | - | - | - | - |
| Fiche calculée automatiquement | ✅ | ✅ | ✅ | Partiel (extensions) | ✅ | Partiel (créateur) | ✅ |
| Jets du joueur visibles chez le Meneur en temps réel | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ✅ |
| Verdict du Meneur (valider, maquiller, modifier) | ❌ | ❌ | Partiel (modifier en secret, sans validation) | ❌ | ❌ | ❌ | ✅ |
| Joueur sur smartphone, Meneur sur grand écran | Partiel | ❌ | ❌ | Partiel | Partiel | — | ✅ |
| Pensé pour accompagner une table physique | Partiel | ❌ | Partiel (module *Onsite Play*) | ❌ | Partiel | Partiel | ✅ |
| Compatible avec les règles de DRAGONS | ❌ | ❌ | ❌ | — | ❌ | ❌ | ✅ |
| Gratuit | Partiel | Partiel | ❌ | Partiel | Partiel | ✅ | ✅ |

## 3. Positionnement

Aucun outil étudié ne réunit les trois points qui comptent pour la cliente :

1. **accompagner une table physique**, sans la remplacer par une table virtuelle ;
2. **réduire les temps morts du Meneur** en calculant à sa place, tout en lui laissant le dernier
   mot sur chaque jet ;
3. **respecter les règles de DRAGONS**, en français.

C'est l'espace que Rolliste occupe. Les tables virtuelles restent des références utiles pour
l'ergonomie du suivi de combat (initiative, PV des ennemis) ; les applications de fiches, pour la
présentation d'une fiche sur téléphone.

## Sources (consultées le 2026-11-26)

- D&D Beyond : [abonnements](https://www.dndbeyond.com/subscribe), [annonce du Game Log](https://www.dndbeyond.com/posts/939-share-your-dice-results-with-the-brand-new-game)
- Roll20 : [abonnements (centre d'aide)](https://help.roll20.net/hc/en-us/articles/28498571071255-Roll20-Subscriptions)
- Foundry VTT : [FAQ et licence](https://foundryvtt.com/article/faq/), [module Onsite Play](https://foundryvtt.com/packages/onsite-play), [module Fumble Switch](https://foundryvtt.com/packages/fumble-switch)
- Owlbear Rodeo : [abonnements](https://blog.owlbear.rodeo/state-of-the-rodeo-lets-talk-about-subscriptions), [extensions](https://extensions.owlbear.rodeo)
- Fight Club 5e : [App Store](https://apps.apple.com/us/app/-/id901057473)
- AideDD : [site](https://www.aidedd.org/)
