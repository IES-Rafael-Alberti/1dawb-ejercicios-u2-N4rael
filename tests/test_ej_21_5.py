from src.ej_21_5 import pedirEdad, pedirIngreso

def test_pedirEdad():
    assert pedirEdad("25") == 25

def test_pedirIngreso():
    assert pedirIngreso("1000") == 1000