
# Cours Complet : Maîtriser les Expressions Régulières (Regex)

---

## Table des Matières

1.  **Introduction : Qu'est-ce qu'une Expression Régulière ?**
2.  **Pourquoi les Regex ? L'Argument Contre les Méthodes de Chaînes Classiques**
3.  **Les Fondamentaux : Les Briques de Base des Regex**
4.  **Les Concepts Avancés : Devenir un Expert**
5.  **Les Regex en Python : Le Module `re`**
6.  **Lexique Exhaustif et Antisèche**
7.  **Bonnes Pratiques et Pièges Courants**
8.  **Conclusion**

---

## 1. Introduction : Qu'est-ce qu'une Expression Régulière ?

### Définition et Analogie : Le "Super-Détective" du Texte

Imaginez que vous avez un immense livre et que vous devez trouver toutes les phrases qui contiennent un nom de ville, suivi d'un code postal à 5 chiffres. Une recherche simple ("Ctrl+F") serait impossible.

Une **expression régulière** (ou **Regex**) est une séquence de caractères qui définit un **pattern de recherche**. C'est comme donner des instructions ultra-précises à un "super-détective" pour qu'il trouve exactement ce que vous cherchez dans un texte.

> **Analogie** : Une regex est au texte ce qu'un plan de construction est à une maison. Elle décrit la structure de ce que vous voulez trouver, pas seulement son contenu exact.

Par exemple, pour trouver un code postal français, au lieu de chercher `75001`, `75002`, etc., vous donnez au détective le pattern suivant :

`\d{5}`

- `\d` : "Trouve un chiffre"
- `{5}` : "...exactement 5 fois de suite"

Ce simple pattern trouvera `75016`, `13008`, `69001`, et tous les autres codes postaux, mais ignorera `1234` ou `abcde`.

### À quoi ça sert ? Cas d'usage concrets

Les regex sont partout en programmation. Voici quelques exemples :

| Domaine | Cas d'Usage | Exemple de Pattern |
|---|---|---|
| **Validation de Formulaires** | Vérifier qu'une adresse e-mail est valide | `[\w.-]+@[\w.-]+\.\w+` |
| **Analyse de Fichiers (Logs)** | Extraire toutes les adresses IP d'un log | `\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}` |
| **Nettoyage de Données** | Supprimer toutes les balises HTML d'un texte | `<[^>]+>` |
| **Édition de Code** | Renommer une variable dans des dizaines de fichiers | `ma_vieille_variable` |
| **Extraction d'Informations** | Récupérer tous les numéros de téléphone d'une page | `0\d[ .]?(\d{2}[ .]?){4}` |

---

## 2. Pourquoi les Regex ? L'Argument Contre les Méthodes de Chaînes Classiques

Python offre de nombreuses méthodes pour manipuler les chaînes de caractères : `.find()`, `.replace()`, `.startswith()`, `.split()`, etc. Alors, pourquoi s'embêter avec les regex ?

### Les Limites des Méthodes Classiques

Imaginez que vous voulez vérifier si une chaîne contient un numéro de téléphone. Comment feriez-vous sans regex ?

```python
def est_un_telephone(chaine):
    if len(chaine) != 10:
        return False
    if not chaine.startswith('0'):
        return False
    for caractere in chaine:
        if not caractere.isdigit():
            return False
    return True
```

C'est verbeux, et ça ne gère qu'un seul format ! Que faire si le numéro contient des espaces (`06 12 34 56 78`) ? Ou des points (`06.12.34.56.78`) ? Le code deviendrait rapidement un monstre complexe et difficile à maintenir.

### Les Super-Pouvoirs des Regex

Les regex résolvent ce problème en décrivant la **structure** de ce que vous cherchez, pas seulement son contenu.

| Super-Pouvoir | Description | Exemple |
|---|---|---|
| **Flexibilité** | Un seul pattern peut correspondre à des milliers de variations. | `^0\d([. ]?\d{2}){4}$` matche `0612345678`, `06 12 34 56 78` et `06.12.34.56.78`. |
| **Puissance** | Exprimez des règles complexes en une seule ligne. | `(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,}` (mot de passe robuste) est presque impossible à faire sans regex. |
| **Concision** | Remplacez des dizaines de lignes de code par un seul pattern. | Le code de validation de téléphone ci-dessus se résume à `re.match(r"^0\d{9}$", chaine)`. |

