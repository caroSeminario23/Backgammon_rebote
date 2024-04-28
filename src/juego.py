from src import Tablero, Jugador, Turno, Estado, Moneda, Fichas
class Juego:
    def __init__(self, turno): # Inicializa un juego de backgammon
        #self.tablero = Tablero()
        self.jugador1 = Jugador('rojo')
        self.jugador2 = Jugador('amarillo')
        #self.turno = Turno(turno)
        #self.fichas = [15,15,0,0,0,0,0,0]
        #self.moneda = Moneda()
        #self.estado = Estado(self.tablero, self.turno, self.fichas, self.moneda)
        self.estado = Estado(Turno(turno))

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
    def adro(self, a, b, n):
        # Calcular valor de c
        if b == 1:
            c = a-n
        elif b == 2:
            c = a+n
        elif b == 1 and n == 1:
            c = a

        # Calcular valor de d
        if a-n >= 1:
            d = b
        else:
            d = b+1

        # Verificar si el movimiento es válido
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
            tablero_2 = self.estado.get_tablero
            tablero_2.actualizar_casilla(a, b, valor_casilla)
            tablero_2.actualizar_casilla(c, d, valor_casilla_2)

            # ACTUALIZAR TIPOS DE FICHAS
            fichas_2 = self.estado.get_fichas
            if tablero_2.estado_casilla(c, d) == 'drf':
                fichas_2.adicionar_ficha_drf()
                fichas_2.eliminar_ficha_dro()

            # ACTUALIZAR FR
            FR_2 = self.estado.get_FR
            FR_2.eliminar_ficha_FR(a, b)
            FR_2.adicionar_ficha_FR(c, d)

            # Actualizar estado
            self.estado.actualizar_estado(tablero_2, 'A', fichas_2 , self.moneda.esperar_lanzamiento(), FR_2, self.estado.get_FA)

            # Se indica que el movimiento fue exitoso
            print('Movimiento exitoso')
        else:
            print('Movimiento no válido')
        
    # Verificar si adro es válido
    def movimiento_adro_valido(self, a, b, c, d, n): # Verificar si un movimiento es válido
        if (self.turno.get_turno_actual == 'R' and self.estado.get_moneda == 'a' and self.estado.get_tablero.estado_casilla(a,b) == 'dro' and 
            (self.estado.get_tablero.estado_casilla(c,d) == 'v' or self.estado.tablero.get_tablero.estado_casilla(c,d) == 'dro') and 
            self.estado.get_fichas[5] == 0 and (c >= 1 or c <= 12) and (d >= 1 or d <= 2) and (n >= 1 or n <= 6)):
            return True
        else:
            return False


    # REGLA 2
    # Avanzar dao de (a,b) a (c,d) según “n” posiciones -> adao(a,b,c,d,n)
    def ada(self, a, b, n): 
        # Calcular valor de c 
        if b == 2:
            c = a-n
        elif b == 1:
            c = a+n
        elif b == 2 and n == 1:
            c = a

        # Calcular valor de d
        if a-n >= 1:
            d = b
        else:
            d = b+1
        
        if self.movimiento_adao_valido(a,b,c,d,n) == True:
            # ACTUALIZAR TABLERO
            # Actualizar casilla (a,b)
            if self.estado.estado_casilla_FA(a,b) == 0:
                valor_casilla = 'v'
            elif self.estado.estado_casilla_FA(a,b) >= 0:
                valor_casilla = 'dao'

            # Actualizar casilla (c,d)
            if (c >= 1 and c <= 6) and (d == 1):
                valor_casilla_2 = 'dao'
            elif (c >= 1 and c <= 12) and (d == 2):
                valor_casilla_2 = 'dao'
            elif (c >= 7 and c <= 12) and (d == 1):
                valor_casilla_2 = 'daf'

            # Aplicar actualizaciones
            tablero_2 = self.estado.get_tablero
            tablero_2.actualizar_casilla(a, b, valor_casilla)
            tablero_2.actualizar_casilla(c, d, valor_casilla_2)

            # ACTUALIZAR TIPOS DE FICHAS
            fichas_2 = self.estado.get_fichas
            if tablero_2.estado_casilla(c, d) == 'daf':
                fichas_2.adicionar_ficha_daf()
                fichas_2.eliminar_ficha_dao()

            # ACTUALIZAR FA
            FA_2 = self.estado.get_FA
            FA_2.eliminar_ficha_FA(a, b)
            FA_2.adicionar_ficha_FA(c, d)

            # Actualizar estado
            self.estado.actualizar_estado(tablero_2, 'R', fichas_2 , self.moneda.esperar_lanzamiento(), self.estado.get_FR, FA_2)

            # Se indica que el movimiento fue exitoso
            print('Movimiento exitoso')
        else:
            print('Movimiento no válido')

    # Verificar si adao es válido
    def movimiento_adao_valido(self, a, b, c, d, n): # Verificar si un movimiento es válido
        if (self.estado.get_turno == 'A' and self.estado.get_moneda == 'a' and self.estado.get_tablero.estado_casilla(a,b) == 'dao' and 
            (self.estado.get_tablero.estado_casilla(c,d) == 'v' or self.estado.get_tablero.estado_casilla(c,d) == 'dao') and 
            self.estado.get_fichas[6] == 0 and (c >= 1 or c <= 12) and (d >= 1 or d <= 2) and (n >= 1 or n <= 6)):
            return True
        else:
            return False


    # REGLA 3
    # Avanzar drf de (a,b) a (c,d) según “n” posiciones -> adrf(a,b,c,d,n)
    def adrf(self, a, b, c, d, n):
        # Calcular valor de c
        c = a+n
        
        # Calcular valor de d
        d = 2
        
        if self.movimiento_adrf_valido(a,b,c,d,n) == True:
            # ACTUALIZAR TABLERO
            # Actualizar casilla (a,b)
            if self.estado.estado_casilla_FR(a,b) == 0:
                valor_casilla = 'v'
            elif self.estado.estado_casilla_FR(a,b) >= 0:
                valor_casilla = 'drf'

            # Actualizar casilla (c,d)
            valor_casilla_2 = 'drf'

            # Aplicar actualizaciones
            tablero_2 = self.estado.get_tablero
            tablero_2.actualizar_casilla(a, b, valor_casilla)
            tablero_2.actualizar_casilla(c, d, valor_casilla_2)

            # ACTUALIZAR TIPOS DE FICHAS
            fichas_2 = self.estado.get_fichas
            if tablero_2.estado_casilla(c, d) == 'drf':
                fichas_2.adicionar_ficha_drf()
                fichas_2.eliminar_ficha_drf()

            # ACTUALIZAR FR
            FR_2 = self.estado.get_FR
            FR_2.eliminar_ficha_FR(a, b)
            FR_2.adicionar_ficha_FR(c, d)

            # Actualizar estado
            self.estado.actualizar_estado(tablero_2, 'A', fichas_2 , self.moneda.esperar_lanzamiento(), FR_2, self.estado.get_FA)

            # Se indica que el movimiento fue exitoso
            print('Movimiento exitoso')
        else:
            print('Movimiento no válido')

    # Verificar si adrf es válido
    def movimiento_adrf_valido(self, a, b, c, d, n): # Verificar si un movimiento es válido
        if (self.estado.get_turno == 'R' and self.estado.get_moneda == 'a' and self.estado.get_tablero.estado_casilla(a,b) == 'drf' and 
            (self.estado.get_tablero.estado_casilla(c,d) == 'v' or self.estado.get_tablero.estado_casilla(c,d) == 'drf') and 
            self.estado.get_fichas[5] == 0 and (c >= 7 or c <= 12) and (d == 2) and (n >= 1 or n <= 6)):
            return True
        else:
            return False


    # REGLA 4
    # Avanzar daf de (a,b) a (c,d) según “n” posiciones -> adaf(a,b,c,d,n)
    def adaf(self, a, b, c, d, n):
        # Calcular valor de c
        c = a+n

        # Calcular valor de d
        d = 1

        if self.movimiento_adaf_valido(a,b,c,d,n) == True:
            # ACTUALIZAR TABLERO
            # Actualizar casilla (a,b)
            if self.estado.estado_casilla_FA(a,b) == 0:
                valor_casilla = 'v'
            elif self.estado.estado_casilla_FA(a,b) >= 0:
                valor_casilla = 'daf'

            # Actualizar casilla (c,d)
            valor_casilla_2 = 'daf'

            # Aplicar actualizaciones
            tablero_2 = self.estado.get_tablero
            tablero_2.actualizar_casilla(a, b, valor_casilla)
            tablero_2.actualizar_casilla(c, d, valor_casilla_2)

            # ACTUALIZAR TIPOS DE FICHAS
            fichas_2 = self.estado.get_fichas
            if tablero_2.estado_casilla(c, d) == 'daf':
                fichas_2.adicionar_ficha_daf()
                fichas_2.eliminar_ficha_daf()

            # ACTUALIZAR FA
            FA_2 = self.estado.get_FA
            FA_2.eliminar_ficha_FA(a, b)
            FA_2.adicionar_ficha_FA(c, d)

            # Actualizar estado
            self.estado.actualizar_estado(tablero_2, 'R', fichas_2 , self.moneda.esperar_lanzamiento(), self.estado.get_FR, FA_2)

            # Se indica que el movimiento fue exitoso
            print('Movimiento exitoso')
        else:
            print('Movimiento no válido')

    # Verificar si adaf es válido
    def movimiento_adaf_valido(self, a, b, c, d, n): # Verificar si un movimiento es válido
        if (self.estado.get_turno == 'A' and self.estado.get_moneda == 'a' and self.estado.get_tablero.estado_casilla(a,b) == 'daf' and 
            (self.estado.get_tablero.estado_casilla(c,d) == 'v' or self.estado.get_tablero.estado_casilla(c,d) == 'daf') and 
            self.estado.get_fichas[6] == 0 and (c >= 7 or c <= 12) and (d == 1) and (n >= 1 or n <= 6)):
            return True
        else:
            return False


    # REGLA 5
    # Retroceder dro de (a,b) a (c,d) según “n” posiciones -> rdro(a,b,c,d,n)
    def rdro(self, a, b, c, d, n):
        # Calcular valor de c
        if b == 1:
            c = a+n
        elif b == 2:
            c = a-n
        elif b == 1 and n == 1:
            c = a
        
        # Calcular valor de d
        if a+n >= 1 and a+n <= 12 and b == 1:
            d = b
        elif a-n > 1 and a-n <= 12 and b == 2:
            d = b
        elif a-n < 1 and b == 2:
            d = b-1

        if self.movimiento_rdro_valido(a,b,c,d,n) == True:
            # ACTUALIZAR TABLERO
            # Actualizar casilla (a,b)
            if self.estado.estado_casilla_FR(a,b) == 0:
                valor_casilla = 'v'
            elif self.estado.estado_casilla_FR(a,b) >= 0:
                valor_casilla = 'dro'

            # Actualizar casilla (c,d)
            valor_casilla_2 = 'dro'

            # Aplicar actualizaciones
            tablero_2 = self.estado.get_tablero
            tablero_2.actualizar_casilla(a, b, valor_casilla)
            tablero_2.actualizar_casilla(c, d, valor_casilla_2)

            # ACTUALIZAR TIPOS DE FICHAS
            fichas_2 = self.estado.get_fichas
            if tablero_2.estado_casilla(c, d) == 'dro':
                fichas_2.adicionar_ficha_dro()
                fichas_2.eliminar_ficha_dro()

            # ACTUALIZAR FR
            FR_2 = self.estado.get_FR
            FR_2.eliminar_ficha_FR(a, b)
            FR_2.adicionar_ficha_FR(c, d)

            # Actualizar estado
            self.estado.actualizar_estado(tablero_2, 'A', fichas_2 , self.moneda.esperar_lanzamiento(), FR_2, self.estado.get_FA)

            # Se indica que el movimiento fue exitoso
            print('Movimiento exitoso')
        else:
            print('Movimiento no válido')

    # Verificar si rdro es válido
    def movimiento_rdro_valido(self, a, b, c, d, n): # Verificar si un movimiento es válido
        if (self.estado.get_turno == 'R' and self.estado.get_moneda == 'r' and self.estado.get_tablero.estado_casilla(a,b) == 'dro' and 
            (self.estado.get_tablero.estado_casilla(c,d) == 'v' or self.estado.get_tablero.estado_casilla(c,d) == 'dro') and 
            self.estado.get_fichas[5] == 0 and (c >= 1 or c <= 12) and (d >= 1 or d <= 2) and (n >= 1 or n <= 6)):
            return True
        else:
            return False


    # REGLA 6
    # Retroceder dao de (a,b) a (c,d) según “n” posiciones -> rdao(a,b,c,d,n)
    def rdao(self, a, b, c, d, n):
        # Calcular valor de c
        if b == 2:
            c = a+n
        elif b == 1:
            c = a-n
        elif b == 2 and n == 1:
            c = a
        
        # Calcular valor de d
        if a-n >= 1 and a-n <= 12 and b == 2:
            d = b
        elif a-n > 1 and a-n <= 12 and b == 1:
            d = b
        elif a-n < 1 and b == 1:
            d = b+1

        if self.movimiento_rdao_valido(a,b,c,d,n) == True:
            # ACTUALIZAR TABLERO
            # Actualizar casilla (a,b)
            if self.estado.estado_casilla_FA(a,b) == 0:
                valor_casilla = 'v'
            elif self.estado.estado_casilla_FA(a,b) >= 0:
                valor_casilla = 'dao'

            # Actualizar casilla (c,d)
            valor_casilla_2 = 'dao'

            # Aplicar actualizaciones
            tablero_2 = self.estado.get_tablero
            tablero_2.actualizar_casilla(a, b, valor_casilla)
            tablero_2.actualizar_casilla(c, d, valor_casilla_2)

            # ACTUALIZAR TIPOS DE FICHAS
            fichas_2 = self.estado.get_fichas
            if tablero_2.estado_casilla(c, d) == 'dao':
                fichas_2.adicionar_ficha_dao()
                fichas_2.eliminar_ficha_dao()

            # ACTUALIZAR FA
            FA_2 = self.estado.get_FA
            FA_2.eliminar_ficha_FA(a, b)
            FA_2.adicionar_ficha_FA(c, d)

            # Actualizar estado
            self.estado.actualizar_estado(tablero_2, 'R', fichas_2 , self.moneda.esperar_lanzamiento(), self.estado.get_FR, FA_2)

            # Se indica que el movimiento fue exitoso
            print('Movimiento exitoso')
        else:
            print('Movimiento no válido')

    # Verificar si rdao es válido
    def movimiento_rdao_valido(self, a, b, c, d, n): # Verificar si un movimiento es válido
        if (self.estado.get_turno == 'A' and self.estado.get_moneda == 'r' and self.estado.get_tablero.estado_casilla(a,b) == 'dao' and 
            (self.estado.get_tablero.estado_casilla(c,d) == 'v' or self.estado.get_tablero.estado_casilla(c,d) == 'dao') and 
            self.estado.get_fichas[6] == 0 and (c >= 1 or c <= 12) and (d >= 1 or d <= 2) and (n >= 1 or n <= 6)):
            return True
        else:
            return False


    # REGLA 7
    # Capturar con dro de (a,b) a dao de (c,d) según “n” posiciones -> cdro(a,b,c,d,n)
    def cdro(self, a, b, c, d, n):
        # Calcular valor de c
        if b == 1:
            c = a-n
        elif b == 2:
            c = a+n
        elif b == 1 and n == 1:
            c = a
        
        # Calcular valor de d
        if a-n >= 1:
            d = b
        elif a-n < 1:
            d = b+1

        if self.movimiento_cdro_valido(a,b,c,d,n) == True:
            # ACTUALIZAR TABLERO
            # Actualizar casilla (a,b)
            if self.estado.estado_casilla_FR(a,b) == 0:
                valor_casilla = 'v'
            elif self.estado.estado_casilla_FR(a,b) >= 0:
                valor_casilla = 'dro'

            # Actualizar casilla (c,d)
            valor_casilla_2 = 'dro'

            # Aplicar actualizaciones
            tablero_2 = self.estado.get_tablero
            tablero_2.actualizar_casilla(a, b, valor_casilla)
            tablero_2.actualizar_casilla(c, d, valor_casilla_2)

            # ACTUALIZAR TIPOS DE FICHAS
            fichas_2 = self.estado.get_fichas
            if tablero_2.estado_casilla(c, d) == 'dro':
                fichas_2.adicionar_ficha_dac()
                fichas_2.eliminar_ficha_dao()

            # ACTUALIZAR FR
            FR_2 = self.estado.get_FR
            FR_2.eliminar_ficha_FR(a, b)
            FR_2.adicionar_ficha_FR(c, d)

            FA_2 = self.estado.get_FA
            FA_2.eliminar_ficha_FA(c, d)

            # Actualizar estado
            self.estado.actualizar_estado(tablero_2, 'A', fichas_2 , self.moneda.esperar_lanzamiento(), FR_2, FA_2)

            # Se indica que el movimiento fue exitoso
            print('Movimiento exitoso')
        else:
            print('Movimiento no válido')

    # Verificar si cdro es válido
    def movimiento_cdro_valido(self, a, b, c, d, n): # Verificar si un movimiento es válido
        if (self.estado.get_turno == 'R' and self.estado.get_moneda == 'a' and self.estado.get_tablero.estado_casilla(a,b) == 'dro' and 
            self.estado.get_tablero.estado_casilla(c,d) == 'dao' and self.estado.estado_casilla_FA(c,d) == 1
            and self.estado.get_fichas[5] == 0 and (c >= 1 or c <= 12) and (d >= 1 or d <= 2) and (n >= 1 or n <= 6)):
            return True
        else:
            return False


    # REGLA 8
    # Capturar con dao de (a,b) a dro de (c,d) según “n” posiciones -> cdao(a,b,c,d,n)
    def cdao(self, a, b, c, d, n):
        # Calcular valor de c
        if b == 2:
            c = a-n
        elif b == 1:
            c = a+n
        elif b == 2 and n == 1:
            c = a
        
        # Calcular valor de d
        if a-n >= 1:
            d = b
        elif a-n < 1:
            d = b+1

        if self.movimiento_cdao_valido(a,b,c,d,n) == True:
            # ACTUALIZAR TABLERO
            # Actualizar casilla (a,b)
            if self.estado.estado_casilla_FA(a,b) == 0:
                valor_casilla = 'v'
            elif self.estado.estado_casilla_FA(a,b) >= 0:
                valor_casilla = 'dao'

            # Actualizar casilla (c,d)
            valor_casilla_2 = 'dao'

            # Aplicar actualizaciones
            tablero_2 = self.estado.get_tablero
            tablero_2.actualizar_casilla(a, b, valor_casilla)
            tablero_2.actualizar_casilla(c, d, valor_casilla_2)

            # ACTUALIZAR TIPOS DE FICHAS
            fichas_2 = self.estado.get_fichas
            if tablero_2.estado_casilla(c, d) == 'dao':
                fichas_2.adicionar_ficha_drc()
                fichas_2.eliminar_ficha_dro()

            # ACTUALIZAR FA
            FA_2 = self.estado.get_FA
            FA_2.eliminar_ficha_FA(a, b)
            FA_2.adicionar_ficha_FA(c, d)

            FR_2 = self.estado.get_FR
            FR_2.eliminar_ficha_FR(c, d)

            # Actualizar estado
            self.estado.actualizar_estado(tablero_2, 'R', fichas_2 , self.moneda.esperar_lanzamiento(), FR_2, FA_2)

            # Se indica que el movimiento fue exitoso
            print('Movimiento exitoso')
        else:
            print('Movimiento no válido')
    
    # Verificar si cdao es válido
    def movimiento_cdao_valido(self, a, b, c, d, n): # Verificar si un movimiento es válido
        if (self.estado.get_turno == 'A' and self.estado.get_moneda == 'a' and self.estado.get_tablero.estado_casilla(a,b) == 'dao' and 
            self.estado.get_tablero.estado_casilla(c,d) == 'dro' and self.estado.estado_casilla_FR(c,d) == 1
            and self.estado.get_fichas[6] == 0 and (c >= 1 or c <= 12) and (d >= 1 or d <= 2) and (n >= 1 or n <= 6)):
            return True
        else:
            return False


    # REGLA 9
    # Liberar drc a (a,b) según “n” posiciones -> ldrc(a,b,n)
    def ldrc(self, a, b, n):
        # Calcular valor de a
        a = 12 - n

        # Calcular valor de b
        b = 1

        if self.movimiento_ldrc_valido(a,b,n) == True:
            # Aplicar actualizaciones
            tablero_2 = self.estado.get_tablero
            tablero_2.actualizar_casilla(a, b, 'dro')

            # ACTUALIZAR TIPOS DE FICHAS
            fichas_2 = self.estado.get_fichas
            if tablero_2.estado_casilla(a, b) == 'dro':
                fichas_2.adicionar_ficha_dro()
                fichas_2.eliminar_ficha_drc()

            # ACTUALIZAR FR
            FR_2 = self.estado.get_FR
            FR_2.adicionar_ficha_FR(a, b)

            # Actualizar estado
            self.estado.actualizar_estado(tablero_2, 'A', fichas_2 , self.moneda.esperar_lanzamiento(), FR_2, self.estado.get_FA)

            # Se indica que el movimiento fue exitoso
            print('Movimiento exitoso')
        else:
            print('Movimiento no válido')
    
    # Verificar si ldrc es válido
    def movimiento_ldrc_valido(self, a, b, n): # Verificar si un movimiento es válido
        if (self.estado.get_turno == 'R' and self.estado.get_moneda == 'a' and self.estado.get_fichas[5] >= 1 
            and self.estado.get_tablero.estado_casilla(a,b) == 'drc' and self.estado.get_tablero.estado_casilla(a,b) == 'v' 
            and (a >= 1 and a <= 12) and (n >= 1 or n <= 6)):
            return True
        else:
            return False


    # REGLA 10
    # Liberar dac a (a,b) según “n” posiciones -> ldac(a,b,n)
    def ldac(self, a, b, n):
        # Calcular valor de a
        a = 12 - n

        # Calcular valor de b
        b = 2

        if self.movimiento_ldac_valido(a,b,n) == True:
            # Aplicar actualizaciones
            tablero_2 = self.estado.get_tablero
            tablero_2.actualizar_casilla(a, b, 'dao')

            # ACTUALIZAR TIPOS DE FICHAS
            fichas_2 = self.estado.get_fichas
            if tablero_2.estado_casilla(a, b) == 'dao':
                fichas_2.adicionar_ficha_dao()
                fichas_2.eliminar_ficha_dac()

            # ACTUALIZAR FA
            FA_2 = self.estado.get_FA
            FA_2.adicionar_ficha_FA(a, b)

            # Actualizar estado
            self.estado.actualizar_estado(tablero_2, 'R', fichas_2 , self.moneda.esperar_lanzamiento(), self.estado.get_FR, FA_2)

            # Se indica que el movimiento fue exitoso
            print('Movimiento exitoso')
        else:
            print('Movimiento no válido')

    # Verificar si ldac es válido
    def movimiento_ldac_valido(self, a, b, n): # Verificar si un movimiento es válido
        if (self.estado.get_turno == 'A' and self.estado.get_moneda == 'a' and self.estado.get_fichas[6] >= 1 
            and self.estado.get_tablero.estado_casilla(a,b) == 'dac' and self.estado.get_tablero.estado_casilla(a,b) == 'v' 
            and (a >= 1 and a <= 12) and (n >= 1 or n <= 6)):
            return True
        else:
            return False
        
    
    # REGLA 11
    # Rebotar drf de (a,b) a (c,d) según “n” posiciones -> rdrf(a,b,c,d,n)
    def rdrf(self, a, b, c, d, n):
        # Calcular valor de c
        c = 26 - (a+n)

        # Calcular valor de d
        d = 2

        if self.movimiento_rdrf_valido(a,b,c,d,n) == True:
            # ACTUALIZAR TABLERO
            # Actualizar casilla (a,b)
            if self.estado.estado_casilla_FR(a,b) == 0:
                valor_casilla = 'v'
            elif self.estado.estado_casilla_FR(a,b) >= 0:
                valor_casilla = 'drf'

            # Actualizar casilla (c,d)
            valor_casilla_2 = 'drf'

            # Aplicar actualizaciones
            tablero_2 = self.estado.get_tablero
            tablero_2.actualizar_casilla(a, b, valor_casilla)
            tablero_2.actualizar_casilla(c, d, valor_casilla_2)

            # ACTUALIZAR TIPOS DE FICHAS
            fichas_2 = self.estado.get_fichas
            if tablero_2.estado_casilla(c, d) == 'drf':
                fichas_2.adicionar_ficha_drf()
                fichas_2.eliminar_ficha_drf()

            # ACTUALIZAR FR
            FR_2 = self.estado.get_FR
            FR_2.eliminar_ficha_FR(a, b)
            FR_2.adicionar_ficha_FR(c, d)

            # Actualizar estado
            self.estado.actualizar_estado(tablero_2, 'A', fichas_2 , self.moneda.esperar_lanzamiento(), FR_2, self.estado.get_FA)

            # Se indica que el movimiento fue exitoso
            print('Movimiento exitoso')
        else:
            print('Movimiento no válido')
    
    # Verificar si rdrf es válido
    def movimiento_rdrf_valido(self, a, b, c, d, n): # Verificar si un movimiento es válido
        if (self.estado.get_turno == 'R' and self.estado.get_moneda == 'a' and self.estado.get_tablero.estado_casilla(a,b) == 'drf' and 
            self.estado.get_fichas[3] <= 15 and (self.estado.get_tablero.estado_casilla(c,d) == 'v' or self.estado.get_tablero.estado_casilla(c,d) == 'drf') 
            and self.estado.get_fichas[5] == 0 and (c >= 8 and c <= 12) and (a >= 8 and a <= 12) and (b == 2) and (n >= 1 or n <= 6)) and a+n > 13:
            return True
        else:
            return False
        
    
    # REGLA 12
    # Rebotar daf de (a,b) a (c,d) según “n” posiciones -> rdaf(a,b,c,d,n)
    def rdaf(self, a, b, c, d, n):
        # Calcular valor de c
        c = 26 - (a+n)

        # Calcular valor de d
        d = 1

        if self.movimiento_rdaf_valido(a,b,c,d,n) == True:
            # ACTUALIZAR TABLERO
            # Actualizar casilla (a,b)
            if self.estado.estado_casilla_FA(a,b) == 0:
                valor_casilla = 'v'
            elif self.estado.estado_casilla_FA(a,b) >= 0:
                valor_casilla = 'daf'

            # Actualizar casilla (c,d)
            valor_casilla_2 = 'daf'

            # Aplicar actualizaciones
            tablero_2 = self.estado.get_tablero
            tablero_2.actualizar_casilla(a, b, valor_casilla)
            tablero_2.actualizar_casilla(c, d, valor_casilla_2)

            # ACTUALIZAR TIPOS DE FICHAS
            fichas_2 = self.estado.get_fichas
            if tablero_2.estado_casilla(c, d) == 'daf':
                fichas_2.adicionar_ficha_daf()
                fichas_2.eliminar_ficha_daf()

            # ACTUALIZAR FA
            FA_2 = self.estado.get_FA
            FA_2.eliminar_ficha_FA(a, b)
            FA_2.adicionar_ficha_FA(c, d)

            # Actualizar estado
            self.estado.actualizar_estado(tablero_2, 'R', fichas_2 , self.moneda.esperar_lanzamiento(), self.estado.get_FR, FA_2)
            
            # Se indica que el movimiento fue exitoso
            print('Movimiento exitoso')
        else:
            print('Movimiento no válido')

    # Verificar si rdaf es válido
    def movimiento_rdaf_valido(self, a, b, c, d, n): # Verificar si un movimiento es válido
        if (self.estado.get_turno == 'A' and self.estado.get_moneda == 'a' and self.estado.get_tablero.estado_casilla(a,b) == 'daf' and 
            self.estado.get_fichas[4] <= 15 and (self.estado.get_tablero.estado_casilla(c,d) == 'v' or self.estado.get_tablero.estado_casilla(c,d) == 'daf') 
            and self.estado.get_fichas[6] == 0 and (c >= 8 and c <= 12) and (a >= 8 and a <= 12) and (b == 1) and (n >= 1 or n <= 6)) and a+n > 13:
            return True
        else:
            return False


    # REGLA 13
    # Sacar drf de (a,b) a fuera del tablero -> sdrf(a,b)
    def sdrf(self, a, b, n):
        if self.movimiento_sdrf_valido(a,b, n) == True:
            # Actualizar casilla (a,b)
            if self.estado.estado_casilla_FR(a,b) == 0:
                valor_casilla = 'v'
            elif self.estado.estado_casilla_FR(a,b) >= 0:
                valor_casilla = 'drf'

            # Aplicar actualizaciones
            tablero_2 = self.estado.get_tablero
            tablero_2.actualizar_casilla(a, b, valor_casilla)

            # ACTUALIZAR TIPOS DE FICHAS
            fichas_2 = self.estado.get_fichas
            fichas_2.eliminar_ficha_drf()
            fichas_2.adicionar_ficha_drl()

            # ACTUALIZAR FR
            FR_2 = self.estado.get_FR
            FR_2.eliminar_ficha_FR(a, b)

            # Actualizar estado
            self.estado.actualizar_estado(tablero_2, 'A', fichas_2 , self.moneda.esperar_lanzamiento(), FR_2, self.estado.get_FA)

            # Se indica que el movimiento fue exitoso
            print('Movimiento exitoso')
        else:
            print('Movimiento no válido')
    
    # Verificar si sdrf es válido
    def movimiento_sdrf_valido(self, a, b, n): # Verificar si un movimiento es válido
        if (self.estado.get_turno == 'R' and self.estado.get_moneda == 'a' and self.estado.get_tablero.estado_casilla(a,b) == 'drf' and 
            self.estado.get_fichas[3] <= 15 and (a >= 8 and a <= 12) and (b == 2) and self.estado.get_fichas[5] == 0
            and (n >= 1 or n <= 6) and a+n == 13):
            return True
        else:
            return False
        
    
    # REGLA 14

    def sdaf(self, a, b):
        # Sacar daf de (a,b) a fuera del tablero
        pass