import random

class Dado: 
    def __init__(self): 
        # Inicializa un dado ordinario con valores del 1 al 6
        self.valores = list(range(1, 7)) # [1, 2, 3, 4, 5, 6]

    def lanzar(self): 
        # Lanza el dado y devuelve un valor aleatorio
        return random.choice(self.valores) # Devuelve un valor aleatorio de la lista de valores