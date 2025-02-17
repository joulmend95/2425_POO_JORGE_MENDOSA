class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        # Constructor de la clase Producto
        # Se inicializan los atributos privados de cada producto
        self._id_producto = id_producto
        self._nombre = nombre
        self._cantidad = cantidad
        self._precio = precio

    # Getters (Métodos para obtener los valores de los atributos)
    def get_id_producto(self):
        return self._id_producto

    def get_nombre(self):
        return self._nombre

    def get_cantidad(self):
        return self._cantidad

    def get_precio(self):
        return self._precio

    # Setters (Métodos para modificar los valores de los atributos)
    def set_nombre(self, nombre):
        self._nombre = nombre

    def set_cantidad(self, cantidad):
        self._cantidad = cantidad

    def set_precio(self, precio):
        self._precio = precio

    # Método para mostrar la información del producto como cadena de texto
    def __str__(self):
        return f"ID: {self._id_producto}, Nombre: {self._nombre}, Cantidad: {self._cantidad}, Precio: ${self._precio}"


class Inventario:
    def __init__(self):
        # Constructor de la clase Inventario
        # Se inicializa una lista vacía para almacenar los productos
        self.productos = []

    def agregar_producto(self, producto):
        # Añadir un nuevo producto al inventario
        # Se verifica que el ID sea único
        for p in self.productos:
            if p.get_id_producto() == producto.get_id_producto():
                print("Error: ID de producto ya existe.")
                return
        self.productos.append(producto)
        print("Producto agregado exitosamente.")

    def eliminar_producto(self, id_producto):
        # Eliminar un producto del inventario por su ID
        for producto in self.productos:
            if producto.get_id_producto() == id_producto:
                self.productos.remove(producto)
                print("Producto eliminado exitosamente.")
                return
        print("Error: Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        # Actualizar la cantidad o el precio de un producto por su ID
        for producto in self.productos:
            if producto.get_id_producto() == id_producto:
                if cantidad is not None:
                    producto.set_cantidad(cantidad)
                if precio is not None:
                    producto.set_precio(precio)
                print("Producto actualizado exitosamente.")
                return
        print("Error: Producto no encontrado.")

    def buscar_producto(self, nombre):
        # Buscar productos por nombre (puede haber nombres similares)
        resultados = []
        for producto in self.productos:
            # Se utiliza lower() para una búsqueda sin distinguir mayúsculas de minúsculas
            if nombre.lower() in producto.get_nombre().lower():
                resultados.append(producto)

        # Mostrar los productos encontrados
        if resultados:
            print("Productos encontrados:")
            for producto in resultados:
                print(producto)
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_inventario(self):
        # Mostrar todos los productos en el inventario
        if not self.productos:
            print("El inventario está vacío.")
        else:
            print("Inventario de productos:")
            for producto in self.productos:
                print(producto)


# Interfaz de usuario en la consola
def menu():
    # Se crea una instancia de Inventario para gestionar los productos
    inventario = Inventario()
    while True:
        # Mostrar el menú de opciones al usuario
        print("\n--- Menú de Gestión de Inventario ---")
        print("1. Agregar Producto")
        print("2. Eliminar Producto")
        print("3. Actualizar Producto")
        print("4. Buscar Producto")
        print("5. Mostrar Inventario")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        # Opción para agregar un nuevo producto
        if opcion == '1':
            id_producto = input("Ingrese el ID del producto: ")
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad del producto: "))
            precio = float(input("Ingrese el precio del producto: "))
            # Se crea una instancia de Producto con los datos ingresados
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.agregar_producto(producto)

        # Opción para eliminar un producto por ID
        elif opcion == '2':
            id_producto = input("Ingrese el ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        # Opción para actualizar un producto por ID
        elif opcion == '3':
            id_producto = input("Ingrese el ID del producto a actualizar: ")
            cantidad = input("Ingrese la nueva cantidad (dejar en blanco para no modificar): ")
            precio = input("Ingrese el nuevo precio (dejar en blanco para no modificar): ")
            # Se convierten los valores ingresados si no están en blanco
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id_producto, cantidad, precio)

        # Opción para buscar productos por nombre
        elif opcion == '4':
            nombre = input("Ingrese el nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)

        # Opción para mostrar todos los productos en el inventario
        elif opcion == '5':
            inventario.mostrar_inventario()

        # Opción para salir del programa
        elif opcion == '6':
            print("Saliendo del sistema de gestión de inventarios.")
            break

        # Manejo de opciones inválidas
        else:
            print("Opción no válida. Por favor, intente de nuevo.")


# Ejecuta el menú solo si el archivo se ejecuta directamente
if __name__ == "__main__":
    menu()
