# Utiliza el método format para insertar varias variables en una cadena. Por ejemplo, crea una oración que incluya el nombre del usuario, su ciudad y su comida favorita.

nombre = str(input("Ingrese su nombre: "))
ciudad = str(input("Ingrese su ciudad: "))
comida_fav = str(input("Ingrese su comida favorita: "))

print("Tu nombre es {fnombre}, vives en {fciudad} y tu comida favorita es {fcomida_fav}".format(fnombre = nombre, fciudad = ciudad, fcomida_fav = comida_fav))

print(f"Tu nombre es {nombre}, vives en {ciudad} y tu comida favorita es {comida_fav}") # MEJOR FORMATO