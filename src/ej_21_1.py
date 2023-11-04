def pedirEdad(edad):
    error = True
    while error == True:
        if edad.isnumeric():
            intEdad = int(edad)
            error = False
            return intEdad
        else:
            print("Debe introducir un número válido.")
            error = True

def main():
    edad = input("Introduzca su edad: ")
    intEdad = pedirEdad(edad)
    if intEdad >= 18:
        print("Eres mayor de edad")
    else:
        print("No eres mayor de edad")


if __name__ == "__main__":
    main()
