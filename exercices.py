#!/usr/bin/env python3

# sudo apt-get install python3-pytest -y
# or
# sudo pip install pytest

# Importez la fonction à tester
def sort_numbers(numbers):
    return sorted(numbers)

# Créez une fonction de test pour tester la fonction de tri
def test_sort_numbers():

    # Vérifiez que la fonction renvoie la liste triée en ordre croissant
    assert sort_numbers([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

    # Vérifiez que la fonction renvoie une liste vide si la liste d'entrée est vide
    assert sort_numbers([]) == []

    # Vérifiez que la fonction renvoie une liste triée si la liste d'entrée est déjà triée
    assert sort_numbers([1, 2, 3, 4, 5, 6, 7]) == [1, 2, 3, 4, 5, 6, 7]

    # Vérifiez que la fonction renvoie une liste triée si la liste d'entrée est triée en ordre inverse
    assert sort_numbers([7, 6, 5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5, 6, 7]

    # Vérifiez que la fonction renvoie une liste triée si la liste d'entrée contient des doublons
    assert sort_numbers([5, 3, 6, 1, 2, 5, 3, 2, 1, 4]) == [1, 1, 2, 2, 3, 3, 4, 5, 5, 6]

# Utilisez des fixtures pour générer des données de test aléatoires pour la fonction de tri
import pytest
import random

@pytest.fixture
def random_list():
    return random.sample(range(100), 10)

# Créez une fonction de test pour utiliser la fixture random_list
def test_random_sort(random_list):
    sorted_list = sorted(random_list)
    assert sort_numbers(random_list) == sorted_list

# Ajoutez des marqueurs de test pour identifier les tests par catégorie
@pytest.mark.smoke
def test_smoke():
    assert sort_numbers([3, 2, 1]) == [1, 2, 3]

@pytest.mark.regression
def test_regression():
    assert sort_numbers([9, 8, 7]) == [7, 8, 9]

@pytest.mark.integration
def test_integration():
    assert sort_numbers([5, 7, 2]) == [2, 5, 7]

# Ajoutez une fonction de test pour vérifier que la fonction de tri lève une exception si la liste d'entrée est invalide
def test_invalid_input():
    with pytest.raises(TypeError):
        sort_numbers('invalid_input')

