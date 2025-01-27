

class Archivo:
    def __init__(self, nombre_archivo):
        self.nombre_archivo = nombre_archivo
        self.archivo = None
        print(f"Nombre archivo: {nombre_archivo}")

    def abrir(self,nodo):
        self.archivo = open("nombre del archivo",nodo)
        print(f"Nombre archivo: {self.nombre_archivo}, el nodo {self.nodo}")


    def leer(self):
        if self.archivo:
            contenido = self.archivo.read()
            print("el contenido del archivo")
            print(contenido)

    def escribir(self,contenido):
        if self.archivo:
            self.archivo.write(contenido)
            print(f"Nombre archivo: {self.nombre_archivo}")

    def cerrar(self):
        if self.archivo:
            self.archivo.close()
            self.archivo = None
            print(f"Nombre archivo: {self.nombre_archivo}")
        else:
            print("El archivo ya esta cerrado")


    def __del__(self):
        if self.archivo:
            self.archivo.close()
            print(f"Nombre archivo: {self.nombre_archivo} cerrado en el destructor")

mi_archivo = Archivo("nombrearchivo.txt")
mi_archivo.abrir("w")
mi_archivo.escribir("Hola mundo")
mi_archivo.cerrar()

del mi_archivo
