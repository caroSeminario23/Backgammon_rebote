from pync import Notifier

def encontrar_posicion_cercana(coord, posiciones_fichas):
    tolerancia = 10  # Puedes ajustar este valor según tus necesidades
    for i, fila in enumerate(posiciones_fichas):
        for j, pos in enumerate(fila):
            if abs(pos[0] - coord[0]) <= tolerancia and abs(pos[1] - coord[1]) <= tolerancia:
                return [i, j]
    return None

# ==================
#   REGLA 1: ADRO
# ==================
# Verificador de la posicion a la que se movera la ficha
def verificador_ADRO(ficha, estado, posiciones):
    aO = ficha.obtenerPosicion()[0]
    bO = ficha.obtenerPosicion()[1]
    a, b = 0, 0

    # Transformar la coordenada de pantalla en valor del arreglo tablero
    coord = (aO, bO)  
    pos = encontrar_posicion_cercana(coord, posiciones)
    if pos is not None:
        print(f'La coordenada {coord} está cerca de la posición {pos} en self.posiciones_fichas')
        a = pos[0]
        b = pos[1]
    else:
        print(f'La coordenada {coord} no está cerca de ninguna posición en self.posiciones_fichas')


    n = (estado.get_dado().get_valor_actual())-1
    print(n, a, b)
    c, d = -1, -1
    valido = False

    print(f"Turno: {estado.get_turno().get_turno_actual()}, Moneda: {estado.get_moneda().get_valor_actual()}")
    if estado.get_turno().get_turno_actual() == 'R' and estado.get_moneda().get_valor_actual() == 'a':
        print(f"Estado de la casilla en ({a}, {b}): {estado.get_tablero().estado_casilla(a, b)}")
        if (estado.get_tablero().estado_casilla(a,b) == 'dro'):
            # CALCULAR C
            if b==1 and n==0 and a==0: # X
                c = a
            elif b==2 and n>=0 and n<=1 and a==0: # X
                c = a
            elif b==2 and n>=2 and n<=5 and a==0: # X
                c = a+1
            elif b==3 and n>=0 and n<=2 and a==0: # X
                c = a
            elif b==3 and n>=3 and n<=5 and a==0: # X
                c = a+1
            elif b==4 and n>=0 and n<=3 and a==0: # X
                c = a
            elif b==4 and n>=4 and n<=5 and a==0: # X
                c = a+1
            elif b==5 and n>=0 and n<=4 and a==0: # X
                c = a
            elif b==5 and n==5 and a==0: # X
                c = a+1
            elif b==0 and n>=0 and n<=5 and a==0: # X
                c = a+1
            elif b>=6 and b<=11 and n>=0 and n<=5 and a==0: # X
                c = a
            elif b==1 and n>=1 and n<=5 and a==0: # X
                c = a+1
            elif b>=0 and b<=6 and n>=0 and n<=5 and a==1: # X
                c = a
            elif b==7 and n>=0 and n<=4 and a==1: # X
                c = a
            elif b==8 and n>=0 and n<=3 and a==1:  # X
                c = a
            elif b==9 and n>=0 and n<=2 and a==1: # X
                c = a
            elif b==10 and n>=0 and n<=1 and a==1: # X
                c = a
            elif b==11 and n==0 and a==1: # X
                c = a
            
            else:
                print('No se cumplen las condiciones para calcular c')
                c = -1
            
            # CALCULAR D
            if b>=6 and b<=11 and n>=0 and n<=5 and a==0:
                d = b-n-1
            elif b==5 and n>=0 and n<=4 and a==0:
                d = b-n-1
            elif b==4 and n>=0 and n<=3 and a==0:
                d = b-n-1
            elif b==3 and n>=0 and n<=2 and a==0:
                d = b-n-1
            elif b==2 and n>=0 and n<=1 and a==0:
                d = b-n-1
            elif b==1 and n==0 and a==0:
                d = b-1
            elif b==0 and n==0 and a==0:
                d = b
            elif b==0 and n>=0 and n<=5 and a==0:
                d = b+n-1+1
            elif b>=0 and b<=5 and n>=0 and n<=5 and a==1:
                d = b+n+1
            elif b==6 and n>=0 and n<=4 and a==1:
                d = b+n+1
            elif b==7 and n>=0 and n<=3 and a==1:
                d = b+n+1
            elif b==8 and n>=0 and n<=2 and a==1:
                d = b+n+1
            elif b==9 and n>=0 and n<=1 and a==1:
                d = b+n+1
            elif b==10 and n==0 and a==1:
                d = b+1
            elif b==1 and n==0 and a==0:
                d = b-n-1
            elif b==1 and n>=1 and n<=5 and a==0:
                d = b+(n-3)+1
            elif b==2 and n>=2 and n<=5 and a==0:
                d = b+(n-5)+1
            elif b==3 and n>=3 and n<=5 and a==0:
                d = b+(n-7)+1
            elif b==4 and n>=4 and n<=5 and a==0:
                d = b+(n-9)+1
            elif b==5 and n==5 and a==0:
                d = b+(n-11)+1

            else:
                print('No se cumplen las condiciones para calcular d')
                d = -1
    
    print(c, d)
    if c >= 0 and c <= 1 and d >= 0 and d <= 11:
        if estado.get_tablero().estado_casilla(c,d) == 'v' or estado.get_tablero().estado_casilla(c,d) == 'dro':
            valido = True
        else:
            valido = False
    else:
        valido = False

    return c, d, valido

