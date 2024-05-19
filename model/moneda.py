import random
from pync import Notifier

class Moneda:
    # Inicializa la moneda con 'i' (inmóvil)
    def __init__(self): 
        self.valor_actual = 'i'
        self.valores = ['a', 'r']
    
    # Lanza la moneda y devuelve un estado aleatorio a: avanzar, r: retroceder
    def lanzar(self): 
        return random(self.valores)
    
    # Espera a que la moneda se detenga
    def esperar_lanzamiento(self): 
        self.valor_actual = 'i'
    
    # Muestra el estado actual de la moneda
    def notificar(self):
        Notifier.notify('Moneda: ' + self.valor_actual, title='Moneda', sound='default')

    def mostrar_moneda(self):
        print('\nMoneda:', self.valor_actual)

    # getter
    def get_valor_actual(self):
        return self.valor_actual