import tkinter as tk
import random

class NavidadView(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("ðŸŽ„ Christmas Air Delivery ðŸŽ„")
        self.geometry("600x650") # Un poco mÃ¡s grande para que quepa todo
        self.configure(bg="#0f172a") # Azul nocturno moderno

        # Variables de estado
        self.luces_encendidas = False
        self.ids_luces = []      # Para guardar las esferas del Ã¡rbol
        self.copos = []          # Para la nieve

        # --- CANVAS (Lienzo de dibujo) ---
        self.canvas = tk.Canvas(self, width=600, height=500, bg="#0f172a", highlightthickness=0)
        self.canvas.pack(pady=10)

        # 1. Dibujar el Paisaje de Fondo
        self.dibujar_fondo()

        # 2. Dibujar el Ãrbol Mejorado
        self.dibujar_arbol_pro()
        
        # 3. Dibujar Regalos en el suelo
        self.dibujar_regalos_suelo()

        # 4. Dibujar el "Tenis Volador" (Nike NavideÃ±o)
        self.crear_tenis_volador()

        # 5. La Estrella Principal (La que controla el sistema)
        self.id_estrella = self.canvas.create_text(300, 90, text="â˜…", font=("Arial", 60), fill="#444")

        # --- PANEL DE DATOS ---
        frame_datos = tk.Frame(self, bg="#b71c1c", bd=4, relief="ridge")
        frame_datos.pack(pady=10, ipadx=10, ipady=5)
        
        tk.Label(frame_datos, text="ðŸŽ… RASTREO DE TRINEO IOT ðŸŽ…", 
                 font=("Impact", 14), bg="#b71c1c", fg="white").pack()

        self.lbl_data = tk.Label(frame_datos, text="ESPERANDO SEÃ‘AL...", 
                                 font=("Consolas", 16, "bold"), bg="#b71c1c", fg="#FFD700")
        self.lbl_data.pack()

        # --- INICIAR ANIMACIONES AUTOMÃTICAS ---
        self.crear_nieve()
        self.animar_nieve()
        self.mover_tenis() # Â¡AquÃ­ vuelan los tenis!

    def dibujar_fondo(self):
        # Luna
        self.canvas.create_oval(500, 50, 560, 110, fill="#fdfbd3", outline="", stipple="gray75")
        # Suelo de nieve
        self.canvas.create_oval(-100, 450, 700, 600, fill="#e2e8f0", outline="")

    def dibujar_arbol_pro(self):
        """Dibuja un Ã¡rbol frondoso por capas"""
        # Tronco
        self.canvas.create_rectangle(280, 420, 320, 480, fill="#3e2723", outline="")

        # Capas del Ã¡rbol (Verde degradado)
        colores_pino = ["#1b5e20", "#2e7d32", "#388e3c", "#43a047"]
        ancho_inicial = 240
        y_inicial = 430
        altura_capa = 60
        
        for i in range(5): # 5 capas de hojas
            x1 = 300 - (ancho_inicial // 2)
            y1 = y_inicial
            x2 = 300 + (ancho_inicial // 2)
            y2 = y_inicial
            pico_x = 300
            pico_y = y_inicial - altura_capa
            
            self.canvas.create_polygon(x1, y1, x2, y2, pico_x, pico_y, 
                                       fill=colores_pino[i % 4], outline="#145a32")
            
            # Subir para la siguiente capa
            y_inicial -= (altura_capa // 2) + 10
            ancho_inicial -= 40

            # AÃ±adir esferas decorativas en esta capa
            self.agregar_esferas(x1, y1, x2, pico_y)

    def agregar_esferas(self, x_min, y_base, x_max, y_pico):
        """Coloca bolitas de luz aleatorias en la capa del Ã¡rbol"""
        for _ in range(3):
            # PosiciÃ³n aleatoria dentro del triÃ¡ngulo (aprox)
            ex = random.randint(int(x_min)+20, int(x_max)-20)
            ey = random.randint(int(y_pico)+20, int(y_base)-10)
            
            # Dibujar esfera apagada (gris oscuro)
            esfera = self.canvas.create_oval(ex, ey, ex+10, ey+10, fill="#333", outline="black")
            self.ids_luces.append(esfera)

    def dibujar_regalos_suelo(self):
        # Regalo 1
        self.canvas.create_rectangle(240, 450, 280, 480, fill="#d32f2f", outline="black")
        self.canvas.create_line(260, 450, 260, 480, fill="gold", width=3)
        # Regalo 2
        self.canvas.create_rectangle(330, 460, 360, 480, fill="#1976d2", outline="black")
        self.canvas.create_line(330, 470, 360, 470, fill="white", width=3)

    # --- EL TENIS VOLADOR ---
    def crear_tenis_volador(self):
        self.x_tenis = -100 # Empieza fuera de la pantalla
        self.y_tenis = 100
        tag = "tenis"

        # 1. El Zapato (Estilo Jordan High-Top)
        # Suela
        self.canvas.create_polygon(0, 40, 60, 40, 55, 30, 5, 30, fill="white", outline="gray", tags=tag)
        # Cuerpo rojo
        self.canvas.create_polygon(5, 30, 35, 30, 35, 10, 5, 15, fill="#d50000", outline="black", tags=tag)
        # Punta blanca
        self.canvas.create_polygon(35, 30, 55, 30, 50, 20, 35, 20, fill="white", outline="black", tags=tag)
        # Ala (Estilo Hermes/Navidad)
        self.canvas.create_polygon(10, 15, 0, 0, 20, 5, fill="#ffd700", outline="orange", tags=tag)

        # 2. Regalo encima del zapato
        self.canvas.create_rectangle(15, 0, 35, 15, fill="#00c853", outline="white", tags=tag)
        
        # Mover todo el grupo a la posiciÃ³n inicial
        self.canvas.move(tag, self.x_tenis, self.y_tenis)

    def mover_tenis(self):
        """Mueve el tenis de izquierda a derecha"""
        self.canvas.move("tenis", 4, 0) # Mover 4 pÃ­xeles a la derecha
        
        # Obtener coordenadas actuales
        coords = self.canvas.coords("tenis")
        # coords devuelve una lista larga, tomamos la primera x
        if coords: 
            # Si el tenis sale por la derecha (x > 650), vuelve a la izquierda
            # Nota: coords[0] es la primera coordenada x del primer polÃ­gono dibujado
            # Es un cÃ¡lculo aproximado
            if self.canvas.bbox("tenis")[2] > 650:
                self.canvas.move("tenis", -750, 0) # Regresar al inicio

        self.after(50, self.mover_tenis)

    # --- NIEVE ---
    def crear_nieve(self):
        for _ in range(70):
            x = random.randint(0, 600)
            y = random.randint(0, 500)
            r = random.randint(1, 3)
            copo = self.canvas.create_oval(x, y, x+r, y+r, fill="white", outline="")
            self.copos.append({"id": copo, "vel": random.uniform(2, 5)})

    def animar_nieve(self):
        for copo in self.copos:
            self.canvas.move(copo["id"], 0, copo["vel"])
            coords = self.canvas.coords(copo["id"])
            if coords[3] > 500: # Si toca el suelo
                self.canvas.move(copo["id"], 0, -510) # Vuelve arriba
        self.after(50, self.animar_nieve)

    # --- CONEXIÃ“N CON CONTROLADOR ---
    def animar_estrella(self, encendido):
        """MÃ©todo que llama el controlador.py"""
        color_estrella = "yellow" if encendido else "#444"
        self.canvas.itemconfig(self.id_estrella, fill=color_estrella)
        
        if encendido:
            self.parpadear_luces_arbol()
        else:
            # Apagar luces del Ã¡rbol
            for luz in self.ids_luces:
                self.canvas.itemconfig(luz, fill="#333")

    def parpadear_luces_arbol(self):
        """Hace que las esferas del Ã¡rbol cambien de color"""
        colores = ["red", "blue", "yellow", "cyan", "magenta", "orange"]
        
        # Solo parpadea si la estrella (sistema) sigue encendida
        color_actual_estrella = self.canvas.itemcget(self.id_estrella, "fill")
        
        if color_actual_estrella == "yellow":
            for luz in self.ids_luces:
                self.canvas.itemconfig(luz, fill=random.choice(colores))
            self.after(300, self.parpadear_luces_arbol)

    def actualizar_etiqueta_clima(self, temp, hum):
        if temp is not None:
            txt = f"ðŸŒ¡ TEMP: {temp}Â°C  |  ðŸ’§ HUM: {hum}%"
            self.lbl_data.config(text=txt, fg="#FFD700")
        else:
            self.lbl_data.config(text="Buscando seÃ±al...", fg="white")
