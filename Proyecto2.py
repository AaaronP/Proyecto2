
"""Esta funcion es para verificar que no hay espacios"""
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

"""Ejemplo de uso
h = [
    ["+", "+", "+", "+"],
    ["+", ".", ".", "."],
    [".", ".", ".", "."],
    [".", ".", ".", "."],
]
print(rotate(h))"""

"""Esta funcion es para verificar si se puede insertar una pieza o no"""
def is_valid(table, pieza, i, j):
    pass

"""Este es nuestro main, en donde piezas es una matriz en donde se decriben las piezas, 
n es el largo de la matriz final, m el ancho de la matriz final
P es la cantidad de piezas"""

def foo(piezas, n, m,p) -> bool:
    table = [["." for _ in range(m)] for _ in range(n)]
    Pila=[]
    while Pila:
        table2,pieza=Pila.pop()
def insertarPiezas(Table,Pieza):
    

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

    return foo(res,int(n), int(m), p)

print(inputFunc())
