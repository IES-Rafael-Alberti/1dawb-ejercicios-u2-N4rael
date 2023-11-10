def imprimirAñosCumplidos(edad):
    for i in range(1, edad + 1):
        print(i)

def main():
    edad = int(input("Escriba su edad: "))
    imprimirAñosCumplidos(edad)

if __name__ == "__main__":
    main()
