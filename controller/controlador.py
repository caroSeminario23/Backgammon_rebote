class Controlador:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista
        self.vista.setControlador(self)

    def mostrar_vista(self):
        self.vista.mostrar()

    def mostrar_resultado(self, resultado):
        self.vista.mostrar_resultado(resultado)

    def calcular(self, num1, num2):
        resultado = self.modelo.sumar(num1, num2)
        self.mostrar_resultado(resultado)