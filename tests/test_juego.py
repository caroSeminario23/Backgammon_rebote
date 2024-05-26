#alternativa para "src"
import sys
sys.path.append('.')
import unittest
#alternativa para "src"

#from unittest.mock import Mock
from src.juego import Juego
from src.juego import Turno
from src.moneda import Moneda
from src.turno import Turno

class TestJuego(unittest.TestCase):
    def setUp(self): # Se ejecuta antes de cada test
        self.juego = Juego('R')

    def test_elegir_turno(self): # Test para verificar que el turno es 'A'
        self.assertEqual(self.juego.elegir_turno(), 'R')

    #def test_mover_ficha_valido(self): # Test para verificar que el movimiento de una ficha es válido
    #    self.assertTrue(self.juego.movimiento_adro_valido(1, 1, 1, 6, 5))

    #def test_mover_ficha_invalido(self): # Test para verificar que el movimiento de una ficha es inválido
    #    self.assertFalse(self.juego.movimiento_adro_valido(1, 2, 3, 4, 7))
    def test_adro(self):
        self.juego.estado_actual.turno=Turno('R')
        print(self.juego.estado_actual.get_turno().get_turno_actual())
        moneda = Moneda()
        moneda.lanzar()
        self.juego.estado_actual.moneda.lanzar()
        #esto funciona MONEDA()
        print(self.juego.estado_actual.get_moneda().estado_actual)
        #self.juego.estado.get_tablero().actualizar_casilla(0,4,'dro')
        #self.juego.estado.get_tablero().actualizar_casilla(0,1,'dao')
        #self.juego.estado.get_fichas().get_ficha(5) == 0
        #:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        self.juego.adro(1, 0, 0, 0, 1)


    def test_adao(self):

        self.juego.estado_actual.turno=Turno('A')
        print(self.juego.estado_actual.get_turno().get_turno_actual())
        moneda = Moneda()
        moneda.lanzar()
        self.juego.estado_actual.moneda.lanzar()
        #esto funciona MONEDA()
        print(self.juego.estado_actual.get_moneda().estado_actual)
        #self.juego.estado.get_tablero().actualizar_casilla(0,4,'dro')
        #self.juego.estado.get_tablero().actualizar_casilla(0,1,'dao')
        #self.juego.estado.get_fichas().get_ficha(5) == 0 
        #:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        self.juego.adao(0, 4, 1, 1, 5)



    def test_adrf(self):
        self.juego.estado_actual.turno=Turno('R')
        print(self.juego.estado_actual.get_turno().get_turno_actual()+" REGLA 3")
        moneda = Moneda()
        moneda.lanzar()
        self.juego.estado_actual.moneda.lanzar()
        #esto funciona MONEDA()
        print(self.juego.estado_actual.get_moneda().estado_actual)
        #self.juego.estado.get_tablero().actualizar_casilla(0,4,'dro')
        self.juego.estado_actual.get_tablero().actualizar_casilla(0,7,'drf')
        #self.juego.estado.get_fichas().get_ficha(5) == 0 
        #:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        self.juego.adrf(0, 7, 0, 10,  3)
   


    def test_adaf(self):

        self.juego.estado_actual.turno=Turno('A')
        print(self.juego.estado_actual.get_turno().get_turno_actual()+" REGLA 4")
        moneda = Moneda()
        moneda.lanzar()
        self.juego.estado_actual.moneda.lanzar()
        #esto funciona MONEDA()
        print(self.juego.estado_actual.get_moneda().estado_actual)
        #self.juego.estado.get_tablero().actualizar_casilla(0,4,'dro')
        self.juego.estado_actual.get_tablero().actualizar_casilla(1,7,'daf')
        #self.juego.estado.get_fichas().get_ficha(5) == 0 
        #:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        
        self.juego.adaf(1, 7, 1, 9, 2)




    def test_rdro(self):  
            self.juego.estado_actual.turno=Turno('R')
            print(self.juego.estado_actual.get_turno().get_turno_actual())
            self.juego.estado_actual.moneda.lanzar()
            print(self.juego.estado_actual.get_moneda().estado_actual)
            self.juego.estado_actual.get_tablero().actualizar_casilla(0,4,'dro')
            self.juego.estado_actual.get_tablero().actualizar_casilla(0,1,'v')
            self.juego.estado_actual.get_fichas().get_ficha(4) == 0 
            print(self.juego.movimiento_rdro_valido(0,4,0,2,3))

    
    def test_rdro1(self):
            self.juego.estado_actual.turno=Turno('R')
            print(self.juego.estado_actual.get_turno().get_turno_actual())
            self.juego.estado_actual.moneda.lanzar()
            print(self.juego.estado_actual.get_moneda().estado_actual)
            self.juego.estado_actual.get_tablero().actualizar_casilla(1,0,'dro')
            self.juego.estado_actual.get_tablero().actualizar_casilla(1,5,'v')
            self.juego.estado_actual.get_fichas().get_ficha(4) == 0 
            print(self.juego.movimiento_rdro_valido(1,0,1,5,5))
            self.juego.rdro(1, 0, 1, 5, 5) 
    
    def test_rdro2(self):
            self.juego.estado_actual.turno=Turno('R')
            print(self.juego.estado_actual.get_turno().get_turno_actual())
            self.juego.estado_actual.moneda.lanzar()
            print(self.juego.estado_actual.get_moneda().estado_actual)
            self.juego.estado_actual.get_fichas().get_ficha(4) == 0 
            self.juego.rdro(0, 4, 1, 1, 6)
    
    def test_rdao(self): # Test para verificar que rdao devuelve 6
        self.juego.estado_actual.turno=Turno('A')
        print(self.juego.estado_actual.get_turno().get_turno_actual())
        self.juego.estado_actual.moneda.lanzar()
        print(self.juego.estado_actual.get_moneda().estado_actual)
        self.juego.estado_actual.get_fichas().get_ficha(5) == 0 
    
        self.juego.rdao(0, 0, 0, 3, 3)
    
    def test_rdao1(self): # Test para verificar que rdao devuelve 6
        self.juego.estado_actual.turno=Turno('A')
        print(self.juego.estado_actual.get_turno().get_turno_actual())
        self.juego.estado_actual.moneda.lanzar()
        print(self.juego.estado_actual.get_moneda().estado_actual)
        self.juego.estado_actual.get_fichas().get_ficha(5) == 0 
    
        self.juego.rdao(1, 4, 0, 1, 6)
  

    def test_rdao2(self): # Test para verificar que rdao devuelve 6
        self.juego.estado_actual.turno=Turno('A')
        print(self.juego.estado_actual.get_turno().get_turno_actual())
        self.juego.estado_actual.moneda.lanzar()
        print(self.juego.estado_actual.get_moneda().estado_actual)
        self.juego.estado_actual.get_fichas().get_ficha(5) == 0 
    
        self.juego.rdao(1, 6, 1, 3, 3)

