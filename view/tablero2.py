import pygame, pygame_gui

from utils.colores import MELON_OSCURO, ROJO, AMARILLO, NEGRO, BEIGE, MELON_CLARO, MELON_TRASLUCIDO
from utils.figuras import dibujar_rectangulo_redondeado
from view.ficha import Ficha
from controller.controlador2 import Controlador2
from controller.controlador_tablero2 import C_Tablero2
from controller.reglas import mover_ADRO, mover_ADAO
from model.dado import Dado
from model.moneda import Moneda
from model.estado import Estado

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

        self.ganador = None

        self.ficha_seleccionada = None

        # CREAR LA VENTANA Y EL ADMINISTRADOR DE INTERFAZ
        self.ventana = pygame.display.set_mode((self.ancho, self.alto))
        #self.manager = pygame_gui.UIManager((self.ancho, self.alto))

        # AGREGAR UN TITULO A LA VENTANA
        pygame.display.set_caption("Backgammon rebote")

        
    def mostrar_pantalla(self, j1, j2, estado):
        # Reloj de Pygame
        clock = pygame.time.Clock()

        # AGREGAR TEXTO
        titulo = self.fTitulo.render("BACKGAMMON REBOTE", True, MELON_OSCURO)

        # TABLERO DE JUEGO
        # Tamaño del rectángulo
        superficie_transparente = pygame.Surface((self.ancho//2.1, self.alto//1.68))
        superficie_transparente.set_alpha(255 * 0.6) 

        # IMAGENES
        # Importar imagen del dado
        imagen_dado = pygame.image.load("imagenes/dado.png")
        imagen_dado = pygame.transform.scale(imagen_dado, (self.alto//13, self.alto//13))

        # Importar imagen de la moneda
        imagen_moneda = pygame.image.load("imagenes/moneda.png")
        imagen_moneda = pygame.transform.scale(imagen_moneda, (self.alto//13, self.alto//13))

        # Importar imagen del jugador 1
        imagen_jugador1 = pygame.image.load("imagenes/jugador.png")
        imagen_jugador1 = pygame.transform.scale(imagen_jugador1, (self.alto//13, self.alto//13))
        
        # Importar imagen del jugador 2
        imagen_jugador2 = pygame.image.load("imagenes/jugador.png")
        imagen_jugador2 = pygame.transform.scale(imagen_jugador2, (self.alto//13, self.alto//13))

        # AGREGAR TEXTO
        valor_dado = self.fTexto1.render(f"Valor obtenido: {estado.get_dado()}", True, NEGRO) 
        valor_moneda = self.fTexto1.render(f"Valor obtenido: {estado.get_moneda()}", True, NEGRO)

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

        estado.get_tablero().obtener_casillas()
        tablero_01 = []
        tablero_p1, tablero_p2 = [], []
        
        for i in range(12):
            if estado.get_tablero().estado_casilla(0, i) == 'v':
                tablero_p1.append(0)
            # Si es rojo
            elif estado.get_tablero().estado_casilla(0, i) in ['dro', 'drf']:
                tablero_p1.append(1)
            # Si es amarillo
            elif estado.get_tablero().estado_casilla(0, i) in ['dao', 'daf']:
                tablero_p1.append(2)
        
        for i in range(12):
            if estado.get_tablero().estado_casilla(1, i) == 'v':
                tablero_p2.append(0)
            # Si es rojo
            elif estado.get_tablero().estado_casilla(1, i) in ['dro', 'drf']:
                tablero_p2.append(1)
            # Si es amarillo
            elif estado.get_tablero().estado_casilla(1, i) in ['dao', 'daf']:
                tablero_p2.append(2)
        
        tablero_01 = [tablero_p1, tablero_p2]
            
        print(str(tablero_01))

        '''m=0
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
            n+=1'''
        
        
        for fila in range(2):
            estado.get_FA().mostrar_FA()
            estado.get_FR().mostrar_FR()
            m = 0
            n = 0
            for i in tablero_01[fila]:
                print(m)
                if i == 1:
                    self.fichas.append(Ficha(ROJO, self.posiciones_fichas[fila][m][0], self.posiciones_fichas[fila][m][1], estado.get_FR().estado_casilla_FR(fila, m))) #self.FR[fila][n]
                    print(estado.get_FR().estado_casilla_FR(fila, m))
                elif i == 2:
                    self.fichas.append(Ficha(AMARILLO, self.posiciones_fichas[fila][m][0], self.posiciones_fichas[fila][m][1], estado.get_FA().estado_casilla_FA(fila, m))) #self.FR[fila][n]
                    print(estado.get_FA().estado_casilla_FA(fila, m))
                m += 1
                #n += 1

        '''for fila in range(len(tablero_01)):
            for columna in range(len(tablero_01[fila])):
                if isinstance(tablero_01[fila][columna], list):
                    for k, i in enumerate(tablero_01[fila][columna]):
                        print(f"Fila {fila}, Columna {columna}, k {k}, Valor {i}, Posición {self.posiciones_fichas[fila][columna]}")
                        if i == 1:
                            print(f"Añadiendo ficha ROJA en Fila {fila}, Columna {columna}, k {k}")
                            self.fichas.append(Ficha(ROJO, self.posiciones_fichas[fila][columna][0], self.posiciones_fichas[fila][columna][1], estado.get_FR().estado_casilla_FR(fila, columna, k)))
                        elif i == 2:
                            print(f"Añadiendo ficha AMARILLA en Fila {fila}, Columna {columna}, k {k}")
                            self.fichas.append(Ficha(AMARILLO, self.posiciones_fichas[fila][columna][0], self.posiciones_fichas[fila][columna][1], estado.get_FA().estado_casilla_FA(fila, columna, k)))
                else:
                    i = tablero_01[fila][columna]
                    print(f"Fila {fila}, Columna {columna}, Valor {i}, Posición {self.posiciones_fichas[fila][columna]}")
                    if i == 1:
                        print(f"Añadiendo ficha ROJA en Fila {fila}, Columna {columna}")
                        self.fichas.append(Ficha(ROJO, self.posiciones_fichas[fila][columna][0], self.posiciones_fichas[fila][columna][1], estado.get_FR().estado_casilla_FR(fila, columna)))
                    elif i == 2:
                        print(f"Añadiendo ficha AMARILLA en Fila {fila}, Columna {columna}")
                        self.fichas.append(Ficha(AMARILLO, self.posiciones_fichas[fila][columna][0], self.posiciones_fichas[fila][columna][1], estado.get_FA().estado_casilla_FA(fila, columna)))'''


        # INDICADOR DE TURNO
        turno = self.fTexto5.render(f"Es turno de las fichas {estado.get_turno().get_turno_actual()}", True, NEGRO)

        reloj = pygame.time.Clock()

        corriendo = True
        while corriendo:
            #time_delta = clock.tick(60)/1000.0 
            
            reloj.tick(60)

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

            #print('hola0')

            #Mover fichas
                



            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    corriendo = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos() # Obtener la posicion del mouse
                    print('Acabas de hacer click')
                    print(pos)
                    if self.ficha_seleccionada is None:
                        print('No hay ninguna ficha seleccionada')
                        for ficha in self.fichas:
                            if ficha.rect.collidepoint(pos):
                                self.ficha_seleccionada = ficha
                                self.ficha_seleccionada.seleccionar(True)
                                self.ficha_seleccionada.mostrarInformacion()
                                print(self.ficha_seleccionada.get_regla())
                                break
                    else:
                        print('Ya hay una ficha seleccionada')
                        if self.ficha_seleccionada.get_regla() == "ADRO":
                            x, y, estado = mover_ADRO(self.ficha_seleccionada, estado, self.posiciones_fichas)
                        elif self.ficha_seleccionada.get_regla() == "ADAO":
                            x, y, estado = mover_ADAO(self.ficha_seleccionada, estado, self.posiciones_fichas)

                        if x != -1 and y != -1:
                            pos = (x, y)
                            print(pos)
                            print(pos[0], pos[1])
                            xn = self.posiciones_fichas[pos[0]][pos[1]][0]
                            yn = self.posiciones_fichas[pos[0]][pos[1]][1]
                            self.ficha_seleccionada.cambiarPosicion(xn, yn, self)
                            self.ficha_seleccionada.seleccionar(False)
                            self.ficha_seleccionada = None
                            estado.get_tablero().mostrar_tablero()
                            turno = self.fTexto5.render(f"Es turno de las fichas {estado.get_turno().get_turno_actual()}", True, NEGRO)
                        else:
                            self.ficha_seleccionada.seleccionar(False)
                            self.ficha_seleccionada = None
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        print('Enter presionado')
                        # Lanzar el dado y la moneda
                        dado, moneda = Dado(), Moneda()

                        dado.lanzar()
                        moneda.lanzar()

                        controlador_juego = Controlador2()
                        controlador_juego.notificar_valor_dado_moneda(dado, moneda)

                        #Registrar el turno y lanzamiento del dado y la moneda
                        estado.set_dado(dado)
                        estado.set_moneda(moneda)
                        valor_dado = self.fTexto1.render(f"Valor obtenido: {estado.get_dado().get_valor_actual()}", True, NEGRO)
                        valor_moneda = self.fTexto1.render(f"Valor obtenido: {estado.get_moneda().get_valor_actual()}", True, NEGRO)
                        


                #self.manager.process_events(event)

                '''controlador = C_Tablero2(self)
                controlador.mover_ficha(event, estado)'''

            

            pygame.display.update()

            '''while self.ganador not in ['R', 'A']:
                print('hola2')
                if self.ganador not in ['R', 'A']:
                    # Indicar de quien es el turno
                    estado.get_turno().notificar()
                    print('hola3')

                    # Lanzar el dado y la moneda
                    dado, moneda = Dado(), Moneda()

                    dado.lanzar()
                    moneda.lanzar()

                    controlador_juego = Controlador2()

                    controlador_juego.notificar_valor_dado_moneda(dado, moneda)
                    print('hola4')
                    
                    #Registrar el turno y lanzamiento del dado y la moneda
                    #estado.set_turno(turno_actual)
                    estado.set_dado(dado)
                    estado.set_moneda(moneda)


                    # Mover fichas según reglas de juego
                    print('Seleccione una ficha de su color para moverla')
                    controlador_tablero = C_Tablero2(self)
                    #estado = self.actualizar_pantalla(controlador_tablero, estado)
                    print('jam')
                    controlador_tablero.mover_ficha(event, estado)
                    print('caro')
                
                ganador = controlador_juego.verificar_estado_meta()
            
            # Mostrar mensaje de victoria o continuar jugando
            #controlador_juego.mostrar_mensaje_victoria(ganador)

            return self.ganador'''
        pygame.quit()

    def actualizar_pantalla(self, controlador, estado):
        clock = pygame.time.Clock()
        corriendo = True

        while corriendo:
            time_delta = clock.tick(60)/1000.0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    corriendo = False

                #self.manager.process_events(event)

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