from Repository import *
import random


class ServiceError(Exception):
    pass


class Service:

    def __init__(self):
        self.__repo = Repository()

    def create_quiz(self, parameters):
        params = parameters.split(" ")
        params[1] = int(params[1])
        # print(len(self.__repo.get_all_questions()))
        if int(params[1]) > len(self.__repo.get_all_questions()):
            raise ServiceError("The number you provided exceeded the number of questions available!")
        else:
            if int(params[1])/2 > len(self.__repo.get_by_difficulty(str(params[0]))):
                raise ServiceError("Not enough questions with this difficulty level!")
            else:
                questionlist = []
                i = 0
                while i < (params[1])/2:
                    a = random.choice(self.__repo.get_by_difficulty(params[0]))
                    if a not in questionlist:
                        questionlist.append(a)
                        i += 1

                while i < (params[1]):
                    a = random.choice(self.__repo.get_all_questions())
                    if a not in questionlist:
                        questionlist.append(a)
                        i += 1

                self.__repo.write_quiz_file(params[2], questionlist)


    def add_question(self, id, text, answer1, answer2, answer3, correct_answer, difficulty):
            self.__repo.add_question(id, text, answer1, answer2, answer3, correct_answer, difficulty)

    def start_quizz(self, parameters):
        questions = self.__repo.readquizfromfile(parameters)
        return questions
