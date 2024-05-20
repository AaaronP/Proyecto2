""" Busca la pieza a quitar y lo reemplaza con un ."""


# Color: elemento identificar de la pieza
def quitar(table, color):
    for i in range(len(table)):
        for j in range(len(table[0])):
            if table[i][j] == color:
                table[i][j] = "."
    return table
