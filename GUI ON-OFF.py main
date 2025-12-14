import tkinter as tk
from modelo import LEDModel
from vista import LEDView
from controlador import LEDController

def main():
    root = tk.Tk()
    modelo = LEDModel(pin=18)
    vista = LEDView(root)
    controlador = LEDController(modelo, vista)
    root.mainloop()
    modelo.limpiar()

if __name__ == "__main__":
    main()
