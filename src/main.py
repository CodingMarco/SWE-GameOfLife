from main_menu import MainMenu
from presets import presets_dict
from board import Board
from controller import Controller


def main():
    menu = MainMenu()

    while True:
        menu.show()
        preset_chosen = menu.preset_chosen
        if menu.exit:
            break

        board = Board(91, 81, presets_dict[preset_chosen])
        controller = Controller(board, cell_size=20)
        controller.run()


if __name__ == '__main__':
    main()

