import copy
import numpy as np


def apply_new_generation(old_board):
    new_board = copy.deepcopy(old_board)

    for x, y in np.ndindex(old_board.width, old_board.height):
        living_neighbours = old_board.get_number_of_living_neighbours(x, y)

        if old_board.get_living(x, y):
            # A living cell dies if there is underpopulation or overpopulation
            if living_neighbours < 2 or living_neighbours > 3:
                new_board.toggle_living(x, y)

        else:
            # Exactly the right condition for a dead cell to become alive
            if living_neighbours == 3:
                new_board.toggle_living(x, y)

    return new_board
