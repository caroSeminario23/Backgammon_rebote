class N_Fichas:
    # Clase que representa la cantidad de fichas del juego por tipo
    def __init__(self):
        self.fichas = [13, 13, 2, 2, 0, 0, 0, 0] # [dro, dao, drf, daf, drc, dac, drl, dal]

    def get_ndro(self):
        return self.fichas[0]

    def get_ndao(self):
        return self.fichas[1]
    
    def get_ndrf(self):
        return self.fichas[2]
    
    def get_ndaf(self):
        return self.fichas[3]
    
    def get_ndrc(self):
        return self.fichas[4]
    
    def get_ndac(self):
        return self.fichas[5]
    
    def get_ndrl(self):
        return self.fichas[6]
    
    def get_ndal(self):
        return self.fichas[7]
    
    # Adicion de una ficha del tipo correspondiente
    def adicionar_ficha_dro(self):
        self.fichas[0] += 1

    def adicionar_ficha_dao(self):
        self.fichas[1] += 1

    def adicionar_ficha_drf(self):
        self.fichas[2] += 1

    def adicionar_ficha_daf(self):
        self.fichas[3] += 1

    def adicionar_ficha_drc(self):
        self.fichas[4] += 1

    def adicionar_ficha_dac(self):
        self.fichas[5] += 1

    def adicionar_ficha_drl(self):
        self.fichas[6] += 1

    def adicionar_ficha_dal(self):
        self.fichas[7] += 1
    
    # Eliminacion de una ficha del tipo correspondiente
    def eliminar_ficha_dro(self):
        self.fichas[0] -= 1

    def eliminar_ficha_dao(self):
        self.fichas[1] -= 1

    def eliminar_ficha_drf(self):
        self.fichas[2] -= 1

    def eliminar_ficha_daf(self):
        self.fichas[3] -= 1

    def eliminar_ficha_drc(self):
        self.fichas[4] -= 1

    def eliminar_ficha_dac(self):
        self.fichas[5] -= 1

    def eliminar_ficha_drl(self):
        self.fichas[6] -= 1

    def eliminar_ficha_dal(self):
        self.fichas[7] -= 1

    def get_fichas(self):
        return self.fichas

    def set_fichas(self, fichas):
        self.fichas = fichas

    # Obtener el valor de una celda del arreglo
    def get_ficha(self, i):
        return self.fichas[i]

    # Muestra el estado de todas las fichas
    def mostrar_n_fichas(self):
        print('\nN fichas por tipo:')
        print('dro:', self.fichas[0])
        print('dao:', self.fichas[1])
        print('drf:', self.fichas[2])
        print('daf:', self.fichas[3])
        print('drc:', self.fichas[4])
        print('dac:', self.fichas[5])
        print('drl:', self.fichas[6])
        print('dal:', self.fichas[7])