### Tableau Comparatif : Regex vs Méthodes Classiques

| Tâche | Méthodes Classiques | Avec Regex |
|---|---|---|
| **Trouver un mot exact** | `if "mot" in texte:` | `re.search(r"mot", texte)` (similaire) |
| **Trouver un mot au début** | `texte.startswith("mot")` | `re.match(r"mot", texte)` (similaire) |
| **Trouver un numéro de téléphone** | Très complexe (plusieurs `if`, boucles) | `re.search(r"^0\d([. ]?\d{2}){4}$", texte)` (simple et flexible) |
| **Extraire tous les e-mails** | Extrêmement difficile | `re.findall(r"[\w.-]+@[\w.-]+\.\w+", texte)` (une seule ligne) |
| **Remplacer des formats de date** | `split()`, `join()`, manipulation de listes | `re.sub(r"(\d{2})/(\d{2})/(\d{4})", r"\3-\2-\1", texte)` (puissant et concis) |

> **Conclusion** : Les méthodes classiques sont parfaites pour des recherches simples et fixes. Dès que vous avez besoin de flexibilité, de validation de format ou d'extraction de données structurées, les **expressions régulières sont l'outil qu'il vous faut**.

---

## 3. Les Fondamentaux : Les Briques de Base des Regex

### Les Caractères Littéraux

La plupart des caractères dans une regex se représentent eux-mêmes. La regex `chat` trouvera exactement la chaîne "chat".

### Les Métacaractères

Ce sont les caractères qui ont un pouvoir spécial. Les plus importants sont :
`. ^ $ * + ? { } [ ] \ | ( )`

Pour chercher un de ces caractères littéralement, il faut l'"échapper" avec un antislash `\`. Par exemple, pour trouver un point `.` littéral, on utilise `\.`. 

### Les Classes de Caractères

| Classe | Description | Exemple |
|---|---|---|
| `[abc]` | N'importe quel caractère de l'ensemble (a, b, ou c) | `gr[ai]s` matche "gras" et "gris" |
| `[^abc]` | N'importe quel caractère qui N'EST PAS dans l'ensemble | `[^0-9]` matche tout ce qui n'est pas un chiffre |
| `[a-z]` | N'importe quel caractère dans l'intervalle (ici, minuscule) | `[a-zA-Z]` matche n'importe quelle lettre |
| `\d` | N'importe quel chiffre (`[0-9]`) | | 
| `\w` | N'importe quel caractère de mot (lettres, chiffres, `_`) | `\w+` matche un mot |
| `\s` | N'importe quel caractère d'espacement (espace, tabulation, nouvelle ligne) | | 
| `.` | N'importe quel caractère (sauf nouvelle ligne par défaut) | | 

### Les Quantificateurs

| Quant. | Description | Exemple |
|---|---|---|
| `*` | Zéro ou plusieurs fois | `ab*c` matche "ac", "abc", "abbc", etc. |
| `+` | Une ou plusieurs fois | `ab+c` matche "abc", "abbc", mais pas "ac" |
| `?` | Zéro ou une fois | `ab?c` matche "ac" et "abc" |
| `{n}` | Exactement n fois | `\d{5}` matche un code postal à 5 chiffres |
| `{n,}` | Au moins n fois | `\d{2,}` matche un nombre avec au moins 2 chiffres |
| `{n,m}` | Entre n et m fois | `\w{3,5}` matche un mot de 3 à 5 lettres |

### Les Ancres

| Ancre | Description | Exemple |
|---|---|---|
| `^` | Début de la chaîne (ou de la ligne avec `re.MULTILINE`) | `^Hello` matche "Hello world" mais pas "world, Hello" |
| `$` | Fin de la chaîne (ou de la ligne avec `re.MULTILINE`) | `world$` matche "Hello world" mais pas "world, Hello" |
| `\b` | Frontière de mot | `\bcat\b` matche "cat" dans "the cat sat" mais pas dans "concatenate" |

---

## 4. Les Concepts Avancés : Devenir un Expert

### Les Groupes et la Capture

Les parenthèses `()` ont deux fonctions : 
1.  **Grouper** des parties de la regex pour appliquer un quantificateur.
2.  **Capturer** le texte qui correspond à la partie de la regex entre parenthèses.