'''
    def test_verificar_gana_rojo(self): # Test para verificar que el jugador rojo gana
        self.juego.estado.get_tablero().actualizar_casilla(0,4,'v')
        self.juego.estado.get_tablero().actualizar_casilla(0,6,'v')
        self.juego.estado.get_tablero().actualizar_casilla(1,0,'v')
        self.juego.estado.get_tablero().actualizar_casilla(1,11,'v')
        fichas_nuevas = [0,7,0,6,0,2,15,0]
        self.juego.estado.get_fichas().set_fichas(fichas_nuevas)
        self.assertEqual(self.juego.verificar_estado_meta(), 'Rojo gana')

    def test_verificar_gana_amarillo(self): # Test para verificar que el jugador rojo gana
        self.juego.estado.get_tablero().actualizar_casilla(0,0,'v')
        self.juego.estado.get_tablero().actualizar_casilla(0,11,'v')
        self.juego.estado.get_tablero().actualizar_casilla(1,4,'v')
        self.juego.estado.get_tablero().actualizar_casilla(1,6,'v')
        fichas_nuevas = [7,0,6,0,2,0,0,15]
        self.juego.estado.get_fichas().set_fichas(fichas_nuevas)
        self.assertEqual(self.juego.verificar_estado_meta(), 'Amarillo gana')

    def test_verificar_empate(self): # Test para verificar que el jugador rojo gana
        self.juego.estado.get_tablero().actualizar_casilla(0,0,'v')
        self.juego.estado.get_tablero().actualizar_casilla(0,11,'v')
        self.juego.estado.get_tablero().actualizar_casilla(1,4,'v')
        self.juego.estado.get_tablero().actualizar_casilla(1,6,'v')
        fichas_nuevas = [3,5,2,2,2,1,8,7]
        self.juego.estado.get_fichas().set_fichas(fichas_nuevas)
        self.juego.tiempo_juego = 31
        self.assertEqual(self.juego.verificar_estado_meta(), 'Empate')

    def test_verificar_juego_continua(self): # Test para verificar que el jugador rojo gana
        self.juego.estado.get_tablero().actualizar_casilla(0,0,'v')
        self.juego.estado.get_tablero().actualizar_casilla(0,11,'v')
        self.juego.estado.get_tablero().actualizar_casilla(1,4,'v')
        self.juego.estado.get_tablero().actualizar_casilla(1,6,'v')
        fichas_nuevas = [3,5,2,2,2,1,8,7]
        self.juego.estado.get_fichas().set_fichas(fichas_nuevas)
        self.juego.tiempo_juego = 25
        self.assertEqual(self.juego.verificar_estado_meta(), 'El juego continúa')

    def test_verificar_estado_meta(self): # Test para verificar que el estado del juego es meta
        self.assertTrue(self.juego.verificar_estado_meta())

    def test_adro(self):
        self.juego.estado.turno=Turno('R')
        print(self.juego.estado.get_turno().get_turno_actual())
        moneda = Moneda()
        moneda.lanzar_moneda()
        self.juego.estado.moneda.lanzar_moneda()
        #esto funciona MONEDA()
        print(self.juego.estado.get_moneda().estado_actual)
        #self.juego.estado.get_tablero().actualizar_casilla(0,4,'dro')
        #self.juego.estado.get_tablero().actualizar_casilla(0,1,'dao')
        #self.juego.estado.get_fichas().get_ficha(5) == 0
        #:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        self.juego.adro(0, 4, 3)
        #self.assertEqual(self.juego.movimiento_adaf_valido(1,2,3),True)
        self.assertEqual(self.juego.estado.get_tablero().estado_casilla(0, 4), 'dro')

    def test_adao(self):

        self.juego.estado.turno=Turno('A')
        print(self.juego.estado.get_turno().get_turno_actual())
        moneda = Moneda()
        moneda.lanzar_moneda()
        self.juego.estado.moneda.lanzar_moneda()
        #esto funciona MONEDA()
        print(self.juego.estado.get_moneda().estado_actual)
        #self.juego.estado.get_tablero().actualizar_casilla(0,4,'dro')
        #self.juego.estado.get_tablero().actualizar_casilla(0,1,'dao')
        #self.juego.estado.get_fichas().get_ficha(5) == 0 
        #:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        self.juego.adao(0, 0, 3)
        self.assertEqual(self.juego.estado.get_tablero().estado_casilla(0, 0), 'dao')
        self.assertEqual(self.juego.estado.get_tablero().estado_casilla(1, 2), 'dao')


    def test_adrf(self):
        self.juego.estado.turno=Turno('R')
        print(self.juego.estado.get_turno().get_turno_actual()+" REGLA 3")
        moneda = Moneda()
        moneda.lanzar_moneda()
        self.juego.estado.moneda.lanzar_moneda()
        #esto funciona MONEDA()
        print(self.juego.estado.get_moneda().estado_actual)
        #self.juego.estado.get_tablero().actualizar_casilla(0,4,'dro')
        self.juego.estado.get_tablero().actualizar_casilla(0,7,'drf')
        #self.juego.estado.get_fichas().get_ficha(5) == 0 
        #:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        self.juego.adrf(0, 7, 3)
        self.assertEqual(self.juego.estado.get_tablero().estado_casilla(0, 10), 'drf')


    def test_adaf(self):

        self.juego.estado.turno=Turno('A')
        print(self.juego.estado.get_turno().get_turno_actual()+" REGLA 4")
        moneda = Moneda()
        moneda.lanzar_moneda()
        self.juego.estado.moneda.lanzar_moneda()
        #esto funciona MONEDA()
        print(self.juego.estado.get_moneda().estado_actual)
        #self.juego.estado.get_tablero().actualizar_casilla(0,4,'dro')
        self.juego.estado.get_tablero().actualizar_casilla(1,6,'daf')
        #self.juego.estado.get_fichas().get_ficha(5) == 0 
        #:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        
        self.juego.adaf(1, 6, 2)

        #self.assertEqual(self.juego.estado.get_tablero().estado_casilla(1, 6), 'dao') #estaba "dao"
        self.assertEqual(self.juego.estado.get_tablero().estado_casilla(1, 8), 'daf')


    def test_rdro1(self):
        self.juego.estado.turno=Turno('R')
        print(self.juego.estado.get_turno().get_turno_actual())
        self.juego.estado.moneda.lanzar_moneda()
        print(self.juego.estado.get_moneda().estado_actual)
        self.juego.estado.get_tablero().actualizar_casilla(1,0,'dro')
        self.juego.estado.get_tablero().actualizar_casilla(1,5,'v')
        self.juego.estado.get_fichas().get_ficha(4) == 0 
        self.juego.rdro(1, 0, 1, 5, 5) 
        self.assertEqual(self.juego.estado.get_tablero().estado_casilla(1,0), 'dro')
        
    def test_rdro2(self):
        self.juego.estado.turno=Turno('R')
        print(self.juego.estado.get_turno().get_turno_actual())
        self.juego.estado.moneda.lanzar_moneda()
        print(self.juego.estado.get_moneda().estado_actual)
        self.juego.estado.get_tablero().actualizar_casilla(1,0,'dro')
        self.juego.estado.get_tablero().actualizar_casilla(0,3,'v')
        self.juego.estado.get_fichas().get_ficha(4) == 0 
        
        self.juego.rdro(0, 4, 1, 1, 6)
        self.assertEqual(self.juego.estado.get_tablero().estado_casilla(0,4), 'dro')
        self.assertEqual(self.juego.estado.get_tablero().estado_casilla(1,1), 'dro')
        self.assertEqual(self.juego.estado.estado_casilla_FR(0,4), 2 )
        self.assertEqual(self.juego.estado.estado_casilla_FR(1,1), 1 )

    
    def test_rdao(self): # Test para verificar que rdao devuelve 6
        self.juego.estado.turno=Turno('A')
        print(self.juego.estado.get_turno().get_turno_actual())
        self.juego.estado.moneda.lanzar_moneda()
        print(self.juego.estado.get_moneda().estado_actual)
        self.juego.estado.get_fichas().get_ficha(5) == 0 
    
        self.juego.rdao(0, 0, 0, 3, 3)
            # Verifica que hay fichas en las posiciones iniciales
        self.assertEqual(self.juego.estado.get_tablero().estado_casilla(0,0), 'dao')
        self.assertEqual(self.juego.estado.get_tablero().estado_casilla(0,3), 'dao')
        self.assertEqual(self.juego.estado.estado_casilla_FA(0,0) , 4 )
        self.assertEqual(self.juego.estado.estado_casilla_FA(0,3), 1 )
    
    def test_rdao1(self): # Test para verificar que rdao devuelve 6
        self.juego.estado.turno=Turno('A')
        print(self.juego.estado.get_turno().get_turno_actual())
        self.juego.estado.moneda.lanzar_moneda()
        print(self.juego.estado.get_moneda().estado_actual)
        self.juego.estado.get_fichas().get_ficha(5) == 0 
    
        self.juego.rdao(1, 4, 0, 1, 6)
            # Verifica que hay fichas en las posiciones iniciales
        self.assertEqual(self.juego.estado.get_tablero().estado_casilla(1,4), 'dao')
  
    
    def test_rdao2(self): # Test para verificar que rdao devuelve 6
        self.juego.estado.turno=Turno('A')
        print(self.juego.estado.get_turno().get_turno_actual())
        self.juego.estado.moneda.lanzar_moneda()
        print(self.juego.estado.get_moneda().estado_actual)
        self.juego.estado.get_fichas().get_ficha(5) == 0 
    
        self.juego.rdao(1, 6, 1, 3, 3)
            # Verifica que hay fichas en las posiciones iniciales
        self.assertEqual(self.juego.estado.get_tablero().estado_casilla(1,6), 'dao')
        self.assertEqual(self.juego.estado.get_tablero().estado_casilla(1,3), 'dao')
        self.assertEqual(self.juego.estado.estado_casilla_FA(1,6) ,4)
        self.assertEqual(self.juego.estado.estado_casilla_FA(1,3), 1 )

    def test_cdro(self): # Test para verificar que cdro devuelve 6
        self.juego.estado.turno=Turno('R')
        print(self.juego.estado.get_turno().get_turno_actual())
        self.juego.estado.moneda.lanzar_moneda()
        print(self.juego.estado.get_moneda().estado_actual)
        self.juego.estado.FR = [[0, 0, 0, 0, 3, 0, 5, 0, 0, 0, 0, 0],
                                [5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2]]          
        self.juego.estado.FA = [[5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
                                [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0]] 
        self.juego.cdro(1, 11, 1, 6, 5)
        self.assertEqual(self.juego.estado.get_tablero().estado_casilla(1, 11), 'dro')

    def test_cdao(self): # Test para verificar que cdao devuelve 6
        self.juego.cdao(1, 2, 3, 4, 5)
        self.assertEqual(self.juego.estado.get_tablero().estado_casilla(1, 2), 'v')
        self.assertEqual(self.juego.estado.get_tablero().estado_casilla(1, 8), 'v')

    def test_ldrc(self): # Test para verificar que ldrc devuelve 4
        self.juego.ldrc(1, 2, 3)
        self.assertEqual(self.juego.estado.get_tablero().estado_casilla(1, 2), 'v')

    def test_ldac(self): # Test para verificar que ldac devuelve 4
        self.juego.ldac(1, 2, 3)
        self.assertEqual(self.juego.estado.get_tablero().estado_casilla(1, 2), 'v')

    def test_rdrf(self): # Test para verificar que rdrf devuelve 6
        self.juego.rdrf(1, 2, 3, 4, 5)
        self.assertEqual(self.juego.estado.get_tablero().estado_casilla(1, 2), 'v')
        self.assertEqual(self.juego.estado.get_tablero().estado_casilla(1, 8), 'v')

    def test_rdaf(self): # Test para verificar que rdaf devuelve 6
        self.juego.rdaf(1, 2, 3, 4, 5)
        self.assertEqual(self.juego.estado.get_tablero().estado_casilla(1, 2), 'v')
        self.assertEqual(self.juego.estado.get_tablero().estado_casilla(1, 8), 'v')

    def test_sdrf(self):
        self.juego.sdrf(1, 2, 3)
        self.assertEqual(self.juego.estado.get_tablero().estado_casilla(1, 2), 'v')

    def test_sdaf(self): # Test para verificar que sdaf devuelve 4
        self.juego.sdaf(1, 2, 3)
        self.assertEqual(self.juego.estado.get_tablero().estado_casilla(1, 2), 'v') 
        
    '''
if __name__ == '__main__': # Permite ejecutar los tests desde la consola
    unittest.main()
