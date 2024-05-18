import pygame

# FUNCION PARA CONVERTIR UN COLOR EN FORMATO HEXADECIMAL A RGB
def hex_to_rgb(hex):
    hex = hex.lstrip('#')
    return tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))

# DEFINICION DE COLORES
NEGRO = hex_to_rgb("#000000")
VERDE = hex_to_rgb("#a8c99e")
PLOMO = hex_to_rgb("#D9D9D9")
AMARILLO = hex_to_rgb("#efd8a4")

# FUNCION PARA DIBUJAR UN RECTÁNGULO CON ESQUINAS REDONDEADAS
def dibujar_rectangulo_redondeado(surface, color, rect, radius):
    x, y, width, height = rect
    pygame.draw.circle(surface, color, (x+radius, y+radius), radius)
    pygame.draw.circle(surface, color, (x+width-radius, y+radius), radius)
    pygame.draw.circle(surface, color, (x+radius, y+height-radius), radius)
    pygame.draw.circle(surface, color, (x+width-radius, y+height-radius), radius)
    pygame.draw.rect(surface, color, (x, y+radius, width, height-2*radius))
    pygame.draw.rect(surface, color, (x+radius, y, width-2*radius, height))