# Movimiento de la ficha
def mover_ADRO(ficha, estado, posiciones):
    c, d, valido = verificador_ADRO(ficha, estado, posiciones)
    estadoN = estado
    if valido:
        posX, posY = c, d
        a = ficha.obtenerPosicion()[0]
        b = ficha.obtenerPosicion()[1]

        # Transformar la coordenada de pantalla en valor del arreglo tablero
        coord = (a, b)  
        pos = encontrar_posicion_cercana(coord, posiciones)
        if pos is not None:
            print(f'La coordenada {coord} está cerca de la posición {pos} en self.posiciones_fichas')
            a = pos[0]
            b = pos[1]
        else:
            print(f'La coordenada {coord} no está cerca de ninguna posición en self.posiciones_fichas')

        estadoN = actualizar_estado_ADRO(estado, a, b, posX, posY)
        print(posX, posY, estadoN.get_tablero().estado_casilla(posX, posY))
        estadoN.get_tablero().mostrar_tablero()
        return posX, posY, estadoN
    else:
        print('Movimiento no válido')
        Notifier.notify('Movimiento no válido', title='Error', sound='default')
        return -1, -1, estadoN

# Actualizar estado del juego
def actualizar_estado_ADRO(estado, xi, yi, xf, yf):
    estado.get_turno().cambio_de_turno()
    estado.get_moneda().esperar_lanzamiento()

    # Actualizar tablero
    # Casilla de origen
    estado.get_FR().eliminar_ficha_FR(xi, yi)
    if estado.get_FR().estado_casilla_FR(xi,yi) == 0:
        estado.get_tablero().convertir_en_vacia(xi, yi)
    else:
        estado.get_tablero().convertir_en_ordinaria(xi, yi)
    
    # Casilla de destino
    estado.get_FR().adicionar_ficha_FR(xf, yf)
    if xf==0 and yf>=0 and yf<=11:
        estado.get_tablero().convertir_en_ordinaria(xf, yf)
    elif xf==1 and yf>=0 and yf<=5:
        estado.get_tablero().convertir_en_ordinaria(xf, yf)
    elif xf==1 and yf>=6 and yf<=11:
        estado.get_tablero().convertir_en_finalista(xf, yf)

    return estado

