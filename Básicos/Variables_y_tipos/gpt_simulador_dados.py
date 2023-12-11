from itertools import product

def calcular_probabilidad_dados(num_dados, suma_total):
    dados = []

    # Solicitar al usuario el número de caras para cada dado
    for i in range(num_dados):
        lados = int(input(f"¿Cuántos lados tiene el dado {i + 1}? "))
        dados.append(lados)

    probabilidad_resultado = 0

    # Calcular la probabilidad
    for combo in product(*[range(1, lados + 1) for lados in dados]):
        if sum(combo) == suma_total:
            probabilidad_resultado += 1

    # Calcular el número total de combinaciones posibles
    numero_combinaciones_posibles = 1
    for lados in dados:
        numero_combinaciones_posibles *= lados

    # Calcular la probabilidad final
    probabilidad_resultado /= numero_combinaciones_posibles
    probabilidad_resultado *= 100  # Convertir a porcentaje

    return probabilidad_resultado

# Ejemplo de uso
num_dados = int(input("¿Cuántos dados quieres lanzar?"))
suma_total = int(input("¿Qué suma total estás buscando?"))

probabilidad = calcular_probabilidad_dados(num_dados, suma_total)
print(f"Probabilidad del resultado total {suma_total}: {probabilidad:.2f}%")
