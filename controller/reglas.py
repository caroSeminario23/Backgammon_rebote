# REGLAS: ADRO
def encontrar_posicion_cercana(coord, posiciones_fichas):
    tolerancia = 10  # Puedes ajustar este valor según tus necesidades
    for i, fila in enumerate(posiciones_fichas):
        for j, pos in enumerate(fila):
            if abs(pos[0] - coord[0]) <= tolerancia and abs(pos[1] - coord[1]) <= tolerancia:
                return [i, j]
    return None

def movimiento_adro_valido(self, a, b, c, d, n, estado_actual): # Verificar si un movimiento es válido
        # Verificar si el turno es del jugador rojo
        if estado_actual.get_turno() == 'R' and estado_actual.get_moneda() == 'a':
            if (estado_actual.get_tablero().estado_casilla(a,b) == 'dro') and (estado_actual.get_tablero().estado_casilla(c,d) == 'v' or estado_actual.get_tablero().estado_casilla(c,d) == 'dro'):
                if estado_actual.get_fichas()[4] == 0:
                    if (c >= 0 and c <= 1) and (d >= 0 and d <= 11) and (n >= 0 and n <= 5):
                        # VALIDACION DE MOVIMIENTO (PARTE 1)
                        if b==1 and n==0 and c==a:
                            validacion1 = True;
                        elif b==2 and n>=0 and n<=1 and c==a:
                            validacion1 = True;
                        elif b==3 and n>=0 and n<=2 and c==a:
                            validacion1 = True;
                        elif b==4 and n>=0 and n<=3 and c==a:
                            validacion1 = True;
                        elif b==5 and n>=0 and n<=4 and c==a:
                            validacion1 = True;
                        elif b>=6 and b<=11 and n>=0 and n<=5 and c==a:
                            validacion1 = True;
                        elif b==0 and n>=0 and n<=5 and c==1:
                            validacion1 = True;
                        elif b==1 and n>=1 and n<=5 and c==a+1:
                            validacion1 = True;
                        elif b==2 and n>=2 and n<=5 and c==a+1:
                            validacion1 = True;
                        elif b==3 and n>=3 and n<=5 and c==a+1:
                            validacion1 = True;
                        elif b==4 and n>=4 and n<=6 and c==a+1:
                            validacion1 = True;
                        elif b==5 and n==5:
                            validacion1 = True;
                        else:
                            validacion1 = False;

                        # VALIDACION DE MOVIMIENTO (PARTE 2)
                        if b>=6 and b<=11 and n>=0 and n<=5 and d==b-n and a==0:
                            validacion2 = True;
                        elif b==5 and n>=0 and n<=4 and d==b-n and a==0:
                            validacion2 = True;
                        elif b==4 and n>=0 and n<=3 and d==b-n and a==0:
                            validacion2 = True;
                        elif b==3 and n>=0 and n<=2 and d==b-n and a==0:
                            validacion2 = True;
                        elif b==2 and n>=0 and n<=1 and d==b-n and a==0:
                            validacion2 = True;
                        elif b==1 and n==0 and d==b-1 and a==0:
                            validacion2 = True;
                        elif b==0 and n>=0 and n<=5 and d==b+n-1 and a==0:
                            validacion2 = True;
                        elif b>=0 and b<=5 and n>=0 and n<=5 and d==b+n and a==1:
                            validacion2 = True;
                        elif b==6 and n>=0 and n<=4 and d==b+n and a==1:
                            validacion2 = True;
                        elif b==7 and n>=0 and n<=3 and d==b+n and a==1:
                            validacion2 = True;
                        elif b==8 and n>=0 and n<=2 and d==b+n and a==1:
                            validacion2 = True;
                        elif b==9 and n>=0 and n<=1 and d==b+n and a==1:
                            validacion2 = True;
                        elif b==10 and n==0 and d==b+1 and a==1:
                            validacion2 = True;
                        else:
                            validacion2 = False;
        
                        # VALIDACION TOTAL
                        if validacion1 == True and validacion2 == True:
                            validacion = True;
                            print('Precondiciones cumplidas')
                        else:
                            validacion = False;
                            print('Precondiciones no cumplidas')
                    else:
                        print('Precondición no cumplida: n debe estar entre 1 y 6')
                        validacion = False;
                else:
                    print('Precondición no cumplida: d debe estar entre 1 y 2')
                    validacion = False;
            else:
                print('Precondición no cumplida: c debe estar entre 1 y 12')
                validacion = False;
        else:
            print('Precondición no cumplida: ndro debe ser igual a 0')
            validacion = False;
        return validacion

