def ecoUsuario():
    cont = False
    while cont == False:
        entrada = input("Escribe algo (o escriba 'salir' para terminar): ")
        if entrada.lower() == "salir":
            cont = True
        print(entrada)

def main():
    ecoUsuario()

if __name__ == "__main__":
    main()
