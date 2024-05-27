class Matriz_FR:
    # Inicializa la matriz de fichas rojas
    def __init__(self): 
        self.FR = [
            [0, 0, 0, 0, 3, 0, 5, 0, 0, 0, 0, 0, 0, 0],
            [5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0]
        ] # FR: matriz que representa el número de fichas rojas por casilla del tablero
    
    # Devuelve el estado de la casilla (a,b) de la matriz de fichas rojas
    def estado_casilla_FR(self, a, b): 
        return self.FR[a][b]
    
    # getter
    def obtener_FR(self):
        return self.FR
    
    # Adiciona una ficha roja a la casilla (a,b)
    def adicionar_ficha_FR(self, a, b):
        self.FR[a][b] += 1
    
    # Elimina una ficha roja de la casilla (a,b)
    def eliminar_ficha_FR(self, a, b):
        self.FR[a][b] -= 1
    
    # Muestra la matriz de fichas rojas
    def mostrar_FR(self):
        print('\nFR:', str(self.FR))