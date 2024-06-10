from pync import Notifier

class Controlador2:

    # Verifica si el estado actual es un estado meta
    def verificar_estado_meta(self, estado, j1):
        ganador = None
        rojo, amarillo = None, None

        if j1.get_colorFicha() == 'R':
            rojo = 'J1'
            amarillo = 'J2'
        else:
            rojo = 'J2'
            amarillo = 'J1'

        if estado.get_n_fichas().get_ndrl() == 15:
            ganador = rojo
        elif estado.get_n_fichas().get_ndal == 15:
            ganador = amarillo
        else:
            ganador = 'NO'
        
        return ganador
    
    def notificar_valor_dado_moneda(self, dado, moneda):
        Notifier.notify(f'Dado: {dado.get_valor_actual()}, Moneda: {moneda.get_valor_actual()}', title='Valores de dado y moneda', sound='default')

    def mostrar_mensaje_victoria(self, ganador):
        Notifier.notify(f'¡El ganador es el jugador {ganador}!', title='Victoria', sound='default')