from datetime import datetime
import tkinter as tk
from tkinter import ttk, Toplevel

import customtkinter as ctk  # <- import the CustomTkinter module


def centrarPantalla(root):
    root.rowconfigure([0, 1, 2, 3], weight=1)
    root.columnconfigure([0, 1, 2, 3], weight=1)
    # root.grid(row=4, colum=4)

    ancho_ventana = 700
    # Colocarla centrada
    # 1. Conocer nuestra pantalla

    ancho_pantalla = root.winfo_screenwidth()
    alto_pantalla = root.winfo_screenheight()
    # 2. Colocar
    alto_ventana = int((alto_pantalla * ancho_ventana) / ancho_pantalla)  # Cuadrada
    pos_x = (ancho_pantalla // 2) - (ancho_ventana // 2)
    pos_y = (alto_pantalla // 2) - (alto_ventana // 2)
    root.geometry(f"{ancho_ventana}x{alto_ventana}+{pos_x}+{pos_y}")


def agregarTarea():
    secundaria = ctk.CTk()
    centrarPantalla(secundaria)
    secundaria.title("Agregar tarea")

    labelTitulo = ctk.CTkLabel(secundaria, text="Título de la tarea:")
    labelTitulo.pack()

    entryTitulo = ctk.CTkEntry(secundaria, width=100)
    entryTitulo.pack(padx=10, pady=5)

    labelPrioridad = ctk.CTkLabel(secundaria, text="Nivel de la prioridad:")
    labelPrioridad.pack(pady=5)

    combobox = ctk.CTkComboBox(secundaria, values=["Alta", "Media", "Baja"])
    combobox.pack(pady=5)

    botonAgregar = ctk.CTkButton(secundaria, text="Agregar",
                                 command=lambda: guardarTarea(entryTitulo, combobox.get()))
    botonAgregar.pack(pady=10)

    botonCerrar = ctk.CTkButton(secundaria, text="Cerrar", fg_color="red", command=secundaria.destroy)
    botonCerrar.pack(pady=15)

    secundaria.mainloop()


tareas = {}


def guardarTarea(titulo, prioridad):
    tituloTarea = titulo.get()
    titulo.delete(0, 'end')
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print(f"El titulo de la tarea es {tituloTarea}, su prioridad es {prioridad} y su fecha de creación es {dt_string}")

    tareas[tituloTarea] = {
        "Prioridad": prioridad,
        "Fecha": now
    }


def verTabla():
    root = tk.Tk()
    root.title("Tabla")
    centrarPantalla(root)
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(1, weight=1)
    root.grid_columnconfigure(1, weight=1)
    tabla = ttk.Treeview(root, columns=("Coll", "Col2", "Col3"), show="headings")
    tabla.heading("Coll", text="Titulo")
    tabla.heading("Col2", text="Prioridad")
    tabla.heading("Col3", text="Fecha")

    for titulo, information in tareas.items():
        prioridad = tareas[titulo]["Prioridad"]
        fecha = tareas[titulo]["Fecha"]
        tabla.insert("", "end", values=(titulo, prioridad, fecha))
    tabla.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

    for titulo in tareas.items():
        print(titulo)


def gestionarTarea():
    verTabla()
