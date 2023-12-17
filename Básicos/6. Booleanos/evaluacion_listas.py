# Escribe un programa que cree diferentes listas (algunas vacías y otras no) y muestre el valor booleano de cada una.

def comprobador(dato):
    if bool(dato) == False:
        print("No hay datos en la lista")
    else:
        print("La lista contiene datos")

lista = []
comprobador(lista)

lista.append(int(input("Ingresa un número: ")))
comprobador(lista)