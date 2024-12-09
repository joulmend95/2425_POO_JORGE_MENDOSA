class CuentaBancaria:
    def __init__(self, saldo_inicial):
        self.__saldo = saldo_inicial  # Propiedad privada: solo accesible dentro de la clase.

    def depositar(self, cantidad):  # Método público para modificar el saldo.
        if cantidad > 0:
            self.__saldo += cantidad

    def retirar(self, cantidad):  # Método público que asegura restricciones al retirar dinero.
        if 0 < cantidad <= self.__saldo:
            self.__saldo -= cantidad
        else:
            print("Fondos insuficientes o cantidad inválida.")  # Manejo de errores.

    def obtener_saldo(self):  # Método público para acceder al saldo.
        return self.__saldo

# Uso de encapsulación
cuenta = CuentaBancaria(1000)  # Se crea una cuenta con un saldo inicial.
cuenta.depositar(500)  # Depositar 500.
cuenta.retirar(300)  # Retirar 300.
print(f"Saldo actual: {cuenta.obtener_saldo()}")  # Consultar el saldo actual.
