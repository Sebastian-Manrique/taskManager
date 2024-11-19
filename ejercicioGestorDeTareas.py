import customtkinter as ctk  # <- import the CustomTkinter module
import functionsGestorDeTareas as funcs
root = ctk.CTk()
root.title("Gestor de tareas")
funcs.centrarPantalla(root)

botonAdd = ctk.CTkButton(root, text="Agregar tarea", command=funcs.agregarTarea)
botonAdd.pack(padx=20, pady=20)

botonGestionar = ctk.CTkButton(root, text="Agregar tarea", command=funcs.gestionarTarea)
botonGestionar.pack(padx=20, pady=20)

root.mainloop()
