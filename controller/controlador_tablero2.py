import pygame

#from view.tablero2 import Tablero2

class C_Tablero2:
    def __init__(self, vista):
        self.vista = vista
        self.ficha_seleccionada = None
    
    def mover_ficha(self, event, estado):
        turno_actual = estado.get_turno().get_turno_actual()
        print('Turno actual:', turno_actual)

        #for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()

            if self.ficha_seleccionada is None:
                for ficha in self.vista.fichas:
                    if ficha.rect.collidepoint(pos): # Si la ficha fue clickeada
                        fColor = None
                        if ficha.get_color() == 'ROJO':
                            fColor = 'R'
                        else:
                            fColor = 'A'

                        if fColor == turno_actual: # Si la ficha pertenece al jugador actual
                            self.ficha_seleccionada = ficha
                            ficha.seleccionar(True) # Seleccionar ficha
                            break
                        else:
                            print('Solo puedes mover fichas de tu color')
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

        return print('hola')
            