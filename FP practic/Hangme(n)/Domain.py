from random import randint


class Sentence:

    def __init__(self):
        self.__text = self.readfromfile("Hangman.txt")

    def readfromfile(self, filename):
        with open(filename, "r") as f:
            lines= f.readlines()
            a = randint(0, len(lines) - 1)
            text = str(lines[a]).strip("\n")
            return text  # Return the value

    def writeinfile(self, filename, sentence):
        with open(filename, 'r') as f:
            lines = f.readlines()
        with open(filename, 'w') as f:

            ok = True
            for line in lines:
                if line.strip("\n") == sentence:
                    ok = False
                f.write(line)
            if ok == False:
                f.close()
                return False
            f.write(sentence + "\n")
        f.close()
        return True

    def __iter__(self):
        words = self.__text.split()  # Split the string into a list of words
        return iter(words)

    def __str__(self):
        return str(self.__text)






