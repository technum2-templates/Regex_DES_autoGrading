"""
Niveau 1 : Expressions Régulières Basiques (8 exercices - 40 points)

Chaque exercice vous demande d'écrire une expression régulière pour résoudre un problème.
Remplacez r"TODO" par votre regex.
"""

import re


def exercice_1_validation_telephone():
    """
    Validez un numéro de téléphone français.
    Format attendu: 0XXXXXXXXX (0 suivi de 9 chiffres)
    
    Cas de test:
    - "0123456789" → Valide ✓
    - "123456789" → Invalide (pas de 0 au début)
    - "01234567890" → Invalide (trop de chiffres)
    """
    pattern = r"TODO"  # À remplacer
    
    # Tests
    assert re.match(pattern, "0123456789") is not None, "0123456789 devrait matcher"
    assert re.match(pattern, "0987654321") is not None, "0987654321 devrait matcher"
    assert re.match(pattern, "123456789") is None, "123456789 ne devrait pas matcher"
    assert re.match(pattern, "01234567890") is None, "01234567890 ne devrait pas matcher"
    print("✅ Exercice 1 réussi")


def exercice_2_mots_ing():
    """
    Extrayez tous les mots se terminant par "ing".
    
    Cas de test:
    - "running jumping" → ["running", "jumping"]
    - "I am running and jumping" → ["running", "jumping"]
    - "sing ring" → ["sing", "ring"]
    """
    pattern = r"TODO"  # À remplacer
    
    # Tests
    result = re.findall(pattern, "running jumping")
    assert result == ["running", "jumping"], f"Attendu ['running', 'jumping'], obtenu {result}"
    
    result = re.findall(pattern, "I am running and jumping")
    assert result == ["running", "jumping"], f"Attendu ['running', 'jumping'], obtenu {result}"
    
    result = re.findall(pattern, "sing ring")
    assert result == ["sing", "ring"], f"Attendu ['sing', 'ring'], obtenu {result}"
    print("✅ Exercice 2 réussi")


def exercice_3_validation_email_simple():
    """
    Validez une adresse e-mail simple.
    Format: quelquechose@domaine.com
    
    Cas de test:
    - "user@example.com" → Valide ✓
    - "john.doe@company.fr" → Valide ✓
    - "invalid@" → Invalide
    - "@example.com" → Invalide
    """
    pattern = r"TODO"  # À remplacer
    
    # Tests
    assert re.match(pattern, "user@example.com") is not None
    assert re.match(pattern, "john.doe@company.fr") is not None
    assert re.match(pattern, "invalid@") is None
    assert re.match(pattern, "@example.com") is None
    print("✅ Exercice 3 réussi")


def exercice_4_extraction_dates():
    """
    Extrayez les dates au format JJ/MM/AAAA.
    
    Cas de test:
    - "15/03/2024" → ["15/03/2024"]
    - "Dates: 01/01/2020 et 31/12/2021" → ["01/01/2020", "31/12/2021"]
    """
    pattern = r"TODO"  # À remplacer
    
    # Tests
    result = re.findall(pattern, "15/03/2024")
    assert result == ["15/03/2024"], f"Attendu ['15/03/2024'], obtenu {result}"
    
    result = re.findall(pattern, "Dates: 01/01/2020 et 31/12/2021")
    assert result == ["01/01/2020", "31/12/2021"], f"Attendu ['01/01/2020', '31/12/2021'], obtenu {result}"
    print("✅ Exercice 4 réussi")


def exercice_5_validation_code_postal():
    """
    Validez un code postal français (5 chiffres).
    
    Cas de test:
    - "75001" → Valide ✓
    - "13013" → Valide ✓
    - "1234" → Invalide (4 chiffres)
    - "123456" → Invalide (6 chiffres)
    """
    pattern = r"TODO"  # À remplacer
    
    # Tests
    assert re.match(pattern, "75001") is not None
    assert re.match(pattern, "13013") is not None
    assert re.match(pattern, "1234") is None
    assert re.match(pattern, "123456") is None
    print("✅ Exercice 5 réussi")


def exercice_6_voyelles_uniquement():
    """
    Extrayez les mots composés uniquement de voyelles (a, e, i, o, u).
    
    Cas de test:
    - "a e i o u" → ["a", "e", "i", "o", "u"]
    - "hello eau" → ["eau"]
    - "aaa eee iii" → ["aaa", "eee", "iii"]
    """
    pattern = r"TODO"  # À remplacer
    
    # Tests
    result = re.findall(pattern, "a e i o u")
    assert result == ["a", "e", "i", "o", "u"], f"Attendu ['a', 'e', 'i', 'o', 'u'], obtenu {result}"
    
    result = re.findall(pattern, "hello eau")
    assert result == ["eau"], f"Attendu ['eau'], obtenu {result}"
    
    result = re.findall(pattern, "aaa eee iii")
    assert result == ["aaa", "eee", "iii"], f"Attendu ['aaa', 'eee', 'iii'], obtenu {result}"
    print("✅ Exercice 6 réussi")


def exercice_7_protocoles_url():
    """
    Extrayez les protocoles d'URL (http, https, ftp, etc.).
    
    Cas de test:
    - "http://example.com" → ["http"]
    - "https://secure.com et ftp://files.com" → ["https", "ftp"]
    """
    pattern = r"TODO"  # À remplacer
    
    # Tests
    result = re.findall(pattern, "http://example.com")
    assert result == ["http"], f"Attendu ['http'], obtenu {result}"
    
    result = re.findall(pattern, "https://secure.com et ftp://files.com")
    assert result == ["https", "ftp"], f"Attendu ['https', 'ftp'], obtenu {result}"
    print("✅ Exercice 7 réussi")


def exercice_8_validation_mot_de_passe_simple():
    """
    Validez un mot de passe simple (au moins 8 caractères).
    
    Cas de test:
    - "MyPass123" → Valide ✓
    - "short" → Invalide (moins de 8 caractères)
    - "12345678" → Valide ✓
    """
    pattern = r"TODO"  # À remplacer
    
    # Tests
    assert re.match(pattern, "MyPass123") is not None
    assert re.match(pattern, "short") is None
    assert re.match(pattern, "12345678") is not None
    print("✅ Exercice 8 réussi")


if __name__ == "__main__":
    print("🚀 Lancement des exercices Niveau 1...\n")
    
    try:
        exercice_1_validation_telephone()
        exercice_2_mots_ing()
        exercice_3_validation_email_simple()
        exercice_4_extraction_dates()
        exercice_5_validation_code_postal()
        exercice_6_voyelles_uniquement()
        exercice_7_protocoles_url()
        exercice_8_validation_mot_de_passe_simple()
        
        print("\n🎉 Tous les exercices du Niveau 1 sont réussis ! (40 points)")
    except AssertionError as e:
        print(f"\n❌ Erreur : {e}")
        exit(1)
