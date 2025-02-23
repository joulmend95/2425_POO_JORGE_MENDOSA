class Producto:
    # Clase que representa un producto con atributos como ID, nombre, cantidad y precio.
    def __init__(self, id_producto, nombre, cantidad, precio):
        self._id_producto = id_producto
        self._nombre = nombre
        self._cantidad = cantidad
        self._precio = precio

    # Métodos para obtener los valores de los atributos del producto
    def get_id_producto(self):
        return self._id_producto
    def get_nombre(self):
        return self._nombre
    def get_cantidad(self):
        return self._cantidad
    def get_precio(self):
        return self._precio

    # Métodos para modificar los valores de los atributos del producto
    def set_nombre(self, nombre):
        self._nombre = nombre
    def set_cantidad(self, cantidad):
        self._cantidad = cantidad
    def set_precio(self, precio):
        self._precio = precio

    # Representación en cadena del producto
    def __str__(self):
        return f"ID: {self._id_producto}, Nombre: {self._nombre}, Cantidad: {self._cantidad}, Precio: ${self._precio}"

# Clase que representa el inventario, gestionando una lista de productos
class Inventario:
    def __init__(self):
        self.productos = []

# Cargar productos desde un archivo, manejando posibles errores
    def cargar_inventario(self):
        try:
            with open('Inventario.txt', 'r') as file:
                for line in file:
                    try:
                        id_producto, nombre, cantidad, precio = line.strip().split(',')
                        self.productos.append(Producto(id_producto, nombre, int(cantidad), float(precio)))
                    except ValueError:
                        print(f"Error al cargar el producto: {line.strip()}")
        except FileNotFoundError:
            print("Error: No se encontró el archivo Inventario.txt. Se creará uno nuevo al guardar el inventario.")
        except PermissionError:
            print("Error: No tienes permisos para leer Inventario.txt.")

    # Guardar productos en un archivo
    def guardar_inventario(self):
        try:
            with open('Inventario.txt', 'w') as file:
                for producto in self.productos:
                    file.write(f"{producto.get_id_producto()},{producto.get_nombre()},{producto.get_cantidad()},{producto.get_precio()}\n")
        except PermissionError:
            print("Error: No tienes permisos para escribir en Inventario.txt.")

    # Agregar un nuevo producto al inventario, evitando duplicados de ID
    def agregar_producto(self, producto):
        for p in self.productos:
            if p.get_id_producto() == producto.get_id_producto():
                print("Error: ID de producto ya existe.")
                return
        self.productos.append(producto)
        print("Producto agregado exitosamente.")
        self.guardar_inventario()

    # Eliminar un producto del inventario basado en su ID
    def eliminar_producto(self, id_producto):
        for producto in self.productos:
            if producto.get_id_producto() == id_producto:
                self.productos.remove(producto)
                self.guardar_inventario()
                print("Producto eliminado exitosamente.")
                return
        print("Error: Producto no encontrado.")

    # Actualizar la cantidad y/o precio de un producto existente en el inventario
    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        for producto in self.productos:
            if producto.get_id_producto() == id_producto:
                if cantidad is not None:
                    producto.set_cantidad(cantidad)
                if precio is not None:
                    producto.set_precio(precio)
                self.guardar_inventario()
                print("Producto actualizado exitosamente.")
                return
        print("Error: Producto no encontrado.")

    # Buscar productos por nombre y mostrar los resultados encontrados
    def buscar_producto(self, nombre):
        resultados = []
        for producto in self.productos:
            if nombre.lower() in producto.get_nombre().lower():
                resultados.append(producto)
        if resultados:
            print("Productos encontrados:")
            for producto in resultados:
                print(producto)
        else:
            print("No se encontraron productos con ese nombre.")

    # Mostrar todos los productos almacenados en el inventario
    def mostrar_inventario(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            print("Inventario de productos:")
            for producto in self.productos:
                print(producto)

# Función principal que muestra el menú interactivo para la gestión del inventario
def menu():
    inventario = Inventario()
    inventario.cargar_inventario()
    while True:
        print("\n--- Menú de Gestión de Inventario ---")
        print("1. Agregar Producto")
        print("2. Eliminar Producto")
        print("3. Actualizar Producto")
        print("4. Buscar Producto")
        print("5. Mostrar Inventario")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            id_producto = input("Ingrese el ID del producto: ")
            nombre = input("Ingrese el nombre del producto: ")
            while True:
                try:
                    cantidad = int(input("Ingrese la cantidad del producto: "))
                    break
                except ValueError:
                    print("Error: Ingrese un número entero válido para la cantidad.")
            while True:
                try:
                    precio = float(input("Ingrese el precio del producto: "))
                    break
                except ValueError:
                    print("Error: Ingrese un número válido para el precio.")
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.agregar_producto(producto)

        elif opcion == '2':
            id_producto = input("Ingrese el ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == '3':
            id_producto = input("Ingrese el ID del producto a actualizar: ")
            cantidad = input("Ingrese la nueva cantidad (dejar en blanco para no modificar): ")
            precio = input("Ingrese el nuevo precio (dejar en blanco para no modificar): ")
            cantidad = int(cantidad) if cantidad.strip().isdigit() else None
            try:
                precio = float(precio) if precio.strip() else None
            except ValueError:
                print("Error: El precio ingresado no es válido.")
                precio = None
            inventario.actualizar_producto(id_producto, cantidad, precio)

        elif opcion == '4':
            nombre = input("Ingrese el nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)

        elif opcion == '5':
            inventario.mostrar_inventario()

        elif opcion == '6':
            print("Saliendo del sistema de gestión de inventarios.")
            break

        else:
            print("Opción no válida. Por favor, intente de nuevo.")

# Verifica si el script se está ejecutando directamente para llamar al menú principal
if __name__ == "__main__":
    menu()
