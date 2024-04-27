import random

class Turno:
    def __init__(self):
        # Inicializa el turno a 'R' (rojo) o 'A' (amarillo) al azar
        self.turno_actual = random.choice(['R', 'A'])