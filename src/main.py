# Press Shift+F10 to execute the code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pygame
from Ui import Ui
from Board import Board
from Controller import Controller


def main():
    pygame.init()
    controller = Controller(10, 10, 50)
    controller.run()


if __name__ == '__main__':
    main()

