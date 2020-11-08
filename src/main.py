# Press Shift+F10 to execute the code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pygame
from controller import Controller


def main():
    pygame.init()
    controller = Controller(20, 20, 30)
    controller.run()


if __name__ == '__main__':
    main()

