dni = str(input("Por favor ingrese su DNI: "))
longitud = len(dni)

if longitud > 9:
    print("El DNI ingresado parece tener más caracteres de los válidos")
elif longitud < 9:
    print("El DNI ingresado parece tener menos caracteres de los válidos")
else:
    print("La longitud del DNI es correcta")

letra_verificador = ["T", "R", "W", "A", "G", "M", "Y", "F", "P", "D", "X", "B", "N", "J", "Z", "S", "Q", "V", "H", "L", "C", "K", "E"]

dni_numeros = ""
dni_letra = ""

for dni_caracter in dni:
    if dni_caracter.isdigit():
        dni_numeros += dni_caracter
    elif dni_caracter.isalpha():
        dni_letra += dni_caracter

dni_numeros_int = int(dni_numeros)
indice_letra = dni_numeros_int % 23

if letra_verificador[indice_letra] == dni_letra:
    print("La letra del DNI es válida")
else:
    print("La letra del DNI no es válida")