class Estado:
    def __init__(self, tablero, turno, fichas, moneda):
        self.tablero = tablero  # T: matriz que representa el tablero
        self.turno = turno  # t: turno
        self.fichas = fichas  # ndr, nda, ndrf, ndaf, ndrc, ndac, ndrl, ndal: número de cada tipo de ficha
        self.moneda = moneda  # m: valor de la moneda

    def actualizar_estado(self, nuevo_tablero, nuevo_turno, nuevas_fichas, nueva_moneda):
        self.tablero = nuevo_tablero
        self.turno = nuevo_turno
        self.fichas = nuevas_fichas
        self.moneda = nueva_moneda
