from Controler import *

class UIError(Exception):
    pass


class UI:

    def __init__(self, controller: Controller):
        self.__controller = controller
        self.score = self.__controller.get_score()

    def start(self):
        try:
            print("~~~~!START!~~~~")

            print("This is your sentence")
            print(str(self.__controller.pleyed_sentence() + " [Your score is: " + str(self.score) + "]"))
            maxx = self.score
            oldstring = self.__controller.pleyed_sentence()
            ok = True

            while self.score != 0:
                ok = True
                while ok:
                    cmd = input()
                    if cmd == "undo":
                        self.__controller.undo()
                        print(self.__controller.pleyed_sentence() + " [Your score is: " + str(self.score) + "]")
                    else:
                        try:
                            cmd = cmd.split(" ")
                            if len(cmd) != 6:
                                raise UIError("Incorrect Format!")
                            elif cmd[0] != "swap" or cmd[3] != "-":
                                raise UIError("Incorrect Format!")
                            elif not cmd[1].isdigit() or not cmd[2].isdigit() or not cmd[4].isdigit() or not cmd[5].isdigit():
                                raise UIError("One of the indices is not a number!")
                            else:
                                c1 = int(cmd[1])
                                c2 = int(cmd[2])
                                c3 = int(cmd[4])
                                c4 = int(cmd[5])
                                oldstring = self.__controller.pleyed_sentence()
                                self.__controller.swapp(c1, c2, c3, c4, self.score)
                                self.score -= 1
                                string = self.__controller.pleyed_sentence()
                                print(str(self.__controller.pleyed_sentence() + " [Your score is: " + str(self.score) + "]"))
                                ok = False

                                if self.__controller.win():
                                    print("You win! Your score is: " + str(self.score))
                                    break
                        except Exception as e:
                             print(f"some error occurred: {str(e)}")
        except Exception as e:
            print(f"some error occurred: {str(e)}")



        if self.__controller.win() == False and self.score == 0:
            print("You lost!")



if __name__ == "__main__":
    repo = Sentence_repo()
    controller = Controller(repo)
    ui = UI(controller)

    ui.start()
