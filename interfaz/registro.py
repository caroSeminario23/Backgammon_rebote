'''import pygame
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
            text_input.handle_event(event) # Actualiza el texto basado en los eventos

        screen.fill((225, 225, 225))

        text_input.draw(screen) # Dibuja el texto en la pantalla

        pygame.display.update()
        clock.tick(30)

if __name__ == "__main__":
    main()'''

import pygame
from utilidades.text_input import TextInput

def main():
    pygame.init()

    screen = pygame.display.set_mode((800, 600)) # Crea una ventana
    clock = pygame.time.Clock() # Reloj de Pygame para controlar la velocidad de fotogramas

    text_input_pseudonimo = TextInput() # Crea un objeto TextInput para el pseudónimo
    text_input_color = TextInput() # Crea un objeto TextInput para el color de las fichas

    fuente = pygame.font.Font("fuentes/Inter-Bold.ttf", 25) # Define la fuente para las instrucciones

    while True: # Bucle principal
        events = pygame.event.get() # Obtiene los eventos de Pygame
        for event in events: # Recorre los eventos
            if event.type == pygame.QUIT: # Si el evento es cerrar la ventana
                return
            text_input_pseudonimo.handle_event(event) # Actualiza el texto del pseudónimo basado en los eventos
            text_input_color.handle_event(event) # Actualiza el texto del color basado en los eventos

        screen.fill((225, 225, 225))

        # Dibuja las instrucciones en la pantalla
        instrucciones = fuente.render("Bienvenido a Backgammon. Por favor ingrese sus datos:", True, (0, 0, 0))
        screen.blit(instrucciones, (20, 20))

        # Dibuja los textos en la pantalla
        screen.blit(fuente.render("Pseudónimo:", True, (0, 0, 0)), (20, 60))
        text_input_pseudonimo.drawPosition(screen, (20, 80))
        screen.blit(fuente.render("Color de fichas que escoge (R/A):", True, (0, 0, 0)), (20, 120))
        text_input_color.drawPosition(screen, (20, 140))

        pygame.display.update()
        clock.tick(30)

if __name__ == "__main__":
    main()
