def imprimirTrianguloNumeros(altura):
    for i in range(1, altura + 1):
        for j in range(i * 2 - 1, 0, -2):
            print(j, end=" ")
        print()

def main():
    altura = int(input("Escrib la altura del triángulo: "))
    imprimirTrianguloNumeros(altura)

if __name__ == "__main__":
    main()
