
def rentaGrupo(rentaUser):
    tipoImpo = "5%"
    if rentaUser >= 60000:
        tipoImpo = "45%"
    elif rentaUser >= 35000:
        tipoImpo = "30%"
    elif rentaUser >= 20000:
        tipoImpo = "20%"
    elif rentaUser >= 10000:
        tipoImpo = "15%"
    
    tipoImpo = str(tipoImpo)
    return tipoImpo

def bucle(rentaUser):
    cont = True
    while cont == True:
        if rentaUser.isnumeric():
            rentaUser = int(rentaUser)
            cont = False
        else:
            print("Tienes que escribir un número")
    return rentaUser

def main():
    rentaUser = input("Escriba su renta anual: ")
    print("Le corresponde un tipo impositivo del " + rentaGrupo(rentaUser))



if __name__ == "__main__":
    main()