# ==================
#   REGLA 1: ADAO
# ==================
# Verificador de la posicion a la que se movera la ficha
def verificador_ADAO(ficha, estado, posiciones):
    aO = ficha.obtenerPosicion()[0]
    bO = ficha.obtenerPosicion()[1]
    a, b = 0, 0

    # Transformar la coordenada de pantalla en valor del arreglo tablero
    coord = (aO, bO)  
    pos = encontrar_posicion_cercana(coord, posiciones)
    if pos is not None:
        print(f'La coordenada {coord} está cerca de la posición {pos} en self.posiciones_fichas')
        a = pos[0]
        b = pos[1]
    else:
        print(f'La coordenada {coord} no está cerca de ninguna posición en self.posiciones_fichas')

    n = (estado.get_dado().get_valor_actual())-1
    print(n, a, b)
    c, d = -1, -1
    valido = False

    print(f"Turno: {estado.get_turno().get_turno_actual()}, Moneda: {estado.get_moneda().get_valor_actual()}")
    if estado.get_turno().get_turno_actual() == 'A' and estado.get_moneda().get_valor_actual() == 'a':
        print(f"Estado de la casilla en ({a}, {b}): {estado.get_tablero().estado_casilla(a, b)}")
        if (estado.get_tablero().estado_casilla(a,b) == 'dao'):
            # CALCULAR C
            if a==0 and b>=0 and b<=5 and n>=0 and n<=5:
                c = a
            elif a==0 and b==6 and n>=0 and n<=4:
                c = a
            elif a==0 and b==7 and n>=0 and n<=3:
                c = a
            elif a==0 and b==8 and n>=0 and n<=2:
                c = a
            elif a==0 and b==9 and n>=0 and n<=1:
                c = a
            elif a==0 and b==10 and n==0:
                c = a
            elif a==1 and b>=6 and b<=11 and n>=0 and n<=5:
                c = a
            elif a==1 and b==5 and n>=0 and n<=4:
                c = a
            elif a==1 and b==4 and n>=0 and n<=3:
                c = a
            elif a==1 and b==3 and n>=0 and n<=2:
                c = a
            elif a==1 and b==2 and n>=0 and n<=1:
                c = a
            elif a==1 and b==1 and n==0:
                c = a
            elif a==1 and b==5 and n==5:
                c = a-1
            elif a==1 and b==4 and n>=4 and n<=5:
                c = a-1
            elif a==1 and b==3 and n>=3 and n<=5:
                c = a-1
            elif a==1 and b==2 and n>=2 and n<=5:
                c = a-1
            elif a==1 and b==1 and n>=1 and n<=5:
                c = a-1
            elif a==1 and b==0 and n>=0 and n<=5:
                c = a-1
            else:
                print('No se cumplen las condiciones para calcular c')
                c = -1

            # CALCULAR D
            if a==1 and b>=6 and b<=11 and n>=0 and n<=5:
                d = b-n-1
            elif a==1 and b==5 and n>=0 and n<=4:
                d = b-n-1
            elif a==1 and b==4 and n>=0 and n<=3:
                d = b-n-1
            elif a==1 and b==3 and n>=0 and n<=2:
                d = b-n-1
            elif a==1 and b==2 and n>=0 and n<=1:
                d = b-n-1
            elif a==1 and b==1 and n==0:
                d = b-n-1
            elif a==0 and b>=0 and b<=5 and n>=0 and n<=5:
                d = b+n+1
            elif a==0 and b==6 and n>=0 and n<=4:
                d = b+n+1
            elif a==0 and b==7 and n>=0 and n<=3:
                d = b+n+1
            elif a==0 and b==8 and n>=0 and n<=2:
                d = b+n+1
            elif a==0 and b==9 and n>=0 and n<=1:
                d = b+n+1
            elif a==0 and b==10 and n==0:
                d = b+n+1
            elif a==1 and b==5 and n==5:
                d = 0
            elif a==1 and b==4 and n>=4 and n<=5:
                d = n-4+1
            elif a==1 and b==3 and n>=3 and n<=5:
                d = n-3+1
            elif a==1 and b==2 and n>=2 and n<=5:
                d = n-2+1
            elif a==1 and b==1 and n>=1 and n<=5:
                d = n-1+1
            elif a==1 and b==0 and n==0:
                d = b
            elif a==1 and b==0 and n>=1 and n<=5:
                d = b+n-1+1
            else:
                print('No se cumplen las condiciones para calcular d')
                d = -1
    
    print(c, d)
    if c >= 0 and c <= 1 and d >= 0 and d <= 11:
        if estado.get_tablero().estado_casilla(c,d) == 'v' or estado.get_tablero().estado_casilla(c,d) == 'dao':
            valido = True
        else:
            valido = False
    else:
        valido = False

    return c, d, valido

# Movimiento de la ficha
def mover_ADAO(ficha, estado, posiciones):
    c, d, valido = verificador_ADAO(ficha, estado, posiciones)
    estadoN = estado
    if valido:
        posX, posY = c, d
        a = ficha.obtenerPosicion()[0]
        b = ficha.obtenerPosicion()[1]

        # Transformar la coordenada de pantalla en valor del arreglo tablero
        coord = (a, b)  
        pos = encontrar_posicion_cercana(coord, posiciones)
        if pos is not None:
            print(f'La coordenada {coord} está cerca de la posición {pos} en self.posiciones_fichas')
            a = pos[0]
            b = pos[1]
        else:
            print(f'La coordenada {coord} no está cerca de ninguna posición en self.posiciones_fichas')

        estadoN = actualizar_estado_ADAO(estado, a, b, posX, posY)
        print(posX, posY, estadoN.get_tablero().estado_casilla(posX, posY))
        estadoN.get_tablero().mostrar_tablero()
        return posX, posY, estadoN
    else:
        print('Movimiento no válido')
        Notifier.notify('Movimiento no válido', title='Error', sound='default')
        return -1, -1, estadoN

# Actualizar estado del juego
def actualizar_estado_ADAO(estado, xi, yi, xf, yf):
        estado.get_turno().cambio_de_turno()
        estado.get_moneda().esperar_lanzamiento()
    
        # Actualizar tablero
        # Casilla de origen
        estado.get_FA().eliminar_ficha_FA(xi, yi)
        if estado.get_FA().estado_casilla_FA(xi,yi) == 0:
            estado.get_tablero().convertir_en_vacia(xi, yi)
        else:
            estado.get_tablero().convertir_en_ordinaria(xi, yi)
        
        # Casilla de destino
        estado.get_FA().adicionar_ficha_FA(xf, yf)
        if xf==0 and yf>=0 and yf<=5:
            estado.get_tablero().convertir_en_ordinaria(xf, yf)
        elif xf==0 and yf>=6 and yf<=11:
            estado.get_tablero().convertir_en_finalista(xf, yf)
        elif xf==1 and yf>=0 and yf<=11:
            estado.get_tablero().convertir_en_ordinaria(xf, yf)
    
        return estado

