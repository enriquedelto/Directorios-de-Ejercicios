import random

num_dados = input("¿Cuantos dados quieres lanzar?")
num_dados_int = int(num_dados)
suma_total = 0

for i in range(num_dados_int):
    lados = int(input(f"¿Cuántos lados tiene el dado {i+1}? "))

    resultado = random.randint(1, lados)
    suma_total += resultado
    print(f"Resultado del dado {i+1}: {resultado}")

# Muestra el resultado total
print(f"Suma total de los dados: {suma_total}")