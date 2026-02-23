"""
Niveau 2 : Expressions Régulières Avancées (8 exercices - 80 points)
À compléter par les étudiants
"""

import re


# ============================================================================
# EXERCICE 1 : Mot de Passe Robuste (avec lookaheads)
# ============================================================================

def valider_mot_de_passe_robuste(mdp):
    """
    Valide un mot de passe robuste :
    - Au moins 8 caractères
    - Au moins une majuscule
    - Au moins une minuscule
    - Au moins un chiffre
    """
    pattern = r"TODO"  # À compléter
    return bool(re.match(pattern, mdp))


# ============================================================================
# EXERCICE 2 : Extraire Username depuis Email
# ============================================================================

def extraire_username_email(email):
    """
    Extrait le username (partie avant @) d'une adresse e-mail.
    """
    pattern = r"TODO"  # À compléter
    match = re.search(pattern, email)
    return match.group(1) if match else None


# ============================================================================
# EXERCICE 3 : Reformatter Dates avec Backreferences
# ============================================================================

def reformatter_date(date_jj_mm_aaaa):
    """
    Reformatte une date de JJ/MM/AAAA en AAAA-MM-JJ.
    Utilise les backreferences.
    """
    pattern = r"TODO"  # À compléter
    return re.sub(pattern, r"TODO", date_jj_mm_aaaa)


# ============================================================================
# EXERCICE 4 : Détecter Mots Dupliqués
# ============================================================================

def detecter_mots_dupliques(texte):
    """
    Détecte les mots qui se répètent consécutivement.
    Utilise les backreferences.
    """
    pattern = r"TODO"  # À compléter
    return re.findall(pattern, texte)


# ============================================================================
# EXERCICE 5 : Extraire Contenu HTML (non-gourmand)
# ============================================================================

def extraire_contenu_html(html):
    """
    Extrait le contenu entre les balises <p> et </p>.
    Utilise les quantificateurs non-gourmands.
    """
    pattern = r"TODO"  # À compléter
    return re.findall(pattern, html)


# ============================================================================
# EXERCICE 6 : Validation Prix avec Lookarounds
# ============================================================================

def valider_prix(prix):
    """
    Valide un prix au format: EUR123.45 ou USD99.99
    Utilise les lookaheads.
    """
    pattern = r"TODO"  # À compléter
    return bool(re.match(pattern, prix))


# ============================================================================
# EXERCICE 7 : Exclusion Mots avec Lookaheads Négatifs
# ============================================================================

def extraire_sans_motclé(texte, motcle):
    """
    Extrait tous les mots SAUF ceux qui commencent par le motclé.
    """
    pattern = r"TODO"  # À compléter
    return re.findall(pattern, texte)


# ============================================================================
# EXERCICE 8 : Extraction Complexe (Combinaison de Techniques)
# ============================================================================

def extraire_donnees_complexes(texte):
    """
    Extrait les données au format: [NOM:valeur] où NOM est en majuscules.
    Retourne un dictionnaire {NOM: valeur}.
    """
    pattern = r"TODO"  # À compléter
    matches = re.findall(pattern, texte)
    return {nom: valeur for nom, valeur in matches}


if __name__ == "__main__":
    print("Tests Niveau 2 - À compléter")
    print("Remplacez 'TODO' par vos patterns regex")
