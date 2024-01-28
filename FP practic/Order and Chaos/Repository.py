from Domain import Board
import random

class RepoError(Exception):
    pass

class Repo:

    def __init__(self):
        self.__board = Board()

    def move(self, piece, x, y):
        if self.__board.data[x][y] != " " and (x, y) not in self.__board.get_vaid_moves():
            raise RepoError("Invalid move!")
        self.__board.move(piece, x, y)

    def get_board(self):
        return self.__board

    def isGameWon(self, piece):
        return self.__board.isGameWon(piece)

    def nospacesleft(self):
        return self.__board.nospacesleft()

class AI:

    def checkforconnections(self, piece, board):
        for i in range(6):
            if board.data[i][0] == board.data[i][1] == board.data[i][2] == board.data[i][3]== piece:
                if board.data[i][4] == " ":
                    return i,4
            if board.data[i][5] == board.data[i][1] == board.data[i][2] == board.data[i][3]== piece:
                if board.data[i][4] == " ":
                    return i,4
            if board.data[0][i] == board.data[1][i] == board.data[2][i] == board.data[3][i]== piece:
                if board.data[4][i] == " ":
                    return 4,i
            if board.data[5][i] == board.data[1][i] == board.data[2][i] == board.data[3][i]== piece:
                if board.data[4][i] == " ":
                    return 4,i
        for i in range(2):
            if board.data[i][i] == board.data[i+1][i+1] == board.data[i+2][i+2] == board.data[i+3][i+3]== piece:
                if board.data[i+4][i+4] == " ":
                    return i+4,i+4

        for i in range (2):
            if board.data[i][5-i] == board.data[i+1][4-i] == board.data[i+2][3-i] == board.data[i+3][2-i]== piece:
                if board.data[i+4][1-i] == " ":
                    return i+4,1-i

        return False

    def move(self, piece, opponent_piece, board):
        if self.checkforconnections(piece, board) != False:
            x, y = self.checkforconnections(piece, board)
            board.move(piece, x, y)
        elif self.checkforconnections(opponent_piece, board) != False:
            x, y = self.checkforconnections(opponent_piece, board)
            board.move(opponent_piece, x, y)
        else:
            moves = board.get_vaid_moves()
            x, y = random.choice(moves)
            board.move(random.choice([piece, opponent_piece]), x, y)








