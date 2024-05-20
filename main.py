# from src.rotate import rotate
from src.isFull import isFull
from src.inputFunc import inputFunc
from src.isValid import is_valid
from src.recortar_matriz import recortar_matriz
from src.insertPiece import insertar


def tomarPieza(M, n=1):
    n = (4 * n) - 1
    mr = []
    mr.append(M[n])
    mr.append(M[n - 1])
    mr.append(M[n - 2])
    mr.append(M[n - 3])
    return mr


"""Este es nuestro main, en donde piezas es una matriz en donde se decriben las piezas, 
n es el largo de la matriz final, m el ancho de la matriz final
P es la cantidad de piezas"""


def katamino(piezas, n, m, p) -> bool:
    table = [["." for _ in range(m)] for _ in range(n)]
    pilaT = [table]

    # while pilaT:
    #     table2 = pilaT.pop()
    #     pieza = piezas.pop()

    #     if isFull(table2) and not pieza:
    #         return table2

    #     for i in range(len(table2)):
    #         for j in range(len(table2[0])):
    #             print(table2[i][j])

    inserted = []
    for i in range(len(table)):
        for j in range(len(table[0])):
            x = 0
            while x < len(piezas):
                # Pieza recortada
                piezaR = recortar_matriz(piezas[x])

                # verificamos si se puede insertar
                # y si la pieza no se ha metido aun
                if is_valid(table, piezaR, i, j) and not x in inserted:
                    insertar(table, piezaR, i, j)
                    inserted.append(x)
                x += 1

    print(table)
    # Si no tiene solucion
    return -1


def main():
    piezas, n, m, p = inputFunc()
    katamino(piezas, n, m, p)


if __name__ == "__main__":
    main()
