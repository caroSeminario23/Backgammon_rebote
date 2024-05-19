class Jugador:
    def __init__(self, pseudonimo, colorFicha):
        self.pseudonimo = pseudonimo
        self.colorFicha = colorFicha
    
    def mostrar(self):
        print('Jugador:', self.pseudonimo, self.colorFicha)

    def get_pseudonimo(self):
        return self.pseudonimo
    
    def get_colorFicha(self):
        return self.colorFicha