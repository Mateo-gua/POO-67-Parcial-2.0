from modelo import NavidadModel
from vista import NavidadView
from controlador import NavidadController
import sys

if __name__ == "__main__":
    try:
        # 1. Instanciar Modelo
        modelo = NavidadModel()
        
        # 2. Instanciar Vista
        vista = NavidadView()
        
        # 3. Instanciar Controlador (conecta modelo y vista)
        controlador = NavidadController(modelo, vista)
        
        # Protocolo de cierre seguro al cerrar la ventana
        vista.protocol("WM_DELETE_WINDOW", lambda: [controlador.cerrar(), vista.destroy()])
        
        # 4. Iniciar Loop GrÃ¡fico
        vista.mainloop()
        
    except KeyboardInterrupt:
        print("Cerrando aplicaciÃ³n...")
        if 'controlador' in locals():
            controlador.cerrar()
        sys.exit(0)
