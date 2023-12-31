import matplotlib.pyplot as plt

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
    desplazamiento = int(input("Ingrese el desplazamiento para el cifrado César: "))
    texto_cifrado = ""
    for caracter in texto:
        if caracter.isalpha():
            ascii_offset = 65 if caracter.isupper() else 97
            indice = (ord(caracter) - ascii_offset + desplazamiento) % 26
            caracter_cifrado = chr(indice + ascii_offset)
            texto_cifrado += caracter_cifrado
        else:
            texto_cifrado += caracter
    return texto_cifrado

def analisis_frecuencia_caracteres(texto):
    frecuencia = {}
    for caracter in texto:
        if caracter in frecuencia:
            frecuencia[caracter] += 1
        else:
            frecuencia[caracter] = 1
    return frecuencia

def grafico_frecuencia_caracteres(texto):
    frecuencia = analisis_frecuencia_caracteres(texto)
    frecuencias_ordenadas = sorted(frecuencia.items(), key=lambda x: x[1], reverse=True)

    caracteres, frecuencias = zip(*frecuencias_ordenadas)

    plt.bar(caracteres, frecuencias)

    plt.xlabel('Caracteres')
    plt.ylabel('Frecuencia')
    plt.title('Frecuencia de Caracteres en el Texto (Ordenada)')

    plt.yticks(range(0, max(frecuencias) + 1))

    plt.show()

def menu_principal():
    while True:
        print("\nMenú Principal:")
        print("1. Contar caracteres específicos")
        print("2. Invertir el texto")
        print("3. Extraer substring")
        print("4. Reemplazar caracteres")
        print("5. Cifrado César Básico")
        print("6. Análisis de frecuencia de caracteres")
        print("7. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            print("El caracter aparece", contar_caracter(texto), "veces en el texto.")
        elif opcion == "2":
            print("Texto invertido:", invertir_texto(texto))
        elif opcion == "3":
            print("Texto extraído:", extraer_texto(texto))
        elif opcion == "4":
            print("Texto con caracteres reemplazados:", reemplazar_caracteres(texto))
        elif opcion == "5":
            print("Texto cifrado:", cifrado_cesar(texto))
        elif opcion == "6":
            grafico_frecuencia_caracteres(texto)
        elif opcion == "7":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor intente de nuevo.")

texto = input("Ingrese el texto que desea analizar: ")
menu_principal()