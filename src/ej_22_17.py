def sumarDigitos(numero):
    suma = 0
    while numero > 0:
        digito = numero % 10
        suma += digito
        numero //= 10
    return suma

def main():
    numero = int(input("Escribe un número entero positivo: "))
    resultado = sumarDigitos(numero)
    print(f"La suma de los dígitos de {numero} es: {resultado}")

if __name__ == "__main__":
    main()
