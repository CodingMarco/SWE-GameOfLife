# Press Shift+F10 to execute the code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pygame
from controller import Controller
from board import Board
import presets
import main_menu


def main():
    while True:
        preset_chosen = main_menu.show_main_menu()
        pygame.init()
        board = Board(91, 81, presets.presets_dict[preset_chosen])
        controller = Controller(board, cell_size=20)
        controller.run()
        pygame.quit()


if __name__ == '__main__':
    main()

