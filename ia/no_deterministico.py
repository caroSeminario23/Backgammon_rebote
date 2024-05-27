import random
from controller.reglas import mover_ADRO, mover_ADAO, mover_ADRF, mover_ADAF

# Identificar fichas en el tablero del color asignado
def identificar_fichas(fichas_tablero, color):
    fichas = []
    for ficha in fichas_tablero:
        if ficha.get_color() == color:
            fichas.append(ficha)
    return fichas

# Identificar las fichas que puede desplazar
def identificar_fichas_validas(fichas_disponibles, posiciones_fichas, estado):
    estadoNuevo = estado
    estadoPrueba = estado
    fichas_validas = []
    for ficha1 in fichas_disponibles:
        print('Ficha 1: ',ficha1.get_regla())
        print(estado.get_turno().get_turno_actual())
        if ficha1.get_regla() == "DAO":
            x, y, estadoPrueba = mover_ADAO(ficha1, estadoNuevo, posiciones_fichas)
            estadoNuevo = estado
            if x != -1 and y != -1:
                fichas_validas.append(ficha1)
                print('agregada')
        elif ficha1.get_regla() == "DAF":
            x, y, estadoPrueba = mover_ADAF(ficha1, estadoNuevo, posiciones_fichas)
            estadoNuevo = estado
            if x != -1 and y != -1:
                fichas_validas.append(ficha1)
                print('agregada')
    return fichas_validas


# Escoger una ficha de manera aleatoria
def escoger_ficha(fichas_disponibles):
    ficha = random.choice(fichas_disponibles)
    return ficha

# Determinar los posibles movimientos de una ficha
'''def movimientos_posibles(estado, posiciones_fichas, fichas_disponibles):
    movimientos = []
    ficha_apta = []

    for ficha in fichas_disponibles:
        if ficha.get_regla() == "DRO":
            ficha_apta.append(ficha)
            x, y, estado = mover_ADRO(ficha, estado, posiciones_fichas)

        elif ficha.get_regla() == "DAO":
            ficha_apta.append(ficha)
            x, y, estado = mover_ADAO(ficha, estado, posiciones_fichas)
        
        if x != -1 and y != -1:
            movimientos.append((x, y))

    return movimientos'''

# Escoger un movimiento de manera aleatoria
'''def escoger_movimiento(movimientos):
    eleccion = random.choice(movimientos)
    return eleccion'''

def mover_ficha(estado, color, posiciones, fichas_totales):
    fichas_disponibles = []
    fichas_validas = []

    print('estado')
    estado.mostrar_estado()
    print('estado1')
    estado1 = estado
    estado1.mostrar_estado()
    print('estado2')
    estado2 = estado
    estado2.mostrar_estado()
    dadoV = estado.get_dado().get_valor_actual()

    print('problema')
    #estado1.mostrar_estado()
    # Identifica las fichas de su color
    fichas_disponibles = identificar_fichas(fichas_totales, color)
    print(fichas_disponibles)
    print(fichas_disponibles[0].get_regla())

    fichas_validas = identificar_fichas_validas(fichas_disponibles, posiciones, estado)
    print('mostrar estados')
    estado1.mostrar_estado()
    estado.mostrar_estado()
    estado.get_turno().cambio_de_turno()
    estado.get_moneda().set_valor_actual('a')
    estado.get_dado().set_valor_actual(dadoV)
    print('Fichas validas: ',fichas_validas)
    if len(fichas_validas) >= 1:
        ficha = escoger_ficha(fichas_validas)
        print('Ficha escogida: ',ficha)
        if ficha.get_regla() == "DAO":
            x, y, estado = mover_ADAO(ficha, estado1, posiciones)

        elif ficha.get_regla() == "DAF":
            x, y, estado = mover_ADAF(ficha, estado1, posiciones)
    else:
        print("No se escogió ninguna ficha válida")
        x, y, estado, ficha = -1, -1, estado, None

    return x, y, estado, ficha

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
