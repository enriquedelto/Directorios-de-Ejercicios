tiempo_competidor_1 = int(input("Ingresa el tiempo de finalización del corredor nº 1: "))
tiempo_competidor_2 = int(input("Ingresa el tiempo de finalización del corredor mº 2: "))
diferencia = int(abs(tiempo_competidor_1 - tiempo_competidor_2))

print(f"El competidor 1 finalizó la carrera en: {tiempo_competidor_1}")
print(f"El competidor 2 finalizó la carrera en: {tiempo_competidor_2}")
print(f"La diferencia temporal entre los resultados ha sido de {diferencia}")