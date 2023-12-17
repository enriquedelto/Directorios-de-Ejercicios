# Escribe un programa que tome un input del usuario, evalúe si es un número (int) o una cadena (str) y muestre el resultado booleano (USANDO el método isnumeric())

def comprobador(dato):
    if dato.isnumeric():
        print("El dato es un número")
    else:
        print("El dato es una cadena de texto: ")

input_usuario = input("Ingrese un número o texto: ")
comprobador(input_usuario)