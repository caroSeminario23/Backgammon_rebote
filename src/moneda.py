import random

class Moneda:
    def __init__(self):
        # Inicializa la moneda a 'a' (avanza), 'r' (retrocede) o 'i' (inmóvil) al azar
        self.estado_actual = random.choice(['a', 'r', 'i'])