def contar_caracter(texto):
    caracter = input("Ingrese el caracter que desea contar: ")
    contador = 0
    for x in texto:
        if x == caracter:
            contador += 1
    return contador

def invertir_texto(texto):
    return texto[::-1]

texto = input("Por favor ingresa el texto que desea analizar: ")
print("El caracter aparece", contar_caracter(texto), "veces en el texto.")
print("Texto invertido:", invertir_texto(texto))

'''
print("1. Contar caracteres específicos")
print("2. Invertir el texto")
print("3. Extraer substring")
print("4. Reemplazar caracteres")
print("5. Cifrado César Básico")
print("6 Análisis de frecuencia de caracteres")
'''