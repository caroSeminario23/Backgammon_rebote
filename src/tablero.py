# from src import Jugador, Juego, Dado, Ficha

class Tablero:
    def __init__(self):
        # Inicializa un tablero de 12x2
        self.tablero = [['v' for _ in range(12)] for _ in range(2)] # 'v' representa una casilla vacía en el tablero


    def mover_ficha(self, ficha, movimiento):
        # Mueve una ficha en el tablero según las reglas del backgammon
        pass

    def estado_juego(self):

        pass # Devuelve el estado actual del juego (quién está ganando, cuántas fichas quedan, etc.)