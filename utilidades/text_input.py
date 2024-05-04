import pygame
import pygame.locals

class TextInput: # Esta clase permite al usuario ingresar texto
    def __init__(self): # Inicializa la fuente y la cadena de texto
        self.font = pygame.font.Font("fuentes/Inter-MediumItalic.otf", 32) # Fuente de texto
        self.input_string = "" # Cadena de texto
        self.rendered = None # Texto renderizado
        self.update_text() # Actualiza el texto

    def handle_event(self, event): # Maneja los eventos de teclado
        if event.type == pygame.locals.KEYDOWN: # Si se presiona una tecla
            if event.key == pygame.locals.K_BACKSPACE: # Si la tecla es retroceso
                self.input_string = self.input_string[:-1] #Elimina el último caracter de la cadena de texto
            else:
                self.input_string += event.unicode # Agrega el caracter a la cadena de texto
            self.update_text()

    def update_text(self): # Actualiza el texto renderizado
        self.rendered = self.font.render(self.input_string, True, (0, 0, 0))

    def draw(self, screen): # Dibuja el texto en la pantalla
        screen.blit(self.rendered, (10, 10))

    def drawPosition(self, surface, position):
        # Código para dibujar el objeto TextInput en la posición especificada
        surface.blit(self.rendered, position)

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

if __name__ == "__main__":
    main()
'''