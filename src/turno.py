import random

class Turno: 
    def __init__(self, turno): # El primer jugador elije el turno que desea
        self.turno_actual = turno # Inicializa el turno a 'R' (rojo) o 'A' (amarillo) al azar

    def cambio_de_turno(self): # Cambia el turno al siguiente jugador
        if self.turno_actual == 'R':
            self.turno_actual = 'A'
        else:
            self.turno_actual = 'R'