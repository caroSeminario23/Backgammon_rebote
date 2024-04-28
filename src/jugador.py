from src import Ficha

class Jugador:
    def __init__(self, color): # Inicializa un jugador con un color de ficha (rojo o amarillo)
        self.color = color # 'R' o 'A'
        self.fichas = [Ficha(color, 'ordinaria') for _ in range(15)]  # Cada jugador comienza con 15 fichas ordinarias
    
    def jugar_turno(self, estado):
        # Selecciona una ficha y la mueve
        pass