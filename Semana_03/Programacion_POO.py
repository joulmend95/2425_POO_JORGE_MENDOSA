# Clase que representa el clima con una temperatura
class Clima:
    # El método __init__ inicializa el objeto con una temperatura
    def __init__(self, temperatura):
        self.temperatura = temperatura  # Atributo de la clase que almacena la temperatura

    # Método para obtener la temperatura
    def get_temperatura(self):
        return self.temperatura

    # Método para mostrar la temperatura de forma legible
    def mostrar_clima(self):
        print(f"Temperatura: {self.temperatura}°C")


# Clase que representa el pronóstico del tiempo
class Pronostico_Tiempo:
    # El método __init__ inicializa una lista vacía para almacenar los objetos de clima
    def __init__(self):
        self.climas = []  # Lista que almacenará instancias de la clase Clima

    # Método para ingresar las temperaturas de los 7 días de la semana
    def ingresar_temperaturas(self):
        print("Ingrese las temperaturas diarias de la semana:")
        # Bucle para pedir las temperaturas de los 7 días
        for i in range(7):
            no_es_un_numero = True  # Bandera para controlar la validez de la entrada
            while no_es_un_numero:
                entrada = input(f"Temperatura del día {i + 1}: ")
                # Verifica si la entrada es válida (número decimal o entero)
                if entrada == "" or not entrada.replace('.', '', 1).isdigit():
                    print("Ingrese un número válido.")
                else:
                    temperatura = float(entrada)  # Convierte la entrada a un número flotante
                    clima = Clima(temperatura)  # Crea una instancia de la clase Clima con la temperatura
                    no_es_un_numero = False  # Entrada válida, salimos del bucle
            self.climas.append(clima)  # Añade la instancia de Clima a la lista
        return self.climas  # Devuelve la lista con los objetos de clima

    # Método para calcular el promedio de las temperaturas
    def promedio_temperaturas(self, climas):
        suma = 0  # Variable para acumular la suma de las temperaturas
        # Itera sobre la lista de objetos 'Clima' sumando sus temperaturas
        for clima in climas:
            suma += clima.get_temperatura()  # Obtiene la temperatura del objeto y la suma
        promedio = suma / len(climas)  # Calcula el promedio
        return promedio  # Devuelve el promedio de las temperaturas


# Crear una instancia de la clase Pronostico_Tiempo
pronostico = Pronostico_Tiempo()

# Llamar al método para ingresar las temperaturas
climas_ingresados = pronostico.ingresar_temperaturas()

# Llamar al método para calcular el promedio de las temperaturas
promedio = pronostico.promedio_temperaturas(climas_ingresados)

# Mostrar el promedio de las temperaturas en formato de dos decimales
print(f"El promedio de las temperaturas es: {promedio:.2f}")
