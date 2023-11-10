def esPrimo(numero):
    if numero < 2:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

def contarPrimos():
    cantidadPrimos = 0
    while True:
        numero = int(input("Escribe un número (0 para terminar): "))
        if numero == 0:
            break
        if numero > 1 and esPrimo(numero):
            cantidadPrimos += 1
    return cantidadPrimos

def main():
    resultado = contarPrimos()
    print(f"Cantidad de números primos ingresados: {resultado}")

if __name__ == "__main__":
    main()
