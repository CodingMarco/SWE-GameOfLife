import pygame
import pygame.color
from board import Board
import copy
import numpy as np


class Ui:
    def __init__(self, cell_size, board: Board):
        self.cell_size = cell_size
        self.living_color = pygame.Color(255, 255, 255)
        self.dead_color = pygame.Color(0, 0, 0)
        self.grid_color = pygame.Color(128, 128, 128)
        self.grid_line_width = 1

        self.window = pygame.display.set_mode((board.width * cell_size + self.grid_line_width,
                                               board.height * cell_size + self.grid_line_width))
        self.window.fill(self.grid_color)
        self.prev_board = copy.deepcopy(board)
        self.draw_game_board(board, draw_full_board=True)

    def draw_game_board(self, board: Board, draw_full_board=False):
        for x, y in np.ndindex(board.width, board.height):
            if draw_full_board or board.get_living(x, y) != self.prev_board.get_living(x, y):
                pygame.draw.rect(self.window,
                                 self.living_color if board.get_living(x, y) else self.dead_color,
                                 pygame.Rect(x * self.cell_size + self.grid_line_width,
                                             y * self.cell_size + self.grid_line_width,
                                             self.cell_size-self.grid_line_width,
                                             self.cell_size-self.grid_line_width))
        self.prev_board = copy.deepcopy(board)

    def mouse_coordinates_to_cell(self):
        x, y = pygame.mouse.get_pos()
        if x < self.grid_line_width:
            x = 0
        else:
            x = (x-self.grid_line_width) // self.cell_size

        if y < self.grid_line_width:
            y = 0
        else:
            y = (y-self.grid_line_width) // self.cell_size

        return x, y

