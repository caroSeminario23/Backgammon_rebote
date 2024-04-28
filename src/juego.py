from src import Tablero, Jugador, Turno, Estado, Moneda, Fichas
class Juego:
    def __init__(self, turno): # Inicializa un juego de backgammon
        self.tablero = Tablero()
        self.jugador1 = Jugador('rojo')
        self.jugador2 = Jugador('amarillo')
        self.turno = Turno(turno)
        self.fichas = [15,15,0,0,0,0,0,0]
        self.moneda = Moneda()
        self.estado = Estado(self.tablero, self.turno, self.fichas, self.moneda)

    def elegir_turno(self): # El primer jugador elije el turno que desea
        turno = input('Elige el turno (R/A): ')
        return turno

    def jugar(self): # Juega una partida de backgammon
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



    # REGLAS DEL JUEGO
    # Avanzar dro de (a,b) a (c,d) según “n” posiciones -> adro(a,b,c,d,n)
    def adro(self, a, b, c, d, n):
        if self.movimiento_adro_valido(a,b,c,d,n) == True:
            # ACTUALIZAR TABLERO
            # Actualizar casilla (a,b)
            if self.estado.estado_casilla_FR(a,b) == 0:
                valor_casilla = 'v'
            elif self.estado.estado_casilla_FR(a,b) >= 0:
                valor_casilla = 'dro'

            # Actualizar casilla (c,d)
            if (c >= 1 and c <= 6) and (d == 2):
                valor_casilla_2 = 'dro'
            elif (c >= 1 and c <= 12) and (d == 1):
                valor_casilla_2 = 'dro'
            elif (c >= 7 and c <= 12) and (d == 2):
                valor_casilla_2 = 'drf'

            # Aplicar actualizaciones
            tablero_2 = self.tablero.actualizar_casilla(a, b, valor_casilla)
            tablero_2 = tablero_2.actualizar_casilla(c, d, valor_casilla_2)

            # ACTUALIZAR TIPOS DE FICHAS
            fichas_2 = self.estado.get_fichas
            if tablero_2.estado_casilla(c, d) == 'drf':
                fichas_2.adicionar_ficha_drf()

            # ACTUALIZAR FR
            FR_2 = self.estado.get_FR
            FR_2.eliminar_ficha_FR(a, b)
            FR_2.adicionar_ficha_FR(c, d)

            # Actualizar estado
            self.estado.actualizar_estado(tablero_2, 'A', fichas_2 , self.moneda.esperar_lanzamiento(), FR_2, self.estado.get_FA)
        
    # Verificar si adro es válido
    def movimiento_adro_valido(self, a, b, c, d, n): # Verificar si un movimiento es válido
        if (self.turno.get_turno_actual == 'R' and self.tablero.estado_casilla(a, b) == 'dro' and 
            (self.tablero.estado_casilla(c, d) == 'v' or self.tablero.estado_casilla(c, d) == 'dro') and 
            self.estado.get_fichas[5] == 0 and (c >= 1 or c <= 12) and (d >= 1 or d <= 2) and (n >= 1 or n <= 6)):
            return True
        else:
            return False

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