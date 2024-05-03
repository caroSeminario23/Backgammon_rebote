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
MELON_TRASLUCIDO = hex_to_rgb("D9D9D9") # Agregar 60% de opacidad "superficie_transparente.set_alpha(255 * 0.6)
BEIGE = hex_to_rgb("#FEFAE4")

# Definir dimensiones de la ventana
# Obtener las dimensiones de la pantalla
pantalla = pygame.display.Info()
ANCHO = pantalla.current_w
ALTO = pantalla.current_h

# Crear la ventana
ventana = pygame.display.set_mode((ANCHO, ALTO))

# Función para dibujar el tablero
def dibujar_tablero():
    ventana.fill(BEIGE)
    # Agregar un titulo a la ventana
    pygame.display.set_caption("Backgammon rebote")

    # Función para dibujar un rectángulo con esquinas redondeadas
    def dibujar_rectangulo_redondeado(surface, color, rect, radius):
        """Dibuja un rectángulo con esquinas redondeadas en Pygame."""
        x, y, width, height = rect
        pygame.draw.circle(surface, color, (x+radius, y+radius), radius)
        pygame.draw.circle(surface, color, (x+width-radius, y+radius), radius)
        pygame.draw.circle(surface, color, (x+radius, y+height-radius), radius)
        pygame.draw.circle(surface, color, (x+width-radius, y+height-radius), radius)
        pygame.draw.rect(surface, color, (x, y+radius, width, height-2*radius))
        pygame.draw.rect(surface, color, (x+radius, y, width-2*radius, height))

    # Dibujar 1 recuadro de color melon oscuro (izquierda)
    dibujar_rectangulo_redondeado(ventana, MELON_OSCURO, (ANCHO//33, ALTO//6.8, ANCHO//4, ALTO//1.33), 10)

    # Dibujar 1 recuadro de color melon oscuro (superior derecha)
    dibujar_rectangulo_redondeado(ventana, MELON_OSCURO, (ANCHO//3.35, ALTO//6.8, ANCHO//1.48, ALTO//11.7), 10)

    # Dibujar 1 recuadro de color melon oscuro (inferior derecha)
    dibujar_rectangulo_redondeado(ventana, MELON_OSCURO, (ANCHO//3.35, ALTO//4, ANCHO//1.48, ALTO//1.54), 10)

    # TÍTULO
    # Importación de la fuente para el titulo
    fTitulo = pygame.font.Font('fuentes/Inter-ExtraBold.ttf', ALTO//15)
    # Agregar un texto en la ventana
    titulo = fTitulo.render("BACKGAMMON REBOTE", True, MELON_OSCURO)
    ventana.blit(titulo, (ANCHO//3.8, ALTO//21))


    # OBJETOS, JUGADORES Y RELOJES
    # Dibujar 1 recuadro de color melon claro (izquierda superior)
    dibujar_rectangulo_redondeado(ventana, MELON_CLARO, (ANCHO//22, ALTO//5.5, ANCHO//4.6, ALTO//4.8), 10)

    # Dibujar 1 recuadro de color melon claro (izquierda medio)
    dibujar_rectangulo_redondeado(ventana, MELON_CLARO, (ANCHO//22, ALTO//2.4, ANCHO//4.6, ALTO//4.8), 10)

    # Dibujar 1 recuadro de color melon claro (izquierda inferior)
    dibujar_rectangulo_redondeado(ventana, MELON_CLARO, (ANCHO//22, ALTO//1.53, ANCHO//4.6, ALTO//4.8), 10)


    # TABLERO DE JUEGO
    # Dibujar 1 recuadro de color melon claro (derecha superior)
    # Crear una nueva superficie con el tamaño del rectángulo
    superficie_transparente = pygame.Surface((ANCHO//2.1, ALTO//1.68)) # Tamaño del rectángulo
    # Establecer el nivel de transparencia (alpha) de la superficie
    superficie_transparente.set_alpha(255 * 0.6)  # 60% de transparencia
    # Rellenar la superficie con el color deseado
    superficie_transparente.fill(MELON_TRASLUCIDO)
    # Dibujar la superficie transparente en la ventana en la posición del rectángulo
    ventana.blit(superficie_transparente, (ANCHO//3.22, ALTO//3.6))


    # TABLERO DE FICHAS LIBERADAS
    # Dibujar 1 recuadro de color melon claro (derecha superior 1)
    dibujar_rectangulo_redondeado(ventana, MELON_CLARO, (ANCHO//1.25, ALTO//3.2, ANCHO//6.4, ALTO//7), 10)

    # Dibujar 1 recuadro de color melon claro (derecha superior 2)
    dibujar_rectangulo_redondeado(ventana, MELON_CLARO, (ANCHO//1.25, ALTO//2.05, ANCHO//6.4, ALTO//18), 10)

    # Dibujar 1 recuadro de color melon claro (derecha inferior 1)
    dibujar_rectangulo_redondeado(ventana, MELON_CLARO, (ANCHO//1.25, ALTO//1.595, ANCHO//6.4, ALTO//7), 10)

    # Dibujar 1 recuadro de color melon claro (derecha inferior 2)
    dibujar_rectangulo_redondeado(ventana, MELON_CLARO, (ANCHO//1.25, ALTO//1.24, ANCHO//6.4, ALTO//18), 10)


    # CRONÓMETROS
    # Dibujar 1 recuadro de color melon oscuro (izquierda inferior 1)
    dibujar_rectangulo_redondeado(ventana, MELON_CLARO, (ANCHO//7, ALTO//1.49, ANCHO//9, ALTO//13), 10)

    # Dibujar 1 recuadro de color melon oscuro (izquierda inferior 2)
    dibujar_rectangulo_redondeado(ventana, MELON_CLARO, (ANCHO//7, ALTO//1.31, ANCHO//9, ALTO//13), 10)

    
    # SECCIONES DEL TABLERO
    # ---- Parte de arriba ----
    # Dibujar 1 recuadro de color rojo
    pygame.draw.rect(ventana, AMARILLO, (ANCHO//3.22, ALTO//3.6, ANCHO//25.2, ALTO//3.6))
    # Dibujar 1 recuadro de color amarillo al lado del anterior
    pygame.draw.rect(ventana, ROJO, (ANCHO//2.85, ALTO//3.6, ANCHO//25.2, ALTO//3.6))
    # Dibujar 1 recuadro de color rojo al lado del anterior
    pygame.draw.rect(ventana, AMARILLO, (ANCHO//2.56, ALTO//3.6, ANCHO//25.2, ALTO//3.6))
    # Dibujar 1 recuadro de color amarillo al lado del anterior
    pygame.draw.rect(ventana, ROJO, (ANCHO//2.32, ALTO//3.6, ANCHO//25.2, ALTO//3.6))
    # Dibujar 1 recuadro de color rojo al lado del anterior
    pygame.draw.rect(ventana, AMARILLO, (ANCHO//2.125, ALTO//3.6, ANCHO//25.2, ALTO//3.6))
    # Dibujar 1 recuadro de color amarillo al lado del anterior
    pygame.draw.rect(ventana, ROJO, (ANCHO//1.96, ALTO//3.6, ANCHO//25.2, ALTO//3.6))
    # Dibujar 1 recuadro de color rojo al lado del anterior
    pygame.draw.rect(ventana, AMARILLO, (ANCHO//1.82, ALTO//3.6, ANCHO//25.2, ALTO//3.6))
    # Dibujar 1 recuadro de color amarillo al lado del anterior
    pygame.draw.rect(ventana, ROJO, (ANCHO//1.695, ALTO//3.6, ANCHO//25.2, ALTO//3.6))
    # Dibujar 1 recuadro de color rojo al lado del anterior
    pygame.draw.rect(ventana, AMARILLO, (ANCHO//1.587, ALTO//3.6, ANCHO//25.2, ALTO//3.6))
    # Dibujar 1 recuadro de color amarillo al lado del anterior
    pygame.draw.rect(ventana, ROJO, (ANCHO//1.493, ALTO//3.6, ANCHO//25.2, ALTO//3.6))
    # Dibujar 1 recuadro de color rojo al lado del anterior
    pygame.draw.rect(ventana, AMARILLO, (ANCHO//1.41, ALTO//3.6, ANCHO//25.2, ALTO//3.6))
    # Dibujar 1 recuadro de color amarillo al lado del anterior
    pygame.draw.rect(ventana, ROJO, (ANCHO//1.339, ALTO//3.6, ANCHO//25.2, ALTO//3.6))
    
    # ---- Parte de abajo ----
    # Dibujar 1 recuadro de color rojo
    pygame.draw.rect(ventana, ROJO, (ANCHO//3.22, ALTO//1.678, ANCHO//25.2, ALTO//3.6))
    # Dibujar 1 recuadro de color amarillo al lado del anterior
    pygame.draw.rect(ventana, AMARILLO, (ANCHO//2.85, ALTO//1.678, ANCHO//25.2, ALTO//3.6))
    # Dibujar 1 recuadro de color rojo al lado del anterior
    pygame.draw.rect(ventana, ROJO, (ANCHO//2.56, ALTO//1.678, ANCHO//25.2, ALTO//3.6))
    # Dibujar 1 recuadro de color amarillo al lado del anterior
    pygame.draw.rect(ventana, AMARILLO, (ANCHO//2.32, ALTO//1.678, ANCHO//25.2, ALTO//3.6))
    # Dibujar 1 recuadro de color rojo al lado del anterior
    pygame.draw.rect(ventana, ROJO, (ANCHO//2.125, ALTO//1.678, ANCHO//25.2, ALTO//3.6))
    # Dibujar 1 recuadro de color amarillo al lado del anterior
    pygame.draw.rect(ventana, AMARILLO, (ANCHO//1.96, ALTO//1.678, ANCHO//25.2, ALTO//3.6))
    # Dibujar 1 recuadro de color rojo al lado del anterior
    pygame.draw.rect(ventana, ROJO, (ANCHO//1.82, ALTO//1.678, ANCHO//25.2, ALTO//3.6))
    # Dibujar 1 recuadro de color amarillo al lado del anterior
    pygame.draw.rect(ventana, AMARILLO, (ANCHO//1.695, ALTO//1.678, ANCHO//25.2, ALTO//3.6))
    # Dibujar 1 recuadro de color rojo al lado del anterior
    pygame.draw.rect(ventana, ROJO, (ANCHO//1.587, ALTO//1.678, ANCHO//25.2, ALTO//3.6))
    # Dibujar 1 recuadro de color amarillo al lado del anterior
    pygame.draw.rect(ventana, AMARILLO, (ANCHO//1.493, ALTO//1.678, ANCHO//25.2, ALTO//3.6))
    # Dibujar 1 recuadro de color rojo al lado del anterior
    pygame.draw.rect(ventana, ROJO, (ANCHO//1.41, ALTO//1.678, ANCHO//25.2, ALTO//3.6))
    # Dibujar 1 recuadro de color amarillo al lado del anterior
    pygame.draw.rect(ventana, AMARILLO, (ANCHO//1.339, ALTO//1.678, ANCHO//25.2, ALTO//3.6))


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
