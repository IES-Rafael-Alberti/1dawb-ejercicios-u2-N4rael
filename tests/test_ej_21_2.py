import pytest
from src.ej_21_2 import testPass

def test_testPass():
    assert testPass("contraseña") == True
    assert testPass("CoNtrASeñA") == True
    assert testPass("contrAseña") == True

def test_testPassNO():
    assert testPass("thecakeisalie") == False
    assert testPass("1234") == False
    assert testPass("coca cola") == False
