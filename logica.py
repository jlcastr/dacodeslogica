#esquina superior de una cuadricula N x M
#mirando a la derecha, sigue camiando un cuadro a la vez en la direccion que esta mirando
#(dirección derecha)

#----------------------
#|(0,0)|(0,1)|(0,2)|
#|(1,0)|(1,1)|(1,2)|
#|(2,0)|(2,1)|(2,2)|
#---------------------

def recorrido(N,M):
    if (N > M):
        if (M % 2 == 0):
            print('Arriba')
        else:
            print('Abajo')
    else:
        if (N%2== 0):
            print('Izquierda')
        else:
            print('Derecha')

#recorrido(0,4)
recorrido(1,1)
recorrido(2,2)
recorrido(3,1)
recorrido(3,3)