class Matriz_FA:
    # Inicializa la matriz de fichas amarillas
    def __init__(self): 
        self.FA = [
            [5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
            [0, 0, 0, 0, 3, 0, 5, 0, 0, 0, 0, 0]
        ] # FA: matriz que representa el número de fichas amarillas por casilla del tablero

    # Devuelve el estado de la casilla (a,b) de la matriz de fichas amarillas
    def estado_casilla_FA(self, a, b): 
        return self.FA[a][b]
    
    # getter
    def obtener_FA(self):
        return self.FA
    
    # Adiciona una ficha amarilla a la casilla (a,b)
    def adicionar_ficha_FA(self, a, b):
        self.FA[a][b] += 1

    # Elimina una ficha amarilla de la casilla (a,b)
    def eliminar_ficha_FA(self, a, b):
        self.FA[a][b] -= 1

    # Muestra la matriz de fichas amarillas
    def mostrar_FA(self):
        print('\nFA:', str(self.FA))