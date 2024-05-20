#alternativa para "src"
import sys
sys.path.append('.')

from src.jugador import Jugador
from src.turno import Turno
from src.estado import Estado
class Juego:
    def __init__(self, turno): # Inicializa un juego de backgammon
        self.jugador1 = Jugador('rojo')
        self.jugador2 = Jugador('amarillo')
        self.estado = Estado(Turno(turno))
        self.tiempo_juego = 0  # Inicializa el tiempo de juego en 0

    # Solicitud al usuario para que escoja su turno
    def elegir_turno(self): # El primer jugador elije el turno que desea
        turno = input('Elige el turno (R/A): ')
        print('Turno:', turno)
        return turno

    # Juega una partida de backgammon rebote
    def jugar(self):
        while self.verificar_estado_meta() == 'El juego continúa': # Juega hasta que el juego termina
            for jugador in [self.jugador1, self.jugador2]:
                movimiento = jugador.jugar_turno(self.estado)
                self.mover_ficha(jugador.color, movimiento)
                if self.verificar_estado_meta() != 'El juego continúa':
                    print(self.verificar_estado_meta())
                    break
    
    # Mover una ficha en el tablero según las reglas del backgammon
    def mover_ficha(self, ficha, movimiento): # Mueve una ficha en el tablero según las reglas del backgammon
        self.tablero.mover_ficha(ficha, movimiento)


    # VERIFICACION DEL ESTADO META
    def verificar_estado_meta(self):
        if self.estado.get_fichas().get_ficha(6) == 15:
            print('Rojo gana')
            return 'Rojo gana'
        elif self.estado.get_fichas().get_ficha(7) == 15:
            print('Amarillo gana')
            return 'Amarillo gana'
        elif self.estado.get_fichas().get_ficha(6) < 15 and self.estado.get_fichas().get_ficha(7) < 15 and self.tiempo_juego > 30:
            print('Empate')
            return 'Empate'
        else:
            print('El juego continúa')
            return 'El juego continúa'

    # REGLAS DEL JUEGO
    # Avanzar dro de (a,b) a (c,d) según “n” posiciones -> adro(a,b,c,d,n)
    def adro(self, a, b, n):
        # Calcular valor de d 
        if a == 0:
            d = b + n
        elif a == 1:
            d = b - n
            if d<0 :
                d = n - b - 1

        # Calcular valor de c
        if b+n>= 0 and b+n <= 11 and a == 0:
            c = 0
        elif b-n >= 0 and b-n <= 11 and a == 1:
            c = 1
        elif b-n < 0 and a == 1:
            c = 0


        # Verificar si el movimiento es válido
        if self.movimiento_adro_valido(a,b,c,d,n) == True:
            # ACTUALIZAR TABLERO
            # Actualizar casilla (a,b)
            if self.estado.estado_casilla_FR(a,b) == 0:
                valor_casilla = 'v'
            elif self.estado.estado_casilla_FR(a,b) >= 0:
                valor_casilla = 'dro'

            # Actualizar casilla (c,d)
            if (d >= 0 and d <= 5) and (c == 0):
                valor_casilla_2 = 'dro'
            elif (d >= 0 and d <= 11) and (c == 1):
                valor_casilla_2 = 'dro'
            elif (d >= 6 and d <= 11) and (c == 0):
                valor_casilla_2 = 'drf'

            # Aplicar actualizaciones
            tablero_2 = self.estado.get_tablero()
            tablero_2.actualizar_casilla(a, b, valor_casilla)
            tablero_2.actualizar_casilla(c, d, valor_casilla_2)

            # ACTUALIZAR TIPOS DE FICHAS
            fichas_2 = self.estado.get_fichas()
            if tablero_2.estado_casilla(c, d) == 'drf':
                fichas_2.adicionar_ficha_drf()
                fichas_2.eliminar_ficha_dro()

            # ACTUALIZAR FR
            FR_2 = self.estado.get_FR()
            self.estado.eliminar_ficha_FR(a, b)
            self.estado.adicionar_ficha_FR(c, d)

            # Actualizar estado
            self.estado.actualizar_estado(tablero_2, 'A', fichas_2 , self.estado.moneda.esperar_lanzamiento(), FR_2, self.estado.get_FA)

            # Se indica que el movimiento fue exitoso
            print('Movimiento exitoso_R1')
        else:
            print('Movimiento no válido_R1')
        
    # Verificar si adro es válido
    def movimiento_adro_valido(self, a, b, c, d, n): # Verificar si un movimiento es válido
        if (self.estado.get_turno().get_turno_actual() == 'R' and 
            self.estado.get_moneda().estado_actual == 'a' and 
            self.estado.get_tablero().estado_casilla(a,b) == 'dro' and 
            (self.estado.get_tablero().estado_casilla(c,d) == 'v' or self.estado.get_tablero().estado_casilla(c,d) == 'dro') and 
            self.estado.get_fichas().get_ficha(4) == 0 and (c >= 0 or c <= 1) and (d >= 0 or d <= 11) and (n >= 1 or n <= 6)):
            return True
        else:
            return False
        
    # REGLA 2
    # Avanzar dao de (a,b) a (c,d) según “n” posiciones -> adao(a,b,c,d,n)
    def adao(self, a, b, n): 
        # Calcular valor de d 
        if a == 1:
            d = b + n
        elif a == 0:
            d = b - n
            if d<0 :
                d = n - b - 1

        # Calcular valor de c
        if b-n>= 0 and b-n <= 11 and a == 0:
            c = 0
        elif b+n >= 0 and b+n <= 11 and a == 1:
            c = 1
        elif b-n < 0 and a == 0:
            c = 1

        #print("VALOR DE A: "+str(a)+" VAlor de B: "+str(b)+" v. de C: "+str(c)+" V. de D: "+str(d))
        
        if self.movimiento_adao_valido(a,b,c,d,n) == True:
            # ACTUALIZAR TABLERO
            # Actualizar casilla (a,b)
            if self.estado.estado_casilla_FA(a,b) == 0:
                valor_casilla = 'v'
            elif self.estado.estado_casilla_FA(a,b) >= 0:
                valor_casilla = 'dao'

            # Actualizar casilla (c,d)
            if (d >= 0 and d <= 5) and (c == 1):
                valor_casilla_2 = 'dao'
            elif (d >= 0 and d <= 11) and (c == 0):
                valor_casilla_2 = 'dao'
            elif (d >= 6 and d <= 11) and (c == 1):
                valor_casilla_2 = 'daf'

            # Aplicar actualizaciones
            tablero_2 = self.estado.get_tablero()
            tablero_2.actualizar_casilla(a, b, valor_casilla)
            tablero_2.actualizar_casilla(c, d, valor_casilla_2)

            # ACTUALIZAR TIPOS DE FICHAS
            fichas_2 = self.estado.get_fichas()
            if tablero_2.estado_casilla(c, d) == 'daf':
                fichas_2.adicionar_ficha_daf()
                fichas_2.eliminar_ficha_dao()

            # ACTUALIZAR FA
            FA_2 = self.estado.get_FA()
            self.estado.eliminar_ficha_FA(a, b)
            self.estado.adicionar_ficha_FA(c, d)

            # Actualizar estado
            self.estado.actualizar_estado(tablero_2, 'R', fichas_2 , self.estado.moneda.esperar_lanzamiento(), self.estado.get_FR, FA_2)

            # Se indica que el movimiento fue exitoso   
            print('Movimiento exitoso_R2')
            #for fila in self.estado.tablero.casillas:
            #    print(fila)
        else:
            print('Movimiento no válido_R2')

    # Verificar si adao es válido
    def movimiento_adao_valido(self, a, b, c, d, n): # Verificar si un movimiento es válido
        if (self.estado.get_turno().get_turno_actual() == 'A' and 
            self.estado.get_moneda().estado_actual == 'a' and 
            self.estado.get_tablero().estado_casilla(a,b) == 'dao' and 
            (self.estado.get_tablero().estado_casilla(c,d) == 'v' or self.estado.get_tablero().estado_casilla(c,d) == 'dao') and 
            self.estado.get_fichas().get_ficha(5) == 0 and (c >= 0 or c <= 1) and (d >= 0 or d <= 11) and (n >= 1 or n <= 6)):
            return True
        else:
            return False

    # REGLA 3
    # Avanzar drf de (a,b) a (c,d) según “n” posiciones -> adrf(a,b,c,d,n)
    def adrf(self, a, b, n):
        # Calcular valor de d
        d = b+n
        # Calcular valor de c
        c = 0
        
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
            tablero_2 = self.estado.get_tablero()
            tablero_2.actualizar_casilla(a, b, valor_casilla)
            tablero_2.actualizar_casilla(c, d, valor_casilla_2)

            # ACTUALIZAR TIPOS DE FICHAS
            fichas_2 = self.estado.get_fichas()
            if tablero_2.estado_casilla(c, d) == 'drf':
                #DUDAS:SERIA LO MISMO ADICIONAR Y LUEGO ELIMINAR
                fichas_2.adicionar_ficha_drf()
                fichas_2.eliminar_ficha_drf()

            # ACTUALIZAR FR
            FR_2 = self.estado.get_FR()
            self.estado.eliminar_ficha_FR(a, b)
            self.estado.adicionar_ficha_FR(c, d)

            # Actualizar estado
            self.estado.actualizar_estado(tablero_2, 'A', fichas_2 , self.estado.moneda.esperar_lanzamiento(), FR_2, self.estado.get_FA)

            # Se indica que el movimiento fue exitoso
            print('Movimiento exitoso_R3')
        else:
            print('Movimiento no válido_R3')

    # Verificar si adrf es válido
    def movimiento_adrf_valido(self, a, b, c, d, n): # Verificar si un movimiento es válido
        if (self.estado.get_turno().get_turno_actual() == 'R' and 
            self.estado.get_moneda().estado_actual == 'a' and 
            self.estado.get_tablero().estado_casilla(a,b) == 'drf' and 
            (self.estado.get_tablero().estado_casilla(c,d) == 'v' or self.estado.get_tablero().estado_casilla(c,d) == 'drf') and 
            self.estado.get_fichas().get_ficha(4) == 0 and (d >= 6 or d <= 11) and (c == 0) and (n >= 1 or n <= 6)):
            return True
        else:
            return False

    # REGLA 4
    # Avanzar daf de (a,b) a (c,d) según “n” posiciones -> adaf(a,b,c,d,n)
    def adaf(self, a, b, n):
        # Calcular valor de d
        d = b+n
        # Calcular valor de c
        c = 1

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
            tablero_2 = self.estado.get_tablero()
            tablero_2.actualizar_casilla(a, b, valor_casilla)
            tablero_2.actualizar_casilla(c, d, valor_casilla_2)

            # ACTUALIZAR TIPOS DE FICHAS
            fichas_2 = self.estado.get_fichas()
            if tablero_2.estado_casilla(c, d) == 'daf':
                #DUDAS:SERIA LO MISMO ADICIONAR Y LUEGO ELIMINAR
                fichas_2.adicionar_ficha_daf()
                fichas_2.eliminar_ficha_daf()

            # ACTUALIZAR FA
            FA_2 = self.estado.get_FA()
            self.estado.eliminar_ficha_FA(a, b)
            self.estado.adicionar_ficha_FA(c, d)

            # Actualizar estado
            self.estado.actualizar_estado(tablero_2, 'R', fichas_2 , self.estado.moneda.esperar_lanzamiento(), self.estado.get_FR, FA_2)

            # Se indica que el movimiento fue exitoso
            print('Movimiento exitoso_R4')
        else:
            print('Movimiento no válido_R4')

    # Verificar si adaf es válido
    def movimiento_adaf_valido(self, a, b, c, d, n): # Verificar si un movimiento es válido
        if (self.estado.get_turno().get_turno_actual() == 'A' and 
            self.estado.get_moneda().estado_actual == 'a' and 
            self.estado.get_tablero().estado_casilla(a,b) == 'daf' and 
            (self.estado.get_tablero().estado_casilla(c,d) == 'v' or self.estado.get_tablero().estado_casilla(c,d) == 'daf') and 
            self.estado.get_fichas().get_ficha(5) == 0 and (d >= 6 or d <= 11) and (c == 1) and (n >= 1 or n <= 6)):
            return True
        else:
            return False


    # REGLA 5
    # Retroceder dro de (a,b) a (c,d) según “n” posiciones -> rdro(a,b,c,d,n)
    def movimiento_rdro_valido(self, a, b, c, d, n): # Verificar si un movimiento es válido
        if (self.estado.get_turno().get_turno_actual() == 'R' and 
            self.estado.get_moneda().estado_actual == 'r' and
            self.estado.get_tablero().estado_casilla(a,b) == 'dro' and 
            (self.estado.get_tablero().estado_casilla(c,d) == 'v' or self.estado.get_tablero().estado_casilla(c,d) == 'dro') and 
            self.estado.get_fichas().get_ficha(4) == 0 and (c >= 0 and c <=1) and (d >= 0 and d <= 11) and 
            (n >= 1 and n <= 6)):
            return True
        else:
            return False

    def rdro(self, a, b, c, d ,n):
    # Calcular valor de d
        if a == 1:
            d = b+n
        elif a == 0:
            d = b-n
            if d < 0:
                d = n-b-1

        # Calcular valor de c
        if b+n >= 0 and b+n <= 11 and a == 1:
            c = 1
        elif b-n >= 0 and b-n <= 11 and a == 0:
            c = 0
        elif b-n < 0 and a == 0:
            c = 1


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
            tablero_2 = self.estado.get_tablero()
            tablero_2.actualizar_casilla(a, b, valor_casilla)
            tablero_2.actualizar_casilla(c, d, valor_casilla_2)

            # ACTUALIZAR TIPOS DE FICHAS
            fichas_2 = self.estado.get_fichas()
            if tablero_2.estado_casilla(c, d) == 'dro':
                fichas_2.adicionar_ficha_dro()
                fichas_2.eliminar_ficha_dro()

            # ACTUALIZAR FR
            FR_2 = self.estado.get_FR()
            self.estado.eliminar_ficha_FR(a, b)
            self.estado.adicionar_ficha_FR(c, d)

            # Actualizar estado

            self.estado.actualizar_estado(tablero_2, 'A', fichas_2 , self.estado.moneda.esperar_lanzamiento() , FR_2, self.estado.get_FA)

            # Se indica que el movimiento fue exitoso
            print('Movimiento exitoso_R5')
        else:
            print('Movimiento no válido_R5')

    # REGLA 6
    # Retroceder dao de (a,b) a (c,d) según “n” posiciones -> rdao(a,b,c,d,n)
    def rdao(self, a, b, c, d, n):
        # Calcular valor de d
        if a == 0:
            d = b + n
        elif a == 1:
            d = b - n
            if d<0 :
                d = n - b - 1

        # Calcular valor de c
        if b+n>= 0 and b+n <= 11 and a == 0:
            c = 0
        elif b-n >= 0 and b-n <= 11 and a == 1:
            c = 1
        elif b-n < 0 and a == 1:
            c = 0

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
            tablero_2 = self.estado.get_tablero()
            tablero_2.actualizar_casilla(a, b, valor_casilla)
            tablero_2.actualizar_casilla(c, d, valor_casilla_2)

            # ACTUALIZAR TIPOS DE FICHAS
            fichas_2 = self.estado.get_fichas()
            if tablero_2.estado_casilla(c, d) == 'dao':
                fichas_2.adicionar_ficha_dao()
                fichas_2.eliminar_ficha_dao()

            # ACTUALIZAR FA
            FA_2 = self.estado.get_FA()
            self.estado.eliminar_ficha_FA(a, b)
            self.estado.adicionar_ficha_FA(c,d)
                    
            # Actualizar estado
            self.estado.actualizar_estado(tablero_2, 'R', fichas_2 , self.estado.moneda.esperar_lanzamiento() , self.estado.get_FR, FA_2)

            # Se indica que el movimiento fue exitoso
            print('Movimiento exitoso_R6')
        else:
            print('Movimiento no válido_R6')

    # Verificar si rdao es válido
    def movimiento_rdao_valido(self, a, b, c, d, n): # Verificar si un movimiento es válido
        if (self.estado.get_turno().get_turno_actual() == 'A' and 
            self.estado.get_moneda().estado_actual == 'r' and 
            self.estado.get_tablero().estado_casilla(a,b) == 'dao' and 
            (self.estado.get_tablero().estado_casilla(c,d) == 'v' or self.estado.get_tablero().estado_casilla(c,d) == 'dao') and 
            self.estado.get_fichas().get_ficha(5) == 0 and (c >= 0 or c <= 1) and (d >= 0 or d <= 11) and (n >= 1 or n <= 6)):
            return True
        else:
            return False

    # REGLA 7
    # Capturar con dro de (a,b) a dao de (c,d) según “n” posiciones -> cdro(a,b,c,d,n)
    def cdro(self, a, b, c, d, n):
      # Calcular valor de d
        if a == 0:
            d = b + n
        elif a == 1:
            d = b - n
            if d<0 :
                d = n - b - 1

        # Calcular valor de c
        if b+n>= 0 and b+n <= 11 and a == 0:
            c = 0
        elif b-n >= 0 and b-n <= 11 and a == 1:
            c = 1
        elif b-n < 0 and a == 1:
            c = 0

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
            tablero_2 = self.estado.get_tablero()
            tablero_2.actualizar_casilla(a, b, valor_casilla)
            tablero_2.actualizar_casilla(c, d, valor_casilla_2)

            # ACTUALIZAR TIPOS DE FICHAS
            fichas_2 = self.estado.get_fichas()
            if tablero_2.estado_casilla(c, d) == 'dro':
                fichas_2.adicionar_ficha_dac()
                fichas_2.eliminar_ficha_dao()

            # ACTUALIZAR FR
            FR_2 = self.estado.get_FR()
            self.estado.eliminar_ficha_FR(a,b)
            self.estado.adicionar_ficha_FR(c,d)

            FA_2 = self.estado.get_FA()
            self.estado.eliminar_ficha_FA(c,d)

            # Actualizar estado
            self.estado.actualizar_estado(tablero_2, 'A', fichas_2 , self.estado.moneda.esperar_lanzamiento(), FR_2, FA_2)

            # Se indica que el movimiento fue exitoso
            print('Movimiento exitoso_R7')
        else:
            print('Movimiento no válido_R7')

    def movimiento_cdro_valido(self, a, b, c, d, n): # Verificar si un movimiento es válido
            if (self.estado.get_turno().get_turno_actual() == 'R' and 
                self.estado.get_moneda().estado_actual == 'a' and 
                self.estado.get_tablero().estado_casilla(a, b) == 'dro' and 
                self.estado.get_tablero().estado_casilla(c, d) == 'dao' and 
                self.estado.estado_casilla_FA(c, d) == 1 and 
                self.estado.get_fichas().get_ficha(4) == 0 and 
                (0 <= c <= 1) and 
                (0 <= d <= 11) and 
                (1 <= n <= 6)):
                return True
            else:
                return False
    # REGLA 8
    # Capturar con dao de (a,b) a dro de (c,d) según “n” posiciones -> cdao(a,b,c,d,n)
    def cdao(self, a, b, c, d, n):
         # Calcular valor de d
        if a == 1:
            d = b + n
        elif a == 2:
            d = b - n
            if d<=0 :
                d = n - b + 1
        
        # Calcular valor de c
        if b+n>= 1 and b+n <= 12 and a == 1:
            c = 1
        elif b-n >= 1 and b-n <= 12 and a == 2:
            c = 2
        elif b-n < 0 and a == 2:
            c = 1

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
            print('Movimiento exitoso_R8')
        else:
            print('Movimiento no válido_R8')
    
    # Verificar si cdao es válido
    def movimiento_cdao_valido(self, a, b, c, d, n): # Verificar si un movimiento es válido
        if(self.estado.get_turno == 'A' and 
            self.estado.get_moneda == 'a' and 
            self.estado.get_tablero.estado_casilla(a,b) == 'dao' and 
            self.estado.get_tablero.estado_casilla(c,d) == 'dro' and 
            self.estado.estado_casilla_FR(c,d) == 1 and 
            self.estado.get_fichas[5] == 0 and 
            (1 <= c <= 2) and 
            (1 <= d <= 12) and 
            (1 <= n <= 6)):
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
        if (self.estado.get_turno == 'R' and self.estado.get_moneda == 'a' and self.estado.get_fichas[4] >= 1 
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
        if (self.estado.get_turno == 'A' and self.estado.get_moneda == 'a' and self.estado.get_fichas[5] >= 1 
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
            self.estado.get_fichas[2] <= 15 and (self.estado.get_tablero.estado_casilla(c,d) == 'v' or self.estado.get_tablero.estado_casilla(c,d) == 'drf') 
            and self.estado.get_fichas[4] == 0 and (c >= 8 and c <= 12) and (a >= 8 and a <= 12) and (b == 2) and (n >= 1 or n <= 6)) and a+n > 13:
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
            self.estado.get_fichas[3] <= 15 and (self.estado.get_tablero.estado_casilla(c,d) == 'v' or self.estado.get_tablero.estado_casilla(c,d) == 'daf') 
            and self.estado.get_fichas[5] == 0 and (c >= 8 and c <= 12) and (a >= 8 and a <= 12) and (b == 1) and (n >= 1 or n <= 6)) and a+n > 13:
            return True
        else:
            return False


    # REGLA 13
    # Sacar drf de (a,b) a fuera del tablero -> sdrf(a,b, n)
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
            self.estado.get_fichas[2] <= 15 and (a >= 8 and a <= 12) and (b == 2) and self.estado.get_fichas[4] == 0
            and (n >= 1 or n <= 6) and a+n == 13):
            return True
        else:
            return False
        
    
    # REGLA 14
    # Sacar daf de (a,b) a fuera del tablero -> sdaf(a,b, n)
    def sdaf(self, a, b, n):
        if self.movimiento_sdaf_valido(a,b, n) == True:
            # Actualizar casilla (a,b)
            if self.estado.estado_casilla_FA(a,b) == 0:
                valor_casilla = 'v'
            elif self.estado.estado_casilla_FA(a,b) >= 0:
                valor_casilla = 'daf'

            # Aplicar actualizaciones
            tablero_2 = self.estado.get_tablero
            tablero_2.actualizar_casilla(a, b, valor_casilla)

            # ACTUALIZAR TIPOS DE FICHAS
            fichas_2 = self.estado.get_fichas
            fichas_2.eliminar_ficha_daf()
            fichas_2.adicionar_ficha_dal()

            # ACTUALIZAR FA
            FA_2 = self.estado.get_FA
            FA_2.eliminar_ficha_FA(a, b)

            # Actualizar estado
            self.estado.actualizar_estado(tablero_2, 'R', fichas_2 , self.moneda.esperar_lanzamiento(), self.estado.get_FR, FA_2)

            # Se indica que el movimiento fue exitoso
            print('Movimiento exitoso')
        else:
            print('Movimiento no válido')

    # Verificar si sdaf es válido
    def movimiento_sdaf_valido(self, a, b, n): # Verificar si un movimiento es válido
        if (self.estado.get_turno == 'A' and self.estado.get_moneda == 'a' and self.estado.get_tablero.estado_casilla(a,b) == 'daf' and 
            self.estado.get_fichas[3] <= 15 and (a >= 8 and a <= 12) and (b == 2) and self.estado.get_fichas[5] == 0
            and (n >= 1 or n <= 6) and a+n == 13):
            return True
        else:
            return False