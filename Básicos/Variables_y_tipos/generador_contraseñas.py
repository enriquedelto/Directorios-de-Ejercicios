import random

print("¡Bienvenido al creador de contraseñas!")
parte_1 = input("Por favor, ingresa una palabra que te resulte graciosa para comenzar como por ejemplo: \"Garbanzo\": ")
print("!Genial, ahora estaría genial repetir un par de monosílabos como por ejemplo: ñaña o tutu ")
parte_2 = input ("Porfi, ingresa la nobería esa jaja a ver como queda: ")
print(f"!Estupendo, ahora la contraseña es: {parte_1}{parte_2}")
print(f"Ahora necesitamos darle más vida la password con caracteres especiales")
print("Voy a generar unos caracteres aleatorios para hacer de la contraseña una supercontraseña")
caracteres_especiales = "!@#$%^&*()-_+={}[]|:;'\"<>,.?/ñ"
cadena_aleatoria = ''.join(random.choice(caracteres_especiales) for _ in range (2))
print(f"La contraseña ha quedado tal que así: {parte_1}{parte_2}{cadena_aleatoria}ñ")
print("Te gusta si o no ;P")