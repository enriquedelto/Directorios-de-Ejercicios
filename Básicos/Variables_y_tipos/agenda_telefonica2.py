def agregar_numero(agenda_telefonica):
    numero = input("Ingrese el número de telefono del contacto: ")
    nombre = input("Ingrese el nombre del contacto: ")
    agenda_telefonica[numero] = nombre
    print(f"El número de {nombre} ha sido agregado: \"{numero}\"")

def eliminar_numero(agenda_telefonica):
    numero_eliminar = input("Ingrese el número que desea eliminar: ")
    if numero_eliminar in agenda_telefonica:
        del agenda_telefonica[numero_eliminar]
    else:
        print("El número ingresado no se encuentra en la lista, intentelo de nuevo bobo")
    
agenda = {}

while True:
    print("1. Agregar número")
    print("2. Eliminar número")
    print("3. Modificar número")
    print("4. Ver lista")
    print("5. Salir")
    opcion = input("Seleciona la opción que deseas ejecutar: ")
    if opcion == 1:
        agregar_numero(agenda)
    elif opcion == 2:
        eliminar_numero(agenda)
    elif opcion == 3:
        modificar_numero(agenda)
    elif opcion == 4:
        ver_lista(agenda)
    elif opcion == 5:
        
    else:
