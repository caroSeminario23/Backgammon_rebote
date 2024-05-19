import pygame

# FUNCION PARA DIBUJAR UN RECTÁNGULO CON ESQUINAS REDONDEADAS
def dibujar_rectangulo_redondeado(surface, color, rect, radius):
    x, y, width, height = rect
    pygame.draw.circle(surface, color, (x+radius, y+radius), radius)
    pygame.draw.circle(surface, color, (x+width-radius, y+radius), radius)
    pygame.draw.circle(surface, color, (x+radius, y+height-radius), radius)
    pygame.draw.circle(surface, color, (x+width-radius, y+height-radius), radius)
    pygame.draw.rect(surface, color, (x, y+radius, width, height-2*radius))
    pygame.draw.rect(surface, color, (x+radius, y, width-2*radius, height))