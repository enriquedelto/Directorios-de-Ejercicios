# Crea una lista con varios ítems de compras, luego agrega, elimina y modifica elementos en la lista.

def print_lista():
    print(f"Lista de la compra actual: {', '.join(lista)}")

lista = ["manzana", "platano", "sandia"]
print_lista()

agregado = str(input("Ingresa un nuevo item: "))
lista.append(agregado)

print_lista()

eliminado = str(input("Elimina un item: "))
lista.remove(eliminado)

print_lista()