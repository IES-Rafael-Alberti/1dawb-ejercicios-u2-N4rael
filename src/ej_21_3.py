

def dividendo(divi):
    while True:
        if divi.isnumeric():
            intDivi = int(divi)
            return intDivi
        else:
            print("Debes introducir un número.")

def divisor(divisor):
    while True:
        if divisor.isnumeric():
            intDivisor = int(divisor)
            if intDivisor <= 0:
                print("El divisor no puede ser igual o menor que 0.")
            else:
                return intDivisor
        else:
            print("Debes introducir un número.")

def main():
    divi = input("Introduce el primer número: ")
    divisor = input("Introduce el segundo número: ")
    print(divi // divisor)

if __name__ == "__main__":
    main()