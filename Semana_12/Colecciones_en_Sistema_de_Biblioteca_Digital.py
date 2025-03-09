
# Importamos la biblioteca json para manejar la lectura y escritura de archivos JSON
import json

class Libro:
    # Clase que representa un libro en la biblioteca
    def __init__(self, isbn, titulo, autor, categoria, prestado=False):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.prestado = prestado

    def to_dict(self):
        # Convierte el objeto Libro a un diccionario para poder guardarlo en un archivo JSON
        return {
            "isbn": self.isbn,
            "titulo": self.titulo,
            "autor": self.autor,
            "categoria": self.categoria,
            "prestado": self.prestado
        }

class Biblioteca:
    # Clase que maneja la colección de libros
    def __init__(self, archivo_json='biblioteca.json'):
        self.archivo_json = archivo_json
        self.libros = self.cargar_libros()

    def cargar_libros(self):
        # Carga los libros desde un archivo JSON, si existe
        try:
            with open(self.archivo_json, 'r') as archivo:
                datos_libros = json.load(archivo)
                return {isbn: Libro(**datos) for isbn, datos in datos_libros.items()}
        except FileNotFoundError:
            return {}

    def guardar_libros(self):
        # Guarda la colección de libros en un archivo JSON
        with open(self.archivo_json, 'w') as archivo:
            json.dump({isbn: libro.to_dict() for isbn, libro in self.libros.items()}, archivo, indent=4)

    def añadir_libro(self, libro):
        # Añade un nuevo libro a la biblioteca y lo guarda
        self.libros[libro.isbn] = libro
        self.guardar_libros()

    def prestar_libro(self, isbn):
        # Marca un libro como prestado si está disponible
        libro = self.libros.get(isbn)
        if libro and not libro.prestado:
            libro.prestado = True
            self.guardar_libros()
            print(f"Libro {isbn} prestado con éxito.")
        else:
            print("Libro no disponible para prestar.")

    def devolver_libro(self, isbn):
        # Marca un libro como disponible si estaba prestado
        libro = self.libros.get(isbn)
        if libro and libro.prestado:
            libro.prestado = False
            self.guardar_libros()
            print(f"Libro {isbn} devuelto con éxito.")
        else:
            print("Error en la devolución del libro")

    def mostrar_libros(self):
        # Muestra todos los libros con su estado (Disponible o Prestado)
        for libro in self.libros.values():
            estado = "Prestado" if libro.prestado else "Disponible"
            print(f"Libro {libro.isbn}: {libro.titulo} por {libro.autor} - {estado}")

def menu():
    # Menú principal de la aplicación
    biblioteca = Biblioteca()
    while True:
        print("\n1. Añadir Libro\n2. Mostrar Libros\n3. Prestar Libro\n4. Devolver Libro\n5. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            # Solicita los datos para añadir un nuevo libro
            isbn = input("Ingrese ISBN: ")
            titulo = input("Ingrese título: ")
            autor = input("Ingrese autor: ")
            categoria = input("Ingrese categoría: ")
            libro = Libro(isbn, titulo, autor, categoria)
            biblioteca.añadir_libro(libro)
        elif opcion == "2":
            # Muestra todos los libros
            biblioteca.mostrar_libros()
        elif opcion == "3":
            # Presta un libro por su ISBN
            isbn = input("ISBN del libro a prestar: ")
            biblioteca.prestar_libro(isbn)
        elif opcion == "4":
            # Devuelve un libro por su ISBN
            isbn = input("ISBN del libro a devolver: ")
            biblioteca.devolver_libro(isbn)
        elif opcion == "5":
            # Sale del sistema
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida. Intente nuevamente")

if __name__ == "__main__":
    menu()