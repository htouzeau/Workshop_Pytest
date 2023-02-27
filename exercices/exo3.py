#!/usr/bin/env python3

# Exercice 3: Test d'une fonction de validation de mot de passe
# Le but de cet exercice est de tester une fonction de validation de mot de passe qui vérifie si un mot de passe est valide selon certains critères. La fonction à tester est la suivante:

import pytest

def valider_mot_de_passe(mot_de_passe):
    """Valide un mot de passe."""
    if not isinstance(mot_de_passe, str):
        raise TypeError('Le mot de passe doit être une chaîne de caractères.')
    if len(mot_de_passe) < 8:
        return False
    majuscule = False
    chiffre = False
    for c in mot_de_passe:
        if c.isupper():
            majuscule = True
        elif c.isdigit():
            chiffre = True
    return majuscule and chiffre

# Vous devez écrire des tests pour cette fonction en couvrant tous les cas possibles, y compris les cas limites, les cas d'erreur et les cas où le mot de passe ne répond pas aux critères de validation.