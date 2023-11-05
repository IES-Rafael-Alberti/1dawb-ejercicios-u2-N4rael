def sumarNumerosHastaCero():
    suma = 0
    cont = False
    while cont == False:
        numero = int(input("Escribe un número (0 para terminar): "))
        if numero == 0:
            cont = True
        if numero > 0:
            suma += numero
    return suma

def main():
    resultado = sumarNumerosHastaCero()
    print(f"La suma de los números es: {resultado}")

if __name__ == "__main__":
    main()
