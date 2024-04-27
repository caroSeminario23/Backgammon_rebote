class Ficha: # Representa a una dama
    def __init__(self, color, estado): # Inicializa una ficha con un color y un estado
        self.color = color # rojo (dr) o amarillo (da)
        self.estado = estado  # 'ordinaria (o)', 'finalista' (f), 'capturada (c)', 'libre (l)'

    def convertir_en_finalista(self): # Convierte una ficha en finalista
        self.estado = 'finalista'
    
    def convertir_en_ordinaria(self): # Convierte una ficha en ordinaria
        self.estado = 'ordinaria'

    def convertir_en_capturada(self): # Convierte una ficha en capturada
        self.estado = 'capturada'
    
    def convertir_en_libre(self): # Convierte una ficha en libre
        self.estado = 'libre'