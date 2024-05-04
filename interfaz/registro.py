import pygame
#import pygame_textinput
from utilidades.text_input import TextInput

def main():
    pygame.init()

    screen = pygame.display.set_mode((800, 600)) # Crea una ventana
    clock = pygame.time.Clock() # Reloj de Pygame para controlar la velocidad de fotogramas

    text_input = TextInput() # Crea un objeto TextInput

    while True: # Bucle principal
        events = pygame.event.get() # Obtiene los eventos de Pygame
        for event in events: # Recorre los eventos
            if event.type == pygame.QUIT: # Si el evento es cerrar la ventana
                return

        text_input.update(events)
        screen.fill((225, 225, 225))

        screen.blit(text_input.get_surface(), (10, 10))

        pygame.display.update()
        clock.tick(30)

if __name__ == "__main__":
    main()

'''
def main(): # Función principal
    pygame.init() # Inicializa Pygame
    screen = pygame.display.set_mode((800, 600)) # Crea una ventana
    clock = pygame.time.Clock() # Reloj
    text_input = TextInput() # Crea un objeto TextInput

    while True: # Bucle principal
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                return
            text_input.handle_event(event)

        screen.fill((225, 225, 225))
        text_input.draw(screen)

        pygame.display.update()
        clock.tick(30)

'''

'''
# Inicializar Pygame
pygame.init()

# Crear una ventana
ventana = pygame.display.set_mode((800, 600))

# Crear un objeto TextInput
text_input = pygame_textinput.TextInput()

clock = pygame.time.Clock()

while True:
    ventana.fill((225, 225, 225))

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()

    # Feed it with events every frame
    if text_input.update(events):
        print(text_input.get_text())

    # Blit its surface onto the screen
    ventana.blit(text_input.get_surface(), (10, 10))

    pygame.display.update()
    clock.tick(30)
'''