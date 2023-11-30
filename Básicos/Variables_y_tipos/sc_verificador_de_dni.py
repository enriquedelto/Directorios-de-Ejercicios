dni = str(input("Por favor ingrese su DNI: "))
longitud = len(dni)

if longitud > 8:
    print("El DNI ingresado parece tener más caracteres de los válidos")
elif longitud < 8:
    print("El DNI ingresado parece tener menos caracteres de los válidos")
else:
    print("La longitud del DNI es correcta")

print(longitud)