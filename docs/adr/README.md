# Architecture Decision Records (ADR)

Chaque décision structurante du projet est consignée dans une ADR courte, numérotée et jamais
supprimée. Une décision remplacée passe au statut « Remplacée par NNNN ».

## Index

| N° | Titre | Statut | Date |
| - | - | - | - |
| [0001](0001-monolithe-modulaire.md) | Monolithe modulaire prêt pour les microservices | **Proposée** | 2026-11-26 |
| [0002](0002-front-expo-nextjs.md) | Front : Expo (joueurs) et Next.js (MJ) | **Proposée** | 2026-11-26 |
| [0003](0003-orm-prisma.md) | ORM : Prisma | **Proposée** | 2026-11-26 |
| [0004](0004-hebergement-gratuit.md) | Hébergement sur offres gratuites | **Proposée** | 2026-11-26 |
| [0005](0005-authentification-maison.md) | Authentification maison | **Proposée** | 2026-11-26 |
| [0006](0006-licence-du-code.md) | Licence du code | **Proposée** | 2026-11-20 |
| [0007](0007-icones-lucide.md) | Bibliothèque d'icônes : Lucide | **Acceptée** | 2026-11-27 |

## Modèle

```markdown
# NNNN — Titre

- **Statut** : Proposée | Acceptée | Remplacée par NNNN | Abandonnée
- **Date** : AAAA-MM-JJ
- **Décideurs** : personas concernés
- **Issue** : #n

## Contexte
Le problème, les contraintes, ce qui force à décider.

## Options envisagées
| Option | Avantages | Inconvénients |

## Décision
L'option retenue, en une phrase, puis la justification.

## Conséquences
Ce qui devient plus facile, plus difficile, et les actions qui en découlent.
```
