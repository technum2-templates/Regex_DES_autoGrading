# Guide de l'Étudiant : Apprendre les Expressions Régulières

---

## 1. Bienvenue dans le Monde des Regex !

Ce projet va vous apprendre à maîtriser les **expressions régulières (Regex)**, un outil incroyablement puissant pour manipuler du texte. Au début, cela peut sembler un peu magique ou compliqué, mais ne vous inquiétez pas : nous allons y aller pas à pas.

Ce guide est votre "mode d'emploi" pour aborder les exercices et tirer le meilleur parti de ce cours.

## 2. Votre Mission

Votre objectif est de compléter les exercices fournis dans le fichier `EXERCICES_REGEX.md`. Chaque exercice vous demandera d'écrire une ou plusieurs expressions régulières pour résoudre un problème concret.

Le projet est divisé en deux niveaux :

-   **Niveau 1 : Les Fondamentaux** (Exercices 1 à 8)
    *   Ici, vous apprendrez les briques de base des regex.
-   **Niveau 2 : Concepts Avancés** (Exercices 9 à 16)
    *   Ici, vous aborderez des techniques plus complexes pour résoudre des problèmes plus difficiles.

## 3. Comment Aborder les Exercices : Votre Workflow

Voici la méthode que nous vous recommandons de suivre pour chaque exercice :

### Étape 1 : Lire et Comprendre l'Énoncé

Lisez attentivement l'énoncé de l'exercice. Assurez-vous de bien comprendre ce que vous devez **trouver**, **valider** ou **extraire**.

Regardez les exemples de chaînes qui doivent "matcher" (correspondre) et celles qui ne doivent pas.

### Étape 2 : Utiliser un Outil en Ligne (Votre Laboratoire)

L'outil le plus important pour apprendre les regex est un testeur en ligne. Nous vous recommandons **[Regex101](https://regex101.com/)**.

**Comment l'utiliser :**

1.  **Sélectionnez la saveur (Flavor)** : Dans le menu de gauche, choisissez **Python**.
2.  **Copiez-collez les exemples** : Prenez les chaînes de test de l'énoncé et mettez-les dans la zone "Test String".
3.  **Écrivez votre regex** : Commencez à taper votre expression régulière dans la zone "Regular Expression".

L'avantage de Regex101 est qu'il vous montre **en temps réel** ce que votre regex est en train de faire, et il vous donne des **explications détaillées** sur chaque partie de votre pattern dans le panneau "Explanation" à droite.

![Image de l'interface de Regex101](https://i.imgur.com/V2y3zCg.png) *(Exemple d'interface de Regex101)*

### Étape 3 : Construire votre Regex Pas à Pas

Ne tentez pas d'écrire la regex parfaite du premier coup. Construisez-la brique par brique.

**Exemple : Valider un numéro de téléphone `0X XX XX XX XX`**

1.  **Commencez simple** : `0` - Ça matche le début.
2.  **Ajoutez un chiffre** : `0\d` - Ça matche `06`.
3.  **Ajoutez les espaces et les paires de chiffres** : `0\d \d{2}` - Ça matche `06 12`.
4.  **Répétez le motif** : `0\d( \d{2}){4}` - Ça y est ! Le groupe `( \d{2})` est répété 4 fois.
5.  **Ancrez votre regex** : `^0\d( \d{2}){4}$` - Le `^` et le `$` s'assurent que la chaîne entière correspond au pattern, et pas seulement une partie.

### Étape 4 : Tester avec le Code Python

Une fois que votre regex fonctionne dans Regex101, il est temps de la tester en Python.

Le fichier `EXERCICES_REGEX.md` vous fournit un petit script de test pour chaque exercice. Copiez-collez ce code dans un fichier Python (par exemple, `test.py`) et exécutez-le.

```python
import re

# --- Exercice 1 : Numéro de téléphone ---
pattern = r"^0\d( \d{2}){4}$"  # Mettez votre pattern ici

# ... (le reste du script de test)
```

Modifiez la variable `pattern` avec votre solution et lancez le script. Il vous dira si vous avez réussi ou non.

### Étape 5 : Consulter la Solution (Seulement si vous êtes bloqué !)

Essayez vraiment de résoudre l'exercice par vous-même. C'est en cherchant (et en faisant des erreurs) que l'on apprend le mieux.

Si vous êtes vraiment bloqué depuis plus de 15-20 minutes, alors jetez un œil à la solution. Mais ne vous contentez pas de la copier-coller ! Essayez de **comprendre pourquoi** elle fonctionne. Lisez les explications détaillées.

## 4. Quelques Conseils pour Réussir

-   **La patience est la clé** : Personne n'écrit des regex parfaites du premier coup.
-   **Décomposez le problème** : Quelle est la plus petite partie que je peux matcher ?
-   **Pensez aux cas limites** : Qu'est-ce qui pourrait casser ma regex ? (Une chaîne vide ? Des majuscules ? Des caractères spéciaux ?)
-   **Utilisez les ressources** : Gardez le `COURS_REGEX.md` (en particulier l'antisèche) ouvert à côté de vous.

---

Bon courage, et amusez-vous bien à devenir un maître des expressions régulières ! 🕵️‍♂️
