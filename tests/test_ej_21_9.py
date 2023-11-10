import pytest
from src.ej_21_9 import pedirEdad, funPrecio

# Pruebas para pedirEdad
def test_pedirEdad_con_numero_valido():
    assert pedirEdad("10") == 10

# Pruebas para funPrecio
def test_funPrecio_con_edad_menor_a_4():
    assert funPrecio("3") == "gratis"

def test_funPrecio_con_edad_entre_4_y_17():
    assert funPrecio("12") == " de 5€"

def test_funPrecio_con_edad_mayor_o_igual_a_18():
    assert funPrecio("20") == "de 10€"

