import heapq

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
