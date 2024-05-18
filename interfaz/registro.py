import pygame
import pygame_gui
import sys
from utilidades.colores import dibujar_rectangulo_redondeado, VERDE, AMARILLO, NEGRO

# INICIALIZAR PYGAME
pygame.init()

# CREAR LA VENTANA
ventana = pygame.display.set_mode((800, 400))

# CREAR EL ADMINISTRADOR DE INTERFAZ DE USUARIO
manager = pygame_gui.UIManager((800, 400))

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


# DIBUJAR EN LA PANTALLA
def dibujar_pantalla_Registro():
    # PINTAR LA VENTANA
    ventana.fill(VERDE)

    # AGREGAR TITULO A LA VENTANA
    pygame.display.set_caption("Registro de jugadores")

    # DIBUJAR RECTANGULO DEL TITULO
    dibujar_rectangulo_redondeado(ventana, AMARILLO, (27, 29, 746, 343), 11) 

    # IMPORTACION DE FUENTES
    ftexto1 = pygame.font.Font('fuentes/Inter-ExtraBold.ttf', 32)
    ftexto2 = pygame.font.Font('fuentes/Inter-ExtraBoldItalic.otf', 24)
    ftexto3 = pygame.font.Font('fuentes/Inter-SemiBoldItalic.otf', 20)

    # AGREGAR TEXTO 
    # 1. DE TITULO
    titulo = ftexto1.render("REGISTRO DE JUGADORES", True, VERDE)
    ventana.blit(titulo, (189, 52))

    # 2. DE JUGADOR 1
    jugador1 = ftexto2.render("Jugador 1", True, NEGRO)
    ventana.blit(jugador1, (137, 108))

    # 3. DE JUGADOR 2
    jugador2 = ftexto2.render("Jugador 2", True, NEGRO)
    ventana.blit(jugador2, (497, 108))

    # 4. DE PSEUDONIMO JUGADOR 1
    pseudonimo1 = ftexto3.render("  - Pseudónimo:", True, NEGRO)
    ventana.blit(pseudonimo1, (43, 166))

    # 5. DE PSEUDONIMO JUGADOR 2
    pseudonimo2 = ftexto3.render("  - Pseudónimo:", True, NEGRO)
    ventana.blit(pseudonimo2, (399, 166))

    # 6. DE COLOR DE FICHAS
    color_fichas = ftexto3.render("Color de fichas:", True, NEGRO)
    ventana.blit(color_fichas, (323, 224))



clock = pygame.time.Clock() # Reloj de Pygame para controlar la velocidad de fotogramas
is_running = True # Variable para controlar el bucle principal


# Bucle principal del juego
while is_running:
    
    time_delta = clock.tick(60)/1000.0 # Actualizar el reloj de Pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            #is_running = False
            pygame.quit()
            sys.exit()

        #if event.type == pygame.USEREVENT:
        if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED:
            if event.ui_element == texto_pseudonimo1:
            #if event.ui_element == texto_pseudonimo1:
                print(f"El usuario ingresó: {event.text}")
        
        #if event.type == pygame.USEREVENT:
        if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED:
            if event.ui_element == texto_pseudonimo2:
            #if event.ui_element == texto_pseudonimo2:
                print(f"El usuario ingresó: {event.text}")
        
        #if event.type == pygame.USEREVENT:
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == button_amarillo:
                selected_option = 'Amarillo'
                button_amarillo.set_text('Jugador 1')
                button_rojo.set_text('Jugador 2')
                print("El usuario seleccionó Amarillo")
            elif event.ui_element == button_rojo:
                selected_option = 'Rojo'
                button_amarillo.set_text('Jugador 2')
                button_rojo.set_text('Jugador 1')
                print("El usuario seleccionó Rojo")
        
        #if event.type == pygame.USEREVENT:
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == button_registrar:
                print("Se ha registrado a los jugadores")

        manager.process_events(event)

    dibujar_pantalla_Registro()

    manager.update(time_delta)

    #ventana.fill((255, 255, 255))

    manager.draw_ui(ventana)

    pygame.display.update()

#pygame.quit()

