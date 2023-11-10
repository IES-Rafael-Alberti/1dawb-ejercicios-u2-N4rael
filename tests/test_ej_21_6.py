import pytest
from src.ej_21_6 import grupoA

def test_grupoA_hombre_con_nombre_valido():
    assert grupoA("hombre", "o") == True

def test_grupoA_hombre_con_nombre_invalido():
    assert grupoA("hombre", "a") == False

def test_grupoA_mujer_con_nombre_valido():
    assert grupoA("mujer", "a") == True

def test_grupoA_mujer_con_nombre_invalido():
    assert grupoA("mujer", "o") == False
