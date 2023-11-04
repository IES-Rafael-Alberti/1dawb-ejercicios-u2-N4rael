
def pedirNum(num):
    while True:
        if num.isnumeric():
            intNum = int(num)
            return intNum
        else:
            print("Debes introducir un número.")

def main():
    num = input("Introduce el número: ")
    if (num % 2) == 0:
        print("El número es par.")
    else:
        print("El número es impar.")
if __name__ == "__main__":
    main()