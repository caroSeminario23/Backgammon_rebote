import pygame, pygame_gui

from utils.colores import VERDE, AMARILLO, NEGRO
from utils.figuras import dibujar_rectangulo_redondeado

class Bienvenida2:
    def __init__(self, alto, ancho):
        # INICIALIZAR PYGAME
        pygame.init()

        self.alto = alto
        self.ancho = ancho

        # IMPORTACION DE FUENTES
        self.ftexto1 = pygame.font.Font('fuentes/Inter-ExtraBold.ttf', 32)
        self.ftexto2 = pygame.font.Font('fuentes/Inter-ExtraBold.ttf', 48)
        self.ftexto3 = pygame.font.Font('fuentes/Inter-SemiBoldItalic.otf', 20)
        self.ftexto4 = pygame.font.Font('fuentes/Inter-Italic.otf', 20)

        # CREAR LA VENTANA Y EL ADMINISTRADOR DE INTERFAZ
        self.ventana = pygame.display.set_mode((self.alto, self.ancho))
        self.manager = pygame_gui.UIManager((self.alto, self.ancho))

        # CREAR BOTONES
        self.button_HH = None
        self.button_HM_principiante = None
        self.button_HM_normal = None
        self.button_HM_experto = None

        # AGREGAR TITULO A LA VENTANA
        pygame.display.set_caption("Bienvenido a Backgammon Rebote")


    def mostrar_pantalla(self, controlador):
        # Reloj de Pygame
        clock = pygame.time.Clock()

        # CREAR LOS BOTONES DE MODO DE JUEGO
        self.button_HH = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((103, 244), (192, 44)), 
                                                    text='Humano-Humano',
                                                    manager=self.manager)

        self.button_HM_principiante = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 314), (125, 44)),
                                                text='Principiante',
                                                manager=self.manager)

        self.button_HM_normal = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((523, 314), (91, 44)),
                                                    text='Normal',
                                                    manager=self.manager)

        self.button_HM_experto = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((679, 314), (95, 44)),
                                                text='Experto',
                                                manager=self.manager)

        # AGREGAR TEXTO 
        # 1. DE TITULO
        titulo1 = self.ftexto1.render("BIENVENIDO A", True, VERDE)
        titulo2 = self.ftexto2.render("BACKGAMMON REBOTE", True, VERDE)

        # 2. DE MODO DE JUEGO
        modo_juego = self.ftexto3.render("Seleccione un modo de juego:", True, NEGRO)

        # 3. OPCIONES DE JUEGO
        modo_juego = self.ftexto4.render("Humano-Máquina", True, NEGRO)

        corriendo = True
        while corriendo:
            time_delta = clock.tick(60)/1000.0 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    corriendo = False

                self.manager.process_events(event)

                dificultad = controlador.eleccion_modo_juego(event)
                if dificultad is not None:
                    return dificultad
                
            # PINTAR LA VENTANA
            self.ventana.fill(VERDE)

            # DIBUJAR RECTANGULO DE SUBTITULO M-M
            dibujar_rectangulo_redondeado(self.ventana, AMARILLO, (32, 32, 814, 369), 11) 
            dibujar_rectangulo_redondeado(self.ventana, VERDE, (452, 244, 201, 44), 11) 

            self.ventana.blit(titulo1, (323, 74))
            self.ventana.blit(titulo2, (153, 113))
            self.ventana.blit(modo_juego, (62, 198))
            self.ventana.blit(modo_juego, (470, 254))

            # Actualiza la ventana
            self.manager.update(time_delta)
            self.manager.draw_ui(self.ventana)
            pygame.display.update()