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

    def verificar_estado_meta(self):
        if self.estado.fichas['drl'] == 15:
            return 'Rojo gana'
        elif self.estado.fichas['dal'] == 15:
            return 'Amarillo gana'
        elif self.estado.fichas['drl'] < 15 and self.estado.fichas['dal'] < 15 and self.tiempo_juego > 30:
            return 'Empate'
        else:
            return 'El juego continúa'

    def adr(self, a, b, c, d, n):
        # Avanzar dr de (a,b) a (c,d) según “n” posiciones
        pass

    def ada(self, a, b, c, d, n):
        # Avanzar da de (a,b) a (c,d) según “n” posiciones
        pass

    def adrf(self, a, b, c, d, n):
        # Avanzar drf de (a,b) a (c,d) según “n” posiciones
        pass

    def adaf(self, a, b, c, d, n):
        # Avanzar daf de (a,b) a (c,d) según “n” posiciones
        pass

    def rdr(self, a, b, c, d, n):
        # Retroceder dr de (a,b) a (c,d) según “n” posiciones
        pass

    def rda(self, a, b, c, d, n):
        # Retroceder da de (a,b) a (c,d) según “n” posiciones
        pass

    def cdr(self, a, b, c, d, n):
        # Captura con dr de (a,b) a da de (c,d) según “n” posiciones
        pass

    def cda(self, a, b, c, d, n):
        # Captura con da de (a,b) a dr de (c,d) según “n” posiciones
        pass

    def ldrc(self, a, b, n):
        # Liberar drc a (a,b) según “n” posiciones
        pass

    def ldac(self, a, b, n):
        # Liberar dac a (a,b) según “n” posiciones
        pass

    def rdrf(self, a, b, c, d, n):
        # Rebotar drf de (a,b) a (c,d) según “n” posiciones
        pass

    def rdaf(self, a, b, c, d, n):
        # Rebotar daf de (a,b) a (c,d) según “n” posiciones
        pass

    def sdrf(self, a, b):
        # Sacar drf de (a,b) a fuera del tablero
        pass

    def sdaf(self, a, b):
        # Sacar daf de (a,b) a fuera del tablero
        pass