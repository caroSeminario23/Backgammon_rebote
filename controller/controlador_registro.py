import pygame, pygame_gui, sys
from view.tablero_GUI import mostrar_pantalla_Tablero

class Controlador_Registro:
    modo_juego = None

    def manejar_salida(self):
        print('Saliendo del juego...')
        pygame.quit()
        sys.exit()

    def manejar_registro_pseudonimo1(self, event, texto_pseudonimo1):
        print(f"El usuario ingresó: {event.text}")
        #J1_pseudonimo = texto_pseudonimo1.get_text()

    def manejar_registro_pseudonimo2(self, event, texto_pseudonimo2):
        print(f"El usuario ingresó: {event.text}")
        #J2_pseudonimo = texto_pseudonimo2.get_text()