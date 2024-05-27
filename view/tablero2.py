import pygame

from utils.colores import MELON_OSCURO, ROJO, AMARILLO, NEGRO, BEIGE, MELON_CLARO, MELON_TRASLUCIDO
from utils.figuras import dibujar_rectangulo_redondeado
from view.ficha import Ficha
from controller.controlador2 import Controlador2
#from controller.controlador_tablero2 import C_Tablero2
from controller.reglas import mover_ADRO, mover_ADAO, mover_ADRF, mover_ADAF, mover_CDRO, mover_CDAO, mover_SDRF, mover_SDAF, mover_LDRC, mover_LDAC
from ia.no_deterministico import mover_ficha
from model.dado import Dado
from model.moneda import Moneda
#from model.estado import Estado

class Tablero2:
    def __init__(self, alto, ancho):
        # INICIALIZAR PYGAME
        pygame.init()

        # DIMENSIONES
        self.alto = alto
        self.ancho = ancho

        # IMPORTACION DE FUENTES
        self.cargar_fuente()

        # POSICIONES DE LAS FICHAS
        self.posiciones_fichas = self.generar_posiciones_fichas()

        # ELEMENTOS
        self.fichas = []
        self.ganador = None
        self.ficha_seleccionada = None

        # CREAR LA VENTANA 
        self.ventana = pygame.display.set_mode((self.ancho, self.alto))
        pygame.display.set_caption("Backgammon rebote")

    def cargar_fuente(self):
        self.fTitulo = pygame.font.Font('fuentes/Inter-ExtraBold.ttf', self.alto//15)
        self.fTexto1 = pygame.font.Font('fuentes/Inter-MediumItalic.otf', self.alto//50)
        self.fTexto2 = pygame.font.Font('fuentes/Inter-MediumItalic.otf', self.alto//60)
        self.fTexto3 = pygame.font.Font('fuentes/Inter-ExtraBold.ttf', self.alto//50)
        self.fTexto4 = pygame.font.Font('fuentes/Inter-Bold.ttf', self.alto//50)
        self.fTexto5 = pygame.font.Font('fuentes/Inter-Bold.ttf', self.alto//30)
    
    def generar_posiciones_fichas(self):
        return [
            [
                (self.ancho//3.02, self.alto//3), (self.ancho//2.7, self.alto//3), (self.ancho//2.44, self.alto//3), (self.ancho//2.22, self.alto//3), (self.ancho//2.04, self.alto//3), (self.ancho//1.89, self.alto//3),
                (self.ancho//1.755, self.alto//3), (self.ancho//1.64, self.alto//3), (self.ancho//1.54, self.alto//3), (self.ancho//1.45, self.alto//3), (self.ancho//1.375, self.alto//3), (self.ancho//1.305, self.alto//3),
                (1262, 458), (1262, 344)
            ],
            [
                (self.ancho//3.02, self.alto//1.28), (self.ancho//2.7, self.alto//1.28), (self.ancho//2.44, self.alto//1.28), (self.ancho//2.22, self.alto//1.28), (self.ancho//2.04, self.alto//1.28), (self.ancho//1.89, self.alto//1.28),
                (self.ancho//1.755, self.alto//1.28), (self.ancho//1.64, self.alto//1.28), (self.ancho//1.54, self.alto//1.28), (self.ancho//1.45, self.alto//1.28), (self.ancho//1.375, self.alto//1.28), (self.ancho//1.305, self.alto//1.28),
                (1262, 756), (1262, 627)
            ]
        ]
        
    def cargar_imagen(self, ruta, escala):
        imagen = pygame.image.load(ruta)
        return pygame.transform.scale(imagen, escala)
    
    def cargar_imagenes(self):
        self.imagen_dado = self.cargar_imagen("imagenes/dado.png", (self.alto//13, self.alto//13))
        self.imagen_moneda = self.cargar_imagen("imagenes/moneda.png", (self.alto//13, self.alto//13))
        self.imagen_jugador1 = self.cargar_imagen("imagenes/jugador.png", (self.alto//13, self.alto//13))
        self.imagen_jugador2 = self.cargar_imagen("imagenes/jugador.png", (self.alto//13, self.alto//13))

    def identificar_fichas(self, estado):
        estado.get_tablero().obtener_casillas()
        tablero_01 = []
        tablero_p1, tablero_p2 = [], []
        
        for i in range(14):
            if estado.get_tablero().estado_casilla(0, i) == 'v':
                tablero_p1.append(0)
            # Si es rojo y dro
            elif estado.get_tablero().estado_casilla(0, i) == 'dro': #in ['dro', 'drf']
                tablero_p1.append(1)
            # Si es rojo y drf
            elif estado.get_tablero().estado_casilla(0, i) == 'drf':
                tablero_p1.append(3)
            # Si es amarillo y dao
            elif estado.get_tablero().estado_casilla(0, i) == 'dao': #in ['dao', 'daf']
                tablero_p1.append(2)
            # Si es amarillo y daf
            elif estado.get_tablero().estado_casilla(0, i) == 'daf':
                tablero_p1.append(4)
            # Si es roja y drc
            elif estado.get_tablero().estado_casilla(0, i) == 'drc':
                tablero_p1.append(5)
            # Si es amarilla y dac
            elif estado.get_tablero().estado_casilla(0, i) == 'dac':
                tablero_p1.append(6)
            # Si es roja y drl
            elif estado.get_tablero().estado_casilla(0, i) == 'drl':
                tablero_p1.append(7)
            # Si es amarilla y dal
            elif estado.get_tablero().estado_casilla(0, i) == 'dal':
                tablero_p1.append(8)
            
        
        for i in range(14):
            if estado.get_tablero().estado_casilla(1, i) == 'v':
                tablero_p2.append(0)
            # Si es rojo y dro
            elif estado.get_tablero().estado_casilla(1, i) == 'dro': #in ['dro', 'drf']
                tablero_p2.append(1)
            # Si es rojo y drf
            elif estado.get_tablero().estado_casilla(1, i) == 'drf':
                tablero_p2.append(3)
            # Si es amarillo y dao
            elif estado.get_tablero().estado_casilla(1, i) == 'dao': #in ['dao', 'daf']
                tablero_p2.append(2)
            # Si es amarillo y daf
            elif estado.get_tablero().estado_casilla(1, i) == 'daf':
                tablero_p2.append(4)
            # Si es roja y drc
            elif estado.get_tablero().estado_casilla(0, i) == 'drc':
                tablero_p1.append(5)
            # Si es amarilla y dac
            elif estado.get_tablero().estado_casilla(0, i) == 'dac':
                tablero_p1.append(6)
            # Si es roja y drl
            elif estado.get_tablero().estado_casilla(0, i) == 'drl':
                tablero_p1.append(7)
            # Si es amarilla y dal
            elif estado.get_tablero().estado_casilla(0, i) == 'dal':
                tablero_p1.append(8)
        
        tablero_01 = [tablero_p1, tablero_p2]
        print("Tablero 01:", tablero_01)
        return tablero_01

    def dibujar_fichas(self, estado, tablero_01):
        for fila in range(2):
            estado.get_FA().mostrar_FA()
            estado.get_FR().mostrar_FR()

            #estado.get_tablero().estado_casilla(0, 0)
            m = 0
            for i in tablero_01[fila]:
                print(m)
                if i == 1:
                    self.fichas.append(Ficha(ROJO, self.posiciones_fichas[fila][m][0], self.posiciones_fichas[fila][m][1], estado.get_FR().estado_casilla_FR(fila, m), 'DRO')) 
                    #print(estado.get_FR().estado_casilla_FR(fila, m))
                elif i == 2:
                    self.fichas.append(Ficha(AMARILLO, self.posiciones_fichas[fila][m][0], self.posiciones_fichas[fila][m][1], estado.get_FA().estado_casilla_FA(fila, m), 'DAO'))
                    #print(estado.get_FA().estado_casilla_FA(fila, m))
                elif i == 3:
                    self.fichas.append(Ficha(ROJO, self.posiciones_fichas[fila][m][0], self.posiciones_fichas[fila][m][1], estado.get_FR().estado_casilla_FR(fila, m), 'DRF')) 
                    #print(estado.get_FR().estado_casilla_FR(fila, m))
                elif i == 4:
                    self.fichas.append(Ficha(AMARILLO, self.posiciones_fichas[fila][m][0], self.posiciones_fichas[fila][m][1], estado.get_FA().estado_casilla_FA(fila, m), 'DAF')) 
                    #print(estado.get_FA().estado_casilla_FA(fila, m))
                elif i == 5:
                    self.fichas.append(Ficha(ROJO, self.posiciones_fichas[fila][m][0], self.posiciones_fichas[fila][m][1], estado.get_FR().estado_casilla_FR(fila, m), 'DRC')) 
                    #print(estado.get_FR().estado_casilla_FR(fila, m))
                elif i == 6:
                    self.fichas.append(Ficha(AMARILLO, self.posiciones_fichas[fila][m][0], self.posiciones_fichas[fila][m][1], estado.get_FA().estado_casilla_FA(fila, m), 'DAC')) 
                    #print(estado.get_FA().estado_casilla_FA(fila, m))
                elif i == 7:
                    self.fichas.append(Ficha(ROJO, self.posiciones_fichas[fila][m][0], self.posiciones_fichas[fila][m][1], estado.get_FR().estado_casilla_FR(fila, m), 'DRL')) 
                    #print(estado.get_FR().estado_casilla_FR(fila, m))
                elif i == 8:
                    self.fichas.append(Ficha(AMARILLO, self.posiciones_fichas[fila][m][0], self.posiciones_fichas[fila][m][1], estado.get_FA().estado_casilla_FA(fila, m), 'DAL')) 
                    #print(estado.get_FA().estado_casilla_FA(fila, m))
                m += 1
    
    def eliminar_fichas_vacias(self):
        #self.fichas = [ficha for ficha in self.fichas if ficha.get_color() != 'v']
        fichasN = []
        self.fichas = fichasN


    def mostrar_pantalla(self, j1, j2, estado, modo_juego):
        # CARGAR IMÁGENES
        self.cargar_imagenes()

        # RELOJ DE PYGAME
        reloj = pygame.time.Clock()

        # AGREGAR TEXTO
        titulo = self.fTitulo.render("BACKGAMMON REBOTE", True, MELON_OSCURO)
        valor_dado = self.fTexto1.render(f"Valor obtenido: {estado.get_dado()}", True, NEGRO) 
        valor_moneda = self.fTexto1.render(f"Valor obtenido: {estado.get_moneda()}", True, NEGRO)
        jugador1 = self.fTexto1.render("JUGADOR 1", True, NEGRO)
        pseudonimo1 = self.fTexto2.render(f" - Pseudónimo: {j1.get_pseudonimo()}", True, NEGRO)
        color_fichas1 = self.fTexto2.render(f" - Color de fichas: {j1.get_colorFicha()}", True, NEGRO)
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
        turno = self.fTexto5.render(f"Es turno de las fichas {estado.get_turno().get_turno_actual()}", True, NEGRO)

        # AGREGAR FIGURAS
        superficie_transparente = pygame.Surface((self.ancho//2.1, self.alto//1.68))
        superficie_transparente.set_alpha(255 * 0.6) 
        superficie_transparente.fill(MELON_TRASLUCIDO)

        # DIBUJADO DE LAS FICHAS
        tablero_01 = self.identificar_fichas(estado)
        print(str(tablero_01))
        self.dibujar_fichas(estado, tablero_01)

        # ADICIONAR OBJETOS A LA PANTALA
        corriendo = True
        while corriendo:
            reloj.tick(60)

            # PINTAR LA PANTALLA
            self.ventana.fill(BEIGE)
            
            # DIBUJAR FIGURAS
            dibujar_rectangulo_redondeado(self.ventana, MELON_OSCURO, (self.ancho//33, self.alto//6.8, self.ancho//4, self.alto//1.33), 10)
            dibujar_rectangulo_redondeado(self.ventana, MELON_OSCURO, (self.ancho//3.35, self.alto//6.8, self.ancho//1.48, self.alto//11.7), 10)
            dibujar_rectangulo_redondeado(self.ventana, MELON_OSCURO, (self.ancho//3.35, self.alto//4, self.ancho//1.48, self.alto//1.54), 10)
            dibujar_rectangulo_redondeado(self.ventana, MELON_CLARO, (self.ancho//22, self.alto//5.5, self.ancho//4.6, self.alto//4.8), 10)
            dibujar_rectangulo_redondeado(self.ventana, MELON_CLARO, (self.ancho//22, self.alto//2.4, self.ancho//4.6, self.alto//4.8), 10)
            dibujar_rectangulo_redondeado(self.ventana, MELON_CLARO, (self.ancho//22, self.alto//1.53, self.ancho//4.6, self.alto//4.8), 10)
            self.ventana.blit(superficie_transparente, (self.ancho//3.22, self.alto//3.6))
            # tableros de fichas liberadas
            dibujar_rectangulo_redondeado(self.ventana, MELON_CLARO, (self.ancho//1.25, self.alto//3.2, self.ancho//6.4, self.alto//7), 10)
            dibujar_rectangulo_redondeado(self.ventana, MELON_CLARO, (self.ancho//1.25, self.alto//2.05, self.ancho//6.4, self.alto//18), 10)
            dibujar_rectangulo_redondeado(self.ventana, MELON_CLARO, (self.ancho//1.25, self.alto//1.595, self.ancho//6.4, self.alto//7), 10)
            dibujar_rectangulo_redondeado(self.ventana, MELON_CLARO, (self.ancho//1.25, self.alto//1.24, self.ancho//6.4, self.alto//18), 10)
            # cronometros
            dibujar_rectangulo_redondeado(self.ventana, MELON_CLARO, (self.ancho//7, self.alto//1.49, self.ancho//9, self.alto//13), 10)
            dibujar_rectangulo_redondeado(self.ventana, MELON_CLARO, (self.ancho//7, self.alto//1.31, self.ancho//9, self.alto//13), 10)
            dibujar_rectangulo_redondeado(self.ventana, MELON_OSCURO, (self.ancho//6.8, self.alto//1.475, self.ancho//10, self.alto//14), 10)
            dibujar_rectangulo_redondeado(self.ventana, MELON_OSCURO, (self.ancho//6.8, self.alto//1.3, self.ancho//10, self.alto//14), 10)
            # tablero
            pygame.draw.rect(self.ventana, AMARILLO, (self.ancho//3.22, self.alto//3.6, self.ancho//25.2, self.alto//3.6))
            pygame.draw.rect(self.ventana, ROJO, (self.ancho//2.85, self.alto//3.6, self.ancho//25.2, self.alto//3.6))
            pygame.draw.rect(self.ventana, AMARILLO, (self.ancho//2.56, self.alto//3.6, self.ancho//25.2, self.alto//3.6))
            pygame.draw.rect(self.ventana, ROJO, (self.ancho//2.32, self.alto//3.6, self.ancho//25.2, self.alto//3.6))
            pygame.draw.rect(self.ventana, AMARILLO, (self.ancho//2.125, self.alto//3.6, self.ancho//25.2, self.alto//3.6))
            pygame.draw.rect(self.ventana, ROJO, (self.ancho//1.96, self.alto//3.6, self.ancho//25.2, self.alto//3.6))
            pygame.draw.rect(self.ventana, AMARILLO, (self.ancho//1.82, self.alto//3.6, self.ancho//25.2, self.alto//3.6))
            pygame.draw.rect(self.ventana, ROJO, (self.ancho//1.695, self.alto//3.6, self.ancho//25.2, self.alto//3.6))
            pygame.draw.rect(self.ventana, AMARILLO, (self.ancho//1.587, self.alto//3.6, self.ancho//25.2, self.alto//3.6))
            pygame.draw.rect(self.ventana, ROJO, (self.ancho//1.493, self.alto//3.6, self.ancho//25.2, self.alto//3.6))
            pygame.draw.rect(self.ventana, AMARILLO, (self.ancho//1.41, self.alto//3.6, self.ancho//25.2, self.alto//3.6))
            pygame.draw.rect(self.ventana, ROJO, (self.ancho//1.339, self.alto//3.6, self.ancho//25.2, self.alto//3.6))
            pygame.draw.rect(self.ventana, ROJO, (self.ancho//3.22, self.alto//1.678, self.ancho//25.2, self.alto//3.6))
            pygame.draw.rect(self.ventana, AMARILLO, (self.ancho//2.85, self.alto//1.678, self.ancho//25.2, self.alto//3.6))
            pygame.draw.rect(self.ventana, ROJO, (self.ancho//2.56, self.alto//1.678, self.ancho//25.2, self.alto//3.6))
            pygame.draw.rect(self.ventana, AMARILLO, (self.ancho//2.32, self.alto//1.678, self.ancho//25.2, self.alto//3.6))
            pygame.draw.rect(self.ventana, ROJO, (self.ancho//2.125, self.alto//1.678, self.ancho//25.2, self.alto//3.6))
            pygame.draw.rect(self.ventana, AMARILLO, (self.ancho//1.96, self.alto//1.678, self.ancho//25.2, self.alto//3.6))
            pygame.draw.rect(self.ventana, ROJO, (self.ancho//1.82, self.alto//1.678, self.ancho//25.2, self.alto//3.6))
            pygame.draw.rect(self.ventana, AMARILLO, (self.ancho//1.695, self.alto//1.678, self.ancho//25.2, self.alto//3.6))
            pygame.draw.rect(self.ventana, ROJO, (self.ancho//1.587, self.alto//1.678, self.ancho//25.2, self.alto//3.6))
            pygame.draw.rect(self.ventana, AMARILLO, (self.ancho//1.493, self.alto//1.678, self.ancho//25.2, self.alto//3.6))
            pygame.draw.rect(self.ventana, ROJO, (self.ancho//1.41, self.alto//1.678, self.ancho//25.2, self.alto//3.6))
            pygame.draw.rect(self.ventana, AMARILLO, (self.ancho//1.339, self.alto//1.678, self.ancho//25.2, self.alto//3.6))

            # ESCRIBIR TEXTO DEL TITULO
            self.ventana.blit(titulo, (self.ancho//3.8, self.alto//21))

            # DIBUJAR IMAGENES
            self.ventana.blit(self.imagen_dado, (self.ancho//17, self.alto//5))
            self.ventana.blit(self.imagen_moneda, (self.ancho//17, self.alto//3.5))
            self.ventana.blit(self.imagen_jugador1, (self.ancho//17, self.alto//2.3))
            self.ventana.blit(self.imagen_jugador2, (self.ancho//17, self.alto//1.9))    

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

            # DIBUJAR FICHAS
            for ficha in self.fichas:
                ficha.dibujar(self.ventana)

            # EVENTOS
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    corriendo = False
                
                # modo humano-humano
                if modo_juego == 'HH':
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        pos = pygame.mouse.get_pos()
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
                            if self.ficha_seleccionada.get_regla() == "DRO":
                                x, y, estado = mover_ADRO(self.ficha_seleccionada, estado, self.posiciones_fichas)
                                #x, y, estado = mover_RDRO(self.ficha_seleccionada, estado, self.posiciones_fichas)
                            elif self.ficha_seleccionada.get_regla() == "DAO":
                                x, y, estado = mover_ADAO(self.ficha_seleccionada, estado, self.posiciones_fichas)
                                #x, y, estado = mover_RDAO(self.ficha_seleccionada, estado, self.posiciones_fichas)
                            elif self.ficha_seleccionada.get_regla() == "DRF":
                                x, y, estado = mover_ADRF(self.ficha_seleccionada, estado, self.posiciones_fichas)
                            elif self.ficha_seleccionada.get_regla() == "DAF":
                                x, y, estado = mover_ADAF(self.ficha_seleccionada, estado, self.posiciones_fichas)
                            elif self.ficha_seleccionada.get_regla() == "DRC":
                                x, y, estado = mover_LDRC(self.ficha_seleccionada, estado, self.posiciones_fichas)
                            elif self.ficha_seleccionada.get_regla() == "DAC":
                                x, y, estado = mover_LDAC(self.ficha_seleccionada, estado, self.posiciones_fichas)
                                

                            if x != -1 and y != -1:
                                pos = (x, y)
                                print(pos)
                                xn = self.posiciones_fichas[pos[0]][pos[1]][0]
                                yn = self.posiciones_fichas[pos[0]][pos[1]][1]
                                self.ficha_seleccionada.cambiarPosicion(xn, yn, self)
                                self.ficha_seleccionada.seleccionar(False)
                                self.ficha_seleccionada = None
                                estado.get_tablero().mostrar_tablero()
                                turno = self.fTexto5.render(f"Es turno de las fichas {estado.get_turno().get_turno_actual()}", True, NEGRO)

                                self.eliminar_fichas_vacias()
                                tablero_01 = self.identificar_fichas(estado)
                                print(str(tablero_01))
                                self.dibujar_fichas(estado, tablero_01)

                            else:
                                self.ficha_seleccionada.seleccionar(False)
                                self.ficha_seleccionada = None
                
                # modo humano-maquina - facil
                elif modo_juego == 'fácil':
                    turno_humano = estado.get_turno().get_turno_actual()
                    if turno_humano == 'R':
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
                                if self.ficha_seleccionada.get_regla() == "DRO":
                                    x, y, estado = mover_ADRO(self.ficha_seleccionada, estado, self.posiciones_fichas)
                                    #x, y, estado = mover_RDRO(self.ficha_seleccionada, estado, self.posiciones_fichas)
                                elif self.ficha_seleccionada.get_regla() == "DRF":
                                    x, y, estado = mover_ADRF(self.ficha_seleccionada, estado, self.posiciones_fichas)
                                elif self.ficha_seleccionada.get_regla() == "DRC":
                                    x, y, estado = mover_LDRC(self.ficha_seleccionada, estado, self.posiciones_fichas)
                            

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
                                    print(estado.get_dado().get_valor_actual())
                                    print(estado.get_moneda().get_valor_actual())
                                    
                                    turno = self.fTexto5.render(f"Es turno de las fichas {estado.get_turno().get_turno_actual()}", True, NEGRO)

                                    if (estado.get_turno().get_turno_actual() == 'A'):
                                        print('\n\n\nYA ENTRE')
                                        # Lanzar el dado y la moneda
                                        dado, moneda = Dado(), Moneda()

                                        dado.lanzar()
                                        moneda.set_valor_actual('a')

                                        controlador_juego = Controlador2()
                                        controlador_juego.notificar_valor_dado_moneda(dado, moneda)

                                        #Registrar el turno y lanzamiento del dado y la moneda
                                        #estado.set_dado(dado)
                                        val_dado = dado.get_valor_actual()
                                        print('valor actual del dado: ', val_dado)
                                        estado.get_dado().set_valor_actual(val_dado)
                                        print('valor registrado del dado: ', estado.get_dado().get_valor_actual())
                                        #estado.set_moneda(moneda)
                                        val_moneda = moneda.get_valor_actual()
                                        print('valor actual de la moneda: ', val_moneda)
                                        estado.get_moneda().set_valor_actual(val_moneda)
                                        print('valor registrado de la moneda: ', estado.get_moneda().get_valor_actual())
                                        valor_dado = self.fTexto1.render(f"Valor obtenido: {estado.get_dado().get_valor_actual()}", True, NEGRO)
                                        valor_moneda = self.fTexto1.render(f"Valor obtenido: {estado.get_moneda().get_valor_actual()}", True, NEGRO)

                                        x, y, estado, ficha = mover_ficha(estado, AMARILLO, self.posiciones_fichas, self.fichas)
                                        if x != -1 and y != -1:
                                            pos = (x, y)
                                            print(pos)
                                            print(pos[0], pos[1])
                                            xn = self.posiciones_fichas[pos[0]][pos[1]][0]
                                            yn = self.posiciones_fichas[pos[0]][pos[1]][1]
                                            self.ficha_seleccionada = ficha
                                            self.ficha_seleccionada.cambiarPosicion(xn, yn, self)
                                            self.ficha_seleccionada.seleccionar(False)
                                            self.ficha_seleccionada = None
                                            estado.get_tablero().mostrar_tablero()
                                            turno = self.fTexto5.render(f"Es turno de las fichas {estado.get_turno().get_turno_actual()}", True, NEGRO)
                                        else:
                                            print('Sin movimientos disponibles')

                                else:
                                    self.ficha_seleccionada.seleccionar(False)
                                    self.ficha_seleccionada = None
                
                # lanzar la moneda y el dado
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        print('Enter presionado')
                        dado, moneda = Dado(), Moneda()
                        dado.lanzar()
                        moneda.lanzar()
                        controlador_juego = Controlador2()
                        controlador_juego.notificar_valor_dado_moneda(dado, moneda)
                        estado.set_dado(dado)
                        estado.set_moneda(moneda)
                        valor_dado = self.fTexto1.render(f"Valor obtenido: {estado.get_dado().get_valor_actual()}", True, NEGRO)
                        valor_moneda = self.fTexto1.render(f"Valor obtenido: {estado.get_moneda().get_valor_actual()}", True, NEGRO)
                    
            pygame.display.update()

        pygame.quit()
