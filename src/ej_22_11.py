def invertirPalabra(palabra):
    palabraInvertida = palabra[::-1]
    for letra in palabraInvertida:
        print(letra)

def main():
    palabra = input("Ingrese una palabra: ")
    invertirPalabra(palabra)

if __name__ == "__main__":
    main()
