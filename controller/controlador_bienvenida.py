import pygame, pygame_gui, sys
from view.registro_GUI import mostrar_pantalla_Registro

class Controlador_Bienvenida:
    modo_juego = None

    def manejar_salida(self):
        print('Saliendo del juego...')
        pygame.quit()
        sys.exit()

    def manejar_click_HH(self):
        modo_juego = 'Humano-Humano'
        print('Modo de juego: ', modo_juego)
        ventana2 = pygame.display.set_mode((800, 400))
        manager2 = pygame_gui.UIManager((800, 400))
        mostrar_pantalla_Registro(ventana2, manager2)

    def manejar_click_HM_principiante(self):
        modo_juego = 'H-M Principiante'
        print('Modo de juego: ', modo_juego)

    def manejar_click_HM_normal(self):
        modo_juego = 'H-M Normal'
        print('Modo de juego: ', modo_juego)
    
    def manejar_click_HM_experto(self):
        modo_juego = 'H-M Experto'
        print('Modo de juego: ', modo_juego)