def analizar_tiempo(tiempo_str):
    try:
        partes = tiempo_str.split(':')
        if len(partes) == 3:
            horas = int(partes[0])
            minutos = int(partes[1])
            segundos = int(partes[2])
            return horas, minutos, segundos #¿?
    except ValueError:
        pass #¿?
    raise ValueError("Formato de tiempo no válido. Debe ser en formato 00:00:00.") # ¿?


try:
    tiempo_competidor_1 = int(input("Ingresa el tiempo de finalización del corredor nº 1: "))
    tiempo_competidor_2 = int(input("Ingresa el tiempo de finalización del corredor nº 2: "))

    diferencia = abs(tiempo_competidor_1 - tiempo_competidor_2)

    print(f"El competidor 1 finalizó la carrera en: {tiempo_competidor_1}")
    print(f"El competidor 2 finalizó la carrera en: {tiempo_competidor_2}")
    print(f"La diferencia temporal entre los resultados ha sido de {diferencia}")

except ValueError:
    print("Error: Debes ingresar valores enteros para los tiempos de finalización.")