import pygame, sys
from pync import Notifier
from utils.colores import AMARILLO, MELON_CLARO, MELON_OSCURO, ROJO, MELON_TRASLUCIDO, BEIGE, NEGRO
from utils.figuras import dibujar_rectangulo_redondeado
from model.ficha import Ficha

pseudonimo1, pseudonimo2, color1, color2 = '', '', '', ''

def setPseudonimos(pseudo1, pseudo2):
    global pseudonimo1, pseudonimo2
    pseudonimo1 = pseudo1
    pseudonimo2 = pseudo2

def setColores(cor1, cor2):
    global color1, color2
    color1 = cor1
    color2 = cor2

def registrar_Datos_Jugadores():
    global pseudonimo1, pseudonimo2, color1, color2
    return pseudonimo1, pseudonimo2, color1, color2

# Funcion para mover una ficha
def mover_ficha(ficha, objetivo, ventana, frames=2, delay=50): 
    dx = (objetivo[0] - ficha.obtenerPosicion()[0]) / frames
    dy = (objetivo[1] - ficha.obtenerPosicion()[1]) / frames

    for i in range(frames):
        # Actualizar la posición de la ficha
        nueva_posicion_x = ficha.obtenerPosicion()[0] + dx
        nueva_posicion_y = ficha.obtenerPosicion()[1] + dy
        ficha.cambiarPosicion(nueva_posicion_x, nueva_posicion_y, ventana)
        
        # Actualizar la ventana de visualización
        pygame.display.update()
        
        # Esperar un breve período de tiempo antes de la siguiente iteración
        pygame.time.wait(delay)


