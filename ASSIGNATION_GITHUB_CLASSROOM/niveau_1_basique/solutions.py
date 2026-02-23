"""
Solutions pour Niveau 1 : Expressions Régulières Basiques
"""

import re


def exercice_1_validation_telephone():
    """Solution: ^0\d{9}$"""
    pattern = r"^0\d{9}$"
    assert re.match(pattern, "0123456789") is not None
    assert re.match(pattern, "0987654321") is not None
    assert re.match(pattern, "123456789") is None
    assert re.match(pattern, "01234567890") is None
    print("✅ Exercice 1 réussi")


def exercice_2_mots_ing():
    """Solution: \b\w+ing\b"""
    pattern = r"\b\w+ing\b"
    
    result = re.findall(pattern, "running jumping")
    assert result == ["running", "jumping"]
    
    result = re.findall(pattern, "I am running and jumping")
    assert result == ["running", "jumping"]
    
    result = re.findall(pattern, "sing ring")
    assert result == ["sing", "ring"]
    print("✅ Exercice 2 réussi")


def exercice_3_validation_email_simple():
    """Solution: ^\w+@\w+\.\w+$"""
    pattern = r"^\w+@\w+\.\w+$"
    
    assert re.match(pattern, "user@example.com") is not None
    assert re.match(pattern, "john.doe@company.fr") is not None
    assert re.match(pattern, "invalid@") is None
    assert re.match(pattern, "@example.com") is None
    print("✅ Exercice 3 réussi")


def exercice_4_extraction_dates():
    """Solution: \d{2}/\d{2}/\d{4}"""
    pattern = r"\d{2}/\d{2}/\d{4}"
    
    result = re.findall(pattern, "15/03/2024")
    assert result == ["15/03/2024"]
    
    result = re.findall(pattern, "Dates: 01/01/2020 et 31/12/2021")
    assert result == ["01/01/2020", "31/12/2021"]
    print("✅ Exercice 4 réussi")


def exercice_5_validation_code_postal():
    """Solution: ^\d{5}$"""
    pattern = r"^\d{5}$"
    
    assert re.match(pattern, "75001") is not None
    assert re.match(pattern, "13013") is not None
    assert re.match(pattern, "1234") is None
    assert re.match(pattern, "123456") is None
    print("✅ Exercice 5 réussi")


def exercice_6_voyelles_uniquement():
    """Solution: \b[aeiou]+\b"""
    pattern = r"\b[aeiou]+\b"
    
    result = re.findall(pattern, "a e i o u")
    assert result == ["a", "e", "i", "o", "u"]
    
    result = re.findall(pattern, "hello eau")
    assert result == ["eau"]
    
    result = re.findall(pattern, "aaa eee iii")
    assert result == ["aaa", "eee", "iii"]
    print("✅ Exercice 6 réussi")


def exercice_7_protocoles_url():
    """Solution: (https?|ftp)"""
    pattern = r"(https?|ftp)"
    
    result = re.findall(pattern, "http://example.com")
    assert result == ["http"]
    
    result = re.findall(pattern, "https://secure.com et ftp://files.com")
    assert result == ["https", "ftp"]
    print("✅ Exercice 7 réussi")


def exercice_8_validation_mot_de_passe_simple():
    """Solution: ^.{8,}$"""
    pattern = r"^.{8,}$"
    
    assert re.match(pattern, "MyPass123") is not None
    assert re.match(pattern, "short") is None
    assert re.match(pattern, "12345678") is not None
    print("✅ Exercice 8 réussi")


if __name__ == "__main__":
    print("🚀 Lancement des solutions Niveau 1...\n")
    
    exercice_1_validation_telephone()
    exercice_2_mots_ing()
    exercice_3_validation_email_simple()
    exercice_4_extraction_dates()
    exercice_5_validation_code_postal()
    exercice_6_voyelles_uniquement()
    exercice_7_protocoles_url()
    exercice_8_validation_mot_de_passe_simple()
    
    print("\n🎉 Toutes les solutions du Niveau 1 sont correctes ! (40 points)")
