import pygame_gui

from view.registro2 import Registro2
from model.jugador import Jugador

class C_Registro2:
    def __init__(self, vista: Registro2, modo_juego):
        self.vista = vista
        self.modo_juego = modo_juego
    
    def registrar_jugadores(self, event):
        if self.modo_juego == 'HH':
            if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED:
                if event.ui_element == self.vista.texto_pseudonimo1:
                    print(f"El jugador 1 ingresó: {event.text}")
                    self.vista.jugador1 = Jugador(self.vista.texto_pseudonimo1.get_text(), None)
                
                elif event.ui_element == self.vista.texto_pseudonimo2:
                    print(f"El jugador 2 ingresó: {event.text}")
                    self.vista.jugador2 = Jugador(self.vista.texto_pseudonimo2.get_text(), None)

            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == self.vista.button_amarillo:
                    self.vista.button_amarillo.set_text('Jugador 1')
                    self.vista.button_rojo.set_text('Jugador 2')
                    print('El jugador 1 seleccionó Amarillo')
                    print('El jugador 2 seleccionó Rojo')
                    self.vista.jugador1.set_colorFicha('A')
                    self.vista.jugador2.set_colorFicha('R')

                elif event.ui_element == self.vista.button_rojo:
                    self.vista.button_amarillo.set_text('Jugador 2')
                    self.vista.button_rojo.set_text('Jugador 1')
                    print('El jugador 1 seleccionó Rojo')
                    print('El jugador 2 seleccionó Amarillo')
                    self.vista.jugador1.set_colorFicha('R')
                    self.vista.jugador2.set_colorFicha('A')
        else:
            if self.vista.jugador2 is None:
                self.vista.texto_pseudonimo2.set_text('CPU')
                self.vista.jugador2 = Jugador('CPU', None)

            if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED:
                if event.ui_element == self.vista.texto_pseudonimo1:
                    print(f"El usuario ingresó: {event.text}")
                    self.vista.jugador1 = Jugador(self.vista.texto_pseudonimo1.get_text(), None)
            
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == self.vista.button_amarillo:
                    self.vista.button_amarillo.set_text('Jugador 1')
                    self.vista.button_rojo.set_text('CPU')
                    print('El jugador seleccionó Amarillo')
                    print('El CPU juega con Rojo')
                    self.vista.jugador1.set_colorFicha('A')
                    self.vista.jugador2.set_colorFicha('R')

                elif event.ui_element == self.vista.button_rojo:
                    self.vista.button_amarillo.set_text('CPU')
                    self.vista.button_rojo.set_text('Jugador 1')
                    print('El jugador seleccionó Rojo')
                    print('El CPU juega con Amarillo')
                    self.vista.jugador1.set_colorFicha('R')
                    self.vista.jugador2.set_colorFicha('A')

        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == self.vista.button_registrar:
                print('Registrando jugadores...')
                return self.vista.jugador1, self.vista.jugador2