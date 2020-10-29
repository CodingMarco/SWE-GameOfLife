class Board:
    def __init__(self, x, y):
        self.board = [[False for i in range(x)]for k in range(y)]

    def setliving(self, x, y, living: bool):
        self.board[x][y] = living

    def getnumberoflivingneighbours(self, x, y):
        print()

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
    board.draw()
    print()
    for i in range(len(board.board)):
        print(board.board[i])
