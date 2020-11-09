import pygame
import pygame.color
from board import Board


class Ui:
    def __init__(self, cell_size, board: Board):
        self.cell_size = cell_size
        self.living_color = pygame.Color(255, 255, 255)
        self.dead_color = pygame.Color(0, 0, 0)
        self.grid_color = pygame.Color(128, 128, 128)
        self.grid_line_width = 2

        self.window = pygame.display.set_mode((board.get_width() * cell_size + self.grid_line_width,
                                               board.get_height() * cell_size + self.grid_line_width))
        self.window.fill(self.grid_color)

    def draw_game_board(self, board: Board):
        self.window.fill(self.grid_color)
        for x in range(0, board.get_width()):
            for y in range(0, board.get_height()):
                pygame.draw.rect(self.window,
                                 self.living_color if board.get_living(x, y) else self.dead_color,
                                 pygame.Rect(x * self.cell_size + self.grid_line_width,
                                             y * self.cell_size + self.grid_line_width,
                                             self.cell_size-self.grid_line_width,
                                             self.cell_size-self.grid_line_width))

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
