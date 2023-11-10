def mostrarMenu():
    print("Menú:")
    print("1- Comenzar programa")
    print("2- Imprimir listado")
    print("3- Finalizar programa")

def main():
    opcion = 0
    while opcion != 3:
        mostrarMenu()
        opcion = int(input("Elija una opción: "))
        if opcion == 1:
            print("Programa iniciado")
        elif opcion == 2:
            print("Imprimiendo listado")
        elif opcion == 3:
            print("Programa finalizado")
        else:
            print("Opción incorrecta. Inténtelo nuevamente.")

if __name__ == "__main__":
    main()
