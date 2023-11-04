
from src.ej_21_8 import comproPunt, obtenerBeneficio, obtenerNivel

def test_comproPunt_con_0():
    assert comproPunt(0.0) == True

def test_comproPunt_con_0_4():
    assert comproPunt(0.4) == True

def test_comproPunt_con_mayor_a_0_6():
    assert comproPunt(0.7) == True

def test_comproPunt_con_otro_valor():
    assert comproPunt(0.5) == False

def test_obtenerBeneficio_con_0_4():
    assert obtenerBeneficio(0.4) == 960

def test_obtenerBeneficio_con_mayor_a_0_6():
    assert obtenerBeneficio(0.7) == 1680

# Pruebas para obtenerNivel
def test_obtenerNivel_con_0():
    assert obtenerNivel(0.0) == "Inaceptable - 0"

def test_obtenerNivel_con_0_4():
    assert obtenerNivel(0.4) == "Aceptable - 960"

def test_obtenerNivel_con_mayor_a_0_6():
    assert obtenerNivel(0.7) == "Meritorio - 1680"
