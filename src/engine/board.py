# src/engine/board.py
from src.config import EMPTY, WALL, GOAL, BOX, PLAYER, BOX_ON_GOAL, PLAYER_ON_GOAL

class Board:
    def __init__(self, level_matrix):
        """
        Inicializa el tablero con una matriz bidimensional (lista de listas).
        La matriz original se duplica para mantener un estado limpio.
        """
        self.width = len(level_matrix[0])
        self.height = len(level_matrix)
        self.matrix = [row[:] for row in level_matrix]
        self.player_pos = self._find_player()

    def _find_player(self):
        """Busca explícitamente la posición inicial (x, y) del jugador en la matriz."""
        for y in range(self.height):
            for x in range(self.width):
                if self.matrix[y][x] in (PLAYER, PLAYER_ON_GOAL):
                    return (x, y)
        raise ValueError("El mapa provisto no contiene una posición de inicio para el jugador.")

    def get_at(self, x, y):
        """Devuelve el valor de la celda si está dentro de los límites."""
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.matrix[y][x]
        return WALL

    def is_walkable(self, x, y):
        """Evalúa explícitamente si una coordenada es transitable (vacía o meta)."""
        cell = self.get_at(x, y)
        return cell in (EMPTY, GOAL)

    def is_box(self, x, y):
        """Determina si la celda contiene una caja (normal o sobre meta)."""
        cell = self.get_at(x, y)
        return cell in (BOX, BOX_ON_GOAL)