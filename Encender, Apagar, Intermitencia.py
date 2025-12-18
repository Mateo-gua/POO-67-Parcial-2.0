import RPi.GPIO as GPIO
import time

class LEDModel:
    def __init__(self, pin=18):
        self.pin = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)
        self.estado = "APAGADO"

    def encender(self):
        GPIO.output(self.pin, GPIO.HIGH)
        self.estado = "ENCENDIDO"
        self.guardar_registro("ENCENDIDO")

    def apagar(self):
        GPIO.output(self.pin, GPIO.LOW)
        self.estado = "APAGADO"
        self.guardar_registro("APAGADO")

    def intermitencia(self, veces=5):
        for _ in range(veces):
            GPIO.output(self.pin, GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(self.pin, GPIO.LOW)
            time.sleep(0.5)
        self.estado = "INTERMITENCIA"
        self.guardar_registro("INTERMITENCIA")

    def get_estado(self):
        return self.estado

    def guardar_registro(self, accion):
        with open("registro_led.txt", "a") as archivo:
            archivo.write(f"{accion}\n")

    def limpiar(self):
        GPIO.cleanup()
