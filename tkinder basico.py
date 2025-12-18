import tkinter as tk

# Crear la ventana de tkinter
root = tk.Tk()

# Crear los widgets que se colocarán en la ventana
label1 = tk.Label(root, text="Widget 1")
label2 = tk.Label(root, text="Widget 2")
label3 = tk.Label(root, text="Widget 3")

# Colocar los widgets en la ventana usando la geometría de cuadrícula
label1.grid(row=0, column=0)
label2.grid(row=1, column=1)
# rowspan y columnspan hacen que el widget ocupe más de una celda
# padx/pady es el espacio externo, ipadx/ipady es el espacio interno
label3.grid(row=2, column=2, rowspan=2, columnspan=2, padx=10, pady=10, ipadx=5, ipady=5)

# Iniciar el bucle principal de la ventana
root.mainloop()
