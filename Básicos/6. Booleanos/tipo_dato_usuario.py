# Escribe un programa que tome un input del usuario, evalúe si es un número (int) o una cadena (str) y muestre el resultado booleano.

def comprobador(dato):
    try:
        int(dato)
        print("El dato ingresado es un número entero (integer).")
    except ValueError:
        print("El dato ingresado es una cadena de texto (string).")

input_usuario = (input("Introduzca una letra o número: "))

comprobador(input_usuario)