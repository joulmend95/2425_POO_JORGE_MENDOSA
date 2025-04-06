import tkinter as tk
from tkinter import ttk

# Función para agregar una tarea a la lista de pendientes
def agregar_tarea():
    tarea = entrada.get().strip()
    if tarea:
        tree_pendientes.insert("", 0, values=(tarea,))
        entrada.delete(0, tk.END)

# Función para marcar una tarea como completada
def completar_tarea():
    items_seleccionados = tree_pendientes.selection()
    if items_seleccionados:
        for item in items_seleccionados:
            tarea = tree_pendientes.item(item, 'values')
            if tarea:
                tree_pendientes.delete(item)
                tree_completadas.insert("", 0, values=(tarea,))

# Función para eliminar tareas seleccionadas (ya sean pendientes o completadas)
def eliminar_tarea():
    items_seleccionados = tree_completadas.selection() + tree_pendientes.selection()
    for item in items_seleccionados:
        if item in tree_completadas.get_children():
            tree_completadas.delete(item)
        elif item in tree_pendientes.get_children():
            tree_pendientes.delete(item)

# Función para deseleccionar tareas al hacer clic fuera de las celdas
def deseleccionar(event):
    if not (tree_pendientes.identify_region(event.x, event.y) == "cell" or
            tree_completadas.identify_region(event.x, event.y) == "cell" or
            boton_eliminar.winfo_containing(event.x_root, event.y_root) == boton_eliminar or
            boton_marcar.winfo_containing(event.x_root, event.y_root) == boton_marcar):
        tree_pendientes.selection_remove(tree_pendientes.selection())
        tree_completadas.selection_remove(tree_completadas.selection())

# Función para cerrar la aplicación
def cerrar_aplicacion(event):
    root.destroy()

# Crear la ventana principal
root = tk.Tk()
root.title("TO DO LIST")
root.geometry('800x600')
root.configure(bg='#4d8a89')

# Marco principal para el título y el campo de entrada
frame = tk.Frame(root, bg='#4d8a89')
frame.pack(pady=20)

# Etiqueta de título
label_Prueba = tk.Label(frame, text="Gestor de Tareas", font=("Arial", 30, "bold"),
                        bg='#4d8a89', fg='white')
label_Prueba.pack(pady=10)

# Etiqueta para el campo de entrada
label_agregar = tk.Label(frame, text="Ingresar Tarea: ", font=("Arial", 14), bg='#4d8a89', fg='white')
label_agregar.pack(side=tk.LEFT, padx=10, pady=30)

# Campo de entrada de texto
entrada = tk.Entry(frame, bg="white", width=40, font=("Arial", 12))
entrada.pack(side=tk.LEFT)
entrada.bind("<Return>", lambda event: agregar_tarea())

# Botón para añadir tarea
boton_añadir = tk.Button(frame, text="Añadir tarea", background="grey", command=agregar_tarea)
boton_añadir.pack(side=tk.LEFT, padx=(10, 0))

# Segundo marco para contener ambas listas de tareas
frame2 = tk.Frame(root, bg='#4d8a89')
frame2.pack(fill=tk.BOTH, expand=True)

# Submarco para tareas pendientes con scrollbar
frame_pendientes = tk.Frame(frame2, bg='#4d8a89')
frame_pendientes.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)

# Submarco para tareas completadas con scrollbar
frame_completadas = tk.Frame(frame2, bg='#4d8a89')
frame_completadas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)

# Estilos para los encabezados de Treeview
style = ttk.Style()
style.theme_use("clam")
style.configure("Pendientes.Treeview.Heading", background="orange", foreground="black", font=("Calibri", 12, "bold"))
style.configure("Completadas.Treeview.Heading", background="light green", foreground="black", font=("Calibri", 12, "bold"))

# Estilo personalizado para las barras de desplazamiento vertical
style.configure("Vertical.TScrollbar", gripcount=0,
                background="lightblue", darkcolor="grey", lightcolor="lightblue",
                troughcolor="white", arrowcolor="blue")

# Treeview de tareas pendientes con scrollbar
scrollbar_pendientes = ttk.Scrollbar(frame_pendientes, orient="vertical", style="Vertical.TScrollbar")
tree_pendientes = ttk.Treeview(frame_pendientes, columns=("PENDIENTES",), show="headings",
                               style="Pendientes.Treeview", yscrollcommand=scrollbar_pendientes.set)
tree_pendientes.heading("PENDIENTES", text="PENDIENTES")
tree_pendientes.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, pady=10)
scrollbar_pendientes.config(command=tree_pendientes.yview)
scrollbar_pendientes.pack(side=tk.RIGHT, fill=tk.Y)

# Treeview de tareas completadas con scrollbar
scrollbar_completadas = ttk.Scrollbar(frame_completadas, orient="vertical", style="Vertical.TScrollbar")
tree_completadas = ttk.Treeview(frame_completadas, columns=("COMPLETADAS",), show="headings",
                                style="Completadas.Treeview", yscrollcommand=scrollbar_completadas.set)
tree_completadas.heading("COMPLETADAS", text="COMPLETADAS")
tree_completadas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, pady=10)
scrollbar_completadas.config(command=tree_completadas.yview)
scrollbar_completadas.pack(side=tk.RIGHT, fill=tk.Y)

# Botón para marcar tareas como completadas
boton_marcar = tk.Button(root, text="Marcar como completada", background="grey", command=completar_tarea)
boton_marcar.pack(pady=(20, 0))

# Atajos de teclado para marcar como completado
tree_pendientes.bind("<KeyPress-C>", lambda event: completar_tarea())
tree_pendientes.bind("<KeyPress-c>", lambda event: completar_tarea())

# Botón para eliminar tareas
boton_eliminar = tk.Button(root, text="Eliminar tarea", background="grey", command=eliminar_tarea)
boton_eliminar.pack(pady=(20, 20))

# Atajos de teclado para eliminar tarea (letra D o d)
for evento in ["<KeyPress-d>", "<KeyPress-D>"]:
    tree_pendientes.bind(evento, lambda event: eliminar_tarea())
    tree_completadas.bind(evento, lambda event: eliminar_tarea())

# Click fuera de los árboles para deseleccionar tareas
root.bind("<Button-1>", deseleccionar)

# Tecla Escape para cerrar la aplicación
root.bind("<Escape>", cerrar_aplicacion)

# Inicia la aplicación
root.mainloop()
