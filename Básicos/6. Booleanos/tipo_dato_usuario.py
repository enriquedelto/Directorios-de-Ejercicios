# Escribe un programa que tome un input del usuario, evalúe si es un número (int) o una cadena (str) y muestre el resultado booleano.

def comprobador(input):
    if type(input) == str:
        print("El dato ingresado es un string")
    elif type(input) == int:
        print("El dato ingresado es un integrer")
    else:
        print("El dato ingresado no es ni cadena de texto ni número entero.")

input = (input("Introduzca una letra o número: "))

comprobador(input)