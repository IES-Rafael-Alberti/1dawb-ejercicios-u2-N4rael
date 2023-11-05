def imprimirImpares(numero):
    impares = [str(i) for i in range(1, numero + 1) if i % 2 != 0]
    print(", ".join(impares))

def main():
    numero = int(input("Escriba un número positivo: "))
    imprimirImpares(numero)

if __name__ == "__main__":
    main()
