def sumarDigitos():
    totalNumerosPares = 0
    while True:
        numero = int(input("Escribe un número entero positivo (-1 para terminar): "))
        if numero == -1:
            break
        if numero % 2 == 0:
            suma = sumarDigitos(numero)
            totalNumerosPares += 1
            print(f"Suma de dígitos en {numero}: {suma}")
    return totalNumerosPares

def main():
    resultado = sumarDigitos()
    print(f"Total de números pares ingresados: {resultado}")

if __name__ == "__main__":
    main()
