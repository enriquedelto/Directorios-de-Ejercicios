def contar_caracter(texto):
    caracter = input("Ingrese el caracter que desea contar: ")
    contador = 0
    for x in texto:
        if x == caracter:
            contador += 1
    return contador

def invertir_texto(texto):
    return texto[::-1]

def extraer_texto(texto):
    print("Selecione cómo desea extraer el texto:")
    print("1. Ingresando la palabra a extraer")
    print("2. Especificando el rango de índices para extraer (inicio y fin)")
    opcion = input("Opción: ")
    if opcion == "1":
        palabra_extraer = input("Ingrese la palabra que desea extraer: ")
        indice = texto.find(palabra_extraer)
        if indice != -1:
            return texto[indice:indice+len(palabra_extraer)]
        else:
            return "Palabra no encontrada"
    elif opcion == "2":
        inicio = int(input("Índice de inicio: "))
        fin = int(input("Índice de fin: "))
        return texto[inicio:fin]
    else:
        return "Opción no válida"

def reemplazar_caracteres(texto):
    caracter_a_reemplazar = input("Ingrese el caracter que desea reemplazar: ")
    nuevo_caracter = input("Ingrese el nuevo caracter: ")
    texto_reemplazado = texto.replace(caracter_a_reemplazar, nuevo_caracter)
    return texto_reemplazado
            
def cifrado_cesar(texto):



texto = input("Ingrese el texto que desea analizar: ")
print("El caracter aparece", contar_caracter(texto), "veces en el texto.")
print("Texto invertido:", invertir_texto(texto))
print("Texto extraído: ", extraer_texto(texto))
print("Texto con caracteres reemplazados:", reemplazar_caracteres(texto))

'''
print("1. Contar caracteres específicos")
print("2. Invertir el texto")
print("3. Extraer substring")
print("4. Reemplazar caracteres")
print("5. Cifrado César Básico")
print("6 Análisis de frecuencia de caracteres")
'''