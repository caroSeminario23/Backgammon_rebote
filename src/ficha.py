# from src import Tablero, Jugador, Juego, Dado

class Ficha:
    def __init__(self, color, estado):
        # Inicializa una ficha con un color y un estado
        self.color = color
        self.estado = estado  # 'finalista', 'capturada', 'libre'