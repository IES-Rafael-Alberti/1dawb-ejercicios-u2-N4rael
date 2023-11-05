def sumarHastaCero():
    suma = 0
    cont = False
    while cont == False:
        numero = int(input("Escribe un número (0 para terminar): "))
        if numero == 0:
            cont = True
        suma += numero
    return suma

def main():
    resultado = sumarHastaCero()
    print(f"La suma de los números ingresados es: {resultado}")

if __name__ == "__main__":
    main()
