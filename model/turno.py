import random

class Turno: 
    def __init__(self): 
        self.turno_actual = random.choice(['R', 'A']) # Inicializa el turno a 'R' (rojo) o 'A' (amarillo) al azar

    # gettter
    def get_turno_actual(self):
        return self.turno_actual

    def cambio_de_turno(self): # Cambia el turno al siguiente jugador
        if self.turno_actual == 'R':
            self.turno_actual = 'A'
        else:
            self.turno_actual = 'R'

    def mostrar_turno(self):
        print('\nTurno:', self.turno_actual)