import tkinter as tk
from tkinter import messagebox

class LEDView:
    def __init__(self, root):
        self.root = root
        self.root.geometry("350x280")
        self.root.title("Control LED GPIO 18")

        self.marco = tk.Frame(self.root)
        self.marco.pack(pady=20)

        self.label = tk.Label(
            self.marco,
            text="Selecciona las opciones:"
        )
        self.label.pack(pady=5)

        self.var_encender = tk.BooleanVar(value=False)
        self.var_apagar = tk.BooleanVar(value=False)
        self.var_intermitencia = tk.BooleanVar(value=False)

        self.cb1 = tk.Checkbutton(
            self.marco,
            text="Encender",
            variable=self.var_encender
        )
        self.cb1.pack(anchor="w")

        self.cb2 = tk.Checkbutton(
            self.marco,
            text="Apagar",
            variable=self.var_apagar
        )
        self.cb2.pack(anchor="w")

        self.cb3 = tk.Checkbutton(
            self.marco,
            text="Intermitencia",
            variable=self.var_intermitencia
        )
        self.cb3.pack(anchor="w")

        self.boton_ejecutar = tk.Button(
            self.marco,
            text="EJECUTAR",
            width=20
        )
        self.boton_ejecutar.pack(pady=15)

    def obtener_opciones(self):
        return {
            "encender": self.var_encender.get(),
            "apagar": self.var_apagar.get(),
            "intermitencia": self.var_intermitencia.get()
        }

    def mostrar_estado(self, estado):
        messagebox.showinfo(
            "Estado del LED",
            f"El LED está: {estado}"
        )
