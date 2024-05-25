from pync import Notifier
from estado import Estado
from tablero import Tablero
from turno import Turno
from n_fichas import N_Fichas
from moneda import Moneda
from matriz_FR import Matriz_FR
from matriz_FA import Matriz_FA

class Reglas:
    # Constructor de la clase
    def __init__(self):
        self.reglas = [self.adro(), self.adao(), self.adrf(), self.adaf(), self.rdro(), 
                       self.rdao(), self.cdro(), self.cdao(), self.ldrc(), self.ldac(), 
                       self.rdrf(), self.rdaf(), self.sdrf(), self.sdaf()]
    
    # Mostrar las reglas
    def mostrar_reglas(self):
        for regla in self.reglas:
            regla.mostrar_regla()

    # Obtener las reglas
    def obtener_reglas(self):
        return self.reglas
    
    # REGLA 1
    # Verificar si adro es válido
    def movimiento_adro_valido(self, a, b, c, d, n, estado_actual): # Verificar si un movimiento es válido
        # Verificar si el turno es del jugador rojo
        if estado_actual.get_turno() == 'R':
            if estado_actual.get_moneda() == 'a':
                if estado_actual.get_tablero().estado_casilla(a,b) == 'dro':
                    if estado_actual.get_tablero().estado_casilla(c,d) == 'v' or estado_actual.get_tablero().estado_casilla(c,d) == 'dro':
                        if estado_actual.get_n_fichas().get_ficha(4) == 0:
                            if c >= 0 and c <= 1:
                                if d >= 0 and d <= 11:
                                    if n >= 0 and n <= 5:
                                        # VALIDACION DE MOVIMIENTO (PARTE 1)
                                        if b==1 and n==0 and c==a:
                                            validacion1 = True;
                                        elif b==2 and n>=0 and n<=1 and c==a:
                                            validacion1 = True;
                                        elif b==3 and n>=0 and n<=2 and c==a:
                                            validacion1 = True;
                                        elif b==4 and n>=0 and n<=3 and c==a:
                                            validacion1 = True;
                                        elif b==5 and n>=0 and n<=4 and c==a:
                                            validacion1 = True;
                                        elif b>=6 and b<=11 and n>=0 and n<=5 and c==a:
                                            validacion1 = True;
                                        elif b==0 and n>=0 and n<=5 and c==1:
                                            validacion1 = True;
                                        else:
                                            validacion1 = False;

                                        # VALIDACION DE MOVIMIENTO (PARTE 2)
                                        if b>=6 and b<=11 and n>=0 and n<=5 and d==b-n and a==0:
                                            validacion2 = True;
                                        elif b==5 and n>=0 and n<=4 and d==b-n and a==0:
                                            validacion2 = True;
                                        elif b==4 and n>=0 and n<=3 and d==b-n and a==0:
                                            validacion2 = True;
                                        elif b==3 and n>=0 and n<=2 and d==b-n and a==0:
                                            validacion2 = True;
                                        elif b==2 and n>=0 and n<=1 and d==b-n and a==0:
                                            validacion2 = True;
                                        elif b==1 and n==0 and d==b-1 and a==0:
                                            validacion2 = True;
                                        elif b==0 and n>=0 and n<=5 and d==b+n-1 and a==0:
                                            validacion2 = True;
                                        elif b>=0 and b<=5 and n>=0 and n<=5 and d==b+n and a==1:
                                            validacion2 = True;
                                        elif b==6 and n>=0 and n<=4 and d==b+n and a==1:
                                            validacion2 = True;
                                        elif b==7 and n>=0 and n<=3 and d==b+n and a==1:
                                            validacion2 = True;
                                        elif b==8 and n>=0 and n<=2 and d==b+n and a==1:
                                            validacion2 = True;
                                        elif b==9 and n>=0 and n<=1 and d==b+n and a==1:
                                            validacion2 = True;
                                        elif b==10 and n==0 and d==b+1 and a==1:
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
                                    print('Precondición no cumplida: d debe estar entre 1 y 2')
                                    validacion = False;
                            else:
                                print('Precondición no cumplida: c debe estar entre 1 y 12')
                                validacion = False;
                        else:
                            print('Precondición no cumplida: ndro debe ser igual a 0')
                            validacion = False;
                    else:
                        print('Precondición no cumplida: la casilla (c,d) debe estar vacía o contener una ficha dro')
                        validacion = False;
                else:
                    print('Precondición no cumplida: la casilla (a,b) debe contener una ficha dro')
                    validacion = False;
        
        return validacion

    # Avanzar dro de (a,b) a (c,d) según “n” posiciones -> adro(a,b,c,d,n)
    def adro(self, a, b, c, d, n, estado_actual):
        # PRECONDICIONES
        validez = self.movimiento_adro_valido(a, b, c, d, n, estado_actual)

        if validez == True:
            # ACCION
            estado_actual.mostrar_estado()

            nuevo_estado = estado_actual

            nuevo_FR = nuevo_estado.get_FR()
            nuevo_FR.eliminar_ficha_FR(a,b)
            nuevo_FR.adicionar_ficha_FR(c,d)

            nuevo_tablero = nuevo_estado.get_tablero()
            nuevo_turno = nuevo_estado.get_turno()
            nuevo_turno.cambio_de_turno()

            nueva_moneda = nuevo_estado.get_moneda()
            nueva_moneda.esperar_lanzamiento()

            nuevo_n_fichas = nuevo_estado.get_n_fichas()
            nuevo_FA = nuevo_estado.get_FA()

            if nuevo_FR.estado_casilla_FR(a,b) == 0:
                print('La casilla (a,b) está vacía')
                nuevo_tablero.convertir_en_vacia(a, b)
            else:
                print('La casilla (a,b) contiene una ficha dro')

            if d==0 and c>=0 and c<=10:
                print('La ficha dro se convierte en ordinaria')
                nuevo_tablero.convertir_en_ordinaria(c, d)
            elif d==1 and c>=0 and c<=5:
                print('La ficha dro se convierte en ordinaria')
                nuevo_tablero.convertir_en_ordinaria(c, d)
            elif d==1 and c>=6 and c<=11:
                print('La ficha dro se convierte en finalista')
                nuevo_tablero.convertir_en_finalista(c, d)

            # NUEVO ESTADO
            estado_actual.actualizar_estado(nuevo_tablero, nuevo_turno, nuevo_n_fichas, nueva_moneda, nuevo_FR, nuevo_FA)

        else:
            Notifier.notify('Movimiento no válido', title='Error', sound='default')
        
