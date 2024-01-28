from Domain import Sentence
import random

class RepositoryError(Exception):
    pass

class Sentence_repo:
    def __init__(self):
        self.__sentence = Sentence()
        self.__shuffeled_sentence = self.suffle_sentence()

    def suffle_sentence(self):
        sentence = str(self.__sentence)
        # print(sentence)
        # print(sentence)
        letters = []
        new_word_list = []
        listt = sentence.split(' ')
        for word in listt:
            if word[len(word) - 1] == "\n":
                for i in range(1, len(word) - 2):
                    letters.append(word[i])
            else:
                ((for i in range(1,len(word)-1):
                    letters.append(word[i])))
        random.shuffle(letters)
        for word in listt:
            new_word = []
            if word[len(word) - 1] == "\n":
                new_word.append(word[0])
                for i in range(1, len(word) - 2):
                    new_word.append(letters[0])
                    letters.pop(0)
                new_word.append(word[len(word)-2])
                word = ''.join(new_word)
                new_word_list.append(word)

            else:
                new_word = []
                new_word.append(word[0])
                for i in range(1, len(word) - 1):
                    new_word.append(letters[0])
                    letters.pop(0)
                if len(word) > 1:
                    new_word.append(word[len(word) - 1])
                new_word.append(" ")
                word = ''.join(new_word)
                new_word_list.append(word)

        shuffeled_sentence = ''.join(new_word_list)
        return shuffeled_sentence


    def played_sentence(self,):
        return self.__shuffeled_sentence

    def initial_sentence(self,):
        return self.__sentence

    def swap_letters(self, c1, c2, c3, c4):
        sentence = self.__shuffeled_sentence
        # print(sentence)
        words = sentence.split(" ")
        letters = list(sentence)
        if c1 > len(words) - 1 or c3 > len(words) - 1:
            raise RepositoryError("The indices of the words are out of range!")
        else:
            if c2 > len(words[c1]) - 2 or c4 > len(words[c3]) - 2 or c2 == 0 or c4 == 0:
                raise RepositoryError("The indices of the letters are out of range!")
            else:
                a = 0
                b = 0
                for j in range(c1):
                    a = a + len(words[j]) + 1
                a += c2
                for j in range(c3):
                    b = b + len(words[j]) + 1
                b += c4
                letters[a], letters[b] = letters[b], letters[a]
        new_list = ''.join(letters)


        self.__shuffeled_sentence= new_list
        # print(self.__sentence)

    def get_number_letters(self):
        letters = []
        sentence = str(self.__sentence)
        words = sentence.split(" ")
        # print(self.__sentence)
        # print(words)
        for word in words:
            if word[len(word) - 1] == "\n":
                for i in range(0, len(word) - 1):
                    letters.append(word[i])
            else:
                for i in range(0, len(word)):
                    letters.append(word[i])
        # print(letters)
        c = len(letters)
        return c

    def win(self):
        if self.__sentence == self.__shuffeled_sentence:
            return True
        else:
            return False

if __name__ == "__main__":
    repo = Sentence_repo()

    print(repo.suffle_sentence())
    print(repo.get_number_letters())



