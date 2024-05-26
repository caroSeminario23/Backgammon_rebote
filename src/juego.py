#alternativa para "src"
import sys
sys.path.append('.')

from src.jugador import Jugador
from src.turno import Turno
from src.estado import Estado
class Juego:

    #estado_Actual = Estado()
    
    def __init__(self,turno):
        self.estado_actual = Estado(Turno(turno))
    
    def obtener_estado(self):
        return self.estado_actual
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
        
    # Verificar si adro es válido
    def movimiento_adro_valido(self, a, b, c, d, n, estado_actual): # Verificar si un movimiento es válido
        # Verificar si el turno es del jugador rojo
        if self.estado_actual.get_turno().get_turno_actual() == 'R' and self.estado_actual.get_moneda().estado_actual == 'a':
            if (self.estado_actual.get_tablero().estado_casilla(a,b) == 'dro') and (self.estado_actual.get_tablero().estado_casilla(c,d) == 'v' or self.estado_actual.get_tablero().estado_casilla(c,d) == 'dro'):
                if self.estado_actual.get_fichas().get_ficha(4) == 0:
                    if (c >= 0 and c <= 1) and (d >= 0 and d <= 11) and (n >= 1 and n <= 6):
                        # VALIDACION DE MOVIMIENTO (PARTE 1)
                        if b==1 and n==1 and c==a:
                            validacion1 = True;
                        elif b==2 and n>=1 and n<=2 and c==a:
                            validacion1 = True;
                        elif b==3 and n>=1 and n<=3 and c==a:
                            validacion1 = True;
                        elif b==4 and n>=1 and n<=4 and c==a:
                            validacion1 = True;
                        elif b==5 and n>=1 and n<=5 and c==a:
                            validacion1 = True;
                        elif b>=6 and b<=11 and n>=1 and n<=6 and c==a:
                            validacion1 = True;
                        elif b==0 and n>=1 and n<=6 and c==0:
                            validacion1 = True;
                        elif b==1 and n>=2 and n<=6 and c==a-1:
                            validacion1 = True;
                        elif b==2 and n>=3 and n<=6 and c==a-1:
                            validacion1 = True;
                        elif b==3 and n>=4 and n<=6 and c==a-1:
                            validacion1 = True;
                        elif b==4 and n>=5 and n<=6 and c==a-1:
                            validacion1 = True;
                        elif b==5 and n==5:
                            validacion1 = True;
                        else:
                            validacion1 = False;

                        # VALIDACION DE MOVIMIENTO (PARTE 2)
                        if b>=6 and b<=11 and n>=1 and n<=6 and d==b-n and a==1:
                            validacion2 = True;
                        elif b==5 and n>=1 and n<=5 and d==b-n and a==1:
                            validacion2 = True;
                        elif b==4 and n>=1 and n<=4 and d==b-n and a==1:
                            validacion2 = True;
                        elif b==3 and n>=1 and n<=3 and d==b-n and a==1:
                            validacion2 = True;
                        elif b==2 and n>=1 and n<=2 and d==b-n and a==1:
                            validacion2 = True;
                        elif b==1 and n==1 and d==b-1 and a==1:
                            validacion2 = True;
                        elif b==0 and n>=1 and n<=6 and d==b+n-1 and a==1:
                            validacion2 = True;
                        elif b==1 and n>=2 and n<=6 and d==b+n-3 and a==1:
                            validacion2 = True;
                        elif b==2 and n>=3 and n<=6 and d==b+n-5 and a==1:
                            validacion2 = True;
                        elif b==3 and n>=4 and n<=6 and d==b+n-7 and a==1:
                            validacion2 = True;
                        elif b==4 and n>=5 and n<=6 and d==b+n-9 and a==1:
                            validacion2 = True;
                        elif b==5 and n>=6 and n<=6 and d==0 and a==1:
                            validacion2 = True;
                        elif b>=0 and b<=5 and n>=1 and n<=6 and d==b+n and a==0:
                            validacion2 = True;
                        elif b==6 and n>=1 and n<=5 and d==b+n and a==0:
                            validacion2 = True;
                        elif b==7 and n>=1 and n<=4 and d==b+n and a==0:
                            validacion2 = True;
                        elif b==8 and n>=1 and n<=3 and d==b+n and a==0:
                            validacion2 = True;
                        elif b==9 and n>=1 and n<=2 and d==b+n and a==0:
                            validacion2 = True;
                        elif b==10 and n==1 and d==b+1 and a==0:
                            validacion2 = True;
                        else:
                            validacion2 = False;
        
                        # VALIDACION TOTAL
                        if validacion1 == True and validacion2 == True:
                            validacion = True;
                            print('Precondiciones cumplidas')
                        else:
                            validacion = False;
                            print('Precondiciones no cumplidas')
                    else:
                        print('Precondición no cumplida: n debe estar entre 1 y 6')
                        validacion = False;
                else:
                    print('Precondición no cumplida: c debe estar entre 1 y 2')
                    validacion = False;
            else:
                print('Precondición no cumplida: d debe estar entre 1 y 12')
                validacion = False;
        else:
            print('Precondición no cumplida: ndro debe ser igual a 0')
            validacion = False;
        return validacion
    
    def adro(self, a, b, c, d, n):
        # ESTADO ACTUAL
        #global estado_actual

        # PRECONDICIONES
        validez = self.movimiento_adro_valido(a, b, c, d, n, self.estado_actual)

        if validez == True:


            FR_2 = self.estado_actual.get_FR()
            tablero_2 = self.estado_actual.get_tablero()
            if FR_2[a][b] == 0:
                print('La casilla (a,b) está vacía')
                valor_casilla = 'v'
                #tablero_2.convertir_en_vacia(a, b)
            else:
                valor_casilla = 'dro'
                print('La casilla (a,b) contiene una ficha dro')

            if c==1 and d>=0 and d<=11:
                print('La ficha dro se convierte en ordinaria')
                valor_casilla_2 = 'dro'
                #tablero_2.convertir_en_ordinaria(c, d)
            elif c==0 and d>=0 and d<=5:
                print('La ficha dro se convierte en ordinaria')
                valor_casilla_2 = 'dro'
                #tablero_2.convertir_en_ordinaria(c, d)
            elif c==0 and d>=6 and d<=11:
                print('La ficha dro se convierte en finalista')
                valor_casilla_2 = 'drf'
                #tablero_2.convertir_en_finalista(c, d)

            #print("Este es el estado: " + tablero_2.estado_casilla(a,b))

            # Aplicar actualizaciones
            tablero_2.actualizar_casilla(a, b, valor_casilla)
            tablero_2.actualizar_casilla(c, d, valor_casilla_2)

            # ACTUALIZAR TIPOS DE FICHAS
            fichas_2 = self.estado_actual.get_fichas()
            if tablero_2.estado_casilla(c, d) == 'drf':
                fichas_2.adicionar_ficha_drf()
                fichas_2.eliminar_ficha_dro()

            # ACTUALIZAR FR
            self.estado_actual.eliminar_ficha_FR(a, b)
            self.estado_actual.adicionar_ficha_FR(c, d)

            # ACCION
            self.estado_actual.mostrar_estado()
            #self.estado_actual.get_tablero()
            #self.estado_actual.eliminar_ficha_FR(a, b)
            #self.estado_actual.adicionar_ficha_FR(c, d)
            # NUEVO ESTADO
            self.estado_actual.actualizar_estado(tablero_2, 'A', self.estado_actual.get_fichas() , self.estado_actual.moneda.esperar_lanzamiento(), FR_2, self.estado_actual.get_FA())

        else:
            print('Movimiento no válido_R1')


    
     # REGLA 2
    # Retroceder dro de (a,b) a (c,d) según “n” posiciones -> rdro(a,b,c,d,n)
    def movimiento_adao_valido(self, a, b, c, d, n):
        # Verificar si el turno es del jugador rojo
        if self.estado_actual.get_turno().get_turno_actual() == 'A' and self.estado_actual.get_moneda().estado_actual == 'a':
            if (self.estado_actual.get_tablero().estado_casilla(a, b) == 'dao') and (self.estado_actual.get_tablero().estado_casilla(c, d) == 'v' or self.estado_actual.get_tablero().estado_casilla(c, d) == 'dao'):
                if self.estado_actual.get_fichas().get_ficha(5) == 0:
                    if (c >= 0 and c <= 1) and (d >= 0 and d <= 11) and (n >= 1 and n <= 6):
                        # VALIDACION DE MOVIMIENTO (PARTE 1)
                        if b==1 and n==1 and c==a:
                            validacion1 = True;
                        elif b==2 and n>=1 and n<=2 and c==a:
                            validacion1 = True;
                        elif b==3 and n>=1 and n<=3 and c==a:
                            validacion1 = True;
                        elif b==4 and n>=1 and n<=4 and c==a:
                            validacion1 = True;
                        elif b==5 and n>=1 and n<=5 and c==a:
                            validacion1 = True;
                        elif b>=6 and b<=11 and n>=1 and n<=6 and c==a:
                            validacion1 = True;
                        elif b==0 and n>=1 and n<=6 and c==1:
                            validacion1 = True;
                        elif b==1 and n>=2 and n<=6 and c==a+1:
                            validacion1 = True;
                        elif b==2 and n>=3 and n<=6 and c==a+1:
                            validacion1 = True;
                        elif b==3 and n>=4 and n<=6 and c==a+1:
                            validacion1 = True;
                        elif b==4 and n>=5 and n<=6 and c==a+1:
                            validacion1 = True;
                        elif b==5 and n==5:
                            validacion1 = True;
                        else:
                            validacion1 = False;

                        # VALIDACION DE MOVIMIENTO (PARTE 2)
                        if b>=6 and b<=11 and n>=1 and n<=6 and d==b-n and a==0:
                            validacion2 = True;
                        elif b==5 and n>=1 and n<=5 and d==b-n and a==0:
                            validacion2 = True;
                        elif b==4 and n>=1 and n<=4 and d==b-n and a==0:
                            validacion2 = True;
                        elif b==3 and n>=1 and n<=3 and d==b-n and a==0:
                            validacion2 = True;
                        elif b==2 and n>=1 and n<=2 and d==b-n and a==0:
                            validacion2 = True;
                        elif b==1 and n==1 and d==b-1 and a==0:
                            validacion2 = True;
                        elif b==0 and n>=1 and n<=6 and d==b+n-1 and a==0: #aca me quede en la correcion
                            validacion2 = True;
                        elif b==1 and n>=2 and n<=6 and d==b+n-3 and a==0: #aca me quede en la correcion
                            validacion2 = True;
                        elif b==2 and n>=3 and n<=6 and d==b+n-5 and a==0: #aca me quede en la correcion
                            validacion2 = True;
                        elif b==3 and n>=4 and n<=6 and d==b+n-7 and a==0: #aca me quede en la correcion
                            validacion2 = True;
                        elif b==4 and n>=5 and n<=6 and d==b+n-9 and a==0: #aca me quede en la correcion
                            validacion2 = True;
                        elif b==5 and n>=6 and n<=6 and d==0 and a==0: #aca me quede en la correcion
                            validacion2 = True;
                        elif b>=0 and b<=5 and n>=1 and n<=6 and d==b+n and a==1:
                            validacion2 = True;
                        elif b==6 and n>=1 and n<=5 and d==b+n and a==1:
                            validacion2 = True;
                        elif b==7 and n>=1 and n<=4 and d==b+n and a==1:
                            validacion2 = True;
                        elif b==8 and n>=1 and n<=3 and d==b+n and a==1:
                            validacion2 = True;
                        elif b==9 and n>=1 and n<=2 and d==b+n and a==1:
                            validacion2 = True;
                        elif b==10 and n==1 and d==b+1 and a==1:
                            validacion2 = True;
                        else:
                            validacion2 = False;
                            
                        # VALIDACION TOTAL
                        if validacion1 == True and validacion2 == True:
                            validacion = True;
                            print('Precondiciones cumplidas')
                        else:
                            validacion = False;
                            print('Precondiciones no cumplidas')
                    else:
                        print('Precondición no cumplida: n debe estar entre 1 y 6')
                        validacion = False;
                else:
                    print('Precondición no cumplida: c debe estar entre 1 y 2')
                    validacion = False;
            else:
                print('Precondición no cumplida: d debe estar entre 1 y 12')
                validacion = False;
        else:
            print('Precondición no cumplida: ndro debe ser igual a 0')
            validacion = False;
        return validacion
    


    def adao(self, a, b, c, d ,n):
        
        if self.movimiento_adao_valido(a,b,c,d,n) == True:
            FA_2 = self.estado_actual.get_FA()
            tablero_2 = self.estado_actual.get_tablero()

            # Actualizar casilla (a,b)
            if FA_2[a][b] == 0:
                print('La casilla (a,b) está vacía')
                valor_casilla = 'v'
                #tablero_2.convertir_en_vacia(a, b)
            else:
                valor_casilla = 'dao'
                print('La casilla (a,b) contiene una ficha dao')
            
            if c==0 and d>=0 and d<=11:
                print('La ficha dao se convierte en ordinaria')
                valor_casilla_2 = 'dao'
                #tablero_2.convertir_en_ordinaria(c, d)
            elif c==1 and d>=0 and d<=5:
                print('La ficha dao se convierte en ordinaria')
                valor_casilla_2 = 'dao'
                #tablero_2.convertir_en_ordinaria(c, d)
            elif c==1 and d>=6 and d<=11:
                print('La ficha dao se convierte en finalista')
                valor_casilla_2 = 'daf'
                #tablero_2.convertir_en_finalista(c, d)

            # Aplicar actualizaciones
            tablero_2 = self.estado_actual.get_tablero()
            tablero_2.actualizar_casilla(a, b, valor_casilla)
            tablero_2.actualizar_casilla(c, d, valor_casilla_2)

            # ACTUALIZAR TIPOS DE FICHAS
            fichas_2 = self.estado_actual.get_fichas()
            if tablero_2.estado_casilla(c, d) == 'daf':
                fichas_2.adicionar_ficha_daf()
                fichas_2.eliminar_ficha_dao()
            
            # ACTUALIZAR FR
            self.estado_actual.eliminar_ficha_FA(a, b)
            self.estado_actual.adicionar_ficha_FA(c, d)

            # Actualizar estado
            self.estado_actual.mostrar_estado()
            self.estado_actual.actualizar_estado(tablero_2, 'R', fichas_2 , self.estado_actual.moneda.esperar_lanzamiento(), self.estado_actual.get_FR, FA_2)


            # Se indica que el movimiento fue exitoso
            print('Movimiento exitoso_R2')
        else:
            print('Movimiento no válido_R2')


    # REGLA 3
    def movimiento_adrf_valido(self, a, b, c, d, n, estado_actual): # Verificar si un movimiento es válido
        # Verificar si el turno es del jugador rojo
        if self.estado_actual.get_turno().get_turno_actual() == 'R' and self.estado_actual.get_moneda().estado_actual == 'a':
            if (self.estado_actual.get_tablero().estado_casilla(a,b) == 'drf') and (self.estado_actual.get_tablero().estado_casilla(c,d) == 'v' or self.estado_actual.get_tablero().estado_casilla(c,d) == 'drf'):
                if self.estado_actual.get_fichas().get_ficha(4) == 0:
                    if (c == 0) and (d >= 6 and d <= 11) and (n >= 1 and n <= 6):
                        # VALIDACION DE MOVIMIENTO (PARTE 1)
                        if b>=6 and b<=11 and n>=1 and n<=6 and c==a:
                            validacion1 = True;
                        else:
                            validacion1 = False;

                        # VALIDACION DE MOVIMIENTO (PARTE 2)
                        if b==6 and n>=1 and n<=5 and d==b+n and a==0:
                            validacion2 = True;
                        elif b==7 and n>=1 and n<=4 and d==b+n and a==0:
                            validacion2 = True;
                        elif b==8 and n>=1 and n<=3 and d==b+n and a==0:
                            validacion2 = True;
                        elif b==9 and n>=1 and n<=2 and d==b+n and a==0:
                            validacion2 = True;
                        elif b==10 and n==1 and d==b+1 and a==0:
                            validacion2 = True;
                        else:
                            validacion2 = False;
        
                        # VALIDACION TOTAL
                        if validacion1 == True and validacion2 == True:
                            validacion = True;
                            print('Precondiciones cumplidas')
                        else:
                            validacion = False;
                            print('Precondiciones no cumplidas')
                    else:
                        print('Precondición no cumplida: n debe estar entre 1 y 6')
                        validacion = False;
                else:
                    print('Precondición no cumplida: c debe estar entre 1 y 2')
                    validacion = False;
            else:
                print('Precondición no cumplida: d debe estar entre 1 y 12')
                validacion = False;
        else:
            print('Precondición no cumplida: ndro debe ser igual a 0')
            validacion = False;
        return validacion

    # Avanzar dro de (a,b) a (c,d) según “n” posiciones -> adro(a,b,c,d,n)
    def adrf(self, a, b, c, d, n):
        # ESTADO ACTUAL
        #global estado_actual

        # PRECONDICIONES
        validez = self.movimiento_adrf_valido(a, b, c, d, n, self.estado_actual)

        if validez == True:

            FR_2 = self.estado_actual.get_FR()
            tablero_2 = self.estado_actual.get_tablero()
            if FR_2[a][b] == 0:
                print('La casilla (a,b) está vacía')
                valor_casilla = 'v'
                #tablero_2.convertir_en_vacia(a, b)
            else:
                valor_casilla = 'drf'
                print('La casilla (a,b) contiene una ficha dro')

            # Actualizar casilla (c,d)
            valor_casilla_2 = 'drf'
                #tablero_2.convertir_en_finalista(c, d)

            #print("Este es el estado: " + tablero_2.estado_casilla(a,b))

            # Aplicar actualizaciones
            tablero_2.actualizar_casilla(a, b, valor_casilla)
            tablero_2.actualizar_casilla(c, d, valor_casilla_2)

            # ACTUALIZAR TIPOS DE FICHAS
            fichas_2 = self.estado_actual.get_fichas()
            if tablero_2.estado_casilla(c, d) == 'drf':
                fichas_2.adicionar_ficha_drf()
                #fichas_2.eliminar_ficha_drf()

            # ACTUALIZAR FR
            self.estado_actual.eliminar_ficha_FR(a, b)
            self.estado_actual.adicionar_ficha_FR(c, d)

            # ACCION
            self.estado_actual.mostrar_estado()
            #self.estado_actual.get_tablero()
            #self.estado_actual.eliminar_ficha_FR(a, b)
            #self.estado_actual.adicionar_ficha_FR(c, d)
            # NUEVO ESTADO
            self.estado_actual.actualizar_estado(tablero_2, 'A', fichas_2 , self.estado_actual.moneda.esperar_lanzamiento(), FR_2, self.estado_actual.get_FA)

        else:
            print('Movimiento no válido_R3')

    # REGLA 4
    # Avanzar daf de (a,b) a (c,d) según “n” posiciones -> adaf(a,b,c,d,n)
    def movimiento_adaf_valido(self, a, b, c, d, n):
        # Verificar si el turno es del jugador rojo
        if self.estado_actual.get_turno().get_turno_actual() == 'A' and self.estado_actual.get_moneda().estado_actual == 'a':
            if (self.estado_actual.get_tablero().estado_casilla(a, b) == 'daf') and (self.estado_actual.get_tablero().estado_casilla(c, d) == 'v' or self.estado_actual.get_tablero().estado_casilla(c, d) == 'daf'):
                if self.estado_actual.get_fichas().get_ficha(5) == 0:
                    if ( c == 1) and (d >= 6 and d <= 11) and (n >= 1 and n <= 6):
                        # VALIDACION DE MOVIMIENTO (PARTE 1)
                        if b>=6 and b<=11 and n>=1 and n<=6 and c==a:
                            validacion1 = True;
                        else:
                            validacion1 = False;

                        # VALIDACION DE MOVIMIENTO (PARTE 2)
                        if b==6 and n>=1 and n<=5 and d==b+n and a==1:
                            validacion2 = True;
                        elif b==7 and n>=1 and n<=4 and d==b+n and a==1:
                            validacion2 = True;
                        elif b==8 and n>=1 and n<=3 and d==b+n and a==1:
                            validacion2 = True;
                        elif b==9 and n>=1 and n<=2 and d==b+n and a==1:
                            validacion2 = True;
                        elif b==10 and n==1 and d==b+1 and a==1:
                            validacion2 = True;
                        else:
                            validacion2 = False;
                            
                        # VALIDACION TOTAL
                        if validacion1 == True and validacion2 == True:
                            validacion = True;
                            print('Precondiciones cumplidas')
                        else:
                            validacion = False;
                            print('Precondiciones no cumplidas')
                    else:
                        print('Precondición no cumplida: n debe estar entre 1 y 6')
                        validacion = False;
                else:
                    print('Precondición no cumplida: c debe estar entre 1 y 2')
                    validacion = False;
            else:
                print('Precondición no cumplida: d debe estar entre 1 y 12')
                validacion = False;
        else:
            print('Precondición no cumplida: ndro debe ser igual a 0')
            validacion = False;
        return validacion
    


    def adaf(self, a, b, c, d ,n):
        if self.movimiento_adaf_valido(a,b,c,d,n) == True:
            FA_2 = self.estado_actual.get_FA()
            tablero_2 = self.estado_actual.get_tablero()

            # Actualizar casilla (a,b)
            if FA_2[a][b] == 0:
                print('La casilla (a,b) está vacía')
                valor_casilla = 'v'
                #tablero_2.convertir_en_vacia(a, b)
            else:
                valor_casilla = 'daf'
                print('La casilla (a,b) contiene una ficha daf')
            
            # Actualizar casilla (c,d)
            valor_casilla_2 = 'daf'
                #tablero_2.convertir_en_finalista(c, d)

            # Aplicar actualizaciones
            tablero_2 = self.estado_actual.get_tablero()
            tablero_2.actualizar_casilla(a, b, valor_casilla)
            tablero_2.actualizar_casilla(c, d, valor_casilla_2)

            # ACTUALIZAR TIPOS DE FICHAS
            fichas_2 = self.estado_actual.get_fichas()
            if tablero_2.estado_casilla(c, d) == 'daf':
                fichas_2.adicionar_ficha_daf()
                #fichas_2.eliminar_ficha_daf()
            
            # ACTUALIZAR FA
            self.estado_actual.eliminar_ficha_FA(a, b)
            self.estado_actual.adicionar_ficha_FA(c, d)

            # Actualizar estado
            self.estado_actual.mostrar_estado()
            self.estado_actual.actualizar_estado(tablero_2, 'R', fichas_2 , self.estado_actual.moneda.esperar_lanzamiento(), self.estado_actual.get_FR, FA_2)


            # Se indica que el movimiento fue exitoso
            print('Movimiento exitoso_R4')
        else:
            print('Movimiento no válido_R4')




    # REGLA 5
    # Retroceder dro de (a,b) a (c,d) según “n” posiciones -> rdro(a,b,c,d,n)
    def movimiento_rdro_valido(self, a, b, c, d, n):
        # Verificar si el turno es del jugador rojo
        validacion = False

        if self.estado_actual.get_turno().get_turno_actual() == 'R' and self.estado_actual.get_moneda().estado_actual == 'r':
            if (self.estado_actual.get_tablero().estado_casilla(a, b) == 'dro') and (self.estado_actual.get_tablero().estado_casilla(c, d) == 'v' or self.estado_actual.get_tablero().estado_casilla(c, d) == 'dro'):
                if self.estado_actual.get_fichas().get_ficha(4) == 0:
                    if (c >= 0 and c <= 1) and (d >= 0 and d <= 11)and(1 <= n <= 6):
                            if a == 0:
                                if 6 <= b <= 11 and d == b - n and c == 0:
                                    validacion = True           
                                elif b == 5 and 1 <= n <= 5 and d == b - n and c == 0:
                                    validacion = True           
                                elif b == 4 and 1 <= n <= 4 and d == b - n and c == 0:
                                    validacion = True
                                elif b == 3 and 1 <= n <= 3 and d == b - n and c == 0:
                                    validacion = True
                                elif b == 2 and 1 <= n <= 2 and d == b - n and c == 0:
                                    validacion = True
                                elif b == 1 and n == 1 and d == b - n and c == 0:
                                    validacion = True
                                elif b == 0 and 1 <= n <= 6 and d == 6 - n - 1 and c == 1:
                                    validacion = True
                                elif b == 1 and 2 <= n <= 6 and d == n - b - 1 and c == 1:
                                    validacion = True
                                elif b == 2 and 3 <= n <= 6 and d == n - b - 1 and c == 1:
                                    validacion = True
                                elif b == 3 and 4 <= n <= 6 and d == n - b - 1 and c == 1:
                                    validacion = True
                                elif b == 4 and 5 <= n <= 6 and d == n - b - 1 and c == 1:
                                    validacion = True
                                elif b == 5 and n == 6 and d == n - b - 1 and c == 1:
                                    validacion = True
                            elif a == 1:
                                if 0 <= b <= 5 and d == b + n and c == 1:
                                    validacion = True
                                elif b == 6 and 1 <= n <= 5 and d == b + n and c == 1:
                                    validacion = True
                                elif b == 7 and 1 <= n <= 4 and d == b + n and c == 1:
                                    validacion = True
                                elif b == 8 and 1 <= n <= 3 and d == b + n and c == 1:
                                    validacion = True
                                elif b == 9 and 1 <= n <= 2 and d == b + n and c == 1:
                                    validacion = True
                                elif b == 10 and n == 1 and d == b + n and c == 1:
                                    validacion = True
                            
                            if validacion==True:
                                print('Precondiciones cumplidas')
                            else:
                                print('Precondiciones no cumplidas')
                    else:
                        print('Precondición no cumplida: n debe estar entre 1 y 6')
                        validacion = False
                
                else:
                    print('Precondición no cumplida: ndcr debe ser igual a 0')
                    validacion = False
            else:
                print('Precondición no cumplida: la casilla de origen debe contener dro y la casilla de destino debe estar vacía o contener dro')
                validacion = False
        else:
            print('Precondición no cumplida: turno o moneda incorrectos')
            validacion = False
        
        return validacion


    def rdro(self, a, b, c, d ,n):
        
        if self.movimiento_rdro_valido(a,b,c,d,n) == True:
            # ACCION
            self.estado_actual.eliminar_ficha_FR(a, b)
            self.estado_actual.adicionar_ficha_FR(c, d)
            
            FR_2 = self.estado_actual.get_FR()
            tablero_2 = self.estado_actual.get_tablero()

            # Actualizar casilla (a,b)
            if FR_2[a][b] == 0:
                print('La casilla (a,b) está vacía')
                tablero_2.convertir_en_vacia(a, b)
            elif FR_2[a][b]  > 0:
                valor_casilla = 'dro'

            # Actualizar casilla (c,d)
            valor_casilla_2 = 'dro'

            # Aplicar actualizaciones
            tablero_2 = self.estado_actual.get_tablero()
            tablero_2.actualizar_casilla(a, b, valor_casilla)
            tablero_2.actualizar_casilla(c, d, valor_casilla_2)

            # ACTUALIZAR TIPOS DE FICHAS
            fichas_2 = self.estado_actual.get_fichas()
            if tablero_2.estado_casilla(c, d) == 'dro':
                fichas_2.adicionar_ficha_dro()
                fichas_2.eliminar_ficha_dro()

            # Actualizar estado
            self.estado_actual.mostrar_estado()
            self.estado_actual.actualizar_estado(tablero_2, 'A', fichas_2 , self.estado_actual.moneda.esperar_lanzamiento() , FR_2, self.estado_actual.get_FA)

            # Se indica que el movimiento fue exitoso
            print('Movimiento exitoso_R5')
        else:
            print('Movimiento no válido_R5')

    # REGLA 6
    # Retroceder dao de (a,b) a (c,d) según “n” posiciones -> rdao(a,b,c,d,n)
    def rdao(self, a, b, c, d, n):
  
        if self.movimiento_rdao_valido(a,b,c,d,n) == True:
            # ACTUALIZAR TABLERO
            self.estado_actual.eliminar_ficha_FA(a, b)
            self.estado_actual.adicionar_ficha_FA(c, d)
            
            FA_2 = self.estado_actual.get_FA()
            tablero_2 = self.estado_actual.get_tablero()

            # Actualizar casilla (a,b)
            if FA_2[a][b] == 0:
                print('La casilla (a,b) está vacía')
                tablero_2.convertir_en_vacia(a, b)
            elif FA_2[a][b]  > 0:
                valor_casilla = 'dao'


            # Actualizar casilla (c,d)
            valor_casilla_2 = 'dao'

            # Aplicar actualizaciones
            tablero_2 = self.estado_actual.get_tablero()
            tablero_2.actualizar_casilla(a, b, valor_casilla)
            tablero_2.actualizar_casilla(c, d, valor_casilla_2)

            # ACTUALIZAR TIPOS DE FICHAS
            fichas_2 = self.estado_actual.get_fichas()
            if tablero_2.estado_casilla(c, d) == 'dao':
                fichas_2.adicionar_ficha_dao()
                fichas_2.eliminar_ficha_dao()

                    
            # Actualizar estado
            self.estado_actual.mostrar_estado()
            self.estado_actual.actualizar_estado(tablero_2, 'R', fichas_2 , self.estado_actual.moneda.esperar_lanzamiento() , self.estado_actual.get_FR, FA_2)

            # Se indica que el movimiento fue exitoso
            print('Movimiento exitoso_R6')
        else:
            print('Movimiento no válido_R6')

    
    def movimiento_rdao_valido(self, a, b, c, d, n):
        # Verificar si el turno es del jugador rojo
        validacion = False

        if self.estado_actual.get_turno().get_turno_actual() == 'A' and self.estado_actual.get_moneda().estado_actual == 'r':
            if (self.estado_actual.get_tablero().estado_casilla(a, b) == 'dao') and (self.estado_actual.get_tablero().estado_casilla(c, d) == 'v' or self.estado_actual.get_tablero().estado_casilla(c, d) == 'da0'):
                if self.estado_actual.get_fichas().get_ficha(5) == 0:
                    if (c >= 0 and c <= 1) and (d >= 0 and d <= 11)and(1 <= n <= 6):
                            if a == 1:
                                if 6 <= b <= 11 and 1<=n<=6 and d == b - n and c == 1:
                                    validacion = True           
                                elif b == 5 and 1 <= n <= 5 and d == b - n and c == 1:
                                    validacion = True           
                                elif b == 4 and 1 <= n <= 4 and d == b - n and c == 1:
                                    validacion = True
                                elif b == 3 and 1 <= n <= 3 and d == b - n and c == 1:
                                    validacion = True
                                elif b == 2 and 1 <= n <= 2 and d == b - n and c == 1:
                                    validacion = True
                                elif b == 1 and n == 1 and d == b - n and c == 1:
                                    validacion = True
                                elif b == 0 and 1 <= n <= 6 and d == n - b - 1 and c == 0:
                                    validacion = True
                                elif b == 1 and 2 <= n <= 6 and d == n - b - 1 and c == 0:
                                    validacion = True
                                elif b == 2 and 3 <= n <= 6 and d == n - b - 1 and c == 0:
                                    validacion = True
                                elif b == 3 and 4 <= n <= 6 and d == n - b - 1 and c == 0:
                                    validacion = True
                                elif b == 4 and 5 <= n <= 6 and d == n - b - 1 and c == 0:
                                    validacion = True
                                elif b == 5 and n == 6 and d == n - b - 1 and c == 0:
                                    validacion = True
                            elif a == 0:
                                if 0 <= b <= 5 and d == b + n and c == 0:
                                    validacion = True
                                elif b == 6 and 1 <= n <= 5 and d == b + n and c == 0:
                                    validacion = True
                                elif b == 7 and 1 <= n <= 4 and d == b + n and c == 0:
                                    validacion = True
                                elif b == 8 and 1 <= n <= 3 and d == b + n and c == 0:
                                    validacion = True
                                elif b == 9 and 1 <= n <= 2 and d == b + n and c == 0:
                                    validacion = True
                                elif b == 10 and n == 1 and d == b + n and c == 0:
                                    validacion = True
                            
                            if validacion==True:
                                print('Precondiciones cumplidas')
                            else:
                                print('Precondiciones no cumplidas')
                    else:
                        print('Precondición no cumplida: n debe estar entre 1 y 6')
                        validacion = False
                
                else:
                    print('Precondición no cumplida: ndcr debe ser igual a 0')
                    validacion = False
            else:
                print('Precondición no cumplida: la casilla de origen debe contener dro y la casilla de destino debe estar vacía o contener dro')
                validacion = False
        else:
            print('Precondición no cumplida: turno o moneda incorrectos')
            validacion = False
        
        return validacion

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
            self.estado_actual.mostrar_estado()
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