**Exemple :** `(ha)+` matche "ha", "haha", "hahaha", etc. Le groupe est `ha`.

```python
import re
match = re.search(r"(\d{2})/(\d{2})/(\d{4})", "25/12/2023")
if match:
    print(match.group(0)) # Le match complet : 25/12/2023
    print(match.group(1)) # Le 1er groupe capturé : 25
    print(match.group(2)) # Le 2ème groupe capturé : 12
    print(match.group(3)) # Le 3ème groupe capturé : 2023
```

### Les Alternatives

Le `|` (pipe) fonctionne comme un "OU" logique.

**Exemple :** `chat|chien` matche "chat" ou "chien".

### Les Lookarounds

C'est le concept le plus puissant (et le plus complexe). Les lookarounds permettent de vérifier la présence de texte **avant** ou **après** votre match, **sans l'inclure dans le résultat final**.

| Lookaround | Description | Exemple |
|---|---|---|
| `(?=...)` | **Lookahead Positif** : Le texte doit être suivi par ... | `Windows(?= 95|98|NT|2000)` matche "Windows" seulement s'il est suivi par une de ces versions. |
| `(?!...)` | **Lookahead Négatif** : Le texte ne doit PAS être suivi par ... | `Windows(?! 95|98)` matche "Windows" seulement s'il n'est pas suivi par 95 ou 98. |
| `(?<=...)` | **Lookbehind Positif** : Le texte doit être précédé par ... | `(?<=EUR)\d+` matche un nombre seulement s'il est précédé par "EUR". |
| `(?<!...)` | **Lookbehind Négatif** : Le texte ne doit PAS être précédé par ... | `(?<!non-)\w+` matche un mot seulement s'il n'est pas précédé par "non-". |

### Les Backreferences

Permet de réutiliser le texte capturé par un groupe plus tôt dans la regex.

**Exemple :** `(\w+)\s+\1` trouve les mots répétés. `\1` fait référence au texte capturé par le premier groupe `(\w+)`.

---

## 5. Les Regex en Python : Le Module `re`

### `re.search(pattern, string)`

-   **Action** : Cherche le `pattern` n'importe où dans la `string`.
-   **Retourne** : Un objet `Match` si trouvé, sinon `None`.
-   **Quand l'utiliser** : Quand vous voulez savoir **si** le pattern existe et où il se trouve.

```python
import re
match = re.search(r"world", "Hello world!")
if match:
    print(f"Trouvé ! à l'index {match.start()}")
```

### `re.match(pattern, string)`

-   **Action** : Cherche le `pattern` **uniquement au début** de la `string`.
-   **Retourne** : Un objet `Match` si trouvé, sinon `None`.
-   **Quand l'utiliser** : Pour la validation de format (ex: la chaîne entière doit être un numéro de téléphone).

```python
import re
match = re.match(r"Hello", "Hello world!") # Trouvé
match_fail = re.match(r"world", "Hello world!") # Non trouvé
```

### `re.findall(pattern, string)`

-   **Action** : Trouve **toutes** les occurrences du `pattern`.
-   **Retourne** : Une liste de toutes les correspondances.
-   **Quand l'utiliser** : Pour extraire toutes les données d'un certain type (tous les e-mails, tous les liens, etc.).

```python
import re
emails = re.findall(r"[\w.-]+@[\w.-]+", "Contactez user1@a.com ou user2@b.com")
print(emails) # ["user1@a.com", "user2@b.com"]
```

### `re.sub(pattern, repl, string)`

-   **Action** : Remplace les occurrences du `pattern` par `repl`.
-   **Retourne** : La nouvelle chaîne de caractères.
-   **Quand l'utiliser** : Pour nettoyer ou reformater du texte.

```python
import re
texte_censure = re.sub(r"(stupide|idiot)", "***", "Ce commentaire est stupide et idiot.")
print(texte_censure) # Ce commentaire est *** et ***.
```

### `re.compile(pattern)`

-   **Action** : Compile une expression régulière en un objet `Pattern`.
-   **Retourne** : Un objet `Pattern`.
-   **Quand l'utiliser** : Si vous utilisez la même regex plusieurs fois dans votre code, la compiler améliore les performances.

```python
import re
pattern_email = re.compile(r"[\w.-]+@[\w.-]+")

emails1 = pattern_email.findall("Contactez user1@a.com")
emails2 = pattern_email.findall("Contactez user2@b.com")
```

