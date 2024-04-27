from src import Tablero, Jugador
class Juego:
    def __init__(self): # Inicializa un juego de backgammon
        self.tablero = Tablero()
        self.jugador1 = Jugador('rojo')
        self.jugador2 = Jugador('amarillo')

    def jugar(self):
        while not self.tablero.juego_terminado(): # Juega hasta que el juego termina
            for jugador in [self.jugador1, self.jugador2]: # Por cada jugador en el juego
                movimiento = jugador.jugar_turno(self.tablero) # El jugador decide qué movimiento hacer
                self.tablero.mover_ficha(jugador.color, movimiento) # Se mueve la ficha en el tablero

                if self.tablero.juego_terminado(): # Si el juego termina, se rompe el ciclo
                    break

        ganador = self.tablero.ganador() # Se determina el ganador del juego
        print(f'El ganador es el jugador con las fichas {ganador}!') # Se imprime el ganador

    def juego_terminado(self): # Devuelve True si el juego ha terminado
        finalizado = False
        if self.tablero.juego_terminado():
            finalizado = True
        return finalizado;
    
    def ganador(self): # Devuelve el color de las fichas del jugador ganador
        return self.tablero.ganador()
    
    def estado_juego(self): # Devuelve el estado actual del juego (quién está ganando, cuántas fichas quedan, etc.)
        return self.tablero.estado_juego()
    
    def mover_ficha(self, ficha, movimiento): # Mueve una ficha en el tablero según las reglas del backgammon
        self.tablero.mover_ficha(ficha, movimiento)