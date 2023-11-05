from src.ej_22_5 import calcularInversion
def test_calcularInversion():
    assert calcularInversion(1000, 5, 3) == 1157.625
    assert calcularInversion(5000, 2.5, 10) == 6410.660536815282
    assert calcularInversion(2000, 10, 5) == 3220.0


