import pygame
import pygame.color
from Board import Board


class Ui:
    def __init__(self, window: pygame.display, cell_size):
        self.cell_size = cell_size
        self.window = window

    def draw_game_goard(self, board: Board):
        for x in range(0, board.get_width()):
            for y in range(0, board.get_height()):
                pygame.draw.rect(self.window,
                                 pygame.Color(255, 255, 255) if board.get_living(x, y) else pygame.Color(0, 0, 0),
                                 pygame.Rect(x * self.cell_size,
                                             y * self.cell_size,
                                             self.cell_size-2,
                                             self.cell_size-2))

