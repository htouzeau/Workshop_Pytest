#!/usr/bin/env python3

# Commande pour installer pytest 3:
# sudo apt-get install python3-pytest -y

def sort_numbers(numbers):
    return sorted(numbers)

def test_sort_numbers():

    assert sort_numbers([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

    assert sort_numbers([]) == []

    assert sort_numbers([1, 2, 3, 4, 5, 6, 7]) == [1, 2, 3, 4, 5, 6, 7]

    assert sort_numbers([7, 6, 5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5, 6, 7]

    assert sort_numbers([5, 3, 6, 1, 2, 5, 3, 2, 1, 4]) == [1, 1, 2, 2, 3, 3, 4, 5, 5, 6]

import pytest
import random

def test_smoke():
    assert sort_numbers([3, 2, 1]) == [1, 2, 3]

def test_regression():
    assert sort_numbers([9, 8, 7]) == [7, 8, 9]

def test_integration():
    assert sort_numbers([5, 7, 2]) == [2, 5, 7]

# Fixture pour générer une liste d'entiers aléatoires
@pytest.fixture
def random_list():
    return random.sample(range(100), 10)

# Créez une fonction de test pour utiliser la fixture random_list
def test_random_sort(random_list):
    sorted_list = sorted(random_list)
    assert sort_numbers(random_list) == sorted_list