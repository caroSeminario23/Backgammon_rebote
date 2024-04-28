import unittest
from src import Juego

class TestJuego(unittest.TestCase):
    def setUp(self): # Se ejecuta antes de cada test
        self.juego = Juego('A')

    def test_elegir_turno(self): # Test para verificar que el turno es 'A'
        self.assertEqual(self.juego.elegir_turno(), 'A')

    def test_mover_ficha_valido(self): # Test para verificar que el movimiento de una ficha es válido
        self.assertTrue(self.juego.movimiento_adro_valido(1, 2, 3, 4, 5))

    def test_mover_ficha_invalido(self): # Test para verificar que el movimiento de una ficha es inválido
        self.assertFalse(self.juego.movimiento_adro_valido(1, 2, 3, 4, 7))

    def test_verificar_estado_meta(self): # Test para verificar que el estado del juego es meta
        self.assertTrue(self.juego.verificar_estado_meta())

    def test_adro(self): # Test para verificar que adro devuelve 4
        self.assertEqual(self.juego.adro(1, 2, 3), 4)

    def test_adao(self): # Test para verificar que ada devuelve 4
        self.assertEqual(self.juego.ada(1, 2, 3), 4)

    def test_adrf(self): # Test para verificar que adrf devuelve 6
        self.assertEqual(self.juego.adrf(1, 2, 3, 4, 5), 6)

    def test_adaf(self): # Test para verificar que adaf devuelve 6
        self.assertEqual(self.juego.adaf(1, 2, 3, 4, 5), 6)

    def test_rdro(self): # Test para verificar que rdro devuelve 6
        self.assertEqual(self.juego.rdro(1, 2, 3, 4, 5), 6)

    def test_rdao(self): # Test para verificar que rdao devuelve 6
        self.assertEqual(self.juego.rdao(1, 2, 3, 4, 5), 6)

    def test_cdro(self): # Test para verificar que cdro devuelve 6
        self.assertEqual(self.juego.cdro(1, 2, 3, 4, 5), 6)

    def test_cdao(self): # Test para verificar que cdao devuelve 6
        self.assertEqual(self.juego.cdao(1, 2, 3, 4, 5), 6)

    def test_ldrc(self): # Test para verificar que ldrc devuelve 4
        self.assertEqual(self.juego.ldrc(1, 2, 3), 4)

    def test_ldac(self): # Test para verificar que ldac devuelve 4
        self.assertEqual(self.juego.ldac(1, 2, 3), 4)

    def test_rdrf(self): # Test para verificar que rdrf devuelve 6
        self.assertEqual(self.juego.rdrf(1, 2, 3, 4, 5), 6)

    def test_rdaf(self): # Test para verificar que rdaf devuelve 6
        self.assertEqual(self.juego.rdaf(1, 2, 3, 4, 5), 6)

    def test_sdrf(self): # Test para verificar que sdrf devuelve 4
        self.assertEqual(self.juego.sdrf(1, 2, 3), 4)

    def test_sdaf(self): # Test para verificar que sdaf devuelve 4
        self.assertEqual(self.juego.sdaf(1, 2, 3), 4)

if __name__ == '__main__': # Permite ejecutar los tests desde la consola
    unittest.main()
