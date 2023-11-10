def contarDigitos():
    totalPares = 0
    totalImpares = 0
    while True:
        numero = int(input("Escribe un número entero positivo (0 para terminar): "))
        if numero == 0:
            break
        while numero > 0:
            digito = numero % 10
            if digito % 2 == 0:
                totalPares += 1
            else:
                totalImpares += 1
            numero //= 10
    return totalPares, totalImpares

def main():
    pares, impares = contarDigitos()
    print(f"Cantidad de dígitos pares: {pares}")
    print(f"Cantidad de dígitos impares: {impares}")

if __name__ == "__main__":
    main()
