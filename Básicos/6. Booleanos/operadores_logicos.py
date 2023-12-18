# Escribe un programa que pida al usuario ingresar dos booleanos y luego muestre el resultado de las operaciones lógicas AND, OR y NOT aplicadas a estos valores.

# AND: Devuelve "True" si ambos operandos son "True".
# OR: Devuelve "True" si al menos uno de los operandos es "True".
# NOT: Invierte el valor del operando.

def solicitar_booleano(mensaje):
    valor = input(mensaje).strip().lower()
    if valor in ["true", "false"]:
        return valor == "true"
    print("Porfavor, ingresa 'True' o 'False'.")

booleano1 = solicitar_booleano("Ingresa el primer valor booleano (True/False): ")
booleano2 = solicitar_booleano("Ingresa el segundo valor booleano (True/False): ")

print(f"{booleano1} AND {booleano2} = {booleano1 and booleano2}")
print(f"{booleano1} OR {booleano2} = {booleano1 or booleano2}")
print(f"NOT {booleano1} = {not booleano1}")
print(f"NOT {booleano2} = {not booleano2}")