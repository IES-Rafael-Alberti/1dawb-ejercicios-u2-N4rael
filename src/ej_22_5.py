def calcularInversion(cantidad, interes, años):
    for i in range(años):
        cantidad *= 1 + interes / 100
        print(f"Año {i + 1}: {cantidad:.2f} euros")

def main():
    cantidad = float(input("Escriba la cantidad a invertir: "))
    interes = float(input("Escribe el interés anual: "))
    años = int(input("Escribe el número de años: "))
    calcularInversion(cantidad, interes, años)

if __name__ == "__main__":
    main()
