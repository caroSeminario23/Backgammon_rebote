import pygame
import pygame_gui
import sys

# Inicializar Pygame
pygame.init()

# Función para convertir un color en formato hexadecimal a RGB
def hex_to_rgb(hex):
    hex = hex.lstrip('#')
    return tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))

# Definir colores
NEGRO = hex_to_rgb("#000000")
VERDE = hex_to_rgb("#a8c99e")
PLOMO = hex_to_rgb("#D9D9D9")
AMARILLO = hex_to_rgb("#efd8a4")

# Crear una ventana
ventana = pygame.display.set_mode((800, 400))

# Crear un administrador de interfaz de usuario 
manager = pygame_gui.UIManager((800, 400), 'tema1.json')

# Dibujar en la pantalla
def dibujar_pantalla_Registro():
    ventana.fill(VERDE)
    #pygame.display.flip()
    # Agregar un titulo a la ventana
    pygame.display.set_caption("Registro de jugadores")

    # Función para dibujar un rectángulo con esquinas redondeadas
    """Dibuja un rectángulo con esquinas redondeadas en Pygame."""
    def dibujar_rectangulo_redondeado(surface, color, rect, radius):
        x, y, width, height = rect
        pygame.draw.circle(surface, color, (x+radius, y+radius), radius)
        pygame.draw.circle(surface, color, (x+width-radius, y+radius), radius)
        pygame.draw.circle(surface, color, (x+radius, y+height-radius), radius)
        pygame.draw.circle(surface, color, (x+width-radius, y+height-radius), radius)
        pygame.draw.rect(surface, color, (x, y+radius, width, height-2*radius))
        pygame.draw.rect(surface, color, (x+radius, y, width-2*radius, height))

    # Dibujar un rectángulo con esquinas redondeadas de color verde
    dibujar_rectangulo_redondeado(ventana, AMARILLO, (27, 29, 746, 343), 11) 
    # Dibujar un rectángulo plomo para pseudonimo 1
    dibujar_rectangulo_redondeado(ventana, PLOMO, (216, 195, 170, 34), 11)
    # Dibujar un rectángulo plomo para pseudonimo 2
    dibujar_rectangulo_redondeado(ventana, PLOMO, (572, 195, 170, 34), 11)

# Crear casilla de texto para pseudonimo 1
texto_pseudonimo1 = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((216, 195), (170, 34)), manager=manager, object_id='#plomoEntrada') # El primer parametro es la posición y el segundo el tamaño
# Suponiendo que 'texto_pseudonimo1' es tu objeto UITextEntryLine

# Crear casilla de texto para pseudonimo 1
texto_pseudonimo2 = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((572, 195), (170, 34)), manager=manager, object_id='#plomoEntrada') 
# Suponiendo que 'texto_pseudonimo1' es tu objeto UITextEntryLine

'''
superficie_pseudonimo1 = texto_pseudonimo1.text_surface

if superficie_pseudonimo1 is not None:
    ventana.blit(superficie_pseudonimo1, (216, 195))
'''

#manager.add_ui_element(texto_pseudonimo1)

# Agregar la casilla de texto al administrador de interfaz de usuario
#manager.add_ui_element(texto_pseudonimo1)
#ventana.blit(superficie_pseudonimo1, (216, 195))
    



    

    


# Crear una casilla de texto
#text_entry = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((350, 275), (100, 50)), manager=manager)


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

        if event.type == pygame.USEREVENT:
            if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED:
                if event.ui_element == texto_pseudonimo1:
                    print(f"El usuario ingresó: {event.text}")
        
        if event.type == pygame.USEREVENT:
            if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED:
                if event.ui_element == texto_pseudonimo2:
                    print(f"El usuario ingresó: {event.text}")

        manager.process_events(event)

    dibujar_pantalla_Registro()

        

    manager.update(time_delta)

    #ventana.fill((255, 255, 255))

    manager.draw_ui(ventana)

    

    pygame.display.update()

#pygame.quit()

