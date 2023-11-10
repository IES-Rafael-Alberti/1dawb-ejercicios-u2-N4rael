def imprimirTrianguloRectangulo(altura):
    for i in range(1, altura + 1):
        print("*" * i)

def main():
    altura = int(input("Escribe la altura del triángulo: "))
    imprimirTrianguloRectangulo(altura)

if __name__ == "__main__":
    main()
