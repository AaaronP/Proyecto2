def isFull(table) -> bool:
    for i in range(len(table)):
        for j in range(len(table[0])):
            if table[i][j] == ".":
                return False
    return True


def is_valid(table, pieza, i, j):
    pass


def foo(piezas, n, m) -> bool:
    table = [["." for _ in range(m)] for _ in range(n)]


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

    return (int(n), int(m), res)
