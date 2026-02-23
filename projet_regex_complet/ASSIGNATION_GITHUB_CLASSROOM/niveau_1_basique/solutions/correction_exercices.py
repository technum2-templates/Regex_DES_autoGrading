"""
Niveau 1 : Solutions Complètes avec Explications
"""

import re


# ============================================================================
# EXERCICE 1 : Valider un Numéro de Téléphone Simple
# ============================================================================

def exercice_1_validation_telephone():
    """
    Pattern: r"^0\d{9}$"
    
    Explication:
    - ^ : Début de la chaîne
    - 0 : Le caractère littéral "0"
    - \d{9} : Exactement 9 chiffres (0-9)
    - $ : Fin de la chaîne
    """
    pattern = r"^0\d{9}$"
    
    assert re.match(pattern, "0123456789") is not None
    assert re.match(pattern, "0987654321") is not None
    assert re.match(pattern, "123456789") is None
    assert re.match(pattern, "01234567890") is None
    print("✅ Exercice 1 réussi")


# ============================================================================
# EXERCICE 2 : Extraire des Mots se Terminant par "ing"
# ============================================================================

def exercice_2_mots_ing():
    """
    Pattern: r"\b\w+ing\b"
    
    Explication:
    - \b : Frontière de mot (début)
    - \w+ : Un ou plusieurs caractères de mot
    - ing : Les caractères littéraux "ing"
    - \b : Frontière de mot (fin)
    """
    pattern = r"\b\w+ing\b"
    
    result = re.findall(pattern, "running jumping")
    assert result == ["running", "jumping"]
    
    result = re.findall(pattern, "I am running and jumping")
    assert result == ["running", "jumping"]
    
    result = re.findall(pattern, "sing ring")
    assert result == ["sing", "ring"]
    print("✅ Exercice 2 réussi")


# ============================================================================
# EXERCICE 3 : Valider une Adresse E-mail Simple
# ============================================================================

def exercice_3_validation_email_simple():
    """
    Pattern: r"^[\w.-]+@[\w.-]+\.\w+$"
    
    Explication:
    - ^ : Début
    - [\w.-]+ : Un ou plusieurs caractères de mot, point ou tiret
    - @ : Le caractère littéral "@"
    - [\w.-]+ : Domaine (caractères de mot, point ou tiret)
    - \. : Un point littéral (échappé)
    - \w+ : Extension (com, fr, co.uk, etc.)
    - $ : Fin
    """
    pattern = r"^[\w.-]+@[\w.-]+\.\w+$"
    
    assert re.match(pattern, "user@example.com") is not None
    assert re.match(pattern, "john.doe@company.fr") is not None
    assert re.match(pattern, "invalid@") is None
    assert re.match(pattern, "@example.com") is None
    print("✅ Exercice 3 réussi")


# ============================================================================
# EXERCICE 4 : Extraction des Dates
# ============================================================================

def exercice_4_extraction_dates():
    """
    Pattern: r"\d{2}/\d{2}/\d{4}"
    
    Explication:
    - \d{2} : Exactement 2 chiffres (jour)
    - / : Séparateur littéral
    - \d{2} : Exactement 2 chiffres (mois)
    - / : Séparateur littéral
    - \d{4} : Exactement 4 chiffres (année)
    """
    pattern = r"\d{2}/\d{2}/\d{4}"
    
    result = re.findall(pattern, "15/03/2024")
    assert result == ["15/03/2024"]
    
    result = re.findall(pattern, "Dates: 01/01/2020 et 31/12/2021")
    assert result == ["01/01/2020", "31/12/2021"]
    print("✅ Exercice 4 réussi")


# ============================================================================
# EXERCICE 5 : Validation Code Postal
# ============================================================================

def exercice_5_validation_code_postal():
    """
    Pattern: r"^\d{5}$"
    
    Explication:
    - ^ : Début
    - \d{5} : Exactement 5 chiffres
    - $ : Fin
    """
    pattern = r"^\d{5}$"
    
    assert re.match(pattern, "75001") is not None
    assert re.match(pattern, "13013") is not None
    assert re.match(pattern, "1234") is None
    assert re.match(pattern, "123456") is None
    print("✅ Exercice 5 réussi")


# ============================================================================
# EXERCICE 6 : Voyelles Uniquement
# ============================================================================

def exercice_6_voyelles_uniquement():
    """
    Pattern: r"\b[aeiou]+\b"
    
    Explication:
    - \b : Frontière de mot
    - [aeiou]+ : Un ou plusieurs caractères de la classe [aeiou]
    - \b : Frontière de mot
    """
    pattern = r"\b[aeiou]+\b"
    
    result = re.findall(pattern, "a e i o u")
    assert result == ["a", "e", "i", "o", "u"]
    
    result = re.findall(pattern, "hello eau")
    assert result == ["eau"]
    
    result = re.findall(pattern, "aaa eee iii")
    assert result == ["aaa", "eee", "iii"]
    print("✅ Exercice 6 réussi")


# ============================================================================
# EXERCICE 7 : Protocoles URL
# ============================================================================

def exercice_7_protocoles_url():
    """
    Pattern: r"(\w+)://"
    
    Explication:
    - (\w+) : Groupe de capture : un ou plusieurs caractères de mot
    - :// : Les caractères littéraux "://"
    
    Nous capturons seulement le protocole (http, https, ftp), pas les "://"
    """
    pattern = r"(\w+)://"
    
    result = re.findall(pattern, "http://example.com")
    assert result == ["http"]
    
    result = re.findall(pattern, "https://secure.com et ftp://files.com")
    assert result == ["https", "ftp"]
    print("✅ Exercice 7 réussi")


# ============================================================================
# EXERCICE 8 : Mot de Passe Simple
# ============================================================================

def exercice_8_validation_mot_de_passe_simple():
    """
    Pattern: r"^.{8,}$"
    
    Explication:
    - ^ : Début
    - .{8,} : N'importe quel caractère, au moins 8 fois
    - $ : Fin
    """
    pattern = r"^.{8,}$"
    
    assert re.match(pattern, "MyPass123") is not None
    assert re.match(pattern, "short") is None
    assert re.match(pattern, "12345678") is not None
    print("✅ Exercice 8 réussi")


if __name__ == "__main__":
    print("🚀 Solutions Niveau 1...\n")
    
    exercice_1_validation_telephone()
    exercice_2_mots_ing()
    exercice_3_validation_email_simple()
    exercice_4_extraction_dates()
    exercice_5_validation_code_postal()
    exercice_6_voyelles_uniquement()
    exercice_7_protocoles_url()
    exercice_8_validation_mot_de_passe_simple()
    
    print("\n🎉 Toutes les solutions Niveau 1 sont correctes ! (40 points)")
