
def grupoA(sexo, nombre):
    if sexo == "hombre" and nombre > "n" or sexo == "mujer" and nombre < "m":
        return True
    else:
        return False
    

def main():
    nombre = input("Escribe tu nombre: ").lower()
    sexo = input("Escribe tu sexo: ").lower()

    if grupoA(sexo, nombre) == True:
        print("Eres del grupo A")
    else:
        print("Eres del grupo B")

if __name__ == "__main__":
    main()