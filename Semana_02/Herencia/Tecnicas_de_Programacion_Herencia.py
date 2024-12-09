# Herencia

#
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def detalles(self):  # Método común a todas las clases derivadas.
        return f"Marca: {self.marca}, Modelo: {self.modelo}"

# Clase derivada
class Coche(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)  # Llamada al constructor de la clase base.
        self.puertas = puertas

    def detalles(self):
        # Sobrescribe el método de la clase base
        return f"{super().detalles()}, Puertas: {self.puertas}"  # Reutiliza detalles de la clase base.

# Uso de herencia
coche = Coche("Toyota", "Corolla", 4)  # Crear un objeto de la clase derivada.
print(coche.detalles())  # Llama al método sobrescrito.

