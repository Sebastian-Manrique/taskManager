from datetime import datetime
import tkinter as tk
from tkinter import ttk
import customtkinter as ctk  # <- import the CustomTkinter module


class classRoot:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de tareas")
        centrarPantalla(self.root)

        self.middleInstance = frameMiddle(self.root)
        self.topInstance = frameTop(self.root, self.middleInstance)
        self.topInstance.pack(side="top", fill="x")

        self.middleInstance.pack(expand=True, fill="both")

        self.bottomInstance = frameBottom(self.root)
        self.bottomInstance.pack(side="bottom", fill="x")


class frameTop(ctk.CTkFrame):  # Usar PEP8 para nombres de clases
    def __init__(self, root, middleInstance):
        super().__init__(root)

        etiqueta = ctk.CTkLabel(self, text="Agregar tarea")
        etiqueta.pack(side="left", padx=(100, 50))

        entryTitulo = ctk.CTkEntry(self, width=100, placeholder_text="Nombre de la tarea")
        entryTitulo.pack(side="left", expand=True, fill="x")

        combobox = ctk.CTkComboBox(self, values=["Alta", "Media", "Baja"])
        combobox.pack(side="left")
        botonAgregar = ctk.CTkButton(self, text="Agregar",
                                     command=lambda: guardarTarea(entryTitulo, combobox.get(), middleInstance))
        botonAgregar.pack(side="left")


class frameMiddle(ctk.CTkFrame):
    def __init__(self, root):
        super().__init__(root)

        # Etiqueta del frame del medio
        etiqueta = ctk.CTkLabel(self, text="Tareas")
        etiqueta.pack()

        self.tabla = ttk.Treeview(self, columns=("Coll", "Col2", "Col3", "Col4"), show="headings")

        self.tabla.heading("Coll", text="Titulo")
        self.tabla.heading("Col2", text="Prioridad")
        self.tabla.heading("Col3", text="Fecha")
        self.tabla.heading("Col4", text="Estado")

        self.tabla.pack()

    def build_tree(self, tituloTarea, prioridad, dt_string):
        self.tabla.insert("", "end", values=(tituloTarea, prioridad, dt_string, "en proceso"))
        print(f"MIDDLE FRAME: {tituloTarea} {prioridad} {dt_string}")


class frameBottom(ctk.CTkFrame):
    def __init__(self, root):
        super().__init__(root)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure([0, 1], weight=1)

        botonGestionar = ctk.CTkButton(self, text="Gestionar tarea", command=gestionarTarea)
        botonGestionar.grid(row=0, column=0)

        botonAspecto = ctk.CTkButton(self, text="Aspecto 🌙", command=cambiarTema)
        botonAspecto.grid(row=0, column=1)


def centrarPantalla(root):
    ancho_ventana = 800
    # Colocarla centrada
    # 1. Conocer nuestra pantalla

    ancho_pantalla = root.winfo_screenwidth()
    alto_pantalla = root.winfo_screenheight()
    # 2. Colocar
    alto_ventana = int((alto_pantalla * ancho_ventana) / ancho_pantalla)  # Cuadrada
    pos_x = (ancho_pantalla // 2) - (ancho_ventana // 2)
    pos_y = (alto_pantalla // 2) - (alto_ventana // 2)
    root.geometry(f"{ancho_ventana}x{alto_ventana}+{pos_x}+{pos_y}")


tareas = {}


def guardarTarea(titulo, prioridad, middleInstance):
    tituloTarea = titulo.get()
    if tituloTarea == "":
        tk.messagebox.showerror(title="Error", message="El nombre de la tarea esta vacío")
    else:
        titulo.delete(0, 'end')
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        print(
            f"El titulo de la tarea es {tituloTarea}, su prioridad es {prioridad} y su fecha de creación es {dt_string}")
        tareas[tituloTarea] = {
            "Prioridad": prioridad,
            "Fecha": dt_string
        }
        middleInstance.build_tree(tituloTarea, prioridad, dt_string)


def gestionarTarea():
    pass


mode = "dark"


def cambiarTema():
    global mode
    if mode == "dark":
        ctk.set_appearance_mode("light")  # Si se modifica el color del frame deja de funcionar ⚠ NO TOCAR ⚠
        mode = "light"

    else:
        ctk.set_appearance_mode("dark")
        mode = "dark"
