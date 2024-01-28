import texttable


class Board:

    def __init__(self):
        self.data = [[" ", " ", " ", " ", " ", " "] for x in range(6)]

    def __str__(self):
        self.table = texttable.Texttable()
        self.table.add_rows(self.data,[])
        return self.table.draw()

    def move(self, piece, row, col):
        self.data[row][col] = piece

    def isGameWon(self, piece):
        for i in range(6):
            if self.data[i][0] == self.data[i][1] == self.data[i][2] == self.data[i][3] == self.data[i][4] == piece:
                return True
            if self.data[i][5] == self.data[i][1] == self.data[i][2] == self.data[i][3] == self.data[i][4] == piece:
                return True
            if self.data[0][i] == self.data[1][i] == self.data[2][i] == self.data[3][i] == self.data[4][i] == piece:
                return True
            if self.data[5][i] == self.data[1][i] == self.data[2][i] == self.data[3][i] == self.data[4][i] == piece:
                return True

        for i in range(2):
            if self.data[i][i] == self.data[i+1][i+1] == self.data[i+2][i+2] == self.data[i+3][i+3] == self.data[i+4][i+4] == piece:
                return True

        if self.data[0][1] == self.data[1][2] == self.data[2][3] == self.data[3][4] == self.data[4][5] == piece:
            return True

        if self.data[1][0] == self.data[2][1] == self.data[3][2] == self.data[4][3] == self.data[5][4] == piece:
            return True

        return False

    def get_vaid_moves(self):
        moves = []
        for i in range(6):
            for j in range(6):
                if self.data[i][j] == " ":
                    moves.append((i, j))
        return moves

    def nospacesleft(self):
        for i in range(6):
            for j in range(6):
                if self.data[i][j] == " ":
                    return False
        return True

    # def get_existent_moves(self):
    #     """
    #     a list of moves and their pieces
    #     :return:
    #     """
    #     moves = []
    #     for i in range(6):
    #         for j in range(6):
    #             if self.data[i][j] != " ":
    #                 moves.append((i, j, self.data[i][j]))
    #     return moves