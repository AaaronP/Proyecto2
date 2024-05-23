from src.grafica import dibujar_tablero

def isFull(table) -> bool:
    for i in range(len(table)):
        for j in range(len(table[0])):
            if table[i][j] == ".":
                return False
    return True

def rotate(M):
    n = len(M)

    for i in range(n):
        for j in range(i):
            temp = M[i][j]
            M[i][j] = M[j][i]
            M[j][i] = temp

    for i in range(n):
        for j in range(n // 2):
            temp = M[i][j]
            M[i][j] = M[i][n - j - 1]
            M[i][n - j - 1] = temp

    return M

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

    return (res, int(n), int(m), p)

def is_valid(table, piezaR, i, j):
    # Verificar que las coordenadas (i, j) estén dentro de los límites del tablero
    if (
        i < 0
        or i + len(piezaR) > len(table)
        or j < 0
        or j + len(piezaR[0]) > len(table[0])
    ):
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

def recortar_matriz(matriz):
    # Encontrar los límites superior, inferior, izquierdo y derecho
    fila_superior = None
    fila_inferior = None
    columna_izquierda = None
    columna_derecha = None

    for i, fila in enumerate(matriz):
        for j, valor in enumerate(fila):
            if valor != ".":
                fila_superior = i if fila_superior is None else min(fila_superior, i)
                fila_inferior = i if fila_inferior is None else max(fila_inferior, i)
                columna_izquierda = (
                    j if columna_izquierda is None else min(columna_izquierda, j)
                )
                columna_derecha = (
                    j if columna_derecha is None else max(columna_derecha, j)
                )

    # Recortar la matriz usando los límites encontrados
    matriz_recortada = [
        fila[columna_izquierda : columna_derecha + 1]
        for fila in matriz[fila_superior : fila_inferior + 1]
    ]
    return matriz_recortada

def insertar(table, pieza, i, j):
    for x in range(len(pieza)):
        for y in range(len(pieza[0])):
            if pieza[x][y] != ".":
                table[i + x][j + y] = pieza[x][y]

    return table

def color(pieza):
    for i in range(len(pieza)):
        for j in range(len(pieza[0])):
            if pieza[i][j] != ".":
                return pieza[i][j]
    return "."

# Color: elemento identificar de la pieza
def quitar(table, color):
    for i in range(len(table)):
        for j in range(len(table[0])):
            if table[i][j] == color:
                table[i][j] = "."
    return table

"""Este es nuestro main, en donde piezas es una matriz en donde se decriben las piezas, 
n es el largo de la matriz final, m el ancho de la matriz final
P es la cantidad de piezas"""


def katamino(piezas, n, m, p):
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
    # EL len del table no deberia de ser siempre de n y el otro de m
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

    # Si no tiene solucion
    return table


def main():
    piezas, n, m, p = inputFunc()
    k = katamino(piezas, n, m, p)

    if k == -1: return -1
    dibujar_tablero(k)


if __name__ == "__main__":
    main()
