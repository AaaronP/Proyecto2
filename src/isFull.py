"""Esta funcion es para verificar que no hay espacios"""


def isFull(table) -> bool:
    for i in range(len(table)):
        for j in range(len(table[0])):
            if table[i][j] == ".":
                return False
    return True
