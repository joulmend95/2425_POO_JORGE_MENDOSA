import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry  # Importamos DateEntry para la selección de fechas


# Función para agregar eventos a la lista
def agregar_evento():
    fecha = entry_fecha.get().strip()
    hora = spin_hora.get().strip()
    minuto = spin_min.get().strip()
    time_str = f"{hora}:{minuto}"
    descripcion = entry_descripcion.get().strip()

    # Verifica que todos los campos tengan valores antes de agregar el evento
    if fecha and time_str and descripcion:
        tree.insert("", tk.END, values=(fecha, time_str, descripcion))
        entry_fecha.set_date(None)

        # Reinicia los valores de los Spinboxes de hora y minutos
        spin_hora.delete(0, tk.END)
        spin_hora.insert(0, "00")
        spin_min.delete(0, tk.END)
        spin_min.insert(0, "00")

        entry_descripcion.delete(0, tk.END)


# Creación de la ventana principal de la aplicación
root = tk.Tk()
root.title("Agenda Personal - Semana 14")
root.geometry("600x600")

# Creación de la lista de eventos usando Treeview
tree = ttk.Treeview(root, columns=("Fecha", "Hora", "Descripción"), show="headings")
tree.heading("Fecha", text="Fecha")
tree.heading("Hora", text="Hora")
tree.heading("Descripción", text="Descripción")
tree.pack(pady=20, fill="both", expand=True)

# Creación del frame para la entrada de datos
frame_entry = tk.Frame(root)
frame_entry.pack(pady=10)

# Creación del frame para la selección de la fecha
frame_date = tk.Frame(frame_entry)
frame_date.pack(pady=5)
tk.Label(frame_date, text="Fecha: ").pack(side=tk.LEFT, padx=5)
entry_fecha = DateEntry(frame_date, date_pattern='yyyy-mm-dd')
entry_fecha.pack(side=tk.LEFT)

# Creación de un frame para la entrada de la hora
frame_time = tk.Frame(frame_entry)
frame_time.pack(pady=5)

# Etiqueta para la hora
tk.Label(frame_time, text="Hora: ").pack(side=tk.LEFT, padx=(40, 5))

# Spinbox para la selección de horas (0 a 24)
spin_hora = tk.Spinbox(frame_time, from_=0, to=24, width=3, format="%02.0f")
spin_hora.pack(side=tk.LEFT)

# Separador visual entre hora y minutos
tk.Label(frame_time, text=":").pack(side=tk.LEFT)

# Spinbox para la selección de minutos (0 a 60)
spin_min = tk.Spinbox(frame_time, from_=0, to=60, width=3, format="%02.0f")
spin_min.pack(side=tk.LEFT, padx=(0, 50))

# Creación del frame para la descripción del evento
frame_description = tk.Frame(frame_entry)
frame_description.pack(pady=5)

tk.Label(frame_description, text="Descripción: ").pack(side=tk.LEFT, padx=5)
entry_descripcion = tk.Entry(frame_description)
entry_descripcion.pack(side=tk.LEFT)

# Creación del frame para los botones de acción
frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=10)

# Botón para agregar un evento a la lista
boton_agregar = tk.Button(frame_buttons, text="Agregar Evento", command=agregar_evento)
boton_agregar.pack(side=tk.LEFT, padx=5)

# Botón para eliminar el evento seleccionado en la lista
boton_eliminar = tk.Button(frame_buttons, text="Eliminar Evento", command=lambda: tree.delete(tree.selection()))
boton_eliminar.pack(side=tk.LEFT, padx=5)

# Botón para salir de la aplicación
boton_salir = tk.Button(frame_buttons, text="Salir", command=root.quit)
boton_salir.pack(side=tk.LEFT, padx=5)

# Inicia el bucle principal de la aplicación
root.mainloop()
