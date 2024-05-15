from src.rotate import rotate
from src.isFull import isFull
from src.isValid import is_valid

"""Este es nuestro main, en donde piezas es una matriz en donde se decriben las piezas, 
n es el largo de la matriz final, m el ancho de la matriz final
P es la cantidad de piezas"""


def foo(piezas, n, m, p) -> bool:
    table = [["." for _ in range(m)] for _ in range(n)]
    pilaT = [table]

    while pilaT:
        table2 = pilaT.pop()
        pieza = piezas.pop()

        if isFull(table2) and pieza == []:
            return table2

        for i in range(len(table2)):
            for j in range(len(table2[0])):
                pass

    # Si no tiene solucion
    return -1


def insertarPiezas(Table, Pieza):
    pass


def tomarPieza(M, n=1):
    n = (4 * n) - 1
    mr = []
    mr.append(M[n])
    mr.append(M[n - 1])
    mr.append(M[n - 2])
    mr.append(M[n - 3])
    return mr


def inputFunc():
    # Ancho, Largo, numero de piezas
    n, m, p = input().split()

    # Obtener las piezas
    res = []
    for _ in range(int(p)):
        aux = []
        for _ in range(4):
            txt = list(input())
            aux.append(txt)
        res.append(aux)

    # return tomarPieza(res, 2)
    return foo(res, int(n), int(m), p)


# inputFunc()
