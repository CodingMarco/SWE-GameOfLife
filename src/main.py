# Press Shift+F10 to execute the code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pygame
from Ui import Ui
from Board import Board


def main(board_width, board_height, cell_size):
    pygame.init()
    board = Board(board_width, board_height)
    board.toggle_living(2, 2)
    board.toggle_living(3, 3)
    ui = Ui(cell_size, board)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        ui.draw_game_goard(board)
        pygame.display.update()


if __name__ == '__main__':
    main(10, 10, 50)

