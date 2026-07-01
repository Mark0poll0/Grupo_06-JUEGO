# src/config.py
import os

# Configuración de pantalla
CELL_SIZE = 64  # Cada celda del Sokoban medirá 64x64 píxeles
FPS = 60

# Colores (RGB)
COLOR_BG = (30, 30, 30)
COLOR_WALL = (80, 80, 80)
COLOR_PLAYER = (50, 120, 240)
COLOR_BOX = (200, 140, 40)
COLOR_GOAL = (50, 200, 80)
COLOR_BOX_ON_GOAL = (40, 180, 40)

# Representación matemática de los elementos en la matriz (Tablero)
EMPTY = 0
WALL = 1
GOAL = 2
BOX = 3
PLAYER = 4
BOX_ON_GOAL = 5
PLAYER_ON_GOAL = 6

# Direcciones de movimiento
MOVE_UP = (0, -1)
MOVE_DOWN = (0, 1)
MOVE_LEFT = (-1, 0)
MOVE_RIGHT = (1, 0)