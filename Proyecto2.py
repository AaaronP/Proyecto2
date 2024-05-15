from src.recortar_matriz import recortar_matriz
from src.rotate import rotate
from src.isFull import isFull

"""Esta funcion es para verificar si se puede insertar una pieza o no"""


def is_valid(table, pieza, i, j):
    piezaR = recortar_matriz(pieza)
    # Verificar que las coordenadas (i, j) estén dentro de los límites del tablero
    if i < 0 or i + 3 >= len(table) or j < 0 or j + 3 >= len(table[0]):
        return False

    # Verificar si la pieza cabe completamente dentro del tablero
    for row in range(len(piezaR)):
        for col in range(len(piezaR[0])):
            if piezaR[row][col] != ".":
                if i + row >= len(table) or j + col >= len(table[0]):
                    return False
                if table[i + row][j + col] != ".":
                    return False

    return True


# Ejemplo de uso:
tablero = [
    [".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", "."],
]

# Ejemplo de pieza de 4x4
pieza = [
    [".", ".", ".", "."],
    [".", "X", "X", "."],
    [".", "X", "X", "."],
    [".", ".", ".", "."],
]

# Verificar si la pieza puede ser colocada en el tablero en la posición (3, 3)
print(is_valid(tablero, pieza, 0, 0))  # Output: True

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
