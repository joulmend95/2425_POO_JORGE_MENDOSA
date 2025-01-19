# Clase vehiculo

class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.__modelo = modelo  #atributo privado, encapsulación.

    # Clase Vehiculo: Clase base para vehículos con los atributos comunes
    class Vehiculo:
        def __init__(self, marca, modelo):
            # Inicializa los atributos marca y modelo, siendo el modelo privado (encapsulado)
            self.marca = marca
            self.__modelo = modelo  # Atributo privado

        def obtener_modelo(self):
            # Método para acceder al atributo privado __modelo
            return self.__modelo

        def descripcion(self):
            # Método de descripción básica que devuelve el modelo y la marca del vehículo
            return f"Modelo: {self.__modelo}, Marca: {self.marca}"





    # Clase Auto: Hereda de Vehiculo y agrega un atributo específico (puertas)
    class Auto(Vehiculo):
        def __init__(self, marca, modelo, puertas):
            # Llama al constructor de Vehiculo para inicializar marca y modelo
            super().__init__(marca, modelo)
            self.puertas = puertas  # Atributo específico de los autos

        def descripcion(self):  # Polimorfismo: sobrescribe el método descripcion
            # Devuelve una descripción más específica para el auto, incluyendo las puertas
            return f"Marca: {self.marca}, Modelo: {self.obtener_modelo()}, Puertas: {self.puertas}"






    # Clase Moto: Hereda de Vehiculo y agrega un atributo específico (cilindraje)
    class Moto(Vehiculo):
        def __init__(self, marca, modelo, cilindraje):
            # Llama al constructor de Vehiculo para inicializar marca y modelo
            super().__init__(marca, modelo)
            self.cilindraje = cilindraje  # Atributo específico de las motos

        def descripcion(self):  # Polimorfismo: sobrescribe el método descripcion
            # Devuelve una descripción más específica para la moto, incluyendo el cilindraje
            return f"Marca: {self.marca}, Modelo: {self.obtener_modelo()}, Cilindraje: {self.cilindraje}"

    # Función que recibe un objeto de tipo Vehiculo y llama a su método descripcion
    def mostrar_descripcion(vehiculo):
        print(vehiculo.descripcion())  # Muestra la descripción del vehículo, sea auto o moto



    # Creación de objetos de tipo Vehiculo, Auto y Moto
    vehiculo = Vehiculo("Chevrolet", "Veloz")  # Vehículo genérico
    auto = Auto("Chevrolet", "Optra", "5 puertas")  # Objeto de tipo Auto
    moto = Moto("Bajaj", "Pulsar", "200 cc")  # Objeto de tipo Moto


    # Mostrar la encapsulación: acceder al atributo privado __modelo a través del método obtener_modelo
    print(vehiculo.obtener_modelo())  # Imprime el modelo del vehículo (Veloz)


    # Mostrar el polimorfismo con objetos más específicos
    mostrar_descripcion(auto)  # Llama al método descripcion sobrescrito para Auto
    mostrar_descripcion(moto)  # Llama al método descripcion sobrescrito para Moto

