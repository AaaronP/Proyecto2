def insertar(table, pieza, i, j):
    for x in range(len(pieza)):
        for y in range(len(pieza[0])):
            if pieza[x][y] != ".":
                table[i + x][j + y] = pieza[x][y]

    return table

#print(insertar([['+', '+', '+', '+', '.', '.'], ['+', '*', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.']],), )
