import pygame, pygame_gui

from utils.colores import MELON_OSCURO, ROJO, AMARILLO, NEGRO, BEIGE, MELON_CLARO, MELON_TRASLUCIDO
from utils.figuras import dibujar_rectangulo_redondeado
from view.ficha import Ficha

class Tablero2:
    def __init__(self, alto, ancho):
        # INICIALIZAR PYGAME
        pygame.init()

        self.alto = alto
        self.ancho = ancho

        # IMPORTACION DE FUENTES
        self.fTitulo = pygame.font.Font('fuentes/Inter-ExtraBold.ttf', self.alto//15)
        self.fTexto1 = pygame.font.Font('fuentes/Inter-MediumItalic.otf', self.alto//50)
        self.fTexto2 = pygame.font.Font('fuentes/Inter-MediumItalic.otf', self.alto//60)
        self.fTexto3 = pygame.font.Font('fuentes/Inter-ExtraBold.ttf', self.alto//50)
        self.fTexto4 = pygame.font.Font('fuentes/Inter-Bold.ttf', self.alto//50)
        self.fTexto5 = pygame.font.Font('fuentes/Inter-Bold.ttf', self.alto//30)

        # LISTA DE POSICIONES
        # Lista de posiciones a las que se puede mover una ficha
        '''self.posiciones_tablero = [(self.ancho//3.02, self.alto//3), (self.ancho//2.7, self.alto//3), (self.ancho//2.44, self.alto//3), (self.ancho//2.22, self.alto//3), (self.ancho//2.04, self.alto//3), (self.ancho//1.89, self.alto//3), 
                            (self.ancho//1.755, self.alto//3), (self.ancho//1.64, self.alto//3), (self.ancho//1.54, self.alto//3), (self.ancho//1.45, self.alto//3), (self.ancho//1.375, self.alto//3), (self.ancho//1.305, self.alto//3), 
                            (self.ancho//3.02, self.alto//1.28), (self.ancho//2.7, self.alto//1.28), (self.ancho//2.44, self.alto//1.28), (self.ancho//2.22, self.alto//1.28), (self.ancho//2.04, self.alto//1.28), (self.ancho//1.89, self.alto//1.28), 
                            (self.ancho//1.755, self.alto//1.28), (self.ancho//1.64, self.alto//1.28), (self.ancho//1.54, self.alto//1.28), (self.ancho//1.45, self.alto//1.28), (self.ancho//1.375, self.alto//1.28), (self.ancho//1.305, self.alto//1.28),]
        '''
        self.posiciones_fichas = [
            [
                (self.ancho//3.02, self.alto//3), (self.ancho//2.7, self.alto//3), (self.ancho//2.44, self.alto//3), (self.ancho//2.22, self.alto//3), (self.ancho//2.04, self.alto//3), (self.ancho//1.89, self.alto//3),
                (self.ancho//1.755, self.alto//3), (self.ancho//1.64, self.alto//3), (self.ancho//1.54, self.alto//3), (self.ancho//1.45, self.alto//3), (self.ancho//1.375, self.alto//3), (self.ancho//1.305, self.alto//3)
            ],
            [
                (self.ancho//3.02, self.alto//1.28), (self.ancho//2.7, self.alto//1.28), (self.ancho//2.44, self.alto//1.28), (self.ancho//2.22, self.alto//1.28), (self.ancho//2.04, self.alto//1.28), (self.ancho//1.89, self.alto//1.28),
                (self.ancho//1.755, self.alto//1.28), (self.ancho//1.64, self.alto//1.28), (self.ancho//1.54, self.alto//1.28), (self.ancho//1.45, self.alto//1.28), (self.ancho//1.375, self.alto//1.28), (self.ancho//1.305, self.alto//1.28)

            ]]
        self.nFichasEnTablero = [[5, 0, 0, 0, 3, 0, 5, 0, 0, 0, 0, 2],[5, 0, 0, 0, 3, 0, 5, 0, 0, 0, 0, 2]]

        self.fichas = []

        # CREAR LA VENTANA Y EL ADMINISTRADOR DE INTERFAZ
        self.ventana = pygame.display.set_mode((self.ancho, self.alto))
        self.manager = pygame_gui.UIManager((self.ancho, self.alto))

        # AGREGAR UN TITULO A LA VENTANA
        pygame.display.set_caption("Backgammon rebote")

        
    def mostrar_pantalla(self, j1, j2, turno_actual, tablero, fr, fa):
        # Reloj de Pygame
        clock = pygame.time.Clock()

        # AGREGAR TEXTO
        # Agregar un texto en la ventana
        titulo = self.fTitulo.render("BACKGAMMON REBOTE", True, MELON_OSCURO)

        # TABLERO DE JUEGO
        # Tamaño del rectángulo
        superficie_transparente = pygame.Surface((self.ancho//2.1, self.alto//1.68))
        # 60% de transparencia 
        superficie_transparente.set_alpha(255 * 0.6) 

        # IMAGENES
        # Importar imagen del dado
        imagen_dado = pygame.image.load("imagenes/dado.png")
        # Escalar la imagen
        imagen_dado = pygame.transform.scale(imagen_dado, (self.alto//13, self.alto//13))

        # Importar imagen de la moneda
        imagen_moneda = pygame.image.load("imagenes/moneda.png")
        # Escalar la imagen
        imagen_moneda = pygame.transform.scale(imagen_moneda, (self.alto//13, self.alto//13))

        # Importar imagen del jugador 1
        imagen_jugador1 = pygame.image.load("imagenes/jugador.png")
        # Escalar la imagen
        imagen_jugador1 = pygame.transform.scale(imagen_jugador1, (self.alto//13, self.alto//13))
        
        # Importar imagen del jugador 2
        imagen_jugador2 = pygame.image.load("imagenes/jugador.png")
        # Escalar la imagen
        imagen_jugador2 = pygame.transform.scale(imagen_jugador2, (self.alto//13, self.alto//13))

        # AGREGAR TEXTO
        # Agregar el texto del valor del dado en la ventana
        valor_dado = self.fTexto1.render("Valor obtenido:", True, NEGRO) # el primer argumento indica el texto, el segundo si se quiere suavizar el texto y el tercero el color
        
        # Agregar el texto del valor de la moneda a la ventana
        valor_moneda = self.fTexto1.render("Valor obtenido:", True, NEGRO)

        # JUGADOR 1
        jugador1 = self.fTexto1.render("JUGADOR 1", True, NEGRO)
        pseudonimo1 = self.fTexto2.render(f" - Pseudónimo: {j1.get_pseudonimo()}", True, NEGRO)
        color_fichas1 = self.fTexto2.render(f" - Color de fichas: {j1.get_colorFicha()}", True, NEGRO)
        
        # JUGADOR 2
        jugador2 = self.fTexto1.render("JUGADOR 2", True, NEGRO)
        pseudonimo2 = self.fTexto2.render(f" - Pseudónimo: {j2.get_pseudonimo()}", True, NEGRO)
        color_fichas2 = self.fTexto2.render(f" - Color de fichas: {j2.get_colorFicha()}", True, NEGRO)

        tiempo_turno1 = self.fTexto3.render("TIEMPO", True, NEGRO)
        tiempo_turno2 = self.fTexto3.render("POR TURNO", True, NEGRO)
        tiempo_juego1 = self.fTexto3.render("TIEMPO", True, NEGRO)
        tiempo_juego2 = self.fTexto3.render("DE JUEGO", True, NEGRO)

        fichas_liberadas1 = self.fTexto4.render("Fichas liberadas", True, NEGRO)
        fichas_capturadas1 = self.fTexto4.render("Fichas capturadas", True, NEGRO)
        fichas_liberadas2 = self.fTexto4.render("Fichas liberadas", True, NEGRO)
        fichas_capturadas2 = self.fTexto4.render("Fichas capturadas", True, NEGRO)


        tablero.obtener_casillas()
        tablero_01 = []
        tablero_p1, tablero_p2 = [], []
        
        for i in range(12):
            if tablero.estado_casilla(0, i) == 'v':
                tablero_p1.append(0)
            # Si es rojo
            elif tablero.estado_casilla(0, i) in ['dro', 'drf']:
                tablero_p1.append(1)
            # Si es amarillo
            elif tablero.estado_casilla(0, i) in ['dao', 'daf']:
                tablero_p1.append(2)
        
        for i in range(12):
            if tablero.estado_casilla(1, i) == 'v':
                tablero_p2.append(0)
            # Si es rojo
            elif tablero.estado_casilla(0, i) in ['dro', 'drf']:
                tablero_p2.append(1)
            # Si es amarillo
            elif tablero.estado_casilla(0, i) in ['dao', 'daf']:
                tablero_p2.append(2)
        
        tablero_01 = [tablero_p1, tablero_p2]
            
        print(str(tablero_01))

        m=0
        for i in tablero_01[0]:
            if i == 1:
                self.fichas.append(Ficha(ROJO, self.posiciones_fichas[0][m][0], self.posiciones_fichas[0][m][1], 7))
            elif i == 2:
                self.fichas.append(Ficha(AMARILLO, self.posiciones_fichas[0][m][0], self.posiciones_fichas[0][m][1], 7))
            m+=1

        n=0
        for i in tablero_01[1]:
            if i == 1:
                self.fichas.append(Ficha(ROJO, self.posiciones_fichas[1][n][0], self.posiciones_fichas[1][n][1], 7))
            elif i == 2:
                self.fichas.append(Ficha(AMARILLO, self.posiciones_fichas[1][n][0], self.posiciones_fichas[1][n][1], 7))
            n+=1



        # INDICADOR DE TURNO
        turno = self.fTexto5.render(f"Es turno de las fichas {turno_actual.get_turno_actual()}", True, NEGRO)


        corriendo = True
        while corriendo:
            time_delta = clock.tick(60)/1000.0 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    corriendo = False

                self.manager.process_events(event)

            # PINTAR LA PANTALLA
            self.ventana.fill(BEIGE)
            
            # Dibujar 1 recuadro de color melon oscuro (izquierda)
            dibujar_rectangulo_redondeado(self.ventana, MELON_OSCURO, (self.ancho//33, self.alto//6.8, self.ancho//4, self.alto//1.33), 10)

            # Dibujar 1 recuadro de color melon oscuro (superior derecha)
            dibujar_rectangulo_redondeado(self.ventana, MELON_OSCURO, (self.ancho//3.35, self.alto//6.8, self.ancho//1.48, self.alto//11.7), 10)

            # Dibujar 1 recuadro de color melon oscuro (inferior derecha)
            dibujar_rectangulo_redondeado(self.ventana, MELON_OSCURO, (self.ancho//3.35, self.alto//4, self.ancho//1.48, self.alto//1.54), 10)

            # ESCRIBIR TEXTO DEL TITULO
            self.ventana.blit(titulo, (self.ancho//3.8, self.alto//21))

            # OBJETOS, JUGADORES Y RELOJES
            # Dibujar 1 recuadro de color melon claro (izquierda superior)
            dibujar_rectangulo_redondeado(self.ventana, MELON_CLARO, (self.ancho//22, self.alto//5.5, self.ancho//4.6, self.alto//4.8), 10)

            # Dibujar 1 recuadro de color melon claro (izquierda medio)
            dibujar_rectangulo_redondeado(self.ventana, MELON_CLARO, (self.ancho//22, self.alto//2.4, self.ancho//4.6, self.alto//4.8), 10)

            # Dibujar 1 recuadro de color melon claro (izquierda inferior)
            dibujar_rectangulo_redondeado(self.ventana, MELON_CLARO, (self.ancho//22, self.alto//1.53, self.ancho//4.6, self.alto//4.8), 10)

            # Dibujar la superficie transparente en la ventana en la posición del rectángulo
            self.ventana.blit(superficie_transparente, (self.ancho//3.22, self.alto//3.6))

            # Rellenar la superficie con el color deseado
            superficie_transparente.fill(MELON_TRASLUCIDO)

            # TABLERO DE FICHAS LIBERADAS
            # Dibujar 1 recuadro de color melon claro (derecha superior 1)
            dibujar_rectangulo_redondeado(self.ventana, MELON_CLARO, (self.ancho//1.25, self.alto//3.2, self.ancho//6.4, self.alto//7), 10)

            # Dibujar 1 recuadro de color melon claro (derecha superior 2)
            dibujar_rectangulo_redondeado(self.ventana, MELON_CLARO, (self.ancho//1.25, self.alto//2.05, self.ancho//6.4, self.alto//18), 10)

            # Dibujar 1 recuadro de color melon claro (derecha inferior 1)
            dibujar_rectangulo_redondeado(self.ventana, MELON_CLARO, (self.ancho//1.25, self.alto//1.595, self.ancho//6.4, self.alto//7), 10)

            # Dibujar 1 recuadro de color melon claro (derecha inferior 2)
            dibujar_rectangulo_redondeado(self.ventana, MELON_CLARO, (self.ancho//1.25, self.alto//1.24, self.ancho//6.4, self.alto//18), 10)

            # CRONÓMETROS
            # Dibujar 1 recuadro de color melon claro (izquierda inferior 1)
            dibujar_rectangulo_redondeado(self.ventana, MELON_CLARO, (self.ancho//7, self.alto//1.49, self.ancho//9, self.alto//13), 10)

            # Dibujar 1 recuadro de color melon claor (izquierda inferior 2)
            dibujar_rectangulo_redondeado(self.ventana, MELON_CLARO, (self.ancho//7, self.alto//1.31, self.ancho//9, self.alto//13), 10)

            # Dibujar 1 recuadro de color melon oscuro (izquierda inferior 3)
            dibujar_rectangulo_redondeado(self.ventana, MELON_OSCURO, (self.ancho//6.8, self.alto//1.475, self.ancho//10, self.alto//14), 10)

            # Dibujar 1 recuadro de color melon oscuro (izquierda inferior 4)
            dibujar_rectangulo_redondeado(self.ventana, MELON_OSCURO, (self.ancho//6.8, self.alto//1.3, self.ancho//10, self.alto//14), 10)
            
            # SECCIONES DEL TABLERO
            # ---- Parte de arriba ----
            # Dibujar 1 recuadro de color rojo
            pygame.draw.rect(self.ventana, AMARILLO, (self.ancho//3.22, self.alto//3.6, self.ancho//25.2, self.alto//3.6))
            # Dibujar 1 recuadro de color amarillo al lado del anterior
            pygame.draw.rect(self.ventana, ROJO, (self.ancho//2.85, self.alto//3.6, self.ancho//25.2, self.alto//3.6))
            # Dibujar 1 recuadro de color rojo al lado del anterior
            pygame.draw.rect(self.ventana, AMARILLO, (self.ancho//2.56, self.alto//3.6, self.ancho//25.2, self.alto//3.6))
            # Dibujar 1 recuadro de color amarillo al lado del anterior
            pygame.draw.rect(self.ventana, ROJO, (self.ancho//2.32, self.alto//3.6, self.ancho//25.2, self.alto//3.6))
            # Dibujar 1 recuadro de color rojo al lado del anterior
            pygame.draw.rect(self.ventana, AMARILLO, (self.ancho//2.125, self.alto//3.6, self.ancho//25.2, self.alto//3.6))
            # Dibujar 1 recuadro de color amarillo al lado del anterior
            pygame.draw.rect(self.ventana, ROJO, (self.ancho//1.96, self.alto//3.6, self.ancho//25.2, self.alto//3.6))
            # Dibujar 1 recuadro de color rojo al lado del anterior
            pygame.draw.rect(self.ventana, AMARILLO, (self.ancho//1.82, self.alto//3.6, self.ancho//25.2, self.alto//3.6))
            # Dibujar 1 recuadro de color amarillo al lado del anterior
            pygame.draw.rect(self.ventana, ROJO, (self.ancho//1.695, self.alto//3.6, self.ancho//25.2, self.alto//3.6))
            # Dibujar 1 recuadro de color rojo al lado del anterior
            pygame.draw.rect(self.ventana, AMARILLO, (self.ancho//1.587, self.alto//3.6, self.ancho//25.2, self.alto//3.6))
            # Dibujar 1 recuadro de color amarillo al lado del anterior
            pygame.draw.rect(self.ventana, ROJO, (self.ancho//1.493, self.alto//3.6, self.ancho//25.2, self.alto//3.6))
            # Dibujar 1 recuadro de color rojo al lado del anterior
            pygame.draw.rect(self.ventana, AMARILLO, (self.ancho//1.41, self.alto//3.6, self.ancho//25.2, self.alto//3.6))
            # Dibujar 1 recuadro de color amarillo al lado del anterior
            pygame.draw.rect(self.ventana, ROJO, (self.ancho//1.339, self.alto//3.6, self.ancho//25.2, self.alto//3.6))
            
            # ---- Parte de abajo ----
            # Dibujar 1 recuadro de color rojo
            pygame.draw.rect(self.ventana, ROJO, (self.ancho//3.22, self.alto//1.678, self.ancho//25.2, self.alto//3.6))
            # Dibujar 1 recuadro de color amarillo al lado del anterior
            pygame.draw.rect(self.ventana, AMARILLO, (self.ancho//2.85, self.alto//1.678, self.ancho//25.2, self.alto//3.6))
            # Dibujar 1 recuadro de color rojo al lado del anterior
            pygame.draw.rect(self.ventana, ROJO, (self.ancho//2.56, self.alto//1.678, self.ancho//25.2, self.alto//3.6))
            # Dibujar 1 recuadro de color amarillo al lado del anterior
            pygame.draw.rect(self.ventana, AMARILLO, (self.ancho//2.32, self.alto//1.678, self.ancho//25.2, self.alto//3.6))
            # Dibujar 1 recuadro de color rojo al lado del anterior
            pygame.draw.rect(self.ventana, ROJO, (self.ancho//2.125, self.alto//1.678, self.ancho//25.2, self.alto//3.6))
            # Dibujar 1 recuadro de color amarillo al lado del anterior
            pygame.draw.rect(self.ventana, AMARILLO, (self.ancho//1.96, self.alto//1.678, self.ancho//25.2, self.alto//3.6))
            # Dibujar 1 recuadro de color rojo al lado del anterior
            pygame.draw.rect(self.ventana, ROJO, (self.ancho//1.82, self.alto//1.678, self.ancho//25.2, self.alto//3.6))
            # Dibujar 1 recuadro de color amarillo al lado del anterior
            pygame.draw.rect(self.ventana, AMARILLO, (self.ancho//1.695, self.alto//1.678, self.ancho//25.2, self.alto//3.6))
            # Dibujar 1 recuadro de color rojo al lado del anterior
            pygame.draw.rect(self.ventana, ROJO, (self.ancho//1.587, self.alto//1.678, self.ancho//25.2, self.alto//3.6))
            # Dibujar 1 recuadro de color amarillo al lado del anterior
            pygame.draw.rect(self.ventana, AMARILLO, (self.ancho//1.493, self.alto//1.678, self.ancho//25.2, self.alto//3.6))
            # Dibujar 1 recuadro de color rojo al lado del anterior
            pygame.draw.rect(self.ventana, ROJO, (self.ancho//1.41, self.alto//1.678, self.ancho//25.2, self.alto//3.6))
            # Dibujar 1 recuadro de color amarillo al lado del anterior
            pygame.draw.rect(self.ventana, AMARILLO, (self.ancho//1.339, self.alto//1.678, self.ancho//25.2, self.alto//3.6))

            # Dibujar la imagen en la ventana
            self.ventana.blit(imagen_dado, (self.ancho//17, self.alto//5))

            # Dibujar la imagen en la ventana
            self.ventana.blit(imagen_moneda, (self.ancho//17, self.alto//3.5))
            
            # Dibujar la imagen en la ventana
            self.ventana.blit(imagen_jugador1, (self.ancho//17, self.alto//2.3))
            
            # Dibujar la imagen en la ventana
            self.ventana.blit(imagen_jugador2, (self.ancho//17, self.alto//1.9))    

            # AGREGAR TEXTO
            self.ventana.blit(valor_dado, (self.ancho//9, self.alto//4.4))
            self.ventana.blit(valor_moneda, (self.ancho//9, self.alto//3.2))
            self.ventana.blit(jugador1, (self.ancho//9, self.alto//2.3))
            self.ventana.blit(pseudonimo1, (self.ancho//9, self.alto//2.15))
            self.ventana.blit(color_fichas1, (self.ancho//9, self.alto//2.05))
            self.ventana.blit(jugador2, (self.ancho//9, self.alto//1.9))
            self.ventana.blit(pseudonimo2, (self.ancho//9, self.alto//1.8))
            self.ventana.blit(color_fichas2, (self.ancho//9, self.alto//1.73))
            self.ventana.blit(tiempo_turno1, (self.ancho//16, self.alto//1.45))
            self.ventana.blit(tiempo_turno2, (self.ancho//16, self.alto//1.4))
            self.ventana.blit(tiempo_juego1, (self.ancho//16, self.alto//1.3))
            self.ventana.blit(tiempo_juego2, (self.ancho//16, self.alto//1.26))
            self.ventana.blit(fichas_liberadas1, (self.ancho//1.205, self.alto//3.5))
            self.ventana.blit(fichas_capturadas1, (self.ancho//1.21, self.alto//2.16))
            self.ventana.blit(fichas_liberadas2, (self.ancho//1.205, self.alto//1.665))
            self.ventana.blit(fichas_capturadas2, (self.ancho//1.21, self.alto//1.283))
            self.ventana.blit(turno, (self.ancho//1.9, self.alto//6))


            # CRONOMETRO POR TURNO
            # Inicializar el cronómetro
            inicio_cronometro_turno = pygame.time.get_ticks() # devuelve el tiempo en milisegundos desde que se llamó al juego
            inicio_cronometro_juego = pygame.time.get_ticks()

            # Calcular el tiempo restante
            tiempo_transcurrido_turno = (pygame.time.get_ticks() - inicio_cronometro_turno) / 1000  # Convertir a segundos
            tiempo_restante_turno = 60 - tiempo_transcurrido_turno  # 60 segundos = 1 minuto

            # Si el tiempo restante es 0 o menos, terminar el juego
            if tiempo_restante_turno <= 0:
                print("¡Tiempo agotado por turno!")

            '''# CRONOMETRO GENERAL DEL JUEGO
            # Calcular el tiempo restante
            tiempo_transcurrido_juego = (pygame.time.get_ticks() - inicio_cronometro_juego) / 1000  # Convertir a segundos
            tiempo_restante_juego = 1800 - tiempo_transcurrido_juego  # 1800 segundos = 30 minutos

            # Si el tiempo restante es 0 o menos, terminar el juego
            if tiempo_restante_juego <= 0:
                print("¡Tiempo agotado! ¡Fin del juego!")

            # Convertir el tiempo restante a formato mm:ss
            minutos_turno = int(tiempo_restante_turno) // 60
            segundos_turno = int(tiempo_restante_turno) % 60
            tiempo_formateado_turno = "{:02d}:{:02d}".format(minutos_turno, segundos_turno)


            # Renderizar el tiempo restante y dibujarlo en la ventana
            fTexto6 = pygame.font.Font('fuentes/Inter-Bold.ttf', self.alto//30)
            cronometro_turno = fTexto6.render(tiempo_formateado_turno, True, NEGRO)
            self.ventana.blit(cronometro_turno, (self.ancho//6, self.alto//1.45))

            # CRONOMETRO GENERAL DEL JUEGO
            # Convertir el tiempo restante a formato mm:ss
            minutos_juego = int(tiempo_restante_juego) // 60
            segundos_juego = int(tiempo_restante_juego) % 60
            tiempo_formateado_juego = "{:02d}:{:02d}".format(minutos_juego, segundos_juego)

            # Renderizar el tiempo restante y dibujarlo en la ventana
            cronometro_juego = fTexto6.render(tiempo_formateado_juego, True, NEGRO)
            self.ventana.blit(cronometro_juego, (self.ancho//6, self.alto//1.28))'''

            
            for ficha in self.fichas:
                ficha.dibujar(self.ventana)

            pygame.display.update()

    def actualizar_pantalla(self, controlador, estado):
        clock = pygame.time.Clock()
        corriendo = True

        while corriendo:
            time_delta = clock.tick(60)/1000.0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    corriendo = False

                self.manager.process_events(event)

                # Mover las fichas
                fichas = controlador.mover_ficha(event, estado)
                self.fichas = fichas

                # Borrar las fichas dibujadas previamente
                for ficha in self.fichas:
                    if ficha.get_imagen_fondo():
                        self.ventana.blit(ficha.get_imagen_fondo(), ficha.get_rect().topleft)
                
                # Vaciamos el arreglo de fichas para "borrar" las fichas dibujadas
                self.fichas.clear()

                for ficha in fichas:
                    ficha.guardar_fondo(self.ventana)
                    ficha.dibujar(self.ventana)
                    self.fichas.append(ficha)
            
            pygame.display.update()

        return estado