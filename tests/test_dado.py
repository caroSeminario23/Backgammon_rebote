import unittest
from src import Dado

class TestDado(unittest.TestCase):
    def setUp(self): # Se ejecuta antes de cada test
        self.dado = Dado()

    def test_valores_iniciales(self): # Test para verificar que los valores iniciales del dado son [1, 2, 3, 4, 5, 6]
        self.assertEqual(self.dado.valores, [1, 2, 3, 4, 5, 6])

    def test_lanzar(self): # Test para verificar que el valor devuelto al lanzar el dado es un valor de la lista de valores
        resultado = self.dado.lanzar()
        self.assertIn(resultado, self.dado.valores)

if __name__ == '__main__': # Permite ejecutar los tests desde la consola
    unittest.main()