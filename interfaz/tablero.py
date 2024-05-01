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
# Obtener las dimensiones de la pantalla
pantalla = pygame.display.Info()
ANCHO = pantalla.current_w
ALTO = pantalla.current_h

# Crear la ventana
ventana = pygame.display.set_mode((ANCHO, ALTO))

# Función para dibujar el tablero
def dibujar_tablero():
    ventana.fill(PLOMO)
    # Agregar un titulo a la ventana
    pygame.display.set_caption("Backgammon rebote")
    # Dibujar 1 recuadro de color melon oscuro (izquierda)
    pygame.draw.rect(ventana, MELON_OSCURO, (ANCHO//33, ALTO//6.8, ANCHO//4, ALTO/1.33)) # El primer argumento indica la ventana, el segundo el color, el tercero la posición y el cuarto el tamaño
    # Dibujar 1 recuadro de color melon oscuro (superior derecha)
    pygame.draw.rect(ventana, MELON_OSCURO, (ANCHO//3.35, ALTO//6.8, ANCHO//1.48, ALTO//11.7))
    # Dibujar 1 recuadro de color melon oscuro (inferior derecha)
    pygame.draw.rect(ventana, MELON_OSCURO, (ANCHO//3.35, ALTO//4, ANCHO//1.48, ALTO/1.54))
    # Importación de la fuente para el titulo
    fTitulo = pygame.font.Font('fuentes/Inter-ExtraBold.ttf', ALTO//15)
    # Agregar un texto en la ventana
    titulo = fTitulo.render("BACKGAMMON REBOTE", True, MELON_OSCURO)
    ventana.blit(titulo, (ANCHO//3.8, ALTO//21))

    # Dibujar 1 recuadro de color melon claro (izquierda superior)
    pygame.draw.rect(ventana, MELON_CLARO, (ANCHO//22, ALTO//5.5, ANCHO//4.6, ALTO//4.8))    
    # Dibujar 1 recuadro de color melon claro (izquierda medio)
    pygame.draw.rect(ventana, MELON_CLARO, (ANCHO//22, ALTO//2.4, ANCHO//4.6, ALTO//4.8))
    # Dibujar 1 recuadro de color melon claro (izquierda inferior)
    pygame.draw.rect(ventana, MELON_CLARO, (ANCHO//22, ALTO//1.53, ANCHO//4.6, ALTO//4.8))

    ''''
    for i in range(13):
        color = ROJO if i % 2 == 0 else ROJO
        pygame.draw.rect(ventana, color, (i * ANCHO // 12, ALTO // 3, ANCHO // 12, ALTO // 3))
        pygame.draw.line(ventana, AMARILLO, (i * ANCHO // 12, 0), (i * ANCHO // 12, ALTO), 1)
    '''
    pygame.display.update()

# Bucle principal del juego
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    dibujar_tablero()
