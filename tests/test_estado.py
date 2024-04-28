import unittest
from src import Estado, Tablero, Fichas, Moneda

class TestEstado(unittest.TestCase):
    def setUp(self): # Se ejecuta antes de cada test
        self.estado = Estado(turno=1)

    def test_get_tablero(self): # Test para verificar que el tablero es una instancia de la clase Tablero
        tablero = self.estado.get_tablero()
        self.assertIsInstance(tablero, Tablero)

    def test_get_turno(self): # Test para verificar que el turno es 1
        turno = self.estado.get_turno()
        self.assertEqual(turno, 1)

    def test_get_fichas(self): # Test para verificar que las fichas son una instancia de la clase Fichas
        fichas = self.estado.get_fichas()
        self.assertIsInstance(fichas, Fichas)

    def test_get_moneda(self): # Test para verificar que la moneda es una instancia de la clase Moneda
        moneda = self.estado.get_moneda()
        self.assertIsInstance(moneda, Moneda)

    def test_actualizar_estado(self): # Test para verificar que el estado del juego se actualiza correctamente
        nuevo_tablero = Tablero()
        nuevo_turno = 2
        nuevas_fichas = Fichas()
        nueva_moneda = Moneda()
        nueva_FR = 3
        nueva_FA = 4

        self.estado.actualizar_estado(nuevo_tablero, nuevo_turno, nuevas_fichas, nueva_moneda, nueva_FR, nueva_FA)

        self.assertEqual(self.estado.get_tablero(), nuevo_tablero)
        self.assertEqual(self.estado.get_turno(), nuevo_turno)
        self.assertEqual(self.estado.get_fichas(), nuevas_fichas)
        self.assertEqual(self.estado.get_moneda(), nueva_moneda)
        self.assertEqual(self.estado.get_FR(), nueva_FR)
        self.assertEqual(self.estado.get_FA(), nueva_FA)

    def test_mostrar_estado(self): # Test para verificar que el estado del juego se muestra correctamente
        # Assuming the implementation of mostrar_estado prints the state to the console

        self.estado.mostrar_estado()

    def test_estado_casilla_FR(self):
        a = 1
        b = 2
        estado_casilla = self.estado.estado_casilla_FR(a, b)
        # Add assertions for the expected behavior of estado_casilla_FR

    def test_estado_casilla_FA(self):
        a = 1
        b = 2
        estado_casilla = self.estado.estado_casilla_FA(a, b)
        # Add assertions for the expected behavior of estado_casilla_FA

    def test_adicionar_ficha_FR(self):
        a = 1
        b = 2
        self.estado.adicionar_ficha_FR(a, b)
        # Add assertions for the expected behavior of adicionar_ficha_FR

    def test_adicionar_ficha_FA(self):
        a = 1
        b = 2
        self.estado.adicionar_ficha_FA(a, b)
        # Add assertions for the expected behavior of adicionar_ficha_FA

    def test_eliminar_ficha_FR(self):
        a = 1
        b = 2
        self.estado.eliminar_ficha_FR(a, b)
        # Add assertions for the expected behavior of eliminar_ficha_FR

    def test_eliminar_ficha_FA(self):
        a = 1
        b = 2
        self.estado.eliminar_ficha_FA(a, b)
        # Add assertions for the expected behavior of eliminar_ficha_FA

if __name__ == '__main__':
    unittest.main()
