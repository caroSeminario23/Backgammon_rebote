class Tablero:
    def __init__(self): # Inicializa el tablero como una matriz de 2x12 
        self.casillas = [['dao','v','v','v','dro','v','dro','v','v','v','v','dao'],
                         ['dro','v','v','v','dao','v','dao','v','v','v','v','dro']] # Inicializa las casillas

    def estado_casilla(self, a, b): # Devuelve el estado de la casilla (a,b)
        return self.casillas[a][b]
        pass

    def actualizar_casilla(self, a, b, valor):
        self.casillas[a][b] = valor