
def testPass(contra):
    passOrig = "contraseña"
    if contra.replace(" ", "").lower() == passOrig:
        return "1"
    else:
        return "2"


def main():
    contra = input("Introduzca una contraseña: ")
    if testPass(contra) == "1":
        print("Has acertado la contraseña")
    else:
        print("Siga jugando")

if __name__ == "__main__":
    main()