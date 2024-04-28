import unittest
from src import Turno

class TestTurno(unittest.TestCase):
    def test_get_turno_actual(self): # Test para verificar que el turno actual es 'R'
        turno = Turno('R')
        self.assertEqual(turno.get_turno_actual(), 'R')

    def test_cambio_de_turno(self): # Test para verificar que el turno cambia de 'R' a 'A' y viceversa
        turno = Turno('R')
        turno.cambio_de_turno()
        self.assertEqual(turno.get_turno_actual(), 'A')

        turno.cambio_de_turno()
        self.assertEqual(turno.get_turno_actual(), 'R')

if __name__ == '__main__': # Permite ejecutar los tests desde la consola
    unittest.main()
