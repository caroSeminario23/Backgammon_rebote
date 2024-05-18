import random
class Dado: 
    def __init__(self): # Inicializa un dado ordinario con valores del 1 al 6
        self.valores = list(range(1, 7)) # [1, 2, 3, 4, 5, 6]

    def lanzar(self): # Lanza el dado y devuelve un valor aleatorio
        return random.choice(self.valores) # Devuelve un valor aleatorio de la lista de valores
    
    '''
    # Función para crear la ventana emergente de lanzar dado
    def mostrar_ventana_dado():
        global dialog
        dialog = pygame_gui.windows.UIMessageWindow(rect=pygame.Rect((300, 100), (300, 200)),
                                                    html_message='Lance el dado',
                                                    manager=manager,
                                                    window_title='Lanzar Dado')

        lanzar_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((100, 100), (100, 50)),
                                                    text='Lanzar',
                                                    manager=manager,
                                                    container=dialog)
    '''