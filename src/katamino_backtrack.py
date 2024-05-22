from src.isFull import isFull
from src.isValid import is_valid
from src.insertPiece import insertar
from src.quitar import quitar

def katamino_backtrack(table, piezas, n, m, p):
  """
  Esta funcion soluciona el puzzle de katamino usando un algoritmo de backtracking en donde
    table: A 2D list representing the table where the pieces will be placed.
    piezas: es la lista de piezas.
    n: el largo del tablero.
    m: el ancho del tablero.
    p: el numero de puezas.
  """

  if isFull(table):
    return table
  for i in range(n):
    for j in range(m):
      # Iterate over the pieces.
      for pieza in piezas:
        # Check if the piece can be inserted at the current cell.
        if is_valid(table, pieza, i, j):
          # Insert the piece into the table.
          insertar(table, pieza, i, j)
          # Recursively solve the puzzle with the remaining pieces.
          solution = katamino_backtrack(table, piezas.remove(pieza), n, m, p - 1)
          # If a solution is found, return it.
          if solution is not None:
            return solution
          # If no solution is found, remove the piece from the table.
          quitar(table, pieza, i, j)
  # If no solution is found, return None.
  return None