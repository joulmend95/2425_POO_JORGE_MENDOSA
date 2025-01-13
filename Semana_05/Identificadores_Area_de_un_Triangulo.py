# Este programa calcula el área de un triángulo a partir de la base y la altura ingresadas por el usuario.
# Utiliza los tipos de datos string, float, y boolean. También valida que los datos sean correctos.

def calcular_area(base, altura):
    """
    Calcula el área de un triángulo.
    :param base: float, la base del triángulo.
    :param altura: float, la altura del triángulo.
    :return: float, el área calculada.
    """
    return (base * altura) / 2  # La fórmula del área de un triángulo es (base * altura) / 2

# Solicitar la base y altura del triángulo
try:
    # Convertir la entrada a float para permitir números decimales
    base = float(input("Ingresa la base del triángulo (en cm): "))  # base es un número decimal (float)
    altura = float(input("Ingresa la altura del triángulo (en cm): "))  # altura también es un número decimal (float)

    # Validar que la base y altura sean valores positivos (booleano)
    if base > 0 and altura > 0:  # Si ambas son mayores que cero, continuamos con el cálculo
        area = calcular_area(base, altura)  # Llamamos a la función para calcular el área
        # Mostramos el resultado con dos decimales
        print(f"\nEl área del triángulo con base {base} cm y altura {altura} cm es: {area:.2f} cm².")
    else:
        print("\nError: La base y la altura deben ser mayores que cero.")  # Mensaje de error si los valores no son positivos
except ValueError:
    # Si ocurre un error de valor (por ejemplo, el usuario ingresa texto en lugar de un número), se muestra este mensaje
    print("\nError: Por favor, ingresa valores numéricos válidos.")
