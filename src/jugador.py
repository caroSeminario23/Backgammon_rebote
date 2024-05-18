from src.ficha import Ficha
from src.dado import Dado
from src.moneda import Moneda

class Jugador:
    def __init__(self, color): # Inicializa un jugador con un color de ficha (rojo o amarillo)
        self.color = color # 'R' o 'A'
        self.fichas = [Ficha(color, 'o') for _ in range(15)]  # Cada jugador comienza con 15 fichas ordinarias

    def __init__(self, pseudonimo, colorFicha):
        self.pseudonimo = pseudonimo
        self.colorFicha = colorFicha
        #self.fichas = [Ficha(color, 'o') for _ in range(15)]
    
    def jugar_turno(self, estado):
        valor_dado = Dado().lanzar()
        valor_moneda = Moneda().lanzar_moneda()
        return valor_dado, valor_moneda