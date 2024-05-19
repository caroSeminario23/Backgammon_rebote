class Tablero:
    # Inicializa el tablero como una matriz de 2x12 
    def __init__(self): 
        self.casillas = [['dao','v','v','v','dro','v','dro','v','v','v','v','dao'],
                         ['dro','v','v','v','dao','v','dao','v','v','v','v','dro']]

    # Devuelve el estado de la casilla (a,b)
    def estado_casilla(self, a, b): 
        return self.casillas[a][b]

    # Muestra el tablero
    def mostrar_tablero(self): 
        print('\nTablero:', str(self.casillas))
    
    # getter
    def obtener_casillas(self):
        return self.casillas
    
    # Convierte la casilla (a,b) en finalista
    def convertir_en_finalista(self, a, b):
        if self.casillas[a][b] == 'dao':
            self.casillas[a][b] = 'daf'
        elif self.casillas[a][b] == 'dro':
            self.casillas[a][b] = 'drf'
    
    # Convierte la casilla (a,b) en ordinaria
    def convertir_en_ordinaria(self, a, b):
        if self.casillas[a][b] == 'daf':
            self.casillas[a][b] = 'dao'
        elif self.casillas[a][b] == 'drf':
            self.casillas[a][b] = 'dro'
    
    # Convierte la casilla (a,b) en capturada
    def convertir_en_capturada(self, a, b):
        if self.casillas[a][b] == 'dao':
            self.casillas[a][b] = 'dac'
        elif self.casillas[a][b] == 'dro':
            self.casillas[a][b] = 'drc'
    
    # Convierte la casilla (a,b) en libre
    def convertir_en_libre(self, a, b):
        if self.casillas[a][b] == 'dac':
            self.casillas[a][b] = 'dao'
        elif self.casillas[a][b] == 'drc':
            self.casillas[a][b] = 'dro'
    
    # Convierte la casilla (a,b) en vacía
    def convertir_en_vacia(self, a, b):
        self.casillas[a][b] = 'v'