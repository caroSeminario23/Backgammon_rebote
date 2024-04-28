import unittest
#from unittest.mock import Mock
from src.juego import Juego

class TestJuego(unittest.TestCase):
    def setUp(self): # Se ejecuta antes de cada test
        self.juego = Juego('A')

    def test_elegir_turno(self): # Test para verificar que el turno es 'A'
        self.assertEqual(self.juego.elegir_turno(), 'A')

    #def test_mover_ficha_valido(self): # Test para verificar que el movimiento de una ficha es válido
    #    self.assertTrue(self.juego.movimiento_adro_valido(1, 1, 1, 6, 5))

    #def test_mover_ficha_invalido(self): # Test para verificar que el movimiento de una ficha es inválido
    #    self.assertFalse(self.juego.movimiento_adro_valido(1, 2, 3, 4, 7))

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
        self.juego.adro(1, 2, 3)
        self.assertEqual(self.juego.estado.get_tablero().estado_casilla(1, 2), 'v')

    def test_adao(self):
        self.juego.adao(1, 2, 3)
        self.assertEqual(self.juego.estado.get_tablero().estado_casilla(1, 2), 'v')

    def test_adrf(self):
        self.juego.adrf(1, 2, 3, 4, 5)
        self.assertEqual(self.juego.estado.get_tablero().estado_casilla(1, 2), 'v')


    def test_adaf(self):
        self.juego.adaf(1, 6, 1, 8, 2)

        self.assertEqual(self.juego.estado.get_tablero().estado_casilla(1, 6), 'dao')
        self.assertEqual(self.juego.estado.get_tablero().estado_casilla(1, 8), 'v')


    def test_rdro(self): 
        self.juego.rdro(1, 2, 3, 4, 5)
        self.assertEqual(self.juego.estado.get_tablero().estado_casilla(1, 2), 'v')
        self.assertEqual(self.juego.estado.get_tablero().estado_casilla(1, 8), 'v')

    def test_rdao(self): # Test para verificar que rdao devuelve 6
        self.juego.rdao(1, 2, 3, 4, 5)
        self.assertEqual(self.juego.estado.get_tablero().estado_casilla(1, 2), 'v')
        self.assertEqual(self.juego.estado.get_tablero().estado_casilla(1, 8), 'v')

    def test_cdro(self): # Test para verificar que cdro devuelve 6
        self.juego.cdro(1, 2, 3, 4, 5)
        self.assertEqual(self.juego.estado.get_tablero().estado_casilla(1, 2), 'v')
        self.assertEqual(self.juego.estado.get_tablero().estado_casilla(1, 8), 'v')

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


if __name__ == '__main__': # Permite ejecutar los tests desde la consola
    unittest.main()
