def analizar_tiempo(tiempo_str):
    try:
        partes = tiempo_str.split(':')
        if len(partes) == 3:
            horas = int(partes[0])
            minutos = int(partes[1])
            segundos = int(partes[2])
            return horas, minutos, segundos
    except ValueError:
        pass 
    raise ValueError("Formato de tiempo no válido. Debe ser en formato 00:00:00.") 

try:
    tiempo_competidor_1_str = input("Ingresa el tiempo de finalización del corredor nº 1 (en formato 00:00:00): ")
    tiempo_competidor_2_str = input("Ingresa el tiempo de finalización del corredor nº 2 (en formato 00:00:00): ")

    tiempo_competidor_1 = analizar_tiempo(tiempo_competidor_1_str)
    tiempo_competidor_2 = analizar_tiempo(tiempo_competidor_2_str)

    tiempo_competidor_1_seg = tiempo_competidor_1[0] * 3600 + tiempo_competidor_1[1] * 60 + tiempo_competidor_1 [2]
    tiempo_competidor_2_seg = tiempo_competidor_2[0] * 3600 + tiempo_competidor_2[1] * 60 + tiempo_competidor_2 [2] 

    diferencia = abs(tiempo_competidor_1_seg - tiempo_competidor_2_seg)

    print(f"El competidor 1 finalizó la carrera en: {tiempo_competidor_1_str}")
    print(f"El competidor 2 finalizó la carrera en: {tiempo_competidor_2_str}")
    print(f"La diferencia temporal entre los resultados ha sido de {diferencia} segundos.")

except ValueError as e:
    print(e)