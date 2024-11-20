import customtkinter as ctk  # <- import the CustomTkinter module
import functionsGestorDeTareas as funcs



# root = ctk.CTk()
# root.title("Gestor de tareas")
# funcs.centrarPantalla(root)
#
# topFrame = ctk.CTkFrame(root)
# topFrame.pack(side="top")
#
# middleFrame = ctk.CTkFrame(root)
# middleFrame.pack()
#
# bottomFrame = ctk.CTkFrame(root)
# bottomFrame.pack(side="bottom")
#
#
#
# botonGestionar = ctk.CTkButton(bottomFrame, text="Gestionar tarea", command=funcs.gestionarTarea)
# botonGestionar.pack(padx=20, pady=20)
#
# root.mainloop()

if __name__ == "__main__":
    root = ctk.CTk()
    app = funcs.classRoot(root)
    root.mainloop()