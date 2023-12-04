# Crea una lista con varios ítems de compras, luego agrega, elimina y modifica elementos en la lista.

def print_lista():
    print(f"Lista de la compra actual: {', '.join(lista)}")

lista = ["manzana", "platano", "sandia"]
print_lista()

agregado = input("Ingresa un nuevo item: ")
lista.append(agregado)
print_lista()

eliminado = input("Elimina un item: ")
if eliminado in lista:
    lista.remove(eliminado)
else:
    print(f"El ítem '{eliminado}' no se encuentra en la lista.")
print_lista()

elemento_a_modificar = input("Ingresa el elemento que deseas modificar: ")
if elemento_a_modificar in lista:
    indice = lista.index(elemento_a_modificar)
    nuevo_item = input("Ingresa el elemento sustituto: ")
    lista[indice] = nuevo_item
else:
    print(f"El ítem '{elemento_a_modificar}' no se encuentra en la lista.")
print_lista()