def contarAtras(numero):
    numeros = [str(i) for i in range(numero, -1, -1)]
    print(", ".join(numeros))

def main():
    numero = int(input("Escribe un número positivo: "))
    contarAtras(numero)

if __name__ == "__main__":
    main()
