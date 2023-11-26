# Pregunta al usuario su año de nacimiento y calcula su edad actual

import datetime

año_de_nacimiento = int(input("Ingrese su año de nacimiento: "))
año_actual = datetime.date.today().year

print(f"Su edad actual es: {año_actual - año_de_nacimiento}")