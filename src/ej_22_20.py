def buscarLetraEnFrase():
    frase = input("Ingrese una frase: ")
    letra = input("Ingrese una letra: ")
    for posicion, caracter in enumerate(frase):
        if caracter == letra:
            print(f"Se encontró la letra '{letra}' en la posición {posicion}.")
            return
    print(f"No se encontró la letra '{letra}' en la frase.")

def main():
    buscarLetraEnFrase()

if __name__ == "__main__":
    main()
