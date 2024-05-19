import pygame, pygame_gui, sys
from utils.colores import VERDE, AMARILLO, NEGRO
from utils.figuras import dibujar_rectangulo_redondeado
from view.tablero_GUI import mostrar_pantalla_Tablero, setPseudonimos, setColores 

J1_pseudonimo, J2_pseudonimo, J1_color, J2_color = '', '', '', ''

def mostrar_pantalla_Registro(ventana, manager):
    global J1_pseudonimo, J2_pseudonimo, J1_color, J2_color

    # CREAR LOS RECUADROS DE TEXTO
    texto_pseudonimo1 = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((216, 161), (170, 34)), manager=manager)
    texto_pseudonimo2 = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((572, 161), (170, 34)), manager=manager)

    # CREAR LOS BOTONES
    # 1. COLOR DE FICHAS
    button_amarillo = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((218, 255), (170, 34)),
                                                text='Amarillo',
                                                manager=manager)

    button_rojo = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((412, 255), (170, 34)),
                                            text='Rojo',
                                            manager=manager)

    selected_option = button_amarillo

    # 2. REGISTRO
    button_registrar = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((308, 320), (184, 33)),
                                                    text='Registrar',
                                                    manager=manager)

    selected_option2 = button_registrar

    # AGREGAR TITULO A LA VENTANA
    pygame.display.set_caption("Registro de jugadores")

    # IMPORTACION DE FUENTES
    ftexto1 = pygame.font.Font('fuentes/Inter-ExtraBold.ttf', 32)
    ftexto2 = pygame.font.Font('fuentes/Inter-ExtraBoldItalic.otf', 24)
    ftexto3 = pygame.font.Font('fuentes/Inter-SemiBoldItalic.otf', 20)

    # AGREGAR TEXTO 
    # 1. DE TITULO
    titulo = ftexto1.render("REGISTRO DE JUGADORES", True, VERDE)

    # 2. DE JUGADOR 1
    jugador1 = ftexto2.render("Jugador 1", True, NEGRO)

    # 3. DE JUGADOR 2
    jugador2 = ftexto2.render("Jugador 2", True, NEGRO)

    # 4. DE PSEUDONIMO JUGADOR 1
    pseudonimo1 = ftexto3.render("  - Pseudónimo:", True, NEGRO)

    # 5. DE PSEUDONIMO JUGADOR 2
    pseudonimo2 = ftexto3.render("  - Pseudónimo:", True, NEGRO)

    # 6. DE COLOR DE FICHAS
    color_fichas = ftexto3.render("Color de fichas:", True, NEGRO)

    clock = pygame.time.Clock() # Reloj de Pygame para controlar la velocidad de fotogramas
    is_running = True # Variable para controlar el bucle principal


    # Bucle principal del juego
    while is_running:
        
        time_delta = clock.tick(60)/1000.0 # Actualizar el reloj de Pygame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED:
                if event.ui_element == texto_pseudonimo1:
                    print(f"El usuario ingresó: {event.text}")
                    J1_pseudonimo = texto_pseudonimo1.get_text()
            
            if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED:
                if event.ui_element == texto_pseudonimo2:
                    print(f"El usuario ingresó: {event.text}")
                    J2_pseudonimo = texto_pseudonimo2.get_text()
            
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == button_amarillo:
                    selected_option = 'Amarillo'
                    button_amarillo.set_text('Jugador 1')
                    button_rojo.set_text('Jugador 2')
                    print("El usuario seleccionó Amarillo")
                    J1_color = 'A'
                    J2_color = 'R'

                elif event.ui_element == button_rojo:
                    selected_option = 'Rojo'
                    button_amarillo.set_text('Jugador 2')
                    button_rojo.set_text('Jugador 1')
                    print("El usuario seleccionó Rojo")
                    J1_color = 'R'
                    J2_color = 'A'
            
                elif event.ui_element == button_registrar:
                    pseudo1, pseduo2, color1, color2 = registrar_Jugadores()
                    setPseudonimos(pseudo1, pseduo2)
                    setColores(color1, color2)
                    print("Se ha registrado a los jugadores")

                    # MEDIR PANTALLA DEL COMPUTADOR
                    ANCHO, ALTO = pygame.display.list_modes()[0]

                    ventana2 = pygame.display.set_mode((ANCHO, ALTO))
                    manager2 = pygame_gui.UIManager((ANCHO, ALTO))
                    mostrar_pantalla_Tablero(ventana2, manager2, ANCHO, ALTO)

            manager.process_events(event)

        
        # DIBUJAR EN LA PANTALLA
        # ---------------------- #
        # 1. PINTAR LA VENTANA
        ventana.fill(VERDE)

        # 2. DIBUJAR RECTANGULO DEL TITULO
        dibujar_rectangulo_redondeado(ventana, AMARILLO, (27, 29, 746, 343), 11)

        # 3. ESCRIBIR LOS TEXTOS
        ventana.blit(titulo, (189, 52))
        ventana.blit(jugador1, (137, 108))
        ventana.blit(jugador2, (497, 108))
        ventana.blit(pseudonimo1, (43, 166))
        ventana.blit(pseudonimo2, (399, 166))
        ventana.blit(color_fichas, (323, 224))

        manager.update(time_delta)
        manager.draw_ui(ventana)
        pygame.display.update()

def registrar_Jugadores():
    global J1_pseudonimo, J2_pseudonimo, J1_color, J2_color
    print("Registrando jugadores...")
    print(f"Jugador 1: {J1_pseudonimo}, Color: {J1_color}")
    print(f"Jugador 2: {J2_pseudonimo}, Color: {J2_color}")
    return J1_pseudonimo, J2_pseudonimo, J1_color, J2_color