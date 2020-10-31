# Press Shift+F10 to execute the code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pygame


def main(board_width, board_height, cell_size):
    pygame.init()
    screen = pygame.display.set_mode((board_width * cell_size, board_height * cell_size))
    screen.fill((100, 255, 100))
    while pygame.event.wait().type != pygame.QUIT:
        pass


if __name__ == '__main__':
    main(10, 10, 10)