# Verificador de la posicion a la que se movera la ficha
def verificador_ADRO(ficha, estado, posiciones):
    aO = ficha.obtenerPosicion()[0]
    bO = ficha.obtenerPosicion()[1]
    a, b = 0, 0

    # Transformar la coordenada de pantalla en valor del arreglo tablero
    coord = (aO, bO)  # Reemplaza esto con la coordenada que quieras verificar
    pos = encontrar_posicion_cercana(coord, posiciones)
    if pos is not None:
        print(f'La coordenada {coord} está cerca de la posición {pos} en self.posiciones_fichas')
        a = pos[0]
        b = pos[1]
    else:
        print(f'La coordenada {coord} no está cerca de ninguna posición en self.posiciones_fichas')


    n = (estado.get_dado().get_valor_actual())-1
    c, d = 0, 0
    valido = False

    if estado.get_turno() == 'R' and estado.get_moneda() == 'a':
        if (estado.get_tablero().estado_casilla(a,b) == 'dro'):
            # CALCULAR C
            if b==1 and n==0 and a==0:
                c = a
            elif b==2 and n>=0 and n<=1 and a==0:
                c = a
            elif b==3 and n>=0 and n<=2 and a==0:
                c = a
            elif b==4 and n>=0 and n<=3 and a==0:
                c = a
            elif b==5 and n>=0 and n<=4 and a==0:
                c = a
            elif b>=6 and b<=11 and n>=0 and n<=5 and a==0:
                c = a
            elif b==0 and n>=0 and n<=5 and a==0:
                c = a+1
            elif b==1 and n>=1 and n<=5 and a==1:
                c = a+1
            elif b==2 and n>=2 and n<=5 and a==1:
                c = a+1
            elif b==3 and n>=3 and n<=5 and a==1:
                c = a+1
            elif b==4 and n>=4 and n<=6 and a==1:
                c = a+1
            elif b==5 and n==5 and a==1:
                c = a+1
            elif b>=0 and b<=5 and n>=0 and n<=5 and a==1:
                c = a
            elif b==6 and n>=0 and n<=4 and a==1:
                c = a
            elif b==7 and n>=0 and n<=3 and a==1:
                c = a
            elif b==8 and n>=0 and n<=2 and a==1:
                c = a
            elif b==9 and n>=0 and n<=1 and a==1:
                c = a
            elif b==10 and n==0 and a==1:
                c = a
            else:
                print('No se cumplen las condiciones para calcular c')
                c = -1
            
            # CALCULAR D
            if b>=6 and b<=11 and n>=0 and n<=5 and a==0:
                d = b-n
            elif b==5 and n>=0 and n<=4 and a==0:
                d = b-n
            elif b==4 and n>=0 and n<=3 and a==0:
                d = b-n
            elif b==3 and n>=0 and n<=2 and a==0:
                d = b-n
            elif b==2 and n>=0 and n<=1 and a==0:
                d = b-n
            elif b==1 and n==0 and a==0:
                d = b-1
            elif b==0 and n==0 and a==0:
                d = b
            elif b==0 and n>=0 and n<=5 and a==1:
                d = b+n-1
            elif b>=0 and b<=5 and n>=0 and n<=5 and a==1:
                d = b+n
            elif b==6 and n>=0 and n<=4 and a==1:
                d = b+n
            elif b==7 and n>=0 and n<=3 and a==1:
                d = b+n
            elif b==8 and n>=0 and n<=2 and a==1:
                d = b+n
            elif b==9 and n>=0 and n<=1 and a==1:
                d = b+n
            elif b==10 and n==0 and a==1:
                d = b+1
            else:
                print('No se cumplen las condiciones para calcular d')
                d = -1
    
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

    if valido:
        posX, posY = c, d
        return posX, posY
    else:
        print('Movimiento no válido')
        return -1, -1