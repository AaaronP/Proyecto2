"""Elimina los espacios vacios donde su columna y su fila no contiene un elemento de la pieza"""

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
