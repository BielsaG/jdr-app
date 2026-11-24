# Modèle conceptuel de données (MCD)

> **Outil** : [Mocodo](https://www.mocodo.net/) (notation Merise, entité + association verbale)
> **Issue** : #20 · **Compétence** : BC01.10 · **Version courante** : [v0.2](v0.2/)

## Organisation

Un dossier par version, qui contient l'export Mocodo complet :

| Fichier | Rôle |
| - | - |
| `MCD.mcd` | Source du modèle (texte Mocodo) |
| `MCD.svg` | Rendu du schéma |
| `MCD_geo.json` | Disposition des boîtes (générée par Mocodo) |
| `MCD_url.url` | Lien vers le modèle sur Mocodo en ligne |

## Règle de versionnement

1. Une version figée **ne se modifie plus**.
2. Pour faire évoluer le modèle : copier le dossier de la dernière version sous un nouveau numéro,
   modifier son `MCD.mcd` sur Mocodo, remplacer l'export, puis ajouter une ligne à l'historique.
3. **Numérotation** :
   - mineure (v0.2 → v0.3) pour un ajout ou une correction ;
   - majeure (v0.x → v1.0) quand le MCD est validé avec le cahier des charges v1.0.

Git garde aussi le détail de chaque modification ; les dossiers de version servent à **montrer
l'évolution du modèle** (dossier et oral BC01).

## Historique

| Version | Date | Changements | Origine |
| - | - | - | - |
| [v0.1](v0.1/) | 2026-11-24 | Construction par briques : compte, PJ et fiche, compendium minimal (peuple, classe, objet), partie et séance, participation, code d'invitation, jet et verdict, surcharge et journal d'actions | Cahier des charges, user stories, entretien n°1 |
| [v0.2](v0.2/) | 2026-11-24 | Suppression du journal d'actions (pas d'annulation en V1). Le code d'invitation devient un attribut de la séance. Pas de demande d'adhésion ni de partie référencée. Maîtrise sans niveau (pas d'expertise). Ajout de l'éveil (PJ) et de la magie par pacte (classe) | Entretien n°2 (24/11) |
