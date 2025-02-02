import os  # Se Importa el módulo os para trabajar con rutas y archivos del sistema operativo

# Se crea una función para mostrar el contenido de un archivo Python
def mostrar_codigo(ruta_script):
    # Convierte la ruta del script en una ruta absoluta para evitar errores de ubicación
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        # Se abre el archivo en modo lectura con codificación UTF-8
        with open(ruta_script_absoluta, 'r', encoding='utf-8') as archivo:
            print(f"\n--- Código de {ruta_script} ---\n")  # Imprime el título del código a mostrar
            print(archivo.read())  # Lee y muestra el contenido del archivo
    except FileNotFoundError:
        #  Con esto se captura el error si el archivo no se encuentra
        print("El archivo no se encontró.")
    except Exception as e:
        # Captura cualquier otro error inesperado
        print(f"Ocurrió un error al leer el archivo: {e}")

# Función para mostrar el menú principal del dashboard
def mostrar_menu():
    # Obtiene la ruta base del archivo actual (dashboard.py)
    ruta_base = os.path.dirname(__file__)

    # Diccionario con las opciones del menú, asociadas a rutas de scripts
    opciones = {
        '1': 'Semana_02/Abstraccion/Tecnicas_de_Programación_Abstraccion.py',
        '2': 'Semana_02/Encapsulamiento/Tecnicas_de_Programacion_Encapsulamiento.py',
        '3': 'Semana_02/Herencia/Tecnicas_de_Programacion_Herencia.py',
        '4': 'Semana_02/Polimorfismo/Tecnicas_de_Programación_Polimorfismo.py',
        '5': 'Semana_03/Programacion_POO.py',
        '6': 'Semana_03/Programacion_Tradicional.py',
        '7': 'Semana_04/EjemplosMundoReal_POO/Ejemplo_Atributos_clase.py',
        '8': 'Semana_04/EjemplosMundoReal_POO/Ejemplo_Motocicleta_y_Acciones.py',
        '9': 'Semana_05/Identificadores_Area_de_un_Triangulo.py',
        '10': 'Semana_06/Clases_Objetos_Herencia_Encapsulamiento_Polimorfismo.py',
        '11': 'Semana_07/Constructores_y_destructores_Clase_archivo.py',
    }

    while True:  # Un bucle infinito hasta que el usuario decida salir
        print("\n********Menu Principal - Dashboard*************")
        # Muestra las opciones disponibles en el menú
        for key in opciones:
            print(f"{key} - {opciones[key]}")
        print("0 - Salir")  # Opción para salir del menú

        # Se solicita al usuario que elija una opción
        eleccion = input("Elige un script para ver su código o '0' para salir: ")

        if eleccion == '0':  # Si elige '0', se sale del bucle
            break
        elif eleccion in opciones:
            # Combina la ruta base con la ruta del script seleccionado
            ruta_script = os.path.join(ruta_base, opciones[eleccion])
            mostrar_codigo(ruta_script)  # Llama a la función para mostrar el código
        else:
            # Si la opción no es válida, muestra un mensaje de error
            print("Opción no válida. Por favor, intenta de nuevo.")

# Punto de entrada del programa
if __name__ == "__main__":
    mostrar_menu()  # Llama a la función principal para iniciar el menú
