import unittest
from src import Fichas

class TestFichas(unittest.TestCase):
    def setUp(self): # Se ejecuta antes de cada test
        self.fichas = Fichas()

    def test_adicionar_ficha_dro(self): # Test para verificar que se agrega una ficha dro
        self.fichas.adicionar_ficha_dro()
        self.assertEqual(len(self.fichas.get_fichas()), 1)

    def test_eliminar_ficha_dro(self): # Test para verificar que se elimina una ficha dro
        self.fichas.adicionar_ficha_dro()
        self.fichas.eliminar_ficha_dro()
        self.assertEqual(len(self.fichas.get_fichas()), 0)

    def test_adicionar_ficha_dao(self): # Test para verificar que se agrega una ficha dao
        self.fichas.adicionar_ficha_dao()
        self.assertEqual(len(self.fichas.get_fichas()), 1)

    def test_eliminar_ficha_dao(self): # Test para verificar que se elimina una ficha dao  
        self.fichas.adicionar_ficha_dao()
        self.fichas.eliminar_ficha_dao()
        self.assertEqual(len(self.fichas.get_fichas()), 0)
    
    def test_adicionar_ficha_drf(self): # Test para verificar que se agrega una ficha drf
        self.fichas.adicionar_ficha_drf()
        self.assertEqual(len(self.fichas.get_fichas()), 1)

    def test_eliminar_ficha_drf(self): # Test para verificar que se elimina una ficha drf
        self.fichas.adicionar_ficha_drf()
        self.fichas.eliminar_ficha_drf()
        self.assertEqual(len(self.fichas.get_fichas()), 0)

    def test_adicionar_ficha_daf(self): # Test para verificar que se agrega una ficha daf
        self.fichas.adicionar_ficha_daf()
        self.assertEqual(len(self.fichas.get_fichas()), 1)

    def test_eliminar_ficha_daf(self): # Test para verificar que se elimina una ficha daf
        self.fichas.adicionar_ficha_daf()
        self.fichas.eliminar_ficha_daf()
        self.assertEqual(len(self.fichas.get_fichas()), 0)
    
    def test_adicionar_ficha_drc(self): # Test para verificar que se agrega una ficha drc
        self.fichas.adicionar_ficha_drc()
        self.assertEqual(len(self.fichas.get_fichas()), 1)

    def test_eliminar_ficha_drc(self): # Test para verificar que se elimina una ficha drc
        self.fichas.adicionar_ficha_drc()
        self.fichas.eliminar_ficha_drc()
        self.assertEqual(len(self.fichas.get_fichas()), 0)

    def test_adicionar_ficha_dac(self): # Test para verificar que se agrega una ficha dac
        self.fichas.adicionar_ficha_dac()
        self.assertEqual(len(self.fichas.get_fichas()), 1)

    def test_eliminar_ficha_dac(self): # Test para verificar que se elimina una ficha dac
        self.fichas.adicionar_ficha_dac()
        self.fichas.eliminar_ficha_dac()
        self.assertEqual(len(self.fichas.get_fichas()), 0)

    def test_adicionar_ficha_drl(self): # Test para verificar que se agrega una ficha drl
        self.fichas.adicionar_ficha_drl()
        self.assertEqual(len(self.fichas.get_fichas()), 1)

    def test_eliminar_ficha_drl(self): # Test para verificar que se elimina una ficha drl
        self.fichas.adicionar_ficha_drl()
        self.fichas.eliminar_ficha_drl()
        self.assertEqual(len(self.fichas.get_fichas()), 0)

    def test_adicionar_ficha_dal(self): # Test para verificar que se agrega una ficha dal
        self.fichas.adicionar_ficha_dal()
        self.assertEqual(len(self.fichas.get_fichas()), 1)

    def test_eliminar_ficha_dal(self): # Test para verificar que se elimina una ficha dal
        self.fichas.adicionar_ficha_dal()
        self.fichas.eliminar_ficha_dal()
        self.assertEqual(len(self.fichas.get_fichas()), 0)

if __name__ == '__main__':
    unittest.main()
