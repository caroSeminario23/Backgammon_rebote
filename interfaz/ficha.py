import pygame

class Ficha:
    def __init__(self, color, x, y, nFichas):
        self.color = color
        self.x = x
        self.y = y
        self.nFichas = nFichas
    
    def cambiarPosicion(self, nuevoX, nuevoY):
        self.x = nuevoX
        self.y = nuevoY

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