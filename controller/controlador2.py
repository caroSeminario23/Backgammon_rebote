from pync import Notifier

class Controlador2:

    # Verifica si el estado actual es un estado meta
    def verificar_estado_meta(self, estado_actual):
        ganador = None

        if estado_actual.get_n_fichas().get_ficha(7) == 15:
            ganador = 'A'
        elif estado_actual.get_n_fichas().get_ficha(6) == 15:
            ganador = 'R'

        return ganador
    
    def notificar_valor_dado_moneda(self, dado, moneda):
        Notifier.notify(f'Dado: {dado.get_valor_actual()}, Moneda: {moneda.get_valor_actual()}', title='Valores de dado y moneda', sound='default')

    def mostrar_mensaje_victoria(self, ganador):
        Notifier.notify(f'¡El ganador es el jugador {ganador}!', title='Victoria', sound='default')