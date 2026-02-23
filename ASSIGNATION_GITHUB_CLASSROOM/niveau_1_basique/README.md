# Niveau 1 : Expressions Régulières Basiques

Bienvenue au premier niveau ! Vous allez apprendre les bases des expressions régulières en Python.

---

##  Concepts Clés

-   **Caractères littéraux** : Caractères qui correspondent exactement à eux-mêmes.
-   **Classes de caractères** : `[abc]` (a, b ou c), `[0-9]` (chiffres), `\d` (chiffres), `\w` (lettres/chiffres/underscore).
-   **Quantificateurs** : `*` (0 ou plus), `+` (1 ou plus), `?` (0 ou 1), `{n}` (exactement n), `{n,m}` (entre n et m).
-   **Ancres** : `^` (début), `$` (fin), `\b` (limite de mot).
-   **Fonctions** : `re.match()` (début), `re.search()` (n'importe où), `re.findall()` (tous les matches).

---

##  Les 8 Exercices

### 1. Validation de Numéro de Téléphone (5 points)
**Objectif** : Valider un numéro de téléphone français au format `0XXXXXXXXX`.

**Indices** :
- Niveau 1 : Utilisez `^` pour le début et `$` pour la fin.
- Niveau 2 : Utilisez `\d` pour les chiffres.
- Niveau 3 : Utilisez `{n}` pour spécifier le nombre exact.

**Solution** : `^0\d{9}$`

---

### 2. Extraction de Mots se Terminant par "ing" (5 points)
**Objectif** : Extraire tous les mots qui se terminent par "ing".

**Indices** :
- Niveau 1 : Utilisez `\b` pour les limites de mots.
- Niveau 2 : Utilisez `\w+` pour les caractères de mot.
- Niveau 3 : Combinez pour `\b\w+ing\b`.

**Solution** : `\b\w+ing\b`

---

### 3. Validation d'Adresse E-mail Simple (5 points)
**Objectif** : Valider une adresse e-mail simple au format `user@domain.com`.

**Indices** :
- Niveau 1 : Utilisez `\w+` pour le nom d'utilisateur.
- Niveau 2 : Utilisez `@` comme séparateur.
- Niveau 3 : Utilisez `\.` pour le point (échappé).

**Solution** : `^\w+@\w+\.\w+$`

---

### 4. Extraction de Dates (5 points)
**Objectif** : Extraire les dates au format `JJ/MM/AAAA`.

**Indices** :
- Niveau 1 : Utilisez `\d` pour les chiffres.
- Niveau 2 : Utilisez `{2}` pour 2 chiffres.
- Niveau 3 : Combinez pour `\d{2}/\d{2}/\d{4}`.

**Solution** : `\d{2}/\d{2}/\d{4}`

---

### 5. Validation de Code Postal (5 points)
**Objectif** : Valider un code postal français (5 chiffres).

**Indices** :
- Niveau 1 : Utilisez `\d` pour les chiffres.
- Niveau 2 : Utilisez `{5}` pour exactement 5.
- Niveau 3 : Ajoutez les ancres `^` et `$`.

**Solution** : `^\d{5}$`

---

### 6. Extraction de Mots avec Voyelles Uniquement (5 points)
**Objectif** : Extraire les mots composés uniquement de voyelles.

**Indices** :
- Niveau 1 : Utilisez `[aeiou]` pour les voyelles.
- Niveau 2 : Utilisez `+` pour 1 ou plus.
- Niveau 3 : Utilisez `\b` pour les limites.

**Solution** : `\b[aeiou]+\b`

---

### 7. Extraction de Protocoles d'URL (5 points)
**Objectif** : Extraire les protocoles (http, https, ftp, etc.).

**Indices** :
- Niveau 1 : Utilisez `https?` pour http ou https.
- Niveau 2 : Utilisez `|` pour "ou".
- Niveau 3 : Combinez pour `(https?|ftp)`.

**Solution** : `(https?|ftp)`

---

### 8. Validation de Mot de Passe Simple (5 points)
**Objectif** : Valider un mot de passe d'au moins 8 caractères.

**Indices** :
- Niveau 1 : Utilisez `.` pour n'importe quel caractère.
- Niveau 2 : Utilisez `{8,}` pour 8 ou plus.
- Niveau 3 : Ajoutez les ancres `^` et `$`.

**Solution** : `^.{8,}$`

---

## 📊 Barème

-   Chaque exercice réussi = 5 points
-   Total du niveau = 40 points

---

## 🚀 Comment Commencer

1. Ouvrez `exercices.py`
2. Pour chaque exercice, remplacez `r"TODO"` par votre regex
3. Testez localement : `python exercices.py`
4. Poussez sur GitHub : `git push origin main`
5. Vérifiez votre score dans l'onglet "Actions"

---

**Bonne chance !** 🎯
