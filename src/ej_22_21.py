def descuentoCompras():
    totalCompras = 0
    while True:
        monto = float(input("Escribe el monto de la compra (0 para terminar): "))
        if monto == 0:
            break
        if monto < 0:
            print("El monto no puede ser negativo. Inténtelo nuevamente.")
        else:
            totalCompras += monto
    if totalCompras > 1000:
        totalCompras -= (totalCompras * 0.10)
    return totalCompras

def main():
    resultado = descuentoCompras()
    print(f"Total a pagar: ${resultado:.2f}")

if __name__ == "__main__":
    main()
