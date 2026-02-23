"""
Solutions pour Niveau 2 : Expressions Régulières Avancées
"""

import re


def exercice_1_mot_de_passe_robuste():
    """Solution: (?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,}"""
    pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,}$"
    
    assert re.match(pattern, "MyPass123") is not None
    assert re.match(pattern, "mypass123") is None
    assert re.match(pattern, "MYPASS123") is None
    assert re.match(pattern, "MyPassABC") is None
    print("✅ Exercice 1 réussi")


def exercice_2_extraction_username():
    """Solution: (\w+)@"""
    pattern = r"(\w+)@"
    
    result = re.findall(pattern, "john.doe@example.com")
    assert result == ["john.doe"]
    
    result = re.findall(pattern, "user123@company.fr")
    assert result == ["user123"]
    
    result = re.findall(pattern, "admin@site.co.uk")
    assert result == ["admin"]
    print("✅ Exercice 2 réussi")


def exercice_3_reformatage_dates():
    """Solution: (\d{2})/(\d{2})/(\d{4}) → \3-\2-\1"""
    pattern = r"(\d{2})/(\d{2})/(\d{4})"
    replacement = r"\3-\2-\1"
    
    result = re.sub(pattern, replacement, "15/03/2024")
    assert result == "2024-03-15"
    
    result = re.sub(pattern, replacement, "01/01/2020")
    assert result == "2020-01-01"
    print("✅ Exercice 3 réussi")


def exercice_4_mots_dupliques():
    """Solution: \b(\w+)\s+\1\b"""
    pattern = r"\b(\w+)\s+\1\b"
    
    assert re.search(pattern, "hello hello") is not None
    assert re.search(pattern, "the the quick") is not None
    assert re.search(pattern, "hello world") is None
    print("✅ Exercice 4 réussi")


def exercice_5_extraction_html():
    """Solution: <[^>]+>([^<]+)</[^>]+>"""
    pattern = r"<[^>]+>([^<]+)</[^>]+>"
    
    result = re.findall(pattern, "<p>Hello</p>")
    assert result == ["Hello"]
    
    result = re.findall(pattern, "<div>Content</div> <span>Text</span>")
    assert result == ["Content", "Text"]
    print("✅ Exercice 5 réussi")


def exercice_6_validation_prix():
    """Solution: ^\$\d+\.\d{2}$|^€\d+,\d{2}$"""
    pattern = r"^(\$\d+\.\d{2}|€\d+,\d{2})$"
    
    assert re.match(pattern, "$19.99") is not None
    assert re.match(pattern, "€15,50") is not None
    assert re.match(pattern, "19.99") is None
    assert re.match(pattern, "$19") is None
    print("✅ Exercice 6 réussi")


def exercice_7_exclusion_mots():
    """Solution: \b(?!the\b|a\b)\w+\b"""
    pattern = r"\b(?!the\b|a\b)\w+\b"
    
    result = re.findall(pattern, "the quick brown fox")
    assert result == ["quick", "brown", "fox"]
    
    result = re.findall(pattern, "a cat and a dog")
    assert result == ["cat", "dog"]
    print("✅ Exercice 7 réussi")


def exercice_8_extraction_complexe():
    """Solution: (\w+)@(\w+)\."""
    pattern = r"(\w+)@(\w+)\."
    
    result = re.findall(pattern, "john.doe@example.com")
    assert result == [("john.doe", "example")]
    
    result = re.findall(pattern, "user@company.co.uk")
    assert result == [("user", "company")]
    print("✅ Exercice 8 réussi")


if __name__ == "__main__":
    print("🚀 Lancement des solutions Niveau 2...\n")
    
    exercice_1_mot_de_passe_robuste()
    exercice_2_extraction_username()
    exercice_3_reformatage_dates()
    exercice_4_mots_dupliques()
    exercice_5_extraction_html()
    exercice_6_validation_prix()
    exercice_7_exclusion_mots()
    exercice_8_extraction_complexe()
    
    print("\n🎉 Toutes les solutions du Niveau 2 sont correctes ! (80 points)")
