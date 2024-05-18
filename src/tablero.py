class Tablero:
    def __init__(self): # Inicializa el tablero como una matriz de 2x12 
        self.casillas = [['dao','v','v','v','dro','v','dro','v','v','v','v','dao'],
                         ['dro','v','v','v','dao','v','dao','v','v','v','v','dro']] # Inicializa las casillas

    def estado_casilla(self, a, b): # Devuelve el estado de la casilla (a,b)
        return self.casillas[a][b]
        
    def actualizar_casilla(self, a, b, valor):
        self.casillas[a][b] = valor

    def mostrar_tablero(self): # Muestra el tablero
        for i in range(2):
            for j in range(12):
                print(self.casillas[i][j], end=' ')
            print()
        print('-------------------')
    
    def obtener_casillas(self):
        return self.casillas
    
    def convertir_en_finalista(self, a, b):
        if self.casillas[a][b] == 'dao':
            self.casillas[a][b] = 'daf'
        elif self.casillas[a][b] == 'dro':
            self.casillas[a][b] = 'drf'
    
    def convertir_en_ordinaria(self, a, b):
        if self.casillas[a][b] == 'daf':
            self.casillas[a][b] = 'dao'
        elif self.casillas[a][b] == 'drf':
            self.casillas[a][b] = 'dro'
    
    def convertir_en_capturada(self, a, b):
        if self.casillas[a][b] == 'dao':
            self.casillas[a][b] = 'dac'
        elif self.casillas[a][b] == 'dro':
            self.casillas[a][b] = 'drc'
    
    def convertir_en_libre(self, a, b):
        if self.casillas[a][b] == 'dac':
            self.casillas[a][b] = 'dao'
        elif self.casillas[a][b] == 'drc':
            self.casillas[a][b] = 'dro'
    
    def convertir_en_vacia(self, a, b):
        self.casillas[a][b] = 'v'