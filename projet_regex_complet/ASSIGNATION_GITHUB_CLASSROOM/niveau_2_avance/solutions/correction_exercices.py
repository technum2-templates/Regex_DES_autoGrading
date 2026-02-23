"""
Niveau 2 : Solutions Complètes avec Explications
"""

import re


# ============================================================================
# EXERCICE 1 : Mot de Passe Robuste
# ============================================================================

def valider_mot_de_passe_robuste(mdp):
    """
    Pattern: r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$"
    
    Explication:
    - ^ : Début
    - (?=.*[a-z]) : Lookahead positif - doit contenir au moins une minuscule
    - (?=.*[A-Z]) : Lookahead positif - doit contenir au moins une majuscule
    - (?=.*\d) : Lookahead positif - doit contenir au moins un chiffre
    - .{8,} : Au moins 8 caractères
    - $ : Fin
    """
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$"
    return bool(re.match(pattern, mdp))


# ============================================================================
# EXERCICE 2 : Extraire Username
# ============================================================================

def extraire_username_email(email):
    """
    Pattern: r"^([^@]+)@"
    
    Explication:
    - ^ : Début
    - ([^@]+) : Groupe de capture - un ou plusieurs caractères qui ne sont pas @
    - @ : Le caractère littéral @
    """
    pattern = r"^([^@]+)@"
    match = re.search(pattern, email)
    return match.group(1) if match else None


# ============================================================================
# EXERCICE 3 : Reformatter Date
# ============================================================================

def reformatter_date(date_jj_mm_aaaa):
    """
    Pattern: r"(\d{2})/(\d{2})/(\d{4})"
    Remplacement: r"\3-\2-\1"
    
    Explication:
    - (\d{2}) : Groupe 1 - jour
    - (\d{2}) : Groupe 2 - mois
    - (\d{4}) : Groupe 3 - année
    - \3-\2-\1 : Backreferences - année-mois-jour
    """
    pattern = r"(\d{2})/(\d{2})/(\d{4})"
    return re.sub(pattern, r"\3-\2-\1", date_jj_mm_aaaa)


# ============================================================================
# EXERCICE 4 : Mots Dupliqués
# ============================================================================

def detecter_mots_dupliques(texte):
    """
    Pattern: r"\b(\w+)\s+\1\b"
    
    Explication:
    - \b : Frontière de mot
    - (\w+) : Groupe 1 - un ou plusieurs caractères de mot
    - \s+ : Un ou plusieurs espaces
    - \1 : Backreference - le même mot que le groupe 1
    - \b : Frontière de mot
    """
    pattern = r"\b(\w+)\s+\1\b"
    return re.findall(pattern, texte)


# ============================================================================
# EXERCICE 5 : Contenu HTML
# ============================================================================

def extraire_contenu_html(html):
    """
    Pattern: r"<p>(.*?)</p>"
    
    Explication:
    - <p> : Balise littérale
    - (.*?) : Groupe de capture - n'importe quel caractère (non-gourmand)
    - </p> : Balise littérale
    
    Le ? rend le quantificateur * non-gourmand (lazy)
    """
    pattern = r"<p>(.*?)</p>"
    return re.findall(pattern, html)


# ============================================================================
# EXERCICE 6 : Validation Prix
# ============================================================================

def valider_prix(prix):
    """
    Pattern: r"^(EUR|USD)\d+\.\d{2}$"
    
    Explication:
    - ^ : Début
    - (EUR|USD) : Groupe - soit EUR soit USD
    - \d+ : Un ou plusieurs chiffres
    - \. : Un point littéral
    - \d{2} : Exactement 2 chiffres
    - $ : Fin
    """
    pattern = r"^(EUR|USD)\d+\.\d{2}$"
    return bool(re.match(pattern, prix))


# ============================================================================
# EXERCICE 7 : Exclusion Mots
# ============================================================================

def extraire_sans_motclé(texte, motcle):
    """
    Pattern: r"\b(?!" + motcle + r")\w+\b"
    
    Explication:
    - \b : Frontière de mot
    - (?!" + motcle + ") : Lookahead négatif - ne doit pas commencer par motcle
    - \w+ : Un ou plusieurs caractères de mot
    - \b : Frontière de mot
    """
    pattern = r"\b(?!" + motcle + r")\w+\b"
    return re.findall(pattern, texte)


# ============================================================================
# EXERCICE 8 : Extraction Complexe
# ============================================================================

def extraire_donnees_complexes(texte):
    """
    Pattern: r"\[([A-Z]+):([^\]]+)\]"
    
    Explication:
    - \[ : Crochet littéral [
    - ([A-Z]+) : Groupe 1 - une ou plusieurs majuscules
    - : : Deux-points littéral
    - ([^\]]+) : Groupe 2 - un ou plusieurs caractères qui ne sont pas ]
    - \] : Crochet littéral ]
    """
    pattern = r"\[([A-Z]+):([^\]]+)\]"
    matches = re.findall(pattern, texte)
    return {nom: valeur for nom, valeur in matches}


if __name__ == "__main__":
    print("🚀 Solutions Niveau 2...\n")
    
    # Tests
    assert valider_mot_de_passe_robuste("MyPass123") == True
    print("✅ Exercice 1 réussi")
    
    assert extraire_username_email("user@example.com") == "user"
    print("✅ Exercice 2 réussi")
    
    assert reformatter_date("25/12/2023") == "2023-12-25"
    print("✅ Exercice 3 réussi")
    
    assert detecter_mots_dupliques("hello hello world") == ["hello"]
    print("✅ Exercice 4 réussi")
    
    assert extraire_contenu_html("<p>Bonjour</p>") == ["Bonjour"]
    print("✅ Exercice 5 réussi")
    
    assert valider_prix("EUR123.45") == True
    print("✅ Exercice 6 réussi")
    
    assert "test" in extraire_sans_motclé("test hello world", "hel")
    print("✅ Exercice 7 réussi")
    
    assert extraire_donnees_complexes("[NAME:John] [AGE:30]") == {"NAME": "John", "AGE": "30"}
    print("✅ Exercice 8 réussi")
    
    print("\n🎉 Toutes les solutions Niveau 2 sont correctes ! (80 points)")
