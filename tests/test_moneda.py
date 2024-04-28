import unittest
from src.moneda import Moneda

class TestMoneda(unittest.TestCase):
    def test_lanzar_moneda(self): # Test para verificar que el estado actual de la moneda es 'a' o 'r'
        moneda = Moneda()
        moneda.lanzar_moneda()
        self.assertIn(moneda.estado_actual, ['a', 'r'])  # Assert that the current state is either 'a' or 'r'

    def test_esperar_lanzamiento(self): # Test para verificar que el estado actual de la moneda es 'i'
        moneda = Moneda()
        moneda.lanzar_moneda()
        moneda.esperar_lanzamiento()
        self.assertEqual(moneda.estado_actual, 'i')  # Assert that the current state is 'i'

if __name__ == '__main__':
    unittest.main()
