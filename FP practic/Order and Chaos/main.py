from Repository import *
import random
class UIError(Exception):
    pass

class UI:

    def __init__(self):
        self.__repo = Repo()
        self.__ai = AI()

    def Menu(self):
        print("1. Start game")
        print("2. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            self.start_game()
        elif choice == "2":
            print("Goodbye!")
            return "exit"
        else:
            print("No such command!")

    def start_game(self):
        try:
            while self.__repo.nospacesleft() == False and self.__repo.isGameWon("X") == False and self.__repo.isGameWon("0") == False:
                ok = False
                while ok == False:
                    print(self.__repo.get_board())
                    line = input("Choose your line: ")
                    column = input("Choose your column: ")
                    piece = input("Choose your piece: X or O: ")

                    if piece not in ["X", "O"]:
                        raise UIError("The chosen piece is not available!")
                    if isinstance(int(line), int) == False:
                        raise UIError("Line is not an integer!")
                    else:
                        if isinstance(int(column), int) == False:
                            raise UIError("Column is not an integer!")
                    if 0 <= int(line) <= 5 and 0 <= int(column) <= 5:
                        if self.__repo.get_board().data[int(line)][int(column)] == " ":
                            self.__repo.move(piece, int(line), int(column))
                            ok = True
                        else:
                            raise UIError("The chosen position is not available!")
                print(self.__repo.get_board())
                if self.__repo.isGameWon("O") == True or self.__repo.isGameWon("X") == True:
                    print("Chaos has won")
                    break
                if self.__repo.nospacesleft() == True:
                    print("Chaos has won")
                    break
                self.__ai.move("X", "O", self.__repo.get_board())
                print(self.__repo.get_board())
                if self.__repo.isGameWon("X") == True or self.__repo.isGameWon("O") == True:
                    print("Order has won")
                    break
                if self.__repo.nospacesleft() == True:
                    print("Chaos has won")
                    break

        except Exception as e:
            print(f"Error: {str(e)}")

    def run(self):
        try:
            while True:
                if self.Menu() == "exit":
                    break
        except Exception as e:
            print(f"Error: {str(e)}")

if __name__ == "__main__":
    ui = UI()
    ui.run()



