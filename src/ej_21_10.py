def esVegetariano(respuesta):
    error = True
    while error:
        if respuesta == "sí" or respuesta == "si":
            error = False
            return True
        elif respuesta == "no":
            error = False
            return False
        else:
            print("Por favor, responde solo con 'Sí' o 'No'.")

def menuPizzaV(opcion):
    ingredientes_disponibles = ["Mozzarella", "Tomate"]

    if opcion == "1":
        ingredientes_disponibles.append("Pimiento")
    elif opcion == "2":
        ingredientes_disponibles.append("Tofu")
    else:
        print("Opción no válida.")
    return ingredientes_disponibles


def menuPizzaNV(opcion):
    ingredientes_disponibles = ["Mozzarella", "Tomate"]

    if opcion == "1":
        ingredientes_disponibles.append("Peperoni")
    elif opcion == "2":
        ingredientes_disponibles.append("Jamón")
    elif opcion == "3":
        ingredientes_disponibles.append("Salmón")
    else:
        print("Opción no válida.")
    return ingredientes_disponibles
    

def main():
    respuesta = input("¿Eres vegetariano? (Sí/No): ").lower()
    esVeget = esVegetariano(respuesta)
    if esVeget:
        print("Ingredientes vegetarianos disponibles:")
        print("1. Pimiento")
        print("2. Tofu")
        opcion = input("Elige un ingrediente (1/2): ")
        ingredientesElegidos = menuPizzaV(opcion)
        
    else:
        print("Ingredientes no vegetarianos disponibles:")
        print("1. Peperoni")
        print("2. Jamón")
        print("3. Salmón")
        opcion = input("Elige un ingrediente (1/2/3): ")
        ingredientesElegidos = menuPizzaNV(opcion)

    tipoPizza = "vegetariana" if esVeget else "no vegetariana"
    
    print(f"Has elegido una pizza {tipoPizza} con los siguientes ingredientes:")
    for ingrediente in ingredientesElegidos:
        print(ingrediente)

if __name__ == "__main__":
    main()
