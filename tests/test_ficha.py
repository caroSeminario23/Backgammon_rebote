from src.ficha import Ficha

def test_convertir_en_finalista(): # Test para verificar que una ficha se convierte en finalista
    ficha = Ficha('rojo', 'l')
    ficha.convertir_en_finalista()
    assert ficha.estado == 'f'

def test_convertir_en_ordinaria(): # Test para verificar que una ficha se convierte en ordinaria
    ficha = Ficha('amarillo', 'l')
    ficha.convertir_en_ordinaria()
    assert ficha.estado == 'o'

def test_convertir_en_capturada(): # Test para verificar que una ficha se convierte en capturada
    ficha = Ficha('rojo', 'l')
    ficha.convertir_en_capturada()
    assert ficha.estado == 'c'

def test_convertir_en_libre(): # Test para verificar que una ficha se convierte en libre
    ficha = Ficha('amarillo', 'c')
    ficha.convertir_en_libre()
    assert ficha.estado == 'l'

# Ejecutar los tests
test_convertir_en_finalista()
test_convertir_en_ordinaria()
test_convertir_en_capturada()
test_convertir_en_libre()
