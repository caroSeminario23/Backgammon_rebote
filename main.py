'''from model.reglas import Reglas
from view.bienvenida_GUI import TableroGUI
from controller.controlador import Controlador'''

'''def main():
    modelo_reglas = Reglas()
    vista_bienvenida = Bienvenida_GUI()
    vista_tablero = TableroGUI()
    controlador = Controlador(modelo_reglas, vista_tablero)

    # Iniciar el juego
    controlador.manejar_eventos()
    vista_tablero.mostrar()

if __name__ == "__main__":
    main()'''

import pygame, pygame_gui
from view.bienvenida_GUI import mostrar_pantalla_Bienvenida

def main():
    print('BIENVENIDO A BACKGAMMON REBOTE')
    pygame.init()
    ventana = pygame.display.set_mode((878,432))
    manager = pygame_gui.UIManager((878,432))

    mostrar_pantalla_Bienvenida(ventana, manager)

    modo_juego = ''
    jugador1 = ''
    jugador2 = ''

    pass

if __name__ == "__main__":
    main()