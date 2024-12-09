
# Clase base
class Ave:
    def volar(self):  # Método genérico que será sobrescrito.
        return "Esta ave vuela."

# Clase derivada que sobrescribe el comportamiento
class Pinguino(Ave):
    def volar(self):  # Pingüino tiene un comportamiento diferente.
        return "Los pingüinos no vuelan, pero nadan muy bien."

# Otra clase derivada
class Aguila(Ave):
    def volar(self):  # Águila redefine el método.
        return "El águila vuela alto en el cielo."

# Uso de polimorfismo
aves = [Pinguino(), Aguila()]  # Lista de objetos que comparten la misma interfaz.
for ave in aves:
    print(ave.volar())  # Llama al método adecuado según la instancia.
