# Importación del MÓDULO datetime para trabajar con fechas
import datetime

# BLOQUE try-except para manejar errores de entrada
try:
    # Se solicita al usuario ingresar su año de nacimiento mediante la FUNCIÓN input y se convierte a entero mediante la FUNCIÓN int(), para luego pasar el dato a la VARIABLE año_de_nacimiento.
    año_de_nacimiento = int(input("Ingrese su año de nacimiento: "))
    
    # La FUNCIÓN today() del MÓDULO datetime se utiliza para obtener la fecha actual, y se extrae el año mediante la PROPIEDAD year, asignándolo a la VARIABLE año_actual.
    año_actual = datetime.date.today().year

    # Estructura condicional IF-ELIF-ELSE para validar el año de nacimiento.
    # El PRIMER IF comprueba si el año de nacimiento es mayor que el año actual.
    if año_de_nacimiento > año_actual:
        # Se muestra un mensaje de error si el año ingresado es mayor que el año actual.
        print("Ha ingresado un año de nacimiento en el futuro. Por favor, ingrese un año válido.")
    # ELIF para comprobar si la edad calculada es mayor a 116 años.
    elif año_actual - año_de_nacimiento > 116:
        # Se muestra un mensaje si la edad calculada es irrazonablemente alta.
        print("La edad ingresada no parece ser válida.")
    # ELSE se ejecuta si ninguna de las condiciones anteriores es verdadera.
    else:
        # Se calcula la edad restando el año de nacimiento del año actual y se muestra el resultado.
        print(f"Su edad actual es: {año_actual - año_de_nacimiento}")
# EXCEPT para capturar un ValueError, que ocurre si la entrada no puede convertirse a entero.
except ValueError:
    # Se muestra un mensaje de error si la entrada no es un número válido.
    print("Por favor, ingrese un número válido para el año de nacimiento.")