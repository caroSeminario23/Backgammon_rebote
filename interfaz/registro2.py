import pygame, pygame_gui

from utils.colores import NEGRO, VERDE, AMARILLO
from utils.figuras import dibujar_rectangulo_redondeado

class Registro2:
    def __init__(self, alto, ancho):
        # INICIALIZAR PYGAME
        pygame.init()

        self.alto = alto
        self.ancho = ancho

        # CREAR LOS BOTONES
        self.button_amarillo = None
        self.button_rojo = None
        self.button_registrar = None

        # CREAR LOS RECUADROS DE TEXTO
        self.texto_pseudonimo1 = None
        self.texto_pseudonimo2 = None

        # IMPORTACION DE FUENTES
        self.ftexto1 = pygame.font.Font('fuentes/Inter-ExtraBold.ttf', 32)
        self.ftexto2 = pygame.font.Font('fuentes/Inter-ExtraBoldItalic.otf', 24)
        self.ftexto3 = pygame.font.Font('fuentes/Inter-SemiBoldItalic.otf', 20)

        # JUGADOR
        self.jugador1 = None
        self.jugador2 = None

        # CREAR LA VENTANA Y EL ADMINISTRADOR DE INTERFAZ
        self.ventana = pygame.display.set_mode((self.alto, self.ancho))
        self.manager = pygame_gui.UIManager((self.alto, self.ancho))

        # AGREGAR TITULO A LA VENTANA
        pygame.display.set_caption("Registro de jugadores")


    def mostrar_pantalla(self, controlador):
        # Reloj de Pygame
        clock = pygame.time.Clock()

        # CREAR LOS RECUADROS DE TEXTO
        self.texto_pseudonimo1 = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((216, 161), (170, 34)), manager=self.manager)
        self.texto_pseudonimo2 = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((572, 161), (170, 34)), manager=self.manager)

        # CREAR LOS BOTONES
        # 1. COLOR DE FICHAS
        self.button_amarillo = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((218, 255), (170, 34)),
                                                    text='Amarillo',
                                                    manager=self.manager)

        self.button_rojo = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((412, 255), (170, 34)),
                                                text='Rojo',
                                                manager=self.manager)

        # AGREGAR TEXTO 
        # 1. DE TITULO
        titulo = self.ftexto1.render("REGISTRO DE JUGADORES", True, VERDE)

        # 2. DE JUGADOR 1
        jugador1 = self.ftexto2.render("Jugador 1", True, NEGRO)

        # 3. DE JUGADOR 2
        jugador2 = self.ftexto2.render("Jugador 2", True, NEGRO)

        # 4. DE PSEUDONIMO JUGADOR 1
        pseudonimo1 = self.ftexto3.render("  - Pseudónimo:", True, NEGRO)

        # 5. DE PSEUDONIMO JUGADOR 2
        pseudonimo2 = self.ftexto3.render("  - Pseudónimo:", True, NEGRO)

        # 6. DE COLOR DE FICHAS
        color_fichas = self.ftexto3.render("Color de fichas:", True, NEGRO)

        # 2. REGISTRO
        self.button_registrar = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((308, 320), (184, 33)),
                                                        text='Registrar',
                                                        manager=self.manager)
        
        corriendo = True
        while corriendo:
            time_delta = clock.tick(60)/1000.0 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    corriendo = False

                self.manager.process_events(event)

                jugadores = controlador.registrar_jugadores(event)
                if jugadores is not None:
                    self.jugador1, self.jugador2 = jugadores
                    if self.jugador1 is not None and self.jugador2 is not None:
                        return self.jugador1, self.jugador2
                    elif self.jugador1 is not None and self.jugador2.get_colorFicha() is not None:
                        return self.jugador1

            # 1. PINTAR LA VENTANA
            self.ventana.fill(VERDE)

            # 2. DIBUJAR RECTANGULO DEL TITULO
            dibujar_rectangulo_redondeado(self.ventana, AMARILLO, (27, 29, 746, 343), 11)

            # 3. ESCRIBIR LOS TEXTOS
            self.ventana.blit(titulo, (189, 52))
            self.ventana.blit(jugador1, (137, 108))
            self.ventana.blit(jugador2, (497, 108))
            self.ventana.blit(pseudonimo1, (43, 166))
            self.ventana.blit(pseudonimo2, (399, 166))
            self.ventana.blit(color_fichas, (323, 224))

            self.manager.update(time_delta)
            self.manager.draw_ui(self.ventana)
            pygame.display.update()