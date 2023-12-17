# Escribe un programa que cree diferentes listas (algunas vacías y otras no) y muestre el valor booleano de cada una.

def comprobador(dato):
    if bool(dato):
        print("La lista contiene datos")
    else:
        print("No hay datos en la lista")

lista = []
comprobador(lista)

lista.append(int(input("Ingresa un número: ")))
comprobador(lista)