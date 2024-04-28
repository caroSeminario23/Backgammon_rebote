# from src import Jugador, Juego, Dado, Ficha

class Tablero:
    def __init__(self): # Inicializa el tablero como una matriz de 2x12 
        self.casillas = [['dao','v','v','v','dro','v','dro','v','v','v','v','dao'],
                         ['dro','v','v','v','dao','v','dao','v','v','v','v','dro']] # Inicializa las casillas

    def mover_ficha(self, color, a, b, c, d):
        # Mueve una ficha del color dado de la casilla (a,b) a la casilla (c,d)
        pass

    def capturar_ficha(self, color, a, b):
        # Captura una ficha del color opuesto en la casilla (a,b)
        pass

    def liberar_ficha(self, color, a, b):
        # Libera una ficha capturada del color dado a la casilla (a,b)
        pass

    def estado_casilla(self, a, b):
        # Devuelve el estado de la casilla (a,b)
        pass