def mostrar_pantalla_Tablero(ventana, manager, ANCHO, ALTO):
    # Agregar un titulo a la ventana
    pygame.display.set_caption("Backgammon rebote")

    # TÍTULO
    # Importación de la fuente para el titulo
    fTitulo = pygame.font.Font('fuentes/Inter-ExtraBold.ttf', ALTO//15)
    # Agregar un texto en la ventana
    titulo = fTitulo.render("BACKGAMMON REBOTE", True, MELON_OSCURO)

    # TABLERO DE JUEGO
    # Dibujar 1 recuadro de color melon claro (derecha superior)
    superficie_transparente = pygame.Surface((ANCHO//2.1, ALTO//1.68)) # Tamaño del rectángulo
    # Establecer el nivel de transparencia (alpha) de la superficie
    superficie_transparente.set_alpha(255 * 0.6)  # 60% de transparencia

    # IMAGENES
    # Importar imagen del dado
    imagen_dado = pygame.image.load("imagenes/dado.png")
    # Escalar la imagen
    imagen_dado = pygame.transform.scale(imagen_dado, (ALTO//13, ALTO//13))

    # Importar imagen de la moneda
    imagen_moneda = pygame.image.load("imagenes/moneda.png")
    # Escalar la imagen
    imagen_moneda = pygame.transform.scale(imagen_moneda, (ALTO//13, ALTO//13))
    
    # Importar imagen del jugador 1
    imagen_jugador1 = pygame.image.load("imagenes/jugador.png")
    # Escalar la imagen
    imagen_jugador1 = pygame.transform.scale(imagen_jugador1, (ALTO//13, ALTO//13))
    
    # Importar imagen del jugador 2
    imagen_jugador2 = pygame.image.load("imagenes/jugador.png")
    # Escalar la imagen
    imagen_jugador2 = pygame.transform.scale(imagen_jugador2, (ALTO//13, ALTO//13))
    

    # AGREGAR TEXTO
    # Importación de la fuente
    fTexto1 = pygame.font.Font('fuentes/Inter-MediumItalic.otf', ALTO//50)
    # Agregar el texto del valor del dado en la ventana
    valor_dado = fTexto1.render("Valor obtenido:", True, NEGRO) # el primer argumento indica el texto, el segundo si se quiere suavizar el texto y el tercero el color
    
    # Agregar el texto del valor de la moneda a la ventana
    valor_moneda = fTexto1.render("Valor obtenido:", True, NEGRO)
    
    
    pseudo1, pseudo2, color1, color2 = registrar_Datos_Jugadores()

    fTexto2 = pygame.font.Font('fuentes/Inter-MediumItalic.otf', ALTO//60)
    # JUGADOR 1
    jugador1 = fTexto1.render("JUGADOR 1", True, NEGRO)
    pseudonimo1 = fTexto2.render(f" - Pseudónimo: {pseudo1}", True, NEGRO)
    color_fichas1 = fTexto2.render(f" - Color de fichas: {color1}", True, NEGRO)
    
    # JUGADOR 2
    jugador2 = fTexto1.render("JUGADOR 2", True, NEGRO)
    pseudonimo2 = fTexto2.render(f" - Pseudónimo: {pseudo2}", True, NEGRO)
    color_fichas2 = fTexto2.render(f" - Color de fichas: {color2}", True, NEGRO)
    
    fTexto3 = pygame.font.Font('fuentes/Inter-ExtraBold.ttf', ALTO//50)
    tiempo_turno1 = fTexto3.render("TIEMPO", True, NEGRO)
    tiempo_turno2 = fTexto3.render("POR TURNO", True, NEGRO)
    tiempo_juego1 = fTexto3.render("TIEMPO", True, NEGRO)
    tiempo_juego2 = fTexto3.render("DE JUEGO", True, NEGRO)
    
    fTexto4 = pygame.font.Font('fuentes/Inter-Bold.ttf', ALTO//50)
    fichas_liberadas1 = fTexto4.render("Fichas liberadas", True, NEGRO)
    fichas_capturadas1 = fTexto4.render("Fichas capturadas", True, NEGRO)
    fichas_liberadas2 = fTexto4.render("Fichas liberadas", True, NEGRO)
    fichas_capturadas2 = fTexto4.render("Fichas capturadas", True, NEGRO)
    

    # INDICADOR DE TURNO
    fTexto5 = pygame.font.Font('fuentes/Inter-Bold.ttf', ALTO//30)
    turno = fTexto5.render("Es turno del Jugador", True, NEGRO)
    
    # CRONOMETRO POR TURNO
    # Inicializar el cronómetro
    inicio_cronometro_turno = pygame.time.get_ticks() # devuelve el tiempo en milisegundos desde que se llamó al juego
    inicio_cronometro_juego = pygame.time.get_ticks()


    # LISTA DE POSICIONES
    # Lista de posiciones a las que se puede mover una ficha
    posiciones_tablero = [(ANCHO//3.02, ALTO//3), (ANCHO//2.7, ALTO//3), (ANCHO//2.44, ALTO//3), (ANCHO//2.22, ALTO//3), (ANCHO//2.04, ALTO//3), (ANCHO//1.89, ALTO//3), 
                        (ANCHO//1.755, ALTO//3), (ANCHO//1.64, ALTO//3), (ANCHO//1.54, ALTO//3), (ANCHO//1.45, ALTO//3), (ANCHO//1.375, ALTO//3), (ANCHO//1.305, ALTO//3), 
                        (ANCHO//3.02, ALTO//1.28), (ANCHO//2.7, ALTO//1.28), (ANCHO//2.44, ALTO//1.28), (ANCHO//2.22, ALTO//1.28), (ANCHO//2.04, ALTO//1.28), (ANCHO//1.89, ALTO//1.28), 
                        (ANCHO//1.755, ALTO//1.28), (ANCHO//1.64, ALTO//1.28), (ANCHO//1.54, ALTO//1.28), (ANCHO//1.45, ALTO//1.28), (ANCHO//1.375, ALTO//1.28), (ANCHO//1.305, ALTO//1.28),]

    nFichasEnTablero = [[5, 0, 0, 0, 3, 0, 5, 0, 0, 0, 0, 2],[5, 0, 0, 0, 3, 0, 5, 0, 0, 0, 0, 2]]

    ficha_seleccionada = None
    destino_seleccionado = None

    # Fichas
    fichas = [
        Ficha(ROJO, posiciones_tablero[4][0], posiciones_tablero[4][1], 3),
        Ficha(ROJO, posiciones_tablero[6][0], posiciones_tablero[6][1], 5),
        Ficha(ROJO, posiciones_tablero[12][0], posiciones_tablero[12][1], 5),
        Ficha(ROJO, posiciones_tablero[23][0], posiciones_tablero[23][1], 2),
        Ficha(AMARILLO, posiciones_tablero[0][0], posiciones_tablero[0][1], 5),
        Ficha(AMARILLO, posiciones_tablero[11][0], posiciones_tablero[11][1], 2),
        Ficha(AMARILLO, posiciones_tablero[16][0], posiciones_tablero[16][1], 3),
        Ficha(AMARILLO, posiciones_tablero[18][0], posiciones_tablero[18][1], 5)
    ]

    
    # Bucle principal del juego
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if evento.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos() # Obtener la posición del mouse
                if ficha_seleccionada is None:
                    for ficha in fichas:
                        if ficha.rect.collidepoint(pos):
                            ficha_seleccionada = ficha
                            ficha_seleccionada.seleccionar(True)
                            ficha_seleccionada.mostrarInformacion()
                            break
                else:
                    for i, pos_tablero in enumerate(posiciones_tablero):
                        rect = pygame.Rect(pos_tablero[0] - 15, pos_tablero[1] - 15, 30, 30)
                        if rect.collidepoint(pos):
                            destino_seleccionado = i
                            ficha_seleccionada.seleccionar(False)
                            mover_ficha(ficha_seleccionada, posiciones_tablero[destino_seleccionado], ventana)
                            ficha_seleccionada = None
                            destino_seleccionado = None
                            break


        # CRONOMETRO POR TURNO
        # Calcular el tiempo restante
        tiempo_transcurrido_turno = (pygame.time.get_ticks() - inicio_cronometro_turno) / 1000  # Convertir a segundos
        tiempo_restante_turno = 60 - tiempo_transcurrido_turno  # 60 segundos = 1 minuto

        # Si el tiempo restante es 0 o menos, terminar el juego
        if tiempo_restante_turno <= 0:
            print("¡Tiempo agotado por turno!")
            #pygame.quit()
            #sys.exit()


        # CRONOMETRO GENERAL DEL JUEGO
        # Calcular el tiempo restante
        tiempo_transcurrido_juego = (pygame.time.get_ticks() - inicio_cronometro_juego) / 1000  # Convertir a segundos
        tiempo_restante_juego = 1800 - tiempo_transcurrido_juego  # 1800 segundos = 30 minutos

        # Si el tiempo restante es 0 o menos, terminar el juego
        if tiempo_restante_juego <= 0:
            print("¡Tiempo agotado! ¡Fin del juego!")
            #pygame.quit()
            #sys.exit()

        # DIBUJAR LA PANTALLA
        # PINTAR LA PANTALLA
        ventana.fill(BEIGE)
        
        # Dibujar 1 recuadro de color melon oscuro (izquierda)
        dibujar_rectangulo_redondeado(ventana, MELON_OSCURO, (ANCHO//33, ALTO//6.8, ANCHO//4, ALTO//1.33), 10)

        # Dibujar 1 recuadro de color melon oscuro (superior derecha)
        dibujar_rectangulo_redondeado(ventana, MELON_OSCURO, (ANCHO//3.35, ALTO//6.8, ANCHO//1.48, ALTO//11.7), 10)

        # Dibujar 1 recuadro de color melon oscuro (inferior derecha)
        dibujar_rectangulo_redondeado(ventana, MELON_OSCURO, (ANCHO//3.35, ALTO//4, ANCHO//1.48, ALTO//1.54), 10)

        # ESCRIBIR TEXTO DEL TITULO
        ventana.blit(titulo, (ANCHO//3.8, ALTO//21))

        # OBJETOS, JUGADORES Y RELOJES
        # Dibujar 1 recuadro de color melon claro (izquierda superior)
        dibujar_rectangulo_redondeado(ventana, MELON_CLARO, (ANCHO//22, ALTO//5.5, ANCHO//4.6, ALTO//4.8), 10)

        # Dibujar 1 recuadro de color melon claro (izquierda medio)
        dibujar_rectangulo_redondeado(ventana, MELON_CLARO, (ANCHO//22, ALTO//2.4, ANCHO//4.6, ALTO//4.8), 10)

        # Dibujar 1 recuadro de color melon claro (izquierda inferior)
        dibujar_rectangulo_redondeado(ventana, MELON_CLARO, (ANCHO//22, ALTO//1.53, ANCHO//4.6, ALTO//4.8), 10)

        # Dibujar la superficie transparente en la ventana en la posición del rectángulo
        ventana.blit(superficie_transparente, (ANCHO//3.22, ALTO//3.6))

        # Rellenar la superficie con el color deseado
        superficie_transparente.fill(MELON_TRASLUCIDO)

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
        # Dibujar 1 recuadro de color melon claro (izquierda inferior 1)
        dibujar_rectangulo_redondeado(ventana, MELON_CLARO, (ANCHO//7, ALTO//1.49, ANCHO//9, ALTO//13), 10)

        # Dibujar 1 recuadro de color melon claor (izquierda inferior 2)
        dibujar_rectangulo_redondeado(ventana, MELON_CLARO, (ANCHO//7, ALTO//1.31, ANCHO//9, ALTO//13), 10)

        # Dibujar 1 recuadro de color melon oscuro (izquierda inferior 3)
        dibujar_rectangulo_redondeado(ventana, MELON_OSCURO, (ANCHO//6.8, ALTO//1.475, ANCHO//10, ALTO//14), 10)

        # Dibujar 1 recuadro de color melon oscuro (izquierda inferior 4)
        dibujar_rectangulo_redondeado(ventana, MELON_OSCURO, (ANCHO//6.8, ALTO//1.3, ANCHO//10, ALTO//14), 10)
        
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

        # Dibujar la imagen en la ventana
        ventana.blit(imagen_dado, (ANCHO//17, ALTO//5))

        # Dibujar la imagen en la ventana
        ventana.blit(imagen_moneda, (ANCHO//17, ALTO//3.5))
        
        # Dibujar la imagen en la ventana
        ventana.blit(imagen_jugador1, (ANCHO//17, ALTO//2.3))
        
        # Dibujar la imagen en la ventana
        ventana.blit(imagen_jugador2, (ANCHO//17, ALTO//1.9))    

        # AGREGAR TEXTO
        ventana.blit(valor_dado, (ANCHO//9, ALTO//4.4))
        ventana.blit(valor_moneda, (ANCHO//9, ALTO//3.2))
        ventana.blit(jugador1, (ANCHO//9, ALTO//2.3))
        ventana.blit(pseudonimo1, (ANCHO//9, ALTO//2.15))
        ventana.blit(color_fichas1, (ANCHO//9, ALTO//2.05))
        ventana.blit(jugador2, (ANCHO//9, ALTO//1.9))
        ventana.blit(pseudonimo2, (ANCHO//9, ALTO//1.8))
        ventana.blit(color_fichas2, (ANCHO//9, ALTO//1.73))
        ventana.blit(tiempo_turno1, (ANCHO//16, ALTO//1.45))
        ventana.blit(tiempo_turno2, (ANCHO//16, ALTO//1.4))
        ventana.blit(tiempo_juego1, (ANCHO//16, ALTO//1.3))
        ventana.blit(tiempo_juego2, (ANCHO//16, ALTO//1.26))
        ventana.blit(fichas_liberadas1, (ANCHO//1.205, ALTO//3.5))
        ventana.blit(fichas_capturadas1, (ANCHO//1.21, ALTO//2.16))
        ventana.blit(fichas_liberadas2, (ANCHO//1.205, ALTO//1.665))
        ventana.blit(fichas_capturadas2, (ANCHO//1.21, ALTO//1.283))
        ventana.blit(turno, (ANCHO//1.9, ALTO//6))


        # CRONOMETRO POR TURNO
        # Convertir el tiempo restante a formato mm:ss
        minutos_turno = int(tiempo_restante_turno) // 60
        segundos_turno = int(tiempo_restante_turno) % 60
        tiempo_formateado_turno = "{:02d}:{:02d}".format(minutos_turno, segundos_turno)


        # Renderizar el tiempo restante y dibujarlo en la ventana
        fTexto6 = pygame.font.Font('fuentes/Inter-Bold.ttf', ALTO//30)
        cronometro_turno = fTexto6.render(tiempo_formateado_turno, True, NEGRO)
        ventana.blit(cronometro_turno, (ANCHO//6, ALTO//1.45))

        # CRONOMETRO GENERAL DEL JUEGO
        # Convertir el tiempo restante a formato mm:ss
        minutos_juego = int(tiempo_restante_juego) // 60
        segundos_juego = int(tiempo_restante_juego) % 60
        tiempo_formateado_juego = "{:02d}:{:02d}".format(minutos_juego, segundos_juego)

        # Renderizar el tiempo restante y dibujarlo en la ventana
        cronometro_juego = fTexto6.render(tiempo_formateado_juego, True, NEGRO)
        ventana.blit(cronometro_juego, (ANCHO//6, ALTO//1.28))

        for ficha in fichas:
            ficha.dibujar(ventana)

        pygame.display.update()