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

print(inputFunc())