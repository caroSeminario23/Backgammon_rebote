import pygame

from view.tablero2 import Tablero2

class C_Tablero2:
    def __init__(self, vista: Tablero2):
        self.vista = vista
        self.ficha_seleccionada = None
    
    def mover_ficha(self, event, estado):
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()

            if self.ficha_seleccionada is None:
                for ficha in self.vista.fichas:
                    if ficha.rect.collidepoint(pos): # Si la ficha fue clickeada
                        self.ficha_seleccionada = ficha
                        ficha.seleccionar(True) # Seleccionar ficha
                        #ficha_seleccionada.set_selected(True) # Seleccionar ficha
                        break
            else:
                for casilla in estado.get_tablero().obtener_casillas():
                    if casilla.rect.collidepoint(pos): # Si la casilla fue clickeada
                        if casilla == 'v'or (
                            estado.get_turno().get_turno_actual() == 'R' and (casilla == 'dro' or casilla == 'drf')) or (
                            estado.get_turno().get_turno_actual() == 'A' and (casilla == 'dao' or casilla == 'daf')):
                            
                            self.ficha_seleccionada.seleccionar(False)
                            self.ficha_seleccionada.cambiarPosicion(casilla.get_posicion()[0], casilla.get_posicion()[1], self.vista.ventana)
                            self.ficha_seleccionada = None
                            break
                        else:
                            print('Casilla ocupada')
                            break

        elif event.type == pygame.MOUSEMOTION: # Mover ficha
            if self.ficha_seleccionada is not None:
                pos = pygame.mouse.get_pos()
                self.ficha_seleccionada.cambiarPosicion(pos[0], pos[1], self.vista.ventana)
        elif event.type == pygame.MOUSEBUTTONUP: # Soltar ficha
            if self.ficha_seleccionada is not None:
                self.ficha_seleccionada.seleccionar(False)
                self.ficha_seleccionada = None
        else:
            pass

        return self.vista.fichas
            