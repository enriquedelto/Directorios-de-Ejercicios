# Crea una función que tome un número como argumento y retorne True si el número es par y False si es impar.

def comprobador(numero):
    if numero % 2 == 0:
        print("El número es par")
    else:
        print("El número es impar")

numero = int(input("Ingrese un número: "))
comprobador(numero)