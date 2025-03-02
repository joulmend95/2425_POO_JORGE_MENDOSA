import json

# Clase Producto: Representa un producto con atributos básicos como ID, nombre, cantidad y precio.
class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Método para actualizar el precio del producto.
    def actualizar_precio(self, nuevo_precio):
        self.precio = nuevo_precio

    # Método para actualizar la cantidad disponible del producto.
    def actualizar_cantidad(self, nueva_cantidad):
        self.cantidad = nueva_cantidad

    # Método para convertir el producto a un diccionario (útil para guardar en JSON).
    def to_dict(self):
        return {"id": self.id, "nombre": self.nombre, "cantidad": self.cantidad, "precio": self.precio}

    # Método para representar el objeto como una cadena de texto.
    def __str__(self):
        return f'ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}'


# Clase Inventario: Gestiona una colección de productos y permite guardarlos/cargarlos desde un archivo JSON.
class Inventario:
    def __init__(self, archivo="inventario.json"):
        self.archivo = archivo
        self.productos = {}  # Diccionario para almacenar productos
        self.cargar_inventario()

    # Método para cargar productos desde un archivo JSON.
    def cargar_inventario(self):
        try:
            with open(self.archivo, 'r') as file:
                data = json.load(file)
                self.productos = {int(k): Producto(**v) for k, v in data.items()}
        except (FileNotFoundError, json.JSONDecodeError):  # Captura errores si el archivo no existe o está mal formateado.
            self.productos = {}

    # Método para guardar productos en un archivo JSON.
    def guardar_inventario(self):
        with open(self.archivo, 'w') as file:
            json.dump({k: v.to_dict() for k, v in self.productos.items()}, file, indent=4)

    # Método para agregar un nuevo producto al inventario.
    def agregar_producto(self, producto):
        if producto.id in self.productos:
            print("Error: El ID del producto ya existe.")
        else:
            self.productos[producto.id] = producto
            self.guardar_inventario()
            print("Producto agregado exitosamente.")

    # Método para eliminar un producto por su ID.
    def eliminar_producto(self, id):
        if id in self.productos:
            del self.productos[id]
            self.guardar_inventario()
            print("Producto eliminado exitosamente.")
        else:
            print("Error: Producto no existe.")

    # Método para actualizar el precio de un producto.
    def actualizar_precio(self, id, nuevo_precio):
        if id in self.productos:
            self.productos[id].actualizar_precio(nuevo_precio)
            self.guardar_inventario()
            print("Precio actualizado exitosamente.")
        else:
            print("Error: Producto no existe.")

    # Método para actualizar la cantidad de un producto.
    def actualizar_cantidad(self, id, nueva_cantidad):
        if id in self.productos:
            self.productos[id].actualizar_cantidad(nueva_cantidad)
            self.guardar_inventario()
            print("Cantidad actualizada exitosamente.")
        else:
            print("Error: Producto no existe.")

    # Método para buscar un producto por nombre.
    def buscar_producto_nombre(self, nombre):
        resultado = [p for p in self.productos.values() if p.nombre.lower() == nombre.lower()]
        return resultado if resultado else "Producto no existe."

    # Método para mostrar todos los productos en el inventario.
    def mostrar_inventario(self):
        if self.productos:
            for producto in self.productos.values():
                print(producto)
        else:
            print("El inventario está vacío.")


# Función menú: Interfaz de usuario en consola para gestionar el inventario.
def menu():
    inventario = Inventario()
    while True:
        print("\n--- Sistema de Gestión de Inventario ---")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar precio de un producto")
        print("4. Actualizar cantidad de un producto")
        print("5. Buscar producto por nombre")
        print("6. Mostrar inventario")
        print("7. Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            id = input("Ingrese el ID del producto: ")  # Se podría validar que sea un número.
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad del producto: "))  # Manejo de errores recomendado.
            precio = float(input("Ingrese el precio del producto: "))
            producto = Producto(id, nombre, cantidad, precio)
            inventario.agregar_producto(producto)

        elif opcion == "2":
            id = int(input("Ingrese el ID del producto a eliminar: "))
            inventario.eliminar_producto(id)

        elif opcion == "3":
            id = int(input("Ingrese el ID del producto: "))
            nuevo_precio = float(input("Ingrese nuevo precio: "))
            inventario.actualizar_precio(id, nuevo_precio)

        elif opcion == "4":
            id = int(input("Ingrese el ID del producto: "))
            nueva_cantidad = int(input("Ingrese nueva cantidad: "))
            inventario.actualizar_cantidad(id, nueva_cantidad)

        elif opcion == "5":
            nombre = input("Ingrese el nombre del producto: ")
            resultado = inventario.buscar_producto_nombre(nombre)
            if isinstance(resultado, list):
                for producto in resultado:
                    print(producto)
            else:
                print(resultado)

        elif opcion == "6":
            inventario.mostrar_inventario()

        elif opcion == "7":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Intente de nuevo")


# Ejecuta el menú si se corre el script directamente.
menu()
