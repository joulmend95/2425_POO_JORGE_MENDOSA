# Importamos herramientas para crear clases abstractas.
from abc import ABC, abstractmethod

# Clase abstracta
class Figura(ABC):
    @abstractmethod
    def calcular_area(self):
        pass

# Clase concreta que implementa la abstracción
class Rectangulo(Figura):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def calcular_area(self):  # Implementación específica para un rectángulo.
        return self.ancho * self.alto

# Otra clase concreta que implementa la abstracción
class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):  # Implementación específica para un círculo.
        return 3.14 * self.radio ** 2

# Uso de la abstracción
figuras = [Rectangulo(4, 5), Circulo(3)]
for figura in figuras:
    print(f"Área: {figura.calcular_area()}")
