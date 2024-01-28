from Domain import Sentence


class RepoError(Exception):
    pass


class Repo:

    def __init__(self):
        self.__sentence = Sentence()
        self.__guesssed_letters = []

    def addsentence(self, sentence):
        s = Sentence()
        string = sentence
        string = string.strip()
        contor = 0
        for i in string:
            if i == " ":
                contor += 1
        if contor < 2:
            raise RepoError("Not enough words!")
        else:
            contor = 0
            for i in string:
                if i != " ":
                    contor += 1
                else:
                    if contor < 3:
                        raise RepoError("One of the words does not have enough letters!")
                    else:
                        contor = 0
            if contor < 3:
                raise RepoError("One of the words does not have enough letters!")
            if not s.writeinfile("Hangman.txt", string):
                raise RepoError("This sentence already exists")

    def get_sentence(self):
        return self.__sentence

    def get_duessed_letters(self):
        return  self.__guesssed_letters


    def dysplay_sentence1(self):
        string = []
        sentence = str(self.__sentence)
        self.__guesssed_letters.append(sentence[0])
        self.__guesssed_letters.append(sentence[-1])
        for i in range(1,len(sentence)-1):
            if sentence[i+1] == " " or sentence[i-1] == " ":
                for letter in self.__guesssed_letters:
                    if letter != sentence[i]:
                        self.__guesssed_letters.append(sentence[i])
        for letter in sentence:
            if letter in self.__guesssed_letters or letter == " ":
                string.append(letter)
            else:
                string.append("_")
        display = ''.join(string)
        return display

    def add_guess(self, guess):
            self.__guesssed_letters.append(guess)




# if __name__ == "__main__":
#     r = Repo()
#     sentence = "This is a sample sentence."
#     r.addsentence("cjsjab hasida aosddahj")
#     print( r.dysplay_sentence())