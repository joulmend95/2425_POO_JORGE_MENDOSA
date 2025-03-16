import tkinter as tk
from idlelib.colorizer import color_config

#Función para agregar un dato a la lista
def agregar():
    dato = entrada.get().strip()
    if dato:
        lista.insert(tk.END,dato)
        entrada.delete(0, tk.END)   #Limpia la entrada después de agregar

#Función para eliminar todos los elementos de la lista
def eliminar_todo():
    lista.delete(0, tk.END)

#Se crea la ventana principal
root = tk.Tk()

root.title("Inicio de la prueba")
root.geometry('1200x800')
root.configure(bg='#440c29')

# Frame para organizar label y entrada
frame = tk.Frame(root, bg='#440c29')
frame.pack(pady=20)


# Se ingresa Label -Etiqueta de Título
label_Prueba = tk.Label(frame, text="Tarea - Semana 13", font=("Arial",30,"bold"), bg='#440c29', fg='white', )
label_Prueba.pack(pady=10)


#Se ingresa Label - Etiqueta para indicar cuadro de entrada
label_agregar = tk.Label(frame, text="Agregar datos", font=("Arial", 14), bg='#440c29', fg='white')
label_agregar.pack(side=tk.LEFT, padx=10, pady=30)


# Se configura el cuadro de entrada de texto
entrada = tk.Entry(frame, bg = "white" , width=40 , font = ("Arial",12))
entrada.pack(side=tk.LEFT)

#Asiganamos la tecla 'Enter' para agregar datos
entrada.bind("<Return>", lambda event: agregar())

#Se agrega un Botón para agregar datos
boton = tk.Button(root, text = "Agregar" , background="skyblue" , command = agregar)
boton.pack(pady = 20)

#Se agrega lista y su respectivo cuadro con dimensiones
lista = tk.Listbox(root, font = ("Arial",12), selectbackground = "gray", selectmode=tk.SINGLE, width=60, height=15)
lista.pack(pady = 15)

#Se agrega botón para limpiar datos
boton_eliminar_todo = tk.Button(root, text="Limpiar" , background="grey" , command = eliminar_todo)
boton_eliminar_todo.pack(pady = 35)

#inicio
root.mainloop()


