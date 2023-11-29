# Pide al usuario que ingrese un número de punto flotante y redondéalo a dos decimales.

num_dec = float(input("Ingresa un número decimal de más de 2 decimales: "))
num_dec = round(num_dec, 2)
print(num_dec)