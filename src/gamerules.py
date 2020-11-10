import copy


class GameRules:
    def __init__(self):
        pass

    def apply_new_generation(self, board):
        copy_board = copy.deepcopy(board)
        for i in range(board.width):
            for k in range(board.height):
                nr_of_living = board.get_number_of_living_neighbours(i, k)
                living = board.get_living(i, k)

                if living == 0:  # check if field is living
                    if nr_of_living == 3:  # if dead and 3 living => turn alive
                        copy_board.toggle_living(i, k)

                else:  # check if field is dead
                    if nr_of_living == 1:  # if alive and less or equal 1 living => turn dead
                        copy_board.toggle_living(i, k)
                    elif nr_of_living >= 4:  # if alive and more or equal 4 living => turn dead
                        copy_board.toggle_living(i, k)
        return copy_board
