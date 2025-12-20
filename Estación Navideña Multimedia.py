import RPi.GPIO as GPIO
import adafruit_dht
import board
import pygame
import time

class NavidadModel:
    def __init__(self):
        # --- CONFIGURACIÃ“N DE PINES ---
        self.PIN_LED = 18    # LED en GPIO 18
        self.PIN_BOTON = 25  # BotÃ³n en GPIO 25
        self.PIN_DHT = board.D4 # Sensor en GPIO 4
        
        # --- INICIALIZACIÃ“N DE GPIO ---
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.PIN_LED, GPIO.OUT)
        # Pull-up resistor para el botÃ³n (conectar a GND)
        GPIO.setup(self.PIN_BOTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        
        # --- INICIALIZACIÃ“N DE SENSOR (PROTEGIDA) ---
        self.sensor = None
        try:
            self.sensor = adafruit_dht.DHT11(self.PIN_DHT)
            print("Sensor DHT11 iniciado correctamente.")
        except Exception as e:
            print(f"ADVERTENCIA: No se pudo iniciar el sensor DHT11. Error: {e}")
            print("El programa continuarÃ¡ sin lecturas de clima.")
        
        # --- INICIALIZACIÃ“N DE AUDIO ---
        try:
            pygame.mixer.init()
            # Cargar archivo de mÃºsica
            pygame.mixer.music.load("jingle_bells.mp3")
            print("Sistema de audio listo.")
        except Exception as e:
            print(f"Error de Audio: {e}")

    def obtener_clima(self):
        # Si el sensor no cargÃ³, devolvemos None sin crashear
        if self.sensor is None:
            return None, None
            
        try:
            return self.sensor.temperature, self.sensor.humidity
        except RuntimeError:
            # Error comÃºn de lectura del DHT11, lo ignoramos
            return None, None
        except Exception as e:
            print(f"Error leyendo sensor: {e}")
            return None, None

    def leer_boton(self):
        # Retorna True si se presiona (conecta a Tierra)
        if GPIO.input(self.PIN_BOTON) == GPIO.LOW:
            time.sleep(0.05) # Filtro anti-rebote
            return True
        return False

    def controlar_led(self, estado):
        GPIO.output(self.PIN_LED, GPIO.HIGH if estado else GPIO.LOW)

    def reproducir_audio(self):
        try:
            if not pygame.mixer.music.get_busy():
                print("Reproduciendo mÃºsica...")
                pygame.mixer.music.play()
        except Exception as e:
            print(f"Error al reproducir: {e}")

    def limpiar_gpio(self):
        if self.sensor:
            self.sensor.exit()
        GPIO.cleanup()
