
def comproPunt(puntos):
    if puntos == 0.0 or puntos == 0.4 or puntos >= 0.6:
        return True
    else:
        return False
    
def obtenerBeneficio(puntos):
    return int(2400 * puntos)


def obtenerNivel(puntos):
    resultado = ""
    if puntos == 0.0:
        resultado = "Inaceptable"
    elif puntos == 0.4:
        resultado = "Aceptable"
    else:
        resultado = "Meritorio"
    
    resultado += " - " + str(obtenerBeneficio(puntos))
    return resultado

def main():
    puntos = float(input("Introduzca su evaluación: "))
    if comproPunt(puntos) == True:
        print("Su resultado es " + obtenerNivel(puntos) + "€")
    else:
        print("*Error* puntos de la evaluación no válidos")

if __name__ == "__main__":
    main()