from Repo import Sentence_repo
class ControllerError(Exception):
    pass

class Controller:

    def __init__(self, repo: Sentence_repo):
        self.__repo = repo
        self.__undo_string = []

    def undo(self):
        if len(self.__undo_string) == 0:
            raise ControllerError("No more undos!!")

        # Pop the last change from __changes
        last_change = self.__undo_string.pop()

        # Apply the opposite swap operation to undo the last change
        c1, c2, c3, c4 = last_change
        self.__repo.swap_letters(c3, c4, c1, c2)

    def shuffle(self):
        return self.__repo.suffle_sentence()

    def swapp(self,c1,c2,c3,c4,count):
        self.__undo_string.append((c1,c2,c3,c4))
        if count > 0:
            return self.__repo.swap_letters(c1,c2,c3,c4)
        else:
            return ControllerError("Your score s 0")

    def pleyed_sentence(self):
        return self.__repo.played_sentence()

    def initial_sentence(self):
        return self.__repo.initial_sentence()

    def get_score(self):
        return self.__repo.get_number_letters()

    def win(self):
        return self.__repo.win()

