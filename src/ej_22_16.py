def encontrarMayorNumero():
    mayor = 0
    cont = False
    while cont == False:
        numero = int(input("Escribe un número positivo (0 para terminar): "))
        if numero == 0:
            cont = True
        if numero > mayor:
            mayor = numero
    return mayor

def main():
    resultado = encontrarMayorNumero()
    print(f"El mayor número ingresado es: {resultado}")

if __name__ == "__main__":
    main()
