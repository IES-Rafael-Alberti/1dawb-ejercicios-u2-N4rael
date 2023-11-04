
def pedirEdad(num):
     while True:
        if num.isnumeric():
            intNum = int(num)
            return intNum
        else:
            print("Debes introducir un número.")

def pedirIngreso(num2):
     while True:
        if num2.isnumeric():
            intNum2 = int(num2)
            return intNum2
        else:
            print("Debes introducir un número.")

def main():
    num = input("Introduce su edad: ")
    num2 = input("Introduzca sus ingresos mensuales: ")
    edad = pedirEdad(num)
    ingresos = pedirIngreso(num2)
    cont = 0
    if edad >= 16:
        cont = cont + 1
    else:
        cont = cont
    if ingresos >= 1000:
        cont = cont + 1
    else:
        cont = cont

    if cont == 2:
        print("El usuario debe tributar.")
    else:
        print("El usuario no debe tributar")

if __name__ == "__main__":
    main()