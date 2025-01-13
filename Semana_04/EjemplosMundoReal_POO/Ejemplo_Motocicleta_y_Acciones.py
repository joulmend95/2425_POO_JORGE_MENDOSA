class Moto:
    def __init__(self, color, marca, modelo):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.velocidad = 0

    def acelerar(self, incremento):
        """Aumenta la velocidad de la moto."""
        self.velocidad += incremento
        print(f"La moto {self.marca} {self.modelo} aceleró a {self.velocidad} km/h")

    def frenar(self, decremento):
        """Disminuye la velocidad de de moto."""
        self.velocidad = max(0, self.velocidad - decremento)
        print(f"La moto {self.marca} {self.modelo} frenó a {self.velocidad} km/h")

# Ejemplo de creación y uso de un objeto Carro
mi_moto = Moto('rojo', 'Bajaj', 'Pulsar 180')
mi_moto.acelerar(90)
mi_moto.frenar(60)
print(f'La velocidad final de mi moto es: {mi_moto.velocidad} km/h')