# Guide d'entretien n°2 — Règles de gestion du modèle de données

> **Compétences** : BC01.2 (analyse de la demande), BC01.10 (modélisation), BC03.6 (points de
> validation avec la cliente)
> **Interviewée** : Marion Leclerc, présidente de *La Guilde du Dé*
> **Équipe** : Gaiane (PO, animation), Karim (Tech Lead, modèle de données), Hugo (connaissance des
> règles de DRAGONS, prise de notes)
> **Durée prévue** : 45 min · **Base** : compte rendu de l'entretien n°1 et MCD en cours (brique 1 à 5)

## Objectif

Pendant la modélisation des données, l'équipe a dû faire des **hypothèses** sur des règles de jeu et
d'usage. Cet entretien les fait **confirmer ou corriger par la cliente** avant de figer le MCD. Chaque
réponse devient une **règle de gestion** (RG) du modèle.

Les questions sont posées dans le vocabulaire de la cliente (partie, séance, fiche, MJ), jamais en
termes techniques.

## Déroulé

| Temps | Séquence |
| - | - |
| 5 min | Rappel : ce qui a été validé au premier entretien, et pourquoi ces nouvelles questions |
| 35 min | Questions par thème (ci-dessous) |
| 5 min | Reformulation des règles retenues, puis prochaines étapes |

## Questions

> ★ = prioritaire si le temps manque. **H** = hypothèse actuelle de l'équipe, à annoncer seulement
> après la réponse spontanée de la cliente, pour ne pas l'influencer.

### A. Les personnages

1. ★ Un même personnage peut-il jouer dans **deux parties en même temps** ?
   *H : non, un personnage n'est engagé que dans une partie active à la fois.*
2. Les **points de vie temporaires** sont-ils utilisés à vos tables ? Sont-ils indispensables dès la
   première version ?
   *H : oui, on les garde (un seul champ sur la fiche).*
3. Le **multiclassage** est-il fréquent chez vos joueurs ? Peut-il attendre une version suivante ?
   *H : il attend une version suivante.*
4. Dans DRAGONS, existe-t-il une **double maîtrise** d'une compétence (expertise) ?
5. Pour la magie, le classement « classe sans magie / magie partielle / magie complète »
   suffit-il, ou existe-t-il d'autres cas (magie apportée par le peuple, par un don) ?
6. ★ Le **grimoire** était jugé important au premier entretien. Peut-il arriver juste après la
   première version, ou faut-il le prévoir dès le départ ?
   *H : il arrive après la première version (liste des sorts à préparer, écrans dédiés).*
7. Pour un joueur **sans téléphone** dont le MJ gère le personnage : qui crée la fiche ? Si ce joueur
   s'équipe plus tard, doit-il pouvoir **récupérer** son personnage sur son propre compte ?

### B. Les jets et les verdicts

8. ★ Quand le MJ valide les jets, le joueur doit-il **voir le résultat de ses dés avant le verdict** ?
   *H : non. Il voit « en attente du MJ », puis seulement le résultat annoncé. Sinon, un résultat
   arrangé par le MJ se remarquerait.*
9. Quand une partie est réglée sur « le résultat des dés fait foi », le MJ peut-il quand même
   **corriger un jet après coup** ?
10. Le MJ peut-il **revenir sur un verdict** déjà annoncé à la table ?
11. Les **jets cachés** concernent-ils seulement les jets du MJ, ou le MJ peut-il aussi demander à un
    joueur un jet dont le résultat ne sera visible que par lui (exemple : perception en secret) ?

### C. Les modifications faites par le MJ

12. ★ Si un MJ donne un bonus ou un malus à un personnage (une malédiction, par exemple), ce
    changement doit-il **suivre le personnage dans une autre partie**, avec un autre MJ ?
    *H : non, la modification ne vaut que dans la partie où elle a été faite.*
13. Jusqu'où le MJ doit-il pouvoir **annuler** : seulement sa dernière action, toute la séance en
    cours, ou aussi des séances précédentes ?
14. ★ Les **états** (empoisonné, à terre…) sont-ils indispensables dès la première version, même si
    le suivi de combat arrivait plus tard ?

### D. Les parties et les séances

15. Le **code d'invitation** est-il valable pour toute la partie, ou faut-il un nouveau code à chaque
    séance ? Combien de temps doit-il rester valable ?
16. Une **liste des parties ouvertes**, visible par tous les membres, vous serait-elle utile, ou le
    code d'invitation suffit-il ?
17. Un joueur peut-il **rejoindre une partie en cours**, entre deux séances ?

## Après l'entretien

- Consigner les réponses dans les notes d'entretien, puis rédiger le compte rendu (documents
  confidentiels, même modèle que l'entretien n°1). Les faire valider par la cliente sous 48 h.
- Reporter chaque réponse dans le **tableau des règles de gestion** du MCD. Corriger les
  cardinalités concernées (questions 1, 7 et 12 notamment).
- Mettre à jour les user stories et le glossaire si une réponse change le vocabulaire.
- Mettre à jour la matrice RNCP (BC01.2, BC01.10).
