def convertir_a_segundos(horas, minutos, segundos):
    return horas * 3600 + minutos * 60 + segundos

def analizar_tiempo(tiempo_str):
    try:
        partes = tiempo_str.split(':')
        if len(partes) == 3:
            horas = int(partes[0])
            minutos = int(partes[1])
            segundos = int(partes[2])
            
            if not (0 <= horas < 24):
                raise ValueError("La hora debe estar entre 0 y 23.")
            if not (0 <= minutos < 60):
                raise ValueError("Los minutos deben estar entre 0 y 59.")
            if not (0 <= segundos < 60):
                raise ValueError("Los segundos deben estar entre 0 y 59.")
            
            return horas, minutos, segundos
    except ValueError as e:
        raise ValueError(e)

try:
    tiempo_competidor_1_str = input("Ingresa el tiempo de finalización del corredor nº 1 (en formato hh:mm:ss): ")
    tiempo_competidor_2_str = input("Ingresa el tiempo de finalización del corredor nº 2 (en formato hh:mm:ss): ")

    tiempo_competidor_1 = analizar_tiempo(tiempo_competidor_1_str)
    tiempo_competidor_2 = analizar_tiempo(tiempo_competidor_2_str)

    tiempo_competidor_1_seg = convertir_a_segundos(*tiempo_competidor_1)
    tiempo_competidor_2_seg = convertir_a_segundos(*tiempo_competidor_2)

    diferencia = abs(tiempo_competidor_1_seg - tiempo_competidor_2_seg)

    print(f"El competidor 1 finalizó la carrera en: {tiempo_competidor_1_str}")
    print(f"El competidor 2 finalizó la carrera en: {tiempo_competidor_2_str}")
    print(f"La diferencia temporal entre los resultados ha sido de {diferencia} segundos.")

except ValueError as e:
    print(e)