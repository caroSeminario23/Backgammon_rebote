import random

# Definir las posibles acciones que puede tomar la IA
acciones_posibles = ["arriba", "abajo", "izquierda", "derecha"]

# Función para que la IA realice su turno
def turno_ia():
    # Elegir aleatoriamente una acción de las posibles
    accion_elegida = random.choice(acciones_posibles)
    return accion_elegida

# Ejemplo de uso
print("Turno de la IA:")
accion_ia = turno_ia()
print("La IA elige:", accion_ia)
