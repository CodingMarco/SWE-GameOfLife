class Board:
    def __init__(self, x, y):
        self.board = [[False for i in range(x)]for k in range(y)]

    def set_living(self, x, y):
        self.board[x][y] = not self.board[x][y]

    def get_number_of_living_neighbours(self, x, y):
        nr_of_liv_neig = 0

        if self.board[x+1][y]:             # 1          # 4 3 2
            nr_of_liv_neig += 1                            # 5 o 1
                                                        # 6 7 8
        if self.board[x + 1][y + 1]:       # 2
            nr_of_liv_neig += 1

        if self.board[x][y + 1]:           # 3
            nr_of_liv_neig += 1

        if self.board[x - 1][y + 1]:       # 4
            nr_of_liv_neig += 1

        if self.board[x - 1][y]:           # 5
            nr_of_liv_neig += 1

        if self.board[x - 1][y - 1]:       # 6
            nr_of_liv_neig += 1

        if self.board[x][y - 1]:           # 7
            nr_of_liv_neig += 1

        if self.board[x + 1][y - 1]:       # 8
            nr_of_liv_neig += 1

        return nr_of_liv_neig

    def get_living(self, x, y):
        return self.board[x][y]

    def draw(self):
        for r in self.board:
            for c in r:
                print(c, end=" ")

            print()


if __name__ == '__main__':
    board = Board(5, 5)
    board.draw()
    print()
    board.set_living(2, 3)
    board.set_living(2, 1)
    board.draw()
    print(board.get_number_of_living_neighbours(2, 2))
    print()
    for i in range(len(board.board)):
        print(board.board[i])
