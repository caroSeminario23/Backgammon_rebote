import random
from controller.reglas import mover_ADRO, mover_ADAO

# Identificar fichas en el tablero del color asignado
def identificar_fichas(fichas_tablero, color):
    fichas = []
    for ficha in fichas_tablero:
        if ficha.get_color() == color:
            fichas.append(ficha)
    return fichas

# Determinar los posibles movimientos de una ficha
def movimientos_posibles(estado, posiciones_fichas, fichas_disponibles):
    movimientos = []

    for ficha in fichas_disponibles:
        if ficha.get_regla() == "ADRO":
            x, y, estado = mover_ADRO(ficha, estado, posiciones_fichas)
        elif ficha.get_regla() == "ADAO":
            x, y, estado = mover_ADAO(ficha, estado, posiciones_fichas)
        
        if x != -1 and y != -1:
            movimientos.append((x, y))

    return movimientos

# Escoger un movimiento de manera aleatoria
def escoger_movimiento(movimientos):
    eleccion = random.choice(movimientos)
    return eleccion

def mover_ficha(estado, color, posiciones, fichas_totales):
    fichas_disponibles = []
    fichas_disponibles = identificar_fichas(fichas_totales, color)

    movimientos = []
    movimientos = movimientos_posibles(estado, posiciones, fichas_disponibles)

    if len(movimientos) == 0:
        return -1, -1, estado
    else:
        movimiento = escoger_movimiento(movimientos)
        return movimiento[0], movimiento[1], estado
    pass

'''# Definir las posibles acciones que puede tomar la IA
acciones_posibles = ["arriba", "abajo", "izquierda", "derecha"]

# Función para que la IA realice su turno
def turno_ia():
    # Elegir aleatoriamente una acción de las posibles
    accion_elegida = random.choice(acciones_posibles)
    return accion_elegida

# Ejemplo de uso
print("Turno de la IA:")
accion_ia = turno_ia()
print("La IA elige:", accion_ia)'''
