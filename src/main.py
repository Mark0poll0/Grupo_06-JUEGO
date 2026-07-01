# src/main.py
import sys
import pygame
from src.config import (
    CELL_SIZE, FPS, COLOR_BG, COLOR_WALL, COLOR_PLAYER, 
    COLOR_BOX, COLOR_GOAL, COLOR_BOX_ON_GOAL,
    EMPTY, WALL, GOAL, BOX, PLAYER, BOX_ON_GOAL, PLAYER_ON_GOAL
)
from src.engine.board import Board

def render_board(screen, board):
    """
    Recorre explícitamente la matriz matemática del tablero y dibuja 
    un rectángulo de color en la ventana de Pygame para cada celda.
    """
    for y in range(board.height):
        for x in range(board.width):
            cell_type = board.get_at(x, y)
            rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            
            if cell_type == WALL:
                pygame.draw.rect(screen, COLOR_WALL, rect)
                # Dibujamos un borde sutil para diferenciar los bloques de pared
                pygame.draw.rect(screen, (50, 50, 50), rect, 1)
            elif cell_type == GOAL:
                pygame.draw.rect(screen, COLOR_GOAL, rect)
            elif cell_type == BOX:
                pygame.draw.rect(screen, COLOR_BOX, rect)
                pygame.draw.rect(screen, (150, 100, 20), rect, 3) # Contorno de caja
            elif cell_type == BOX_ON_GOAL:
                pygame.draw.rect(screen, COLOR_BOX_ON_GOAL, rect)
                pygame.draw.rect(screen, (20, 100, 20), rect, 3)
            elif cell_type in (PLAYER, PLAYER_ON_GOAL):
                # Si el jugador está sobre una meta, dibujamos el fondo de la meta primero
                if cell_type == PLAYER_ON_GOAL:
                    pygame.draw.rect(screen, COLOR_GOAL, rect)
                # Dibujamos al jugador como un círculo centrado en la celda
                center = (x * CELL_SIZE + CELL_SIZE // 2, y * CELL_SIZE + CELL_SIZE // 2)
                radius = CELL_SIZE // 3
                pygame.draw.circle(screen, COLOR_PLAYER, center, radius)

def main():
    # 1. Inicialización explícita de Pygame y reloj
    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption("Sokoban AI - Prueba de Matriz y Renderizado")

    # 2. Definición de un mapa de prueba (Matriz típica de Sokoban)
    # 1: Pared, 2: Meta, 3: Caja, 4: Jugador, 0: Vacío
    level_test = [
        [1, 1, 1, 1, 1, 1, 1],
        [1, 4, 0, 1, 2, 0, 1],
        [1, 0, 3, 0, 2, 0, 1],
        [1, 0, 3, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1]
    ]

    # Instanciamos el tablero con la lógica matemática que programamos
    board = Board(level_test)

    # 3. Calcular las dimensiones de la ventana dinámicamente basadas en el mapa
    window_width = board.width * CELL_SIZE
    window_height = board.height * CELL_SIZE
    screen = pygame.display.set_device_mode((window_width, window_height)) if hasattr(pygame, 'set_device_mode') else pygame.display.set_mode((window_width, window_height))

    print(f"Tablero cargado con éxito. Dimensiones: {board.width}x{board.height}")
    print(f"Posición inicial detectada del jugador: {board.player_pos}")

    # 4. Bucle principal del juego
    running = True
    while running:
        # Control de FPS
        clock.tick(FPS)

        # Manejo de Eventos (Captura el cierre de ventana)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        # Limpieza de pantalla con el color de fondo de la configuración
        screen.fill(COLOR_BG)

        # Dibujar el estado actual del tablero matemático
        render_board(screen, board)

        # Actualizar el buffer de la pantalla
        pygame.display.flip()

    # Salida limpia
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()