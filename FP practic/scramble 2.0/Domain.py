from random import randint

class Sentence:

    def __init__(self):
        self.__text = self.readfromfile("Sentences.txt")

    def readfromfile(self, fname):
        with open(fname, 'r') as f:
            lines = f.readlines()
            a = randint(0, len(lines) - 1)
            text = str(lines[a]).strip("\n")
            return text  # Return the value

    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, new_sentence):
        self.__text = new_sentence

    def __str__(self):
        return str(self.__text)

    def __eq__(self, other):
        if not isinstance(other, Sentence):  # Fix the logic here
            return False

        return self.text == other.text

    def __iter__(self):
        words = self.__text.split()  # Split the string into a list of words
        return iter(words)


