import tkinter as tk
from tkinter import ttk

# Función para agregar una tarea a la lista de pendientes
def agregar_tarea():
    tarea = entrada.get().strip()  # Obtiene el texto ingresado y elimina espacios innecesarios
    if tarea:
        tree_pendientes.insert("", tk.END, values=(tarea,))  # Agrega la tarea al Treeview de pendientes
        entrada.delete(0, tk.END)  # Limpia el campo de entrada después de agregar la tarea

# Función para marcar una tarea como completada
def completar_tarea():
    items_seleccionados = tree_pendientes.selection()  # Obtiene las tareas seleccionadas en la lista de pendientes
    if items_seleccionados:
        for item in items_seleccionados:
            tarea = tree_pendientes.item(item, 'values')  # Obtiene el valor de la tarea
            if tarea:
                tree_pendientes.delete(item)  # Elimina la tarea de la lista de pendientes
                tree_completadas.insert("", tk.END, values=(tarea,))  # La agrega a la lista de completadas

# Función para eliminar una tarea seleccionada de ambas listas
def eliminar_tarea():
    items_seleccionados = tree_completadas.selection() + tree_pendientes.selection()  # Obtiene tareas seleccionadas de ambas listas
    for item in items_seleccionados:
        if item in tree_completadas.get_children():
            tree_completadas.delete(item)  # Elimina la tarea de la lista de completadas
        elif item in tree_pendientes.get_children():
            tree_pendientes.delete(item)  # Elimina la tarea de la lista de pendientes

# Función para deseleccionar elementos si se hace clic fuera de las listas
def deseleccionar(event):
    if not (tree_pendientes.identify_region(event.x, event.y) == "cell" or
            tree_completadas.identify_region(event.x, event.y) == "cell" or
            boton_eliminar.winfo_containing(event.x_root, event.y_root) == boton_eliminar or
            boton_marcar.winfo_containing(event.x_root, event.y_root) == boton_marcar):
        tree_pendientes.selection_remove(tree_pendientes.selection())  # Quita la selección de pendientes
        tree_completadas.selection_remove(tree_completadas.selection())  # Quita la selección de completadas

# Configuración de la ventana principal
root = tk.Tk()
root.title("TO DO LIST")
root.geometry('800x600')
root.configure(bg='#2f3d4b')

# Creación del marco principal
frame = tk.Frame(root, bg='#2f3d4b')
frame.pack(pady=20)

# Etiqueta de título
label_Prueba = tk.Label(frame, text="Tarea - Semana 15", font=("Arial",30,"bold"), bg='#2f3d4b', fg='white')
label_Prueba.pack(pady=10)

# Etiqueta y campo de entrada de la tarea
label_agregar = tk.Label(frame, text="Ingresar Tarea: ", font=("Arial", 14), bg='#2f3d4b', fg='white')
label_agregar.pack(side=tk.LEFT, padx=10, pady=30)

entrada = tk.Entry(frame, bg="white", width=40, font=("Arial", 12))
entrada.pack(side=tk.LEFT)
entrada.bind("<Return>", lambda event: agregar_tarea())  # Permite agregar tareas con Enter

# Botón para añadir una tarea
boton_añadir = tk.Button(frame, text="Añadir tarea", background="grey", command=agregar_tarea)
boton_añadir.pack(side=tk.LEFT, padx=(10, 0))

# Segundo marco para listas de tareas
frame2 = tk.Frame(root, bg='#2f3d4b')
frame2.pack()

# Configuración de estilos para los Treeview
style = ttk.Style()
style.theme_use("clam")

style.configure("Pendientes.Treeview.Heading", background="orange", foreground="black", font=("Calibri", 12, "bold"))
style.configure("Completadas.Treeview.Heading", background="light green", foreground="black", font=("Calibri", 12, "bold"))

# Creación de la lista de tareas pendientes
tree_pendientes = ttk.Treeview(frame2, columns=("PENDIENTES",), show="headings", style="Pendientes.Treeview")
tree_pendientes.heading("PENDIENTES", text="PENDIENTES")
tree_pendientes.pack(side=tk.LEFT, pady=10)

# Creación de la lista de tareas completadas
tree_completadas = ttk.Treeview(frame2, columns=("COMPLETADAS",), show="headings", style="Completadas.Treeview")
tree_completadas.heading("COMPLETADAS", text="COMPLETADAS")
tree_completadas.pack(side=tk.LEFT, pady=10)

# Permitir completar una tarea con doble clic en la lista de pendientes
tree_pendientes.bind("<Double-1>", lambda event: completar_tarea())

# Botón para marcar como completada
boton_marcar = tk.Button(root, text="Marcar como completada", background="grey", command=completar_tarea)
boton_marcar.pack(pady=(20, 0))

# Botón para eliminar tareas
boton_eliminar = tk.Button(root, text="Eliminar tarea", background="grey", command=eliminar_tarea)
boton_eliminar.pack(pady=(20, 0))

# Evento para deseleccionar tareas al hacer clic fuera de las listas
root.bind("<Button-1>", deseleccionar)

# Inicia la aplicación
tk.mainloop()
