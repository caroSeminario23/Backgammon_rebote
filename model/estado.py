from model.tablero import Tablero
from model.turno import Turno
from model.n_fichas import N_Fichas
from model.moneda import Moneda
from model.matriz_FR import Matriz_FR
from model.matriz_FA import Matriz_FA
from model.dado import Dado

class Estado:
    # Inicializa el estado del juego
    '''def __init__(self):
        self.tablero = Tablero()  # T: matriz que representa el tablero
        self.turno = Turno()  # t: turno
        self.n_fichas = N_Fichas() #[15,15,0,0,0,0,0,0]  # ndro, ndao, ndrf, ndaf, ndrc, ndac, ndrl, ndal: número de cada tipo de ficha
        self.moneda = Moneda()  # m: valor de la moneda 
        self.FR = Matriz_FR() # FR: matriz que representa el número de fichas rojas por casilla del tablero
        self.FA = Matriz_FA() # FA: matriz que representa el número de fichas amarillas por casilla del tablero
    '''
    def __init__(self, turno=None):
        self.tablero = Tablero()
        if turno is None:
            self.turno = 'No escogido'
        else:
            self.turno = turno
        self.n_fichas = N_Fichas()
        self.moneda = 'i'
        self.dado = 0
        self.FR = Matriz_FR()
        self.FA = Matriz_FA()

    def set_tablero(self, tablero):
        self.tablero = tablero

    def set_turno(self, turno):
        self.turno = turno

    def set_n_fichas(self, n_fichas):
        self.n_fichas = n_fichas

    def set_moneda(self, moneda):
        self.moneda = moneda
    
    def set_dado(self, dado):
        self.dado = dado

    def set_FR(self, FR):
        self.FR = FR
    
    def set_FA(self, FA):
        self.FA = FA
        
    # getters
    def get_tablero(self):
        """Devuelve el tablero del juego"""
        return self.tablero
    
    def get_turno(self):
        """Devuelve el turno actual del juego"""
        return self.turno
    
    def get_n_fichas(self):
        """Devuelve las fichas del juego"""
        return self.n_fichas

    def get_dado(self):
        """Devuelve el valor del dado"""
        return self.dado
    
    def get_moneda(self):
        """Devuelve el valor de la moneda"""
        return self.moneda
    
    def get_FR(self):
        """Devuelve la matriz de fichas rojas"""
        return self.FR
    
    def get_FA(self):
        """Devuelve la matriz de fichas amarillas"""
        return self.FA

    # Actualiza el estado del juego
    def actualizar_estado(self, nuevo_tablero, nuevo_turno, nuevo_n_fichas, nueva_moneda, nueva_FR, nueva_FA): 
        self.tablero = nuevo_tablero
        self.turno = nuevo_turno
        self.n_fichas = nuevo_n_fichas
        self.moneda = nueva_moneda
        self.FR = nueva_FR
        self.FA = nueva_FA

    # Muestra el estado actual del juego
    def mostrar_estado(self): 
        print('\n-------------------')
        self.tablero.mostrar_tablero()
        self.turno.mostrar_turno()
        self.n_fichas.mostrar_n_fichas()
        self.moneda.mostrar_moneda()
        self.dado.mostrar()
        self.FR.mostrar_FR()
        self.FA.mostrar_FA()
        print('-------------------')