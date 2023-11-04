from src.ej_21_3 import dividendo, divisor

def test_dividendo():
    assert dividendo("3") == 3
    assert dividendo("25") == 25

def test_divisor():
    assert divisor("3") == 3
    assert divisor("25") == 25