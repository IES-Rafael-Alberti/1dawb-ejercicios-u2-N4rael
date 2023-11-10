def contarDigitos():
    totalLineas = 0
    cont = False
    while cont == False:
        linea = input("Ingrese un título de libro ('*' para terminar línea): ")
        if linea == "*":
            cont = True
        digitos = 0
        for caracter in linea:
            if caracter.isdigit():
                digitos += 1
        if digitos > 0:
            print(f"Línea completa. Aparecen {digitos} dígitos numéricos.")
        totalLineas += 1
    return totalLineas

def main():
    lineas = contarDigitos()
    print(f"Se leyeron {lineas} líneas completas.")

if __name__ == "__main__":
    main()
