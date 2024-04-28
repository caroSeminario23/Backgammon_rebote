import unittest
from src.tablero import Tablero

class TestTablero(unittest.TestCase):
    def setUp(self): # Se ejecuta antes de cada test
        self.tablero = Tablero()

    def test_inicializacion_tablero(self): # Test para verificar que el tablero se inicializa correctamente
        # Verificar que el tablero se inicializa como una matriz de 2x12
        self.assertEqual(len(self.tablero.casillas), 2)
        self.assertEqual(len(self.tablero.casillas[0]), 12)
        self.assertEqual(len(self.tablero.casillas[1]), 12)

    def test_estado_casilla(self): # Test para verificar que el método estado_casilla devuelve el estado correcto de la casilla
        # Verificar que el método estado_casilla devuelve el estado correcto de la casilla
        self.tablero.actualizar_casilla(0, 0, "ocupada")
        self.assertEqual(self.tablero.estado_casilla(0, 0), "ocupada")

    def test_actualizar_casilla(self): # Test para verificar que el método actualizar_casilla actualiza el valor de la casilla correctamente
        # Verificar que el método actualizar_casilla actualiza el valor de la casilla correctamente
        self.tablero.actualizar_casilla(1, 5, "vacía")
        self.assertEqual(self.tablero.casillas[1][5], "vacía")

if __name__ == '__main__': # Permite ejecutar los tests desde la consola
    unittest.main()
