#!/usr/bin/env python3

# Exercice 1: Test d'une fonction de tri
# Le but de cet exercice est de tester une fonction de tri qui trie une liste d'entiers dans l'ordre croissant. La fonction à tester est la suivante:
import pytest

def trier_liste(liste):
    """Trie une liste d'entiers dans l'ordre croissant."""
    return sorted(liste)

# Vous devez écrire des tests pour cette fonction en couvrant tous les cas possibles, y compris les cas limites, les cas d'erreur et les cas où la liste est vide.