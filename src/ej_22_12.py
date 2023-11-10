def contarLetraEnFrase(frase, letra):
    contador = 0
    for caracter in frase:
        if caracter == letra:
            contador += 1
    return contador

def main():
    frase = input("Ingrese una frase: ")
    letra = input("Ingrese una letra: ")
    cantidad = contarLetraEnFrase(frase, letra)
    print(f'La letra "{letra}" aparece {cantidad} veces en la frase.')

if __name__ == "__main__":
    main()
