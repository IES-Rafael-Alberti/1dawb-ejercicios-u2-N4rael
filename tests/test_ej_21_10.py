
from src.ej_21_10 import esVegetariano, menuPizzaV, menuPizzaNV

def test_esVegetariano_si():
    respuesta = "sí"
    assert esVegetariano(respuesta) == True

def test_esVegetariano_no():
    respuesta = "no"
    assert esVegetariano(respuesta) == False

def test_menuPizzaV_pimiento():
    opcion = "1"
    ingredientes = menuPizzaV(opcion)
    assert ingredientes == ["Mozzarella", "Tomate", "Pimiento"]

def test_menuPizzaV_tofu():
    opcion = "2"
    ingredientes = menuPizzaV(opcion)
    assert ingredientes == ["Mozzarella", "Tomate", "Tofu"]

def test_menuPizzaV_opcion_invalida():
    opcion = "3"
    ingredientes = menuPizzaV(opcion)
    assert ingredientes == ["Mozzarella", "Tomate"]

def test_menuPizzaNV_peperoni():
    opcion = "1"
    ingredientes = menuPizzaNV(opcion)
    assert ingredientes == ["Mozzarella", "Tomate", "Peperoni"]

def test_menuPizzaNV_jamon():
    opcion = "2"
    ingredientes = menuPizzaNV(opcion)
    assert ingredientes == ["Mozzarella", "Tomate", "Jamón"]

def test_menuPizzaNV_salmon():
    opcion = "3"
    ingredientes = menuPizzaNV(opcion)
    assert ingredientes == ["Mozzarella", "Tomate", "Salmón"]

def test_menuPizzaNV_opcion_invalida():
    opcion = "4"
    ingredientes = menuPizzaNV(opcion)
    assert ingredientes == ["Mozzarella", "Tomate"]

