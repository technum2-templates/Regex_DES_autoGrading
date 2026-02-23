# Niveau 2 : Expressions Régulières Avancées

Bienvenue au deuxième niveau ! Vous allez maîtriser les techniques avancées des expressions régulières.

---

##  Concepts Clés

-   **Lookaheads** : `(?=...)` (positif), `(?!...)` (négatif) - Vérifier sans consommer.
-   **Lookbehinds** : `(?<=...)` (positif), `(?<!...)` (négatif) - Vérifier en arrière.
-   **Groupes** : `(...)` pour capturer, `(?:...)` pour non-capturer.
-   **Backreferences** : `\1`, `\2`, etc. pour référencer les groupes capturés.
-   **Quantificateurs Non-Gourmands** : `*?`, `+?`, `??`, `{n,m}?` pour matcher le moins possible.
-   **Substitution** : `re.sub(pattern, replacement, string)` pour remplacer.

---

##  Les 8 Exercices

### 1. Validation de Mot de Passe Robuste (10 points)
**Objectif** : Valider un mot de passe avec lookaheads.

**Critères** :
- Au moins 8 caractères
- Au moins une majuscule
- Au moins une minuscule
- Au moins un chiffre

**Indices** :
- Niveau 1 : Utilisez `(?=...)` pour les lookaheads.
- Niveau 2 : Utilisez `(?=.*[A-Z])` pour vérifier une majuscule.
- Niveau 3 : Combinez les lookaheads.

**Solution** : `^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,}$`

---

### 2. Extraction de Nom d'Utilisateur (10 points)
**Objectif** : Extraire le nom d'utilisateur depuis une e-mail.

**Indices** :
- Niveau 1 : Utilisez `(\w+)` pour capturer.
- Niveau 2 : Utilisez `@` comme délimiteur.
- Niveau 3 : Utilisez `re.findall()` pour extraire.

**Solution** : `(\w+)@`

---

### 3. Reformatage de Dates avec Backreferences (10 points)
**Objectif** : Convertir JJ/MM/AAAA en AAAA-MM-JJ.

**Indices** :
- Niveau 1 : Capturez les trois parties avec `(\d{2})`.
- Niveau 2 : Utilisez `\1`, `\2`, `\3` pour les backreferences.
- Niveau 3 : Utilisez `re.sub()` pour remplacer.

**Solution** : Pattern `(\d{2})/(\d{2})/(\d{4})`, Replacement `\3-\2-\1`

---

### 4. Détection de Mots Dupliqués (10 points)
**Objectif** : Détecter les mots répétés consécutifs.

**Indices** :
- Niveau 1 : Capturez un mot avec `(\w+)`.
- Niveau 2 : Utilisez `\s+` pour l'espace.
- Niveau 3 : Utilisez `\1` pour référencer le même mot.

**Solution** : `\b(\w+)\s+\1\b`

---

### 5. Extraction de Contenu HTML (10 points)
**Objectif** : Extraire le contenu entre les balises HTML.

**Indices** :
- Niveau 1 : Utilisez `<[^>]+>` pour les balises.
- Niveau 2 : Utilisez `([^<]+)` pour le contenu.
- Niveau 3 : Utilisez `?` pour non-gourmand.

**Solution** : `<[^>]+>([^<]+)</[^>]+>`

---

### 6. Validation de Prix (10 points)
**Objectif** : Valider un prix avec devise.

**Formats** :
- `$19.99` (dollar)
- `€15,50` (euro)

**Indices** :
- Niveau 1 : Utilisez `\$` pour le dollar.
- Niveau 2 : Utilisez `|` pour "ou".
- Niveau 3 : Combinez les deux formats.

**Solution** : `^(\$\d+\.\d{2}|€\d+,\d{2})$`

---

### 7. Exclusion de Mots Spécifiques (10 points)
**Objectif** : Extraire les mots SAUF "the" et "a".

**Indices** :
- Niveau 1 : Utilisez `(?!...)` pour lookahead négatif.
- Niveau 2 : Utilisez `\b` pour les limites.
- Niveau 3 : Combinez pour exclure plusieurs mots.

**Solution** : `\b(?!the\b|a\b)\w+\b`

---

### 8. Extraction Complexe (10 points)
**Objectif** : Extraire le nom et le domaine d'une e-mail.

**Indices** :
- Niveau 1 : Capturez le nom avec `(\w+)`.
- Niveau 2 : Capturez le domaine avec `(\w+)`.
- Niveau 3 : Utilisez `re.findall()` pour extraire les tuples.

**Solution** : `(\w+)@(\w+)\.`

---

##  Barème

-   Chaque exercice réussi = 10 points
-   Total du niveau = 80 points

---
 Comment Commencer

1. Ouvrez `exercices.py`
2. Pour chaque exercice, remplacez `r"TODO"` par votre regex
3. Testez localement : `python exercices.py`
4. Poussez sur GitHub : `git push origin main`
5. Vérifiez votre score dans l'onglet "Actions"


**Bonne chance !** 
