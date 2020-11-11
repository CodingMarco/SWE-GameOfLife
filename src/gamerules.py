import copy


def apply_new_generation(old_board):
    new_board = copy.deepcopy(old_board)
    for x in range(old_board.width):
        for y in range(old_board.height):
            nr_of_living_neighbours = old_board.get_number_of_living_neighbours(x, y)
            is_current_cell_living = old_board.get_living(x, y)

            if not is_current_cell_living:
                if nr_of_living_neighbours == 3:
                    new_board.toggle_living(x, y)

            else:
                if nr_of_living_neighbours < 2:
                    new_board.toggle_living(x, y)
                elif nr_of_living_neighbours > 3:
                    new_board.toggle_living(x, y)
    return new_board
