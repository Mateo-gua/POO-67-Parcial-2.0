class LEDController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        self.view.boton_ejecutar.config(command=self.ejecutar)

    def ejecutar(self):
        opciones = self.view.obtener_opciones()

        if opciones["intermitencia"]:
            self.model.intermitencia()
        elif opciones["encender"]:
            self.model.encender()
        elif opciones["apagar"]:
            self.model.apagar()
        else:
            self.view.mostrar_estado("NINGUNA OPCIÓN SELECCIONADA")
            return

        estado = self.model.get_estado()
        self.view.mostrar_estado(estado)
