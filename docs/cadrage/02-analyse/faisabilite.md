# Étude de faisabilité

> Phase P0, étape 2 — issue #9. Porteur : Karim (Tech Lead), décision : Gaiane (PO).
> Compétence : **BC01.4**. Version 1.0 du 2026-11-26.

Cette étude vérifie que le projet peut être mené **avec les moyens réels** : une développeuse,
quelques heures par semaine, un budget nul, et une soutenance en août 2028.

## 1. Faisabilité technique

| Exigence | Solution retenue | Verdict |
| - | - | - |
| Application joueur sur Android, testable vite | Expo : APK et Expo Go ([ADR 0002](../../adr/0002-front-expo-nextjs.md)) | ✅ Technologie éprouvée |
| Interface Meneur dense et accessible | Next.js ([ADR 0002](../../adr/0002-front-expo-nextjs.md)) | ✅ Stack déjà maîtrisée |
| Temps réel : jet visible chez le Meneur en moins de 500 ms | WebSocket (Socket.IO), accepté par l'offre gratuite de Render | ⚠️ Atteignable **hors démarrage à froid** (~1 min après 15 min d'inactivité) |
| Calcul automatique de la fiche | Bibliothèque pure `rules-dragons`, testée unitairement | ✅ Logique isolée et testable |
| Évolutivité vers des microservices | Monolithe modulaire ([ADR 0001](../../adr/0001-monolithe-modulaire.md)) | ✅ Sans surcoût au démarrage |
| Sécurité de l'authentification | Module maison selon l'OWASP ASVS niveau 1 ([ADR 0005](../../adr/0005-authentification-maison.md)) | ⚠️ Faisable, mais demande des tests sérieux |

**Conclusion technique** : faisable. Aucune technologie n'est expérimentale. Le seul point dur est
le démarrage à froid, contourné le jour de la soutenance par une instance payante temporaire.

## 2. Faisabilité humaine

| Élément | Constat |
| - | - |
| Charge du socle certifiant | ≈ 287 h, marge de 15 % comprise (cahier des charges §12) |
| Capacité nécessaire | ≈ 3,3 h par semaine sur ≈ 88 semaines (décembre 2026 → août 2028) |
| Capacité réelle prévue | ~4 h par semaine (base de planification du sprint SP-00.1) |
| Compétences maîtrisées | TypeScript, Next.js, développement web |
| Compétences à acquérir | React Native et Expo, temps réel (Socket.IO), sécurité de l'authentification |
| Point d'attention | La séance du 26/11 a consommé 6 à 8 h hors périmètre : la capacité réelle varie fortement d'une semaine à l'autre |

**Conclusion humaine** : faisable, avec une **marge faible** (~0,7 h par semaine). Elle impose un
MVP réduit à une tranche verticale, les extensions (P7) restant optionnelles, et un suivi de la
vélocité à chaque sprint pour recaler le planning tôt.

## 3. Faisabilité financière (budget : 0 €)

| Poste | Solution | Coût |
| - | - | - |
| Hébergement API et base | Render et Neon, offres gratuites ([ADR 0004](../../adr/0004-hebergement-gratuit.md)) | 0 € |
| Interface web du Meneur | Hébergement statique gratuit | 0 € |
| Application Android | APK distribué directement aux bêta-testeurs, sans Google Play | 0 € |
| Build de l'APK | EAS (~30 builds par mois) ou build local illimité | 0 € |
| Intégration continue, suivi | GitHub (dépôt public, Actions, Projects) | 0 € |
| Supervision | Sentry, sonde de disponibilité externe (offres gratuites) | 0 € |
| Jour de la soutenance | Instance Render payante, quelques jours seulement | Quelques € |
| Exclu | Publication sur Google Play ou l'App Store (frais de compte développeur) | — |

**Conclusion financière** : faisable à 0 € pendant toute la bêta. La seule dépense prévue est
ponctuelle et volontaire (jour de la soutenance).

## 4. Faisabilité juridique

| Sujet | Situation | Verdict |
| - | - | - |
| Contenus de DRAGONS (textes, bestiaire, encyclopédie) | Demande d'autorisation à Studio Agate rédigée le 20/11, **à envoyer** | ⚠️ Bloquant pour les contenus seulement |
| Mécaniques de jeu (formules, règles de calcul) | Règles de base 5e publiées sous licence libre (SRD 5.1, Creative Commons CC-BY-4.0, version française) | ✅ Codables sans autorisation, avec la mention de crédit exigée par la licence |
| Données de démonstration | Données inventées compatibles 5e, écrites à la main (cahier des charges §9.1) | ✅ |
| Nom et marque | « Rolliste » : nom propre, éloigné de « Donjons & Dragons » (marque de Wizards of the Coast) | ✅ |
| Données personnelles (RGPD) | E-mail et pseudo seulement ; droit à l'effacement ; hébergement en Union européenne | ✅ Faisable par conception |
| Licence du code | En cours de décision ([ADR 0006](../../adr/0006-licence-du-code.md)) | ⚠️ À trancher avant la publication du dépôt |

**Conclusion juridique** : faisable. L'absence d'autorisation de Studio Agate ne bloque pas le
projet : elle limite seulement les **contenus** affichés, et le comportement de repli est déjà prévu
(cahier des charges §9).

## 5. Conclusion

### ✅ GO sous conditions

| # | Condition | Responsable | Échéance |
| - | - | - | - |
| C1 | Envoyer la demande d'autorisation à Studio Agate et suivre la réponse (#12) | Gaiane (PO) | Avant la fin de P0 |
| C2 | Limiter le MVP à la tranche verticale ; les extensions (P7) ne démarrent que si la marge le permet | Gaiane (PO) | Toute la durée du projet |
| C3 | Relever la vélocité à chaque revue de sprint ; recaler le planning si l'écart dépasse 30 % sur 2 sprints | Thomas (Scrum Master) | Chaque sprint |
| C4 | Revérifier les limites des offres gratuites avant chaque jalon | Yuki (DevOps) | Chaque jalon |
| C5 | Prévoir du temps de formation sur Expo et le temps réel avant P2 | Karim (Tech Lead) | Fin de P1 |
| C6 | Choisir la licence du code avant de rendre le dépôt public (ADR 0006) | Gaiane (PO) | Avant la publication |

Les risques associés à ces conditions sont suivis dans la matrice des risques (#10).

## Sources

- Charge et planning : [cahier des charges §12](../cahier-des-charges.md)
- Hébergement et limites des offres gratuites : [cahier des charges §8](../cahier-des-charges.md)
- Propriété intellectuelle : [cahier des charges §9](../cahier-des-charges.md)
- SRD 5.1 en français sous licence Creative Commons : [document officiel (PDF)](https://media.wizards.com/2023/downloads/dnd/SRD_CC_v5.1_FR.pdf)
