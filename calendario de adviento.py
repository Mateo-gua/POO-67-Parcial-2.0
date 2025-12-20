import tkinter as tk
from tkinter import messagebox
import random

ANCHO, ALTO, FPS = 800, 650, 60

BG = "#1a1a2e"
BOX = "#e94560"
RIBBON = "#fcd0a1"
OPEN = "#16213e"

actividades = [
    "Decorar el árbol", "Hacer galletas", "Escuchar villancicos",
    "Carta a Santa", "Envolver regalos", "Foto navideña",
    "Encender velas", "Leer un cuento", "Dibujar Navidad",
    "Chocolate caliente", "Película navideña", "Hacer una donación",
    "Cantar", "Cocinar juntos", "Manualidades",
    "Llamar a la familia", "Decorar la puerta", "Dar gracias",
    "Donar juguetes", "Jugar juegos de mesa", "Comer postre",
    "Ver televisión", "Relajarse", "Cena de Navidad"
]

dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

class JuegoCalendario:
    def __init__(self, root):
        root.title("Calendario de Adviento")
        self.root = root

        self.c = tk.Canvas(root, width=ANCHO, height=ALTO, bg=BG, highlightthickness=0)
        self.c.pack()

        self.particulas = []
        self.nieve = []
        self.abiertas = set()

        self.titulo()
        self.crear_dias()
        self.crear_nieve()
        self.crear_cajas()
        self.loop()

    def titulo(self):
        self.c.create_text(ANCHO//2, 45, text="CALENDARIO DE ADVIENTO",
                           font=("Consolas", 32, "bold"), fill="#e94560")
        self.c.create_text(ANCHO//2, 80, text="Level: Diciembre 2025",
                           font=("Arial", 16), fill="white")

    def crear_dias(self):
        for i, dia in enumerate(dias_semana):
            x = 80 + i * 95 + 35
            self.c.create_text(x, 105, text=dia,
                               font=("Arial", 10, "bold"), fill="white")

    def crear_cajas(self):
        for d in range(1, 25):
            x = 80 + ((d-1) % 7) * 95
            y = 120 + ((d-1) // 7) * 95
            self.caja(x, y, d)

    def caja(self, x, y, d):
        t, s = f"c{d}", 70
        self.c.create_rectangle(x, y, x+s, y+s, fill=BOX, outline="white", width=2, tags=t)
        self.c.create_rectangle(x+s//2-5, y, x+s//2+5, y+s, fill=RIBBON, tags=t)
        self.c.create_rectangle(x, y+s//2-5, x+s, y+s//2+5, fill=RIBBON, tags=t)
        self.c.create_text(x+s//2, y+s//2, text=d, fill="white",
                           font=("Arial", 16, "bold"), tags=t)

        self.c.tag_bind(t, "<Button-1>", lambda e, d=d, x=x, y=y: self.click(d, x, y))
        self.c.tag_bind(t, "<Enter>", lambda e, t=t: self.hover(t, True))
        self.c.tag_bind(t, "<Leave>", lambda e, t=t: self.hover(t, False))

    def hover(self, tag, on):
        d = int(tag[1:])
        if d in self.abiertas: return
        for i in self.c.find_withtag(tag):
            if self.c.type(i) == "rectangle" and self.c.itemcget(i, "outline"):
                self.c.itemconfig(i, outline="#fcd0a1" if on else "white",
                                  width=4 if on else 2)

    def click(self, d, x, y):
        if d in self.abiertas: return
        self.abiertas.add(d)

        for i in self.c.find_withtag(f"c{d}"):
            if self.c.type(i) == "rectangle":
                self.c.itemconfig(i, fill=OPEN, outline="gray")

        self.explosion(x+35, y+35)
        self.root.after(100, lambda:
            messagebox.showinfo(f"Día {d}", random.choice(actividades))
        )

    def explosion(self, x, y):
        for _ in range(25):
            self.particulas.append([
                self.c.create_oval(x, y, x+5, y+5,
                                   fill=random.choice(["red", "blue", "yellow", "green"]),
                                   outline=""),
                random.uniform(-5, 5),
                random.uniform(-8, -2),
                100
            ])

    def crear_nieve(self):
        for _ in range(60):
            x, y = random.randint(0, ANCHO), random.randint(0, ALTO)
            i = self.c.create_oval(x, y, x+2, y+2, fill="white", outline="")
            self.nieve.append([i, random.uniform(1, 3)])

    def loop(self):
        for n in self.nieve:
            self.c.move(n[0], 0, n[1])
            if self.c.coords(n[0])[1] > ALTO:
                x = random.randint(0, ANCHO)
                self.c.coords(n[0], x, -5, x+2, -3)

        for p in self.particulas[:]:
            self.c.move(p[0], p[1], p[2])
            p[2] += 0.4
            p[3] -= 2
            if p[3] <= 0:
                self.c.delete(p[0])
                self.particulas.remove(p)

        self.root.after(1000 // FPS, self.loop)

root = tk.Tk()
JuegoCalendario(root)
root.mainloop()

