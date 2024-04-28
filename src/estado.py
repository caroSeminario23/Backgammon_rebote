class Estado:
    def __init__(self, tablero, turno, fichas, moneda):
        self.tablero = tablero  # T: matriz que representa el tablero
        self.turno = turno  # t: turno
        self.fichas = fichas #[15,15,0,0,0,0,0,0]  # ndro, ndao, ndrf, ndaf, ndrc, ndac, ndrl, ndal: número de cada tipo de ficha
        self.moneda = moneda  # m: valor de la moneda 
        self.FR = [[0, 0, 0, 0, 3, 0, 5, 0, 0, 0, 0, 0],
                   [5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2]] # FR: matriz que representa el número de fichas rojas por casilla del tablero
        self.FA = [[5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
                   [0, 0, 0, 0, 3, 0, 5, 0, 0, 0, 0, 0]] # FA: matriz que representa el número de fichas amarillas por casilla del tablero

    # getters
    def get_tablero(self):
        return self.tablero
    
    def get_turno(self):
        return self.turno
    
    def get_fichas(self):
        return self.fichas
    
    def get_moneda(self):
        return self.moneda
    
    def get_FR(self):
        return self.FR
    
    def get_FA(self):
        return self.FA

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

    def estado_casilla_FR(self, a, b):
        return self.FR[a][b]
    
    def estado_casilla_FA(self, a, b):
        return self.FA[a][b]
    
    # Adicion de una ficha del tipo correspondiente
    def adicionar_ficha_dro():
        self.fichas[0] += 1

    def adicionar_ficha_dao():
        self.fichas[1] += 1
    
    def adicionar_ficha_drf():
        self.fichas[2] += 1
    
    def adicionar_ficha_daf():
        self.fichas[3] += 1
    
    def adicionar_ficha_drc():
        self.fichas[4] += 1

    def adicionar_ficha_dac():
        self.fichas[5] += 1
    
    def adicionar_ficha_drl():
        self.fichas[6] += 1
    
    def adicionar_ficha_dal():
        self.fichas[7] += 1
    
    # Eliminacion de una ficha del tipo correspondiente
    def eliminar_ficha_dro():
        self.fichas[0] -= 1
    
    def eliminar_ficha_dao():
        self.fichas[1] -= 1

    def eliminar_ficha_drf():
        self.fichas[2] -= 1
    
    def eliminar_ficha_daf():
        self.fichas[3] -= 1
    
    def eliminar_ficha_drc():
        self.fichas[4] -= 1
    
    def eliminar_ficha_dac():
        self.fichas[5] -= 1
    
    def eliminar_ficha_drl():
        self.fichas[6] -= 1
    
    def eliminar_ficha_dal():
        self.fichas[7] -= 1