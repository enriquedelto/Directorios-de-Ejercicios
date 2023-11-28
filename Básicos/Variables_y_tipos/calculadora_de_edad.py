# Pregunta al usuario su año de nacimiento y calcula su edad actual

import datetime

año_de_nacimiento = int(input("Ingrese su año de nacimiento: "))
año_actual = datetime.date.today().year

if año_de_nacimiento > año_actual:
    print("Ha ingresado un año de nacimiento en el futuro. Por favor, ingrese un año válido.")
elif año_actual - año_de_nacimiento > 116:
    print("La edad ingresada no parece ser válida.")
else:
    print(f"Su edad actual es: {año_actual - año_de_nacimiento}")