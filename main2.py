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

import pygame

from view.bienvenida2 import Bienvenida2
from view.registro2 import Registro2
from view.tablero2 import Tablero2
from controller.controlador_bienvenida2 import C_Bienvenida2
from controller.controlador_registro2 import C_Registro2
from controller.controlador2 import Controlador2
from model.turno import Turno
from model.estado import Estado

def main():

    print('BIENVENIDO A BACKGAMMON REBOTE')
    interfaz_bienvenida = Bienvenida2(878, 432)
    controlador_bienvenida = C_Bienvenida2(interfaz_bienvenida)

    # Seleccionar modo de juego
    modo_juego = None

    while modo_juego not in ['HH', 'fácil', 'medio', 'difícil']:
        modo_juego = interfaz_bienvenida.mostrar_pantalla(controlador_bienvenida)
    
    print('Modo de juego seleccionado:', modo_juego)
    
    # Registro de jugadores y seleccion de color de ficha
    jugador1, jugador2 = None, None
    interfaz_registro = Registro2(800, 400)
    controlador_registro = C_Registro2(interfaz_registro, modo_juego)

    while jugador1 is None and jugador2 is None:
        jugador1, jugador2 = interfaz_registro.mostrar_pantalla(controlador_registro)

    if jugador1 is not None and jugador2 is not None:
        print('Jugadores registrados:', jugador1.get_pseudonimo(), ' y ', jugador2.get_pseudonimo())
        print('Color de fichas:', '\nJ1: ', jugador1.get_colorFicha(), '\nJ2: ', jugador2.get_colorFicha())
    else:
        print('No se han registrado todos los jugadores.')
        return

    # Elección del turno
    turno = Turno('indefinido')

    while turno.get_turno_actual() not in ['R', 'A']:
        if modo_juego == 'HH':
            turno = Turno() # aleatorio
        else:
            turno = Turno(jugador1.get_colorFicha()) # del humano

    # Iniciar el juego
    print('Iniciando el juego...')
    ANCHO, ALTO = pygame.display.list_modes()[0]

    estado_inicial = Estado(turno)
    estado_actual = estado_inicial
    estado_actual.get_turno().mostrar_turno()
    
    interfaz_tablero = Tablero2(ALTO, ANCHO)

    # Verificar si algún jugador cumple el estado meta
    ganador = interfaz_tablero.mostrar_pantalla(jugador1, jugador2, estado_actual, modo_juego)
    
    controlador_juego = Controlador2()
    if ganador is not None:
        case = {
            'J1': '¡Felicidades! El jugador 1 ha ganado.',
            'J2': '¡Felicidades! El jugador 2 ha ganado.',
            'Empate': '¡Empate! No hay ganadores.'
        }
        print(case[ganador])
    else:
        print('Ha ocurrido un error')

    # Mostrar mensaje de victoria o continuar jugando
    controlador_juego.mostrar_mensaje_victoria(ganador)

    # Finalizar el juego
    print('Fin del juego')

if __name__ == "__main__":
    main()