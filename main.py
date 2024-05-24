from grafica import dibujar_tablero


def isFull(table) -> bool:
    for i in range(len(table)):
        for j in range(len(table[0])):
            if table[i][j] == ".":
                return False
    return True


def rotate(M):
    m = len(M[0])
    r = []
    for x in range(m):
        fila = []
        n = len(M) - 1
        while n >= 0:
            fila.append(M[n][x])
            n -= 1
        r.append(fila)
    return r


def inputFunc():
    # Ancho, Largo, numero de piezas
    n, m, p = list(map(int, input().split()))

    # Obtener las piezas
    res = []
    for _ in range(p):
        aux = []
        for _ in range(4):
            txt = list(input())
            aux.append(txt)
        res.append((aux, 0))

    return (res, n, m, p)


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


def katamino_backtrack(table, piezas, n, m, p):
    """
    Esta funcion soluciona el puzzle de katamino usando un algoritmo de backtracking en donde
      table: A 2D list representing the table where the pieces will be placed.
      piezas: es la lista de piezas.
      n: el largo del tablero.
      m: el ancho del tablero.
      p: el numero de puezas.
    """
    # [([], 0), ([], 0)]
    if piezas == []:
        return table
    for pieza, contador in piezas:
        piezas.remove((pieza, contador))
        pieza = recortar_matriz(pieza)
        while contador <= 3:
            for i in range(n):
                for j in range(m):
                    if is_valid(table, pieza, i, j):
                        insertar(table, pieza, i, j)
                        solution = katamino_backtrack(table, piezas, n, m, p - 1)
                        if solution == -1:
                            quitar(table, color(pieza))
                        else:
                            return solution
            contador += 1
            pieza = rotate(pieza)
        piezas.insert(0, (pieza, 0))
        return -1
    return -1


def main():
    piezas, n, m, p = inputFunc()
    table = [["." for _ in range(m)] for _ in range(n)]
    k = katamino_backtrack(table, piezas, n, m, p)
    if k == -1:
        return -1
    dibujar_tablero(k)


if __name__ == "__main__":
    main()
