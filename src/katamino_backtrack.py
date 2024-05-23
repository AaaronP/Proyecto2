from src.isFull import isFull
from src.isValid import is_valid
from src.insertPiece import insertar
from src.quitar import quitar
from src.rotate import rotate

def katamino_backtrack(table, piezas, n, m, p):
  """
  Esta funcion soluciona el puzzle de katamino usando un algoritmo de backtracking en donde
    table: A 2D list representing the table where the pieces will be placed.
    piezas: es la lista de piezas.
    n: el largo del tablero.
    m: el ancho del tablero.
    p: el numero de puezas.
  """
  # [([], 0), ([], 0)]
  if isFull(table):
    return table
  for i in range(n):
    for j in range(m):
      for pieza in piezas:
        if is_valid(table, pieza, i, j):
          insertar(table, pieza, i, j)
          piezas.remove(pieza)
          solution = katamino_backtrack(table, piezas, n, m, p - 1)

          # pieza = T[0]
          # piezasC = T[1]

          if not solution and piezasC <= 3:
            piezas.append((rotate(pieza, piezasC + 1)))
            
          if solution is not None:
            return solution
          
          quitar(table, pieza, i, j)
  return None