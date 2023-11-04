
def testPass(password):
    passOrig = "contraseña"
    if password.replace(" ", "").lower() == passOrig:
        return True
    else:
        return False


def main():
    password = input("Introduzca una contraseña: ")
    if testPass(password) == True:
        print("Has acertado la contraseña")
    else:
        print("Siga jugando")

if __name__ == "__main__":
    main()