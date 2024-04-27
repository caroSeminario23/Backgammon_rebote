class Estado:
    def __init__(self, tablero, turno, fichas, moneda):
        self.tablero = tablero  # T: matriz que representa el tablero
        self.turno = turno  # t: turno
        self.fichas = fichas  # ndr, nda, ndrf, ndaf, ndrc, ndac, ndrl, ndal: número de cada tipo de ficha
        self.moneda = moneda  # m: valor de la moneda 
        self.FR = [[0, 0, 0, 0, 3, 0, 5, 0, 0, 0, 0, 0],
                   [5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2]] # FR: matriz que representa el número de fichas rojas por casilla del tablero
        self.FA = [[5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
                   [0, 0, 0, 0, 3, 0, 5, 0, 0, 0, 0, 0]] # FA: matriz que representa el número de fichas amarillas por casilla del tablero

    def actualizar_estado(self, nuevo_tablero, nuevo_turno, nuevas_fichas, nueva_moneda, nueva_FR, nueva_FA): # Actualiza el estado del juego
        self.tablero = nuevo_tablero
        self.turno = nuevo_turno
        self.fichas = nuevas_fichas
        self.moneda = nueva_moneda
        self.FR = nueva_FR
        self.FA = nueva_FA

    def mostrar_estado(self): # Muestra el estado actual del juego
        print('Tablero:', self.tablero)
        print('Turno:', self.turno)
        print('Fichas:', self.fichas)
        print('Moneda:', self.moneda)
        print('FR:', self.FR)
        print('FA:', self.FA)
        print('-------------------')