""" Obtiene el elemento identificador de una pieza """


def color(pieza):
    for i in range(len(pieza)):
        for j in range(len(pieza[0])):
            if pieza[i][j] != ".":
                return pieza[i][j]
    return "."
