import random
from pync import Notifier

class Dado: 
    # Inicializa un dado ordinario con valores del 1 al 6
    def __init__(self): 
        self.valor_actual = 0
        self.valores = list(range(1, 7)) # [1, 2, 3, 4, 5, 6]

    # Lanza el dado y devuelve un valor aleatorio
    def lanzar(self): 
        self.valor_actual = random.choice(self.valores) # Devuelve un valor aleatorio de la lista de valores
    
    # Muestra el valor del dado
    def mostrar(self):
        Notifier.notify('Dado: ' + str(self.valor_actual), title='Dado', sound='default')

    # getter
    def get_valores(self):
        return self.valores
    
    def get_valor_actual(self):
        return self.valor_actual
    
    def esperar_lanzamiento(self):
        self.valor_actual = 0
    
    def set_valor_actual(self, valor):
        self.valor_actual = valor