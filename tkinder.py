import tkinter as tk

# Creamos la ventana principal
root = tk.Tk()

# Configuramos la cuadrícula con dos filas y dos columnas
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

# Creamos los widgets y los ubicamos en la cuadrícula
label1 = tk.Label(root, text="Etiqueta 1")
label1.grid(row=0, column=0)

label2 = tk.Label(root, text="Etiqueta 2")
label2.grid(row=0, column=1)

button1 = tk.Button(root, text="Botón 1")
button1.grid(row=1, column=0)

button2 = tk.Button(root, text="Botón 2")
button2.grid(row=1, column=1)

# Mostramos la ventana
root.mainloop()
