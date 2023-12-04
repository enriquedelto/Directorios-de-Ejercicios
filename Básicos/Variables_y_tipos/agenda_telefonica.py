def agregar_contacto(agenda_telefonica):

    pass

def eliminar_contacto(agenda_telefonica):

    pass

def editar_contacto(agenda_telefonica):

    pass

def ver_lista(agenda_telefonica):

    pass

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