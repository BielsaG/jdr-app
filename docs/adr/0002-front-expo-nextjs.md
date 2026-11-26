# 0002 — Front : Expo pour les joueurs, Next.js pour le Meneur

- **Statut** : Proposée (en attente de la décision de la PO)
- **Date** : 2026-11-26
- **Décideurs** : Karim (Tech Lead), Sarah (Dev Front Web), Hugo (Dev Mobile), Gaiane (PO)
- **Issue** : #17

## Contexte

- **Deux usages très différents** : le joueur utilise un **smartphone** (fiche, dés, notifications)
  ; le Meneur utilise un **ordinateur portable ou une tablette** (tableau de bord dense, ≥ 1024 px).
- **Livraison mobile** : un **APK Android** installable, et des tests rapides avec Expo Go.
- **Fonctions natives** côté joueur : notifications push, vibration, secousse pour lancer les dés.
- **Accessibilité** visée : RGAA / WCAG 2.1 AA, surtout sur l'interface web du Meneur.
- **Capacité** : une seule développeuse ; la logique doit être partagée pour ne pas être écrite deux
  fois.

## Options envisagées

| Option | Avantages | Inconvénients |
| - | - | - |
| A. Expo seul (APK et web via react-native-web) | Une seule base de code ; coût en temps le plus faible ; APK natif | Interface Meneur dense peu adaptée (peu de composants desktop) ; accessibilité web moyenne (pas de HTML sémantique natif) |
| B. **Expo (joueur) + Next.js (Meneur)** | Chaque support a l'outil le plus adapté ; natif côté joueur ; web accessible et dense côté Meneur ; logique partagée via `libs/` | Deux applications à maintenir |
| C. Next.js seul, empaqueté en APK (PWA + Capacitor) | Stack maîtrisée ; bonne accessibilité web | L'APK n'est qu'une WebView ; pas d'Expo Go ; push et capteurs via plugins, plus de configuration |

## Décision

**Option B : Expo pour l'application joueur, Next.js pour l'interface Meneur.** Les deux interfaces
n'ont presque aucun écran en commun : deux applications ne doublent donc pas le travail. Ce qui est
commun est partagé dans `libs/` : `contracts` (DTO), `dice-engine`, `rules-dragons` et un client
d'API typé.

**Repli** si le temps manque : option A, décidée par une nouvelle ADR qui remplacera celle-ci.

## Conséquences

- **Plus facile** : expérience native côté joueur (push via Expo Push Service, vibration, capteurs)
  ; interface Meneur accessible et adaptée au grand écran ; preuve directe d'un prototype
  multi-supports (BC02.3).
- **Plus difficile** : deux chaînes de build (EAS ou build local pour l'APK, hébergement web pour
  Next.js) ; deux jeux de tests E2E.
- **Actions** : créer `apps/mobile` et `apps/web` dans le monorepo Nx dès le socle (P1) ; aucune
  logique métier dans les apps, tout ce qui se partage va dans `libs/`.
