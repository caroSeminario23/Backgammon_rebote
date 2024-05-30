import heapq
from ia.no_deterministico import identificar_fichas, identificar_fichas_validas, escoger_ficha

funcion_evaluadora = [
    [20, 19, 18 , 17, 16, 15, 5, 4, 3, 2, 1, 0, 0, 5000],
    [30, 31, 32, 33, 34, 35, 60, 65, 70, 75, 80, 85, 0, 5000]
]
# para rojo
funcion_evaluadora_rojo = [
    [20, 19, 18 , 17, 16, 15, 5, 4, 3, 2, 1, 0, 0, 5000],
    [30, 31, 32, 33, 34, 35, 60, 65, 70, 75, 80, 85, 0, 5000]
]

# para amarillo
funcion_evaluadora_amarillo = [
    [-20, -19, -18 , -17, -16, -15, -5, -4, -3, -2, -1, 0, 0, -5000],
    [-30, -31, -32, -33, -34, -35, -60, -65, -70, -75, -80, -85, 0, -5000]
]

# OBJETIVO
objetivo = 5000
objetivo_rojo = 5000
objetivo_amarillo = -5000

# Funcion para escoger el mejor
def escoger_ficha(funcion_evaluadora, fichas_disponibles):
    pass




# MOVER LA FICHA
def mover_fichaPEM(estado, color, posiciones, fichas_totales):
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
        '''ficha = escoger_ficha(fichas_validas)
        print('Ficha escogida: ',ficha)
        if ficha.get_regla() == "DAO":
            x, y, estado = mover_ADAO(ficha, estado1, posiciones)

        elif ficha.get_regla() == "DAF":
            x, y, estado = mover_ADAF(ficha, estado1, posiciones)'''
    else:
        print("No se escogió ninguna ficha válida")
        x, y, estado, ficha = -1, -1, estado, None

    return x, y, estado, ficha






# Función heurística para calcular la distancia euclidiana desde un nodo hasta el objetivo
def heuristica(nodo, objetivo):
    x1, y1 = nodo
    x2, y2 = objetivo
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

# Función para realizar la búsqueda usando el algoritmo "primero el mejor"
def primero_el_mejor(inicio, objetivo, grafo):
    # Inicializar la cola de prioridad con el nodo inicial
    cola_prioridad = [(heuristica(inicio, objetivo), inicio)]
    heapq.heapify(cola_prioridad)
    
    while cola_prioridad:
        # Obtener el nodo más prometedor de la cola de prioridad
        _, nodo_actual = heapq.heappop(cola_prioridad)
        
        # Si alcanzamos el objetivo, retornar el camino
        if nodo_actual == objetivo:
            return "Se encontró el objetivo"
        
        # Expandir el nodo actual y agregar los nodos vecinos a la cola de prioridad
        for vecino in grafo[nodo_actual]:
            heapq.heappush(cola_prioridad, (heuristica(vecino, objetivo), vecino))
    
    # Si no se encontró el objetivo, retornar un mensaje de error
    return "No se encontró el objetivo"

# Ejemplo de uso
inicio = (0, 0)
objetivo = (4, 4)
grafo = {
    (0, 0): [(1, 0), (0, 1)],
    (1, 0): [(2, 0), (1, 1), (0, 0)],
    (2, 0): [(3, 0), (2, 1), (1, 0)],
    (3, 0): [(4, 0), (3, 1), (2, 0)],
    (4, 0): [(4, 1), (3, 0)],
    (0, 1): [(1, 1), (0, 2), (0, 0)],
    (1, 1): [(2, 1), (1, 2), (0, 1), (1, 0)],
    (2, 1): [(3, 1), (2, 2), (1, 1), (2, 0)],
    (3, 1): [(4, 1), (3, 2), (2, 1), (3, 0)],
    (4, 1): [(4, 2), (3, 1), (4, 0)],
    (0, 2): [(1, 2), (0, 3), (0, 1)],
    (1, 2): [(2, 2), (1, 3), (0, 2), (1, 1)],
    (2, 2): [(3, 2), (2, 3), (1, 2), (2, 1)],
    (3, 2): [(4, 2), (3, 3), (2, 2), (3, 1)],
    (4, 2): [(4, 3), (3, 2), (4, 1)],
    (0, 3): [(1, 3), (0, 4), (0, 2)],
    (1, 3): [(2, 3), (1, 4), (0, 3), (1, 2)],
    (2, 3): [(3, 3), (2, 4), (1, 3), (2, 2)],
    (3, 3): [(4, 3), (3, 4), (2, 3), (3, 2)],
    (4, 3): [(4, 4), (3, 3), (4, 2)],
    (0, 4): [(1, 4), (0, 3)],
    (1, 4): [(2, 4), (0, 4), (1, 3)],
    (2, 4): [(3, 4), (1, 4), (2, 3)],
    (3, 4): [(4, 4), (2, 4), (3, 3)],
    (4, 4): [(3, 4), (4, 3)]
}

print(primero_el_mejor(inicio, objetivo, grafo))
