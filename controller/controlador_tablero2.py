import pygame

from view.tablero2 import Tablero2

class C_Tablero2:
    def __init__(self, vista: Tablero2):
        self.vista = vista
    
    def mover_ficha(self, event, estado):
        ficha_seleccionada = None
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()

            if ficha_seleccionada is None:
                for ficha in self.vista.fichas:
                    if ficha.rect.collidepoint(pos): # Si la ficha fue clickeada
                        ficha_seleccionada = ficha
                        ficha_seleccionada.set_selected(True) # Seleccionar ficha
                        break
            else:
                for casilla in estado.get_tablero().obtener_casillas():
                    if casilla.rect.collidepoint(pos): # Si la casilla fue clickeada
                        if casilla == 'v':
                            ficha_seleccionada.set_selected(False)
                            ficha_seleccionada.set_posicion(casilla.get_posicion())
                            ficha_seleccionada = None
                            break
                        elif estado.get_turno().get_turno_actual() == 'R' and (casilla == 'dro' or casilla == 'drf'):
                            ficha_seleccionada.set_selected(False)
                            ficha_seleccionada.set_posicion(casilla.get_posicion())
                            ficha_seleccionada = None
                            break
                        elif estado.get_turno().get_turno_actual() == 'A' and (casilla == 'dao' or casilla == 'daf'):
                            ficha_seleccionada.set_selected(False)
                            ficha_seleccionada.set_posicion(casilla.get_posicion())
                            ficha_seleccionada = None
                            break
                        else:
                            print('Casilla ocupada')
                            break
        elif event.type == pygame.MOUSEMOTION: # Mover ficha
            if ficha_seleccionada is not None:
                pos = pygame.mouse.get_pos()
                ficha_seleccionada.set_posicion(pos) 
        elif event.type == pygame.MOUSEBUTTONUP: # Soltar ficha
            if ficha_seleccionada is not None:
                ficha_seleccionada.set_selected(False)
                ficha_seleccionada = None
        else:
            pass
        fichas = []

        return fichas
            