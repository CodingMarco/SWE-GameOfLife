import pygame
import pygame.color
from board import Board
import copy
import numpy as np


class Ui:
    WHITE = pygame.Color(255, 255, 255)
    BLACK = pygame.Color(0, 0, 0)
    GREY = pygame.Color(128, 128, 128)

    def __init__(self, cell_size, board: Board):
        self.living_color = self.WHITE
        self.dead_color = self.BLACK

        self._cell_size = cell_size
        self._grid_color = self.GREY
        self._grid_line_width = 1

        self._previous_board = copy.deepcopy(board)
        self._pygame_window = pygame.display.set_mode((board.width * cell_size + self._grid_line_width,
                                                       board.height * cell_size + self._grid_line_width))

        self._pygame_window.fill(self._grid_color)
        self.draw_game(board, draw_full_board=True)

    def draw_game(self, board: Board, draw_full_board=False):
        for x, y in np.ndindex(board.width, board.height):
            if draw_full_board or board.get_living(x, y) != self._previous_board.get_living(x, y):
                current_cell_color = self.living_color if board.get_living(x, y) else self.dead_color
                current_cell_rect = self._cell_coordinates_to_rect(x, y)
                pygame.draw.rect(self._pygame_window, current_cell_color, current_cell_rect)

        self._previous_board = copy.deepcopy(board)

    def mouse_coordinates_to_cell(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()

        if mouse_x < self._grid_line_width:
            cell_x = 0
        else:
            cell_x = (mouse_x - self._grid_line_width) // self._cell_size

        if mouse_y < self._grid_line_width:
            cell_y = 0
        else:
            cell_y = (mouse_y - self._grid_line_width) // self._cell_size

        return cell_x, cell_y

    def _cell_coordinates_to_rect(self, x, y):
        return pygame.Rect(x * self._cell_size + self._grid_line_width,
                           y * self._cell_size + self._grid_line_width,
                           self._cell_size - self._grid_line_width,
                           self._cell_size - self._grid_line_width)
