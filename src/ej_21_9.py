
def pedirEdad(edad):
    cont = False
    while cont == False:
        if edad.isnumeric:
            edad = int(edad)
            cont = True
            return edad
        else:
            print("Debes introducir un número")

def funPrecio(edad):
    edad = pedirEdad(edad)
    if edad < 4:
        precio = "gratis"
    elif edad >= 4 and edad < 18:
        precio = " de 5€"
    else:
        precio = "de 10€"
    return precio

def main():
    edad = input("Introduzca su edad: ")
    precio = funPrecio(edad)
    print("EL precio de entrada es " + precio + ".") 

if __name__ == "__main__":
    main()