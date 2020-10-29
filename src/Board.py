class Board:
    def __init__(self, x, y):
        self.board = [[False for i in range(x)]for k in range(y)]

    def setliving(self, x, y, living: bool):
        self.board[x][y] = living

    def getnumberoflivingneighbours(self, x, y):
        nrOfLivNeig = 0

        if self.board[x+1][y]:             # 1          # 4 3 2
            nrOfLivNeig += 1                            # 5 o 1
                                                        # 6 7 8
        if self.board[x + 1][y + 1]:       # 2
            nrOfLivNeig += 1

        if self.board[x][y + 1]:           # 3
            nrOfLivNeig += 1

        if self.board[x - 1][y + 1]:       # 4
            nrOfLivNeig += 1

        if self.board[x - 1][y]:           # 5
            nrOfLivNeig += 1

        if self.board[x - 1][y - 1]:       # 6
            nrOfLivNeig += 1

        if self.board[x][y - 1]:           # 7
            nrOfLivNeig += 1

        if self.board[x + 1][y - 1]:       # 8
            nrOfLivNeig += 1

        return nrOfLivNeig

    def getliving(self, x, y):
        print(self.board[x][y])

    def draw(self):
        for r in self.board:
            for c in r:
                print(c, end=" ")

            print()


if __name__ == '__main__':
    board = Board(5, 5)
    board.draw()
    print()
    board.setliving(2, 3, True)
    board.setliving(2, 1, True)
    board.draw()
    print(board.getnumberoflivingneighbours(2, 2))
    print()
    for i in range(len(board.board)):
        print(board.board[i])
