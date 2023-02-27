#!/usr/bin/env python3

# Exercice 2: Test d'une fonction de conversion
# Le but de cet exercice est de tester une fonction de conversion qui convertit un nombre de minutes en heures et minutes. La fonction à tester est la suivante:

import pytest

def convertir_minutes_en_heures(minutes):
    """Convertit un nombre de minutes en heures et minutes."""
    if not isinstance(minutes, int):
        raise TypeError('La valeur doit être un entier.')
    if minutes < 0:
        raise ValueError('La valeur doit être positive.')
    heures = minutes // 60
    minutes_restantes = minutes % 60
    return heures, minutes_restantes

# Vous devez écrire des tests pour cette fonction en couvrant tous les cas possibles, y compris les cas limites, les cas d'erreur et les cas où le nombre de minutes est égal à 0.