import pygame, pygame_gui
from utils.colores import VERDE, AMARILLO, NEGRO
from utils.figuras import dibujar_rectangulo_redondeado
from controller.controlador_bienvenida import Controlador_Bienvenida

def mostrar_pantalla_Bienvenida(ventana, manager):

    # CREAR LOS BOTONES DE MODO DE JUEGO
    button_HH = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((103, 244), (192, 44)), 
                                                text='Humano-Humano',
                                                manager=manager)

    button_HM_principiante = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 314), (125, 44)),
                                            text='Principiante',
                                            manager=manager)

    button_HM_normal = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((523, 314), (91, 44)),
                                                text='Normal',
                                                manager=manager)

    button_HM_experto = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((679, 314), (95, 44)),
                                            text='Experto',
                                            manager=manager)
    selected_option = button_HH

    # AGREGAR TITULO A LA VENTANA
    pygame.display.set_caption("Bienvenido a Backgammon Rebote")

    # IMPORTACION DE FUENTES
    ftexto1 = pygame.font.Font('fuentes/Inter-ExtraBold.ttf', 32)
    ftexto2 = pygame.font.Font('fuentes/Inter-ExtraBold.ttf', 48)
    ftexto3 = pygame.font.Font('fuentes/Inter-SemiBoldItalic.otf', 20)
    ftexto4 = pygame.font.Font('fuentes/Inter-Italic.otf', 20)

    # AGREGAR TEXTO 
    # 1. DE TITULO
    titulo1 = ftexto1.render("BIENVENIDO A", True, VERDE)
    titulo2 = ftexto2.render("BACKGAMMON REBOTE", True, VERDE)
    
    # 2. DE MODO DE JUEGO
    modo_juego = ftexto3.render("Seleccione un modo de juego:", True, NEGRO)
    

    # 3. OPCIONES DE JUEGO
    humano_maquina = ftexto4.render("Humano-Máquina", True, NEGRO)
    

    # Función para resetear los botones
    def reset_buttons():
        button_HH.set_text('Humano-Humano')
        button_HM_principiante.set_text('Principiante')
        button_HM_normal.set_text('Normal')
        button_HM_experto.set_text('Experto')

    clock = pygame.time.Clock()
    is_running = True

    # BUCLE PRINCIPAL DEL JUEGO
    while is_running:
        time_delta = clock.tick(60)/1000.0 # Actualizar el reloj de Pygame
        for event in pygame.event.get():
            controlador = Controlador_Bienvenida()
            if event.type == pygame.QUIT:
                controlador.manejar_salida()

            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == button_HH:
                    reset_buttons()
                    button_HH.set_text('SELECCIONADO')
                    controlador.manejar_click_HH()

                elif event.ui_element == button_HM_principiante:
                    reset_buttons()
                    button_HM_principiante.set_text('SELECCIONADO')
                    controlador.manejar_click_HM_principiante()

                elif event.ui_element == button_HM_normal:
                    reset_buttons()
                    button_HM_normal.set_text('SELECCIONADO')
                    controlador.manejar_click_HM_normal()

                elif event.ui_element == button_HM_experto:
                    reset_buttons()
                    button_HM_experto.set_text('SELECCIONADO')
                    controlador.manejar_click_HM_experto()
            
            manager.process_events(event)
        
        # PINTAR LA VENTANA
        ventana.fill(VERDE)

        # DIBUJAR RECTANGULO DE SUBTITULO M-M
        dibujar_rectangulo_redondeado(ventana, AMARILLO, (32, 32, 814, 369), 11) 
        dibujar_rectangulo_redondeado(ventana, VERDE, (452, 244, 201, 44), 11) 

        ventana.blit(titulo1, (323, 74))
        ventana.blit(titulo2, (153, 113))

        ventana.blit(modo_juego, (62, 198))

        ventana.blit(humano_maquina, (470, 254))

        #dibujar_pantalla_Bienvenida()
        manager.update(time_delta)
        manager.draw_ui(ventana)
        pygame.display.update()