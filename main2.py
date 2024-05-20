# SECUENCIA DEL JUEGO
# 1. Seleccionar un nivel HH o HM (fácil, medio, difícil)
# 2. Registro de jugadores
# 3. Seleccionar un color de ficha
# 4. Elección del turno 
# 5. Iniciar el juego
# 6. Lanzar el dado y la moneda
# 7. Mover fichas según reglas de juego
# 8. Verificar si algún jugador cumple el estado meta
# 9. Mostrar mensaje de victoria o continuar jugando
# 10. Finalizar el juego

def main():
    print('BIENVENIDO A BACKGAMMON REBOTE')
    interfaz_bienvenida = mostrar_pantalla_bienvenida()

    # Seleccionar modo de juego
    modo_juego = None

    while modo_juego not in ['HH', 'fácil', 'medio', 'difícil']:
        modo_juego = eleccion_modo_juego()
    
    # Registro de jugadores
    jugador1, jugador2 = '', ''
    interfaz_registro = mostrar_pantalla_registro()

    if modo_juego == 'HH':
        while jugador1 == '' and jugador2 == '':
            jugador1, jugador2 = registro_jugadores()
    else:
        while jugador1 == '':
            jugador2 = 'CPU'
            jugador1 = registro_jugador()

    # Seleccionar color de ficha
    color_ficha_J1, color_ficha_J2 = None, None

    while color_ficha not in ['R', 'A']:
        color_ficha_J1, color_ficha_J2 = eleccion_colores_ficha()

    # Elección del turno
    turno = None

    while turno not in ['R', 'A']:
        if modo_juego == 'HH':
            turno = eleccion_turno()
        else:
            turno = Turno(jugador1.get_colorFicha())

    # Iniciar el juego
    print('Iniciando el juego...')
    interfaz_tablero = mostrar_tablero()

    estado_inicial = Estado()
    estado_actual = estado_inicial

    # Verificar si algún jugador cumple el estado meta
    ganador = None

    while ganador not in ['R', 'A']:
        ganador = verificar_estado_meta(estado_actual)

        if ganador not in ['R', 'A']:
            # Indicar de quien es el turno
            turno.notificar()

            # Lanzar el dado y la moneda
            dado, moneda = None, None

            dado = lanzar_dado()
            moneda = lanzar_moneda()

            # Registrar el turno y lanzamiento del dado y la moneda
            estado_actual.set_turno(turno)
            estado_actual.set_dado(dado)
            estado_actual.set_moneda(moneda)

            # Mover fichas según reglas de juego
            estado_actual = mover_fichas(estado_actual)
    
    # Mostrar mensaje de victoria o continuar jugando
    mostrar_mensaje_victoria()

    # Finalizar el juego
    print('Fin del juego')
