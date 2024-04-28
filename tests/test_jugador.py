from src import Jugador

def test_jugador_jugar_turno(): # Prueba de la función jugar_turno de la clase Jugador
    jugador = Jugador("rojo")
    estado = "estado de prueba"
    
    valor_dado, valor_moneda = jugador.jugar_turno(estado)
    
    # Verificar que el valor del dado sea un entero entre 1 y 6
    assert isinstance(valor_dado, int), "El valor del dado debe ser un entero" 
    assert valor_dado >= 1 and valor_dado <= 6, "El valor del dado debe estar entre 1 y 6"
    
    # Verificar que el valor de la moneda sea una cadena de texto con valor 'cara' o 'cruz'
    assert isinstance(valor_moneda, str), "El valor de la moneda debe ser una cadena de texto"
    assert valor_moneda == "cara" or valor_moneda == "cruz", "El valor de la moneda debe ser 'cara' o 'cruz'"
