# Instructions pour l'Assignation : Expressions Régulières

Bienvenue ! Votre mission est d'écrire des expressions régulières pour résoudre une série de problèmes.

---

## Votre Objectif

Pour chaque niveau (`niveau_1_basique`, `niveau_2_avance`) :

1.  Ouvrez le fichier `exercices.py`.
2.  Pour chaque exercice marqué avec `# TODO`, écrivez la regex appropriée.
3.  Testez votre regex avec les cas fournis.
4.  Vous ne devez **PAS** modifier la structure des fonctions.

---

## Comment Travailler

### 1. Cloner le Dépôt

```bash
git clone <url-de-votre-depot>
cd <nom-du-depot>
```

### 2. Comprendre la Structure

Chaque exercice suit ce modèle :

```python
def exercice_1_validation_telephone():
    """
    TODO: Écrivez une regex pour valider un numéro de téléphone français
    Format attendu: 0XXXXXXXXX (0 suivi de 9 chiffres)
    """
    pattern = r"TODO"  # À remplacer par votre regex
    
    # Cas de test
    assert re.match(pattern, "0123456789") is not None
    assert re.match(pattern, "123456789") is None
```

### 3. Écrire une Regex

Remplacez `r"TODO"` par votre expression régulière :

```python
def exercice_1_validation_telephone():
    pattern = r"^0\d{9}$"  # Votre regex
    
    assert re.match(pattern, "0123456789") is not None
    assert re.match(pattern, "123456789") is None
```

### 4. Tester Localement

```bash
# Lancer tous les exercices
python niveau_1_basique/exercices.py

# Lancer un niveau spécifique
python niveau_2_avance/exercices.py
```

### 5. Sauvegarder et Pousser

```bash
git add .
git commit -m "Termine les exercices Regex niveau 1"
git push origin main
```

### 6. Voir votre Score

-   Allez sur votre dépôt GitHub.
-   Cliquez sur l'onglet **"Actions"**.
-   Vous verrez votre score et les exercices réussis.

---

##  Conseils

-   **Testez régulièrement** : Lancez les exercices après chaque modification.
-   **Utilisez des ressources** : [regex101.com](https://regex101.com/) est votre ami !
-   **Lisez les commentaires** : Chaque exercice explique ce qu'il faut faire.
-   **Progressez graduellement** : Commencez par le Niveau 1 avant le Niveau 2.

---

Bonne chance ! 
