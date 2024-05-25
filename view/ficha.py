import pygame

class Ficha:
    def __init__(self, color, x, y, nFichas):
        self.color_original = color
        self.color = color
        self.x = x
        self.y = y
        self.nFichas = nFichas
        self.rect = pygame.Rect(self.x-25, self.y-25, 50, 50)  # Asume que las fichas son rectángulos de 50x50
        self.imagen_fondo = None

    def obtenerPosicion(self):
        return [self.x, self.y]
    
    def cambiarPosicion(self, nuevoX, nuevoY, ventana):
        self.x = nuevoX
        self.y = nuevoY
        self.rect.topleft = (nuevoX - 25, nuevoY - 25)

        # Volver a dibujar la ficha para reflejar el cambio
        self.dibujar(ventana)

    def dibujar(self, ventana):
        negro = (0, 0, 0)
        fuente = pygame.font.Font("fuentes/Inter-MediumItalic.otf", 20)

        # Crear una superficie con el texto
        texto = fuente.render(str(self.nFichas), True, negro)

        pygame.draw.circle(ventana, negro, (self.x, self.y), 22)

        if self.color == "ROJO":
            #pygame.draw.circle(ventana, negro, (self.x, self.y), 22)
            pygame.draw.circle(ventana, self.color, (self.x, self.y), 20) # El primer parametro es la ventana, el segundo es el color y el tercero es la posición
        else:
            #pygame.draw.circle(ventana, negro, (self.x, self.y), 22)
            pygame.draw.circle(ventana, self.color, (self.x, self.y), 20)
        
        # Dibujar el texto en la ventana
        ventana.blit(texto, (self.x - texto.get_width() // 2, self.y - texto.get_height() // 2))

    def cambiarValorFichas(self, nuevoNFichas, ventana):
        self.nFichas = nuevoNFichas

        # Volver a dibujar la ficha para reflejar el cambio
        self.dibujar(ventana)

    '''def cambiarPosicion(self, x, y, ventana):
        self.x = x
        self.y = y
        self.rect.topleft = (x - 15, y - 15)
        self.dibujar(ventana)'''

    def seleccionar(self, seleccionado):
        if seleccionado:
            self.color = (255, 255, 255)  # Blanco
        else:
            self.color = self.color_original

    #imprimir informacion de la ficha
    def mostrarInformacion(self):
        print(f"Color: {self.color}")
        print(f"Posición: ({self.x}, {self.y})")
        print(f"Número de fichas: {self.nFichas}")

    def guardar_fondo(self, ventana):
        if self.imagen_fondo is None:
            self.imagen_fondo = pygame.Surface((self.rect.width, self.rect.height))
        self.imagen_fondo.blit(ventana, (0, 0), self.rect)

    def get_imagen_fondo(self):
        return self.imagen_fondo
    
    def get_rect(self):
        return self.rect