---

## 6. Lexique Exhaustif et Antisèche

### Tableau des Métacaractères

| Métacaractère | Nom | Description |
|---|---|---|
| `.` | Point | N'importe quel caractère sauf nouvelle ligne |
| `^` | Circonflexe | Début de chaîne |
| `$` | Dollar | Fin de chaîne |
| `*` | Astérisque | 0 ou plusieurs répétitions |
| `+` | Plus | 1 ou plusieurs répétitions |
| `?` | Point d'interrogation | 0 ou 1 répétition (ou rend non-gourmand) |
| `[]` | Crochets | Classe de caractères |
| `\` | Antislash | Échappe un métacaractère |
| `|` | Pipe | Alternative (OU logique) |
| `()` | Parenthèses | Groupe de capture |
| `{}` | Accolades | Quantificateur explicite |

### Tableau des Séquences Spéciales

| Séquence | Description |
|---|---|
| `\d` | Chiffre (`[0-9]`) |
| `\D` | Non-chiffre (`[^0-9]`) |
| `\w` | Caractère de mot (`[a-zA-Z0-9_]`) |
| `\W` | Non-caractère de mot |
| `\s` | Espace blanc (`[ \t\n\r\f\v]`) |
| `\S` | Non-espace blanc |
| `\b` | Frontière de mot |
| `\A` | Début de la chaîne (similaire à `^`) |
| `\Z` | Fin de la chaîne (similaire à `$`) |

### Tableau des Flags

Les flags modifient le comportement des expressions régulières.

| Flag | Nom court | Description |
|---|---|---|
| `re.IGNORECASE` | `re.I` | Ignore la casse (majuscules/minuscules) |
| `re.MULTILINE` | `re.M` | `^` et `$` matchent le début/fin de chaque ligne |
| `re.DOTALL` | `re.S` | Le `.` matche aussi les nouvelles lignes |
| `re.VERBOSE` | `re.X` | Permet d'écrire des regex sur plusieurs lignes avec des commentaires |

---

## 7. Bonnes Pratiques et Pièges Courants

### La Simplicité avant tout

Ce n'est pas parce que vous pouvez écrire une regex de 100 caractères pour tout faire en une seule fois que vous devez le faire. Parfois, il est plus lisible et plus maintenable d'utiliser deux ou trois regex plus simples.

### Commenter vos Regex

Avec le flag `re.VERBOSE` (`re.X`), vous pouvez écrire des regex beaucoup plus lisibles.

```python
pattern = re.compile(r"""
    ^               # Début de la chaîne
    (\d{4})         # Groupe 1 : Année (4 chiffres)
    -               # Séparateur
    (\d{2})         # Groupe 2 : Mois (2 chiffres)
    -               # Séparateur
    (\d{2})         # Groupe 3 : Jour (2 chiffres)
    $               # Fin de la chaîne
""", re.VERBOSE)
```

### Le "Catastrophic Backtracking"

C'est le piège de performance le plus courant. Il se produit lorsque la regex a trop de chemins possibles à explorer, souvent avec des quantificateurs imbriqués comme `(a*)*`.

**Exemple de regex dangereuse :** `(x+x+)+y`
Sur une chaîne comme `xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`, le moteur de regex peut prendre un temps exponentiel pour déterminer qu'il n'y a pas de `y` à la fin.

**Comment l'éviter :**
-   Soyez aussi spécifique que possible.
-   Évitez les quantificateurs imbriqués sur des patterns qui peuvent se chevaucher.
-   Utilisez des groupes non-capturants `(?:...)` si vous n'avez pas besoin de capturer.

### Utiliser des Outils en Ligne

Ne travaillez jamais à l'aveugle. Des outils comme [Regex101](https://regex101.com/) sont indispensables pour développer, tester et déboguer vos expressions régulières.

---

## 8. Conclusion

Les expressions régulières sont un outil extrêmement puissant, mais qui demande de la pratique. N'ayez pas peur d'expérimenter, de faire des erreurs et de consulter la documentation.

En maîtrisant les concepts de ce cours, vous avez acquis une compétence fondamentale en programmation qui vous sera utile dans d'innombrables situations, de la simple validation de formulaire à l'analyse complexe de données textuelles.

**Le voyage ne fait que commencer. La meilleure façon d'apprendre est de pratiquer !**
