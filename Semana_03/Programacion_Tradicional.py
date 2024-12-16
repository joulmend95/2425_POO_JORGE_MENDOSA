# Función para ingresar temperaturas
def ingresar_temperaturas():
    # Lista vacía para almacenar las temperaturas
    temperaturas = []
    print("Ingrese las temperaturas diarias de la semana:")

    # Bucle para solicitar las temperaturas de 7 días
    for i in range(7):
        no_es_un_numero = True  # Bandera para controlar la validación de entrada
        while no_es_un_numero:
            # Solicita la entrada del usuario para cada día
            entrada = input(f"Temperatura del día {i + 1}: ")

            # Verifica si la entrada es válida:
            # - No está vacía
            # - Es un número (permite un solo punto decimal)
            if entrada == "" or not entrada.replace('.', '', 1).isdigit():
                print("Ingrese un número válido.")  # Mensaje de error si no es válido
            else:
                # Convierte la entrada en un número decimal (float)
                temperatura = float(entrada)
                no_es_un_numero = False  # Entrada válida, salimos del bucle

        # Agrega la temperatura válida a la lista
        temperaturas.append(temperatura)

    # Devuelve la lista completa de temperaturas
    return temperaturas


# Función para calcular el promedio de una lista de temperaturas
def promedio_temperaturas(temperaturas):
    suma = 0  # Variable para almacenar la suma de las temperaturas

    # Suma todas las temperaturas en la lista
    for temperatura in temperaturas:
        suma += temperatura

    # Calcula el promedio dividiendo la suma entre el número de elementos
    promedio = suma / len(temperaturas)

    # Devuelve el promedio
    return promedio


# Flujo principal del programa
# Llama a la función para ingresar las temperaturas
temperaturas = ingresar_temperaturas()

# Calcula el promedio con la función
promedio = promedio_temperaturas(temperaturas)

# Muestra el promedio en la consola con dos decimales de precisión
print(f"Promedio de las temperaturas es: {promedio:.2f}")


