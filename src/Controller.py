import pygame
from Ui import Ui
from Board import Board


class Controller:
    def __init__(self, board_width, board_height, cell_size):
        self.board = Board(board_width, board_height)
        self.board.toggle_living(2, 2)
        self.board.toggle_living(3, 3)
        self.ui = Ui(cell_size, self.board)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
            self.ui.draw_game_goard(self.board)
            pygame.display.update()
