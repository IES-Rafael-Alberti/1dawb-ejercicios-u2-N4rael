def palabra():
    frase = input("Escribe una frase: ")
    palabras = frase.split()
    masLarga = ""
    for palabra in palabras:
        if len(palabra) > len(masLarga):
            masLarga = palabra
    return masLarga, len(palabras)

def main():
    palabraLarga, cantidadPalabras = palabra()
    print(f"Palabra más larga: {palabraLarga}")
    print(f"Cantidad de palabras: {cantidadPalabras}")

if __name__ == "__main__":
    main()
