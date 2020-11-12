# Press Shift+F10 to execute the code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pygame
from controller import Controller
from board import Board
import presets


def main():
    pygame.init()
    board = Board(91, 81, presets.pulsar)
    controller = Controller(board, cell_size=10)
    controller.run()


if __name__ == '__main__':
    main()

