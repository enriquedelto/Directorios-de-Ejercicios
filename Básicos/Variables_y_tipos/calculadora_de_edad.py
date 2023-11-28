# Pregunta al usuario su año de nacimiento y calcula su edad actual

import datetime #Se importa una libreria que extrae la fecha actual del sistema

try: #Se abre el bloque try-except para manejar posibles errores al ingresar datos con formatos nó validos
    año_de_nacimiento = int(input("Ingrese su año de nacimiento: ")) #Se crea una variable entera con un input que ingresa el usuario tras realizar una pregunta.
    año_actual = datetime.date.today().year #Se extrae el dato de la fecha actual y se ingresa a la variable año_actual
        #Comienza un "no se" que comprueba si la fecha ingresada aún siendo un formato correcto es un año de nacimiento razonable.
    if año_de_nacimiento > año_actual:
        print("Ha ingresado un año de nacimiento en el futuro. Por favor, ingrese un año válido.")
    elif año_actual - año_de_nacimiento > 116:
        print("La edad ingresada no parece ser válida.")
    else:
        print(f"Su edad actual es: {año_actual - año_de_nacimiento}")
except ValueError:
    print("Por favor, ingrese un número válido para el año de nacimiento.")