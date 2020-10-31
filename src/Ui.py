import pygame
import pygame.color
from Board import Board


class Ui:
    def __init__(self, window: pygame.display, cell_size):
        self.cell_size = cell_size
        self.window = window
        self.living_color = pygame.Color(255, 255, 255)
        self.dead_color = pygame.Color(0, 0, 0)
        self.grid_color = pygame.Color(128, 128, 128)
        self.grid_line_width = 2

    def draw_game_goard(self, board: Board):
        self.window.fill(self.grid_color)
        for x in range(0, board.get_width()):
            for y in range(0, board.get_height()):
                pygame.draw.rect(self.window,
                                 self.living_color if board.get_living(x, y) else self.dead_color,
                                 pygame.Rect(x * self.cell_size,
                                             y * self.cell_size,
                                             self.cell_size-self.grid_line_width,
                                             self.cell_size-self.grid_line_width))

