class Fichas:
    def __init__(self):
        self.fichas = [15, 15, 0, 0, 0, 0, 0, 0] # [dro, dao, drf, daf, drc, dac, drl, dal]

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

    # Muestra el estado de las fichas
    def __str__(self):
        return 'Fichas: ' + str(self.fichas)
    
    def mostrar_fichas(self):
        print('Fichas:', self.fichas)