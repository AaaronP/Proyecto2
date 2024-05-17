"""Esta funcion es para verificar si se puede insertar una pieza o no"""


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
