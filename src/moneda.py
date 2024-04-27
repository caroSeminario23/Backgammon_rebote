import random

class Moneda:
    def __init__(self): # Inicializa la moneda con 'i' (inmóvil)
        self.estado_actual = 'i'
    
    def lanzar_moneda(self): # Lanza la moneda y devuelve un estado aleatorio a: avanzar, r: retroceder
        self.estado_actual = random.choice(['a', 'r']) # Actualiza el estado de la moneda con un valor aleatorio
        return self.estado_actual # Devuelve el estado de la moneda
    
    def esperar_lanzamiento(self): # Espera a que la moneda se detenga
        self.estado_actual = 'i' # Actualiza el estado de la moneda a inmóvil