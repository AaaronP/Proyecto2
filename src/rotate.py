"""Rota una matriz de nxm -90 grados"""


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
