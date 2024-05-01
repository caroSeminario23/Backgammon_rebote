from ctypes.wintypes import RGB
import pygame # Importar la librería Pygame para crear la interfaz
import sys # Importar la librería sys para poder salir del juego

# Inicializar Pygame
pygame.init() # Inicializar Pygame para poder usar sus funciones

# Función para convertir un color en formato hexadecimal a RGB
def hex_to_rgb(hex):
    hex = hex.lstrip('#')
    return tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))

# Definir colores
AMARILLO = hex_to_rgb("#efd8a4")
MELON_CLARO = hex_to_rgb("#e8ae96")
MELON_OSCURO = hex_to_rgb("#e49d89")
ROJO = hex_to_rgb("#e47f83")
PLOMO = hex_to_rgb("#FCFCFC")

# Definir dimensiones de la ventana
ANCHO = 1300
ALTO = 700

# Crear la ventana
ventana = pygame.display.set_mode((ANCHO, ALTO)) # Crear la ventana con las dimensiones definidas

# Función para dibujar el tablero
def dibujar_tablero():
    ventana.fill(PLOMO)
    for i in range(13):
        pygame.draw.line(ventana, ROJO, (i * ANCHO // 12, 0), (i * ANCHO // 12, ALTO), 1)
    pygame.display.update()

# Bucle principal del juego
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    dibujar_tablero()
