# Press Shift+F10 to execute the code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pygame
from controller import Controller
from board import Board
import presets


def main():
    pygame.init()
    board = Board(11, 11, presets.square)
    controller = Controller(board, 30)
    controller.run()


if __name__ == '__main__':
    main()

