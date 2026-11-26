# 0005 — Authentification maison (module identity)

- **Statut** : Proposée (en attente de la décision de la PO)
- **Date** : 2026-11-26
- **Décideurs** : Karim (Tech Lead), Gaiane (PO)
- **Issue** : #17

## Contexte

- **Comptes** : inscription par e-mail et mot de passe, connexion, réinitialisation, suppression du
  compte (droit à l'effacement).
- **Deux clients** : l'application mobile (Expo) et le web du Meneur (Next.js).
- **Budget : 0 €** et **données personnelles minimisées** (RGPD) : moins il y a de prestataires
  qui reçoivent des données, plus la conformité est simple.
- **Certification** : la sécurité de l'authentification est une preuve attendue (BC02.5, OWASP).

## Options envisagées

| Option | Avantages | Inconvénients |
| - | - | - |
| A. Fournisseur d'identité externe (Auth0, Clerk, Supabase Auth…) | Sécurité éprouvée ; connexion sociale ; moins de code | Données des utilisateurs chez un tiers (RGPD, sous-traitant à déclarer) ; dépendance à une offre gratuite qui peut changer ; peu de preuve de compétence sur la sécurité |
| B. Serveur d'identité auto-hébergé (Keycloak) | Standard (OpenID Connect) ; complet | Un service de plus à héberger et à superviser, hors des quotas gratuits ; complexité disproportionnée |
| C. **Module `identity` maison, avec des bibliothèques éprouvées** | Données gardées chez nous ; aucune dépendance payante ; maîtrise et preuve de la sécurité | Responsabilité de la sécurité ; à tester sérieusement |

## Décision

**Option C : un module `identity` maison**, construit sur des bibliothèques reconnues plutôt que sur
du code cryptographique écrit à la main. Il suit l'**OWASP ASVS niveau 1** :

- mots de passe hachés en **Argon2id** ;
- **JWT d'accès court** et **jeton de rafraîchissement avec rotation** (SecureStore sur mobile,
  cookie httpOnly sur le web) ;
- **limitation de débit** sur la connexion ;
- **jeton de réinitialisation à usage unique** ;
- même message d'erreur que le compte existe ou non, à la connexion.

## Conséquences

- **Plus facile** : aucune donnée personnelle chez un tiers ; aucun coût ; preuve directe pour
  BC02.5.
- **Plus difficile** : l'équipe porte la responsabilité de la sécurité. Tests unitaires et
  d'intégration obligatoires sur ce module ; revue de sécurité avant la bêta.
- **Point ouvert** : à l'inscription, le message « e-mail déjà utilisé » (seq-01) révèle qu'un
  compte existe. Risque accepté pour le MVP ; correction possible plus tard avec un envoi d'e-mail
  de confirmation.
- **Réversibilité** : si le besoin évolue (connexion sociale), un fournisseur externe pourra être
  branché derrière le même port d'authentification, par une nouvelle ADR.
