def agregar_contacto(agenda_telefonica):
    nombre = input("Ingrese el nombre del contacto: ")
    numero = input("Ingrese el número de teléfono: ")
    agenda_telefonica[nombre] = numero
    print(f"Contacto {nombre} agregado.")

def eliminar_contacto(agenda_telefonica):
    print("¿Qué contacto de la agenda desea eliminar?")
    print(agenda_telefonica)
    nombre = input("Ingrese el nombre del contacto a eleminar: ")
    if nombre in agenda_telefonica:
        del agenda_telefonica[nombre]

def editar_contacto(agenda_telefonica):
    nombre = input("Ingrese el nombre del contacto a editar: ")
    if nombre in agenda_telefonica:
        numero_nuevo = input("Ingrese el nuevo número del contacto: ")
        agenda_telefonica[nombre] = numero_nuevo
        print("Contacto actualizado.")
    else:
        print("Contacto no encontrado.")

def ver_lista(agenda_telefonica):
    if agenda_telefonica:
        for nombre, numero in agenda_telefonica.items():
            print(f"Contacto: {nombre}, Número: {numero}")
    else:
        print("La agenda está vacía.")

agenda_telefonica = {}

while True:
    print("1. Agregar contacto")
    print("2. Eliminar contacto")
    print("3. Editar contacto")
    print("4. Ver lista de contactos")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        agregar_contacto(agenda_telefonica)
    elif opcion == "2":
        eliminar_contacto(agenda_telefonica)
    elif opcion == "3":
        editar_contacto(agenda_telefonica)
    elif opcion == "4":
        ver_lista(agenda_telefonica)
    elif opcion == "5":
        print("Saliendo de la agenda...")
        break
    else:
        print("Opción no válida. Intente de nuevo")