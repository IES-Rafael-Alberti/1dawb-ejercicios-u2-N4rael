def calcularInversion(cantidad, interes, años):
    resultado = []
    for i in range(años):
        cantidad *= 1 + interes / 100
        resultado.append((i + 1, cantidad))
    return resultado
     

def main():
    cantidad = float(input("Escriba la cantidad a invertir: "))
    interes = float(input("Escribe el interés anual: "))
    años = int(input("Escribe el número de años: "))
    resultado = calcularInversion(cantidad, interes, años)

    for años, cantidad in resultado:
        print(f"Año {años}: {cantidad:.2f} euros")

if __name__ == "__main__":
    main()
