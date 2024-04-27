# from src import Tablero, Juego, Dado, Ficha

class Jugador:
    def __init__(self, color):
        # Inicializa un jugador con un color de ficha
        self.color = color
        self.fichas = [Ficha(color, 'libre') for _ in range(15)]  # Cada jugador comienza con 15 fichas libres

    def jugar_turno(self, tablero):
        # Decide qué movimiento hacer basándose en el estado actual del tablero
        pass