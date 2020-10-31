# Press Shift+F10 to execute the code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pygame
from Ui import Ui
from Board import Board


def main(board_width, board_height, cell_size):
    pygame.init()
    window = pygame.display.set_mode((board_width * cell_size, board_height * cell_size))
    window.fill((128, 128, 128))

    board = Board(board_width, board_height)
    board.toggle_living(2, 2)
    board.toggle_living(3, 3)
    ui = Ui(window, cell_size)
    ui.draw_game_goard(board)

    while pygame.event.wait().type != pygame.QUIT:
        pass


if __name__ == '__main__':
    main(10, 10, 50)

