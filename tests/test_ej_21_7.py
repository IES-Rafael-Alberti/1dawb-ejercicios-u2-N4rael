from src.ej_21_7 import rentaGrupo, bucle

def test_rentaGrupo_mayor_o_igual_a_60000():
    assert rentaGrupo(65000) == "45%"

def test_rentaGrupo_mayor_o_igual_a_35000():
    assert rentaGrupo(40000) == "30%"

def test_rentaGrupo_mayor_o_igual_a_20000():
    assert rentaGrupo(25000) == "20%"

def test_rentaGrupo_mayor_o_igual_a_10000():
    assert rentaGrupo(15000) == "15%"

def test_rentaGrupo_menor_a_10000():
    assert rentaGrupo(8000) == "5%"

def test_bucle():
    assert bucle("25000") == 25000




