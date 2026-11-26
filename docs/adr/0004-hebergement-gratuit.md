# 0004 — Hébergement sur offres gratuites

- **Statut** : Proposée (en attente de la décision de la PO)
- **Date** : 2026-11-26
- **Décideurs** : Yuki (DevOps), Karim (Tech Lead), Gaiane (PO)
- **Issue** : #17

## Contexte

- **Budget : 0 €** pendant toute la bêta. Seul le jour de la soutenance peut justifier une petite
  dépense.
- **Besoins** : une API NestJS avec **WebSocket** (temps réel), une base **PostgreSQL**, une
  interface web (Next.js) et un APK.
- **Exploitation (BC04)** : déploiement continu depuis GitHub, supervision, sonde `/health`.
- **Portabilité** : pouvoir changer d'hébergeur sans réécrire l'application (configuration
  12-factor, image Docker).

## Options envisagées

| Option | Avantages | Inconvénients |
| - | - | - |
| A. **Render (API) + Neon (PostgreSQL) + hébergement web gratuit** | 0 € ; déploiement depuis GitHub ; image Docker et WebSocket acceptés ; Neon sans expiration | Mise en veille de l'API après 15 min d'inactivité (~1 min de redémarrage) ; quotas Neon (1 Go, 100 CU-heures par mois) |
| B. AWS (offre gratuite) | Écosystème complet ; compétence recherchée | Offre gratuite limitée dans le temps ou en crédits ; risque de facturation en cas d'erreur de configuration ; configuration lourde pour une personne |
| C. Serveur privé virtuel (VPS) | Pas de mise en veille ; contrôle total | Payant (quelques € par mois) ; système, sécurité et sauvegardes à la charge de l'équipe |
| D. Auto-hébergement local | Gratuit | Pas de disponibilité garantie ; exposition d'un réseau personnel ; inadapté à une bêta |

## Décision

**Option A : Render pour l'API, Neon pour PostgreSQL, et un hébergement statique gratuit pour le
web du Meneur** (Render static, Vercel Hobby ou Netlify, choix final en P1). Le jour de la
soutenance, l'API passe temporairement sur une instance Render payante pour éviter la mise en veille.

Les limites des offres gratuites ont été vérifiées en novembre 2026 et seront revérifiées avant
chaque jalon.

## Conséquences

- **Plus facile** : coût nul, déploiement continu simple, aucune administration système.
- **Plus difficile** : le premier appel après une période d'inactivité est lent (démarrage à froid),
  ce qui pèse sur l'exigence « jet visible chez le MJ en moins de 500 ms » ; elle s'entend donc
  **hors démarrage à froid**.
- **Risque** : modification ou fin d'une offre gratuite. Parade : image Docker standard et
  configuration par variables d'environnement, pour migrer rapidement (à suivre dans la matrice des
  risques).
- **Actions** : Dockerfile et variables d'environnement documentées en P1 ; sonde `/health`
  surveillée par un service externe gratuit.
