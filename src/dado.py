# from src import Tablero, Jugador, Juego, Ficha, Turno, Moneda
import random

class Dado:
    def __init__(self):
        # Inicializa un dado ordinario
        self.valores = list(range(1, 7))

    def lanzar(self):
        # Devuelve un valor aleatorio entre 1 y 6
        return random.choice(self.valores)