import pygame, pygame_gui

from view.bienvenida2 import Bienvenida2

class C_Bienvenida2:
    def __init__(self, vista: Bienvenida2):
        self.vista = vista

    def eleccion_modo_juego(self, event):
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == self.vista.button_HH:
                self.reset_buttons()
                self.vista.button_HH.set_text('SELECCIONADO')
                print('Modo de juego: Humano-humano')
                #ventana2 = pygame.display.set_mode((800, 400))
                #manager2 = pygame_gui.UIManager((800, 400))
                #mostrar_pantalla_Registro(ventana2, manager2)
                return 'HH'

            elif event.ui_element == self.vista.button_HM_principiante:
                #selected_option = "H-M Principiante"
                self.reset_buttons()
                self.vista.button_HM_principiante.set_text('SELECCIONADO')
                print('Modo de juego: H-M Principiante')
                return 'fácil'

            elif event.ui_element == self.vista.button_HM_normal:
                #selected_option = "H-M Normal"
                self.reset_buttons()
                self.vista.button_HM_normal.set_text('SELECCIONADO')
                print('Modo de juego: H-M Normal')
                return 'medio'

            elif event.ui_element == self.vista.button_HM_experto:
                #selected_option = "H-M Experto"
                self.reset_buttons()
                self.vista.button_HM_experto.set_text('SELECCIONADO')
                print('Modo de juego: H-M Experto')
                return 'difícil'

    
    # Función para resetear los botones
    def reset_buttons(self):
        self.vista.button_HH.set_text('Humano-Humano')
        self.vista.button_HM_principiante.set_text('Principiante')
        self.vista.button_HM_normal.set_text('Normal')
        self.vista.button_HM_experto.set_text('Experto')