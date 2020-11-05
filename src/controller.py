import pygame
from ui import Ui
from board import Board


class Controller:
    def __init__(self, board_width, board_height, cell_size):
        self.board = Board(board_width, board_height)
        self.ui = Ui(cell_size, self.board)

    def run(self):
        while True:
            events = [pygame.event.wait()] + pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = self.ui.mouse_coordinates_to_cell()
                    self.board.toggle_living(x, y)

            self.ui.draw_game_goard(self.board)
            pygame.display.update()
