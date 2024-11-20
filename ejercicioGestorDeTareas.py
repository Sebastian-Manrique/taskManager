import customtkinter as ctk  # <- import the CustomTkinter module
import functionsGestorDeTareas as funcs

if __name__ == "__main__":
    root = ctk.CTk()
    app = funcs.classRoot(root)
    root.mainloop()
