import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("Ejemplo Combobox")

label = tk.Label(root, text="Selecciona tu opción:")
label.pack(pady=10)

opciones = ["Opción 1", "Opción 2", "Opción 3"]

combo = ttk.Combobox(root, values=opciones, state="readonly")
combo.pack()

def seleccionado(event):
    label.config(text=f"Seleccionaste {combo.get()}")

combo.bind("<<ComboboxSelected>>", seleccionado)

root.mainloop()
