# 0001 — Monolithe modulaire prêt pour les microservices

- **Statut** : Proposée (en attente de la décision de la PO)
- **Date** : 2026-11-26
- **Décideurs** : Karim (Tech Lead), Gaiane (PO)
- **Issue** : #17

## Contexte

- **Budget nul** : l'API doit tenir sur une offre d'hébergement gratuite (Render), qui limite le
  nombre de services et met en veille les services inactifs (démarrage à froid).
- **Capacité réelle** : une seule développeuse, environ 3 h par semaine, jusqu'en août 2028.
- **Domaine** : cinq contextes métier identifiés (`identity`, `character`, `table`, `compendium`,
  `realtime`), dont les frontières ne sont pas encore éprouvées par l'usage.
- **Exploitation (BC04)** : la bêta devra être supervisée, corrigée et mise à jour par la même
  personne.
- **Évolutivité** : le projet doit pouvoir passer à des microservices si la charge ou l'équipe
  l'exigent, sans tout réécrire.

## Options envisagées

| Option | Avantages | Inconvénients |
| - | - | - |
| A. Monolithe classique (découpage en couches techniques) | Le plus rapide à démarrer ; un seul déploiement | Frontières métier floues ; le code se couple vite ; passage aux microservices très coûteux |
| B. Microservices (un service par contexte) | Déploiement et montée en charge indépendants ; équipes autonomes | Messagerie, transactions distribuées, traçage, N pipelines et N déploiements ; dépasse les quotas gratuits ; coût fixe hors de portée d'une personne |
| C. **Monolithe modulaire** (un processus, des modules aux frontières strictes) | Un seul déploiement et une seule supervision ; frontières métier vérifiées en CI ; chaque module peut devenir un service plus tard | Discipline à tenir (règles d'import, un schéma par module) ; outillage de contrôle à mettre en place |

## Décision

**Option C : monolithe modulaire NestJS, découpé par contexte métier, prêt pour les
microservices.** C'est la recommandation de l'état de l'art pour une petite équipe dont le domaine
n'est pas encore stabilisé (*Monolith First*, Martin Fowler). Le projet garde ainsi la simplicité
d'un seul déploiement, tout en préparant l'extraction d'un module si elle devient utile.

Règles qui rendent le monolithe « prêt pour les microservices » :

1. Un module = un contexte métier, organisé en Clean Architecture (`domain`, `application`,
   `infrastructure`, `presentation`).
2. Un module n'importe que l'API publique (`contracts`) d'un autre module. Contrôle en CI par les
   tags Nx et dependency-cruiser.
3. Un schéma PostgreSQL par module, sans jointure entre schémas.
4. Communication entre modules par événements de domaine (bus `@nestjs/cqrs` et table *outbox*).

## Conséquences

- **Plus facile** : un seul déploiement, une seule sonde `/health`, un seul journal des versions ;
  hébergement gratuit possible.
- **Plus difficile** : les règles de frontières doivent être outillées dès le socle (P1), sinon
  elles seront contournées.
- **Critères de bascule vers un service séparé** : profil de charge différent, rythme de livraison
  différent ou équipe dédiée. `realtime` serait le premier candidat.
- **À éviter** : un découpage par entité (personnage, monstre, combat), qui produit un « monolithe
  distribué ».
- **Actions** : configurer les tags Nx et dependency-cruiser en P1 ; ADR 0003 (ORM) et C4 niveau 2
  doivent refléter ce découpage.
