# Comparar dos números dados y muestre si el primero es mayor, igual o menor que el segundo

def comparador(primer_num, segundo_num):
    if primer_num > segundo_num:
        print("El primer número es mayor que el segundo")
    elif primer_num == segundo_num:
        print("Los números son iguales")
    else:
        print("El primer número es menor que el segundo")
try:
    primer_num = float(input("Ingrese un primer número: "))
    segundo_num = float(input("Ingrese el segundo número: "))
    comparador(primer_num, segundo_num)
except ValueError:
    print("Por favor, ingrese números válidos.")