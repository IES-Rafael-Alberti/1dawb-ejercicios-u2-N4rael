def verificarContraseña(contraseñaCorrecta):
    cont = False
    while cont == False:
        contrasena = input("Escribe la contraseña: ")
        if contrasena == contraseñaCorrecta:
            print("Contraseña correcta. Acceso permitido.")
            cont == True
        else:
            print("Contraseña incorrecta. Inténtelo nuevamente.")

def main():
    contraseñaCorrecta = "contraseña" 
    verificarContraseña(contraseñaCorrecta)

if __name__ == "__main__":
    main()
