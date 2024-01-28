from Domain import Question


class ReposioryError(Exception):
    pass


class Repository:

    def __init__(self):
        self.__data = self.load_data()
        self.file = "QuizzList.txt"


    def load_data(self):
        try:
            new_quiz_list = {}
            with open("QuizzList.txt", "r") as load_file:
                loaded_data = load_file.readlines()
                for data_line in loaded_data:
                    data_line = data_line.split(", ")
                    if len(data_line) == 7:
                        question = Question(str(data_line[0]), str(data_line[1]), str(data_line[2]), str(data_line[3]), str(data_line[4]), str(data_line[5]), str(data_line[6]))
                        new_quiz_list[question.id] = question
            load_file.close()
            return new_quiz_list
        except FileNotFoundError:
            return {}

    def save_data(self):
        with open ("QuizzList.txt", "w") as save_file:
            for question in self.__data.values():
                save_data = str(question.id) + ", " + str(question.text) + ", " + str(question.choice_a + ", " + str(question.choice_b) + ", " + str(question.choice_c) + ", " + str(question.correct_choice) + ", " + str(question.difficulty))
                save_file.write(save_data)
            save_file.close()

    def add_question(self, id, text, choice_a, choice_b, choice_c, correct, difficulty):
        question = Question(id, text, choice_a, choice_b, choice_c, correct, difficulty)
        if question.id in self.__data or question.text in self.__data:
            raise ReposioryError ("Already exists!")
        self.__data[question.id] = question
        self.save_data()

    def get_by_difficulty(self, difficulty_level):
        list = []
        # print(difficulty_level)
        for question in self.__data.values():
            # print((question.difficulty))
            if question.difficulty[:-1] == difficulty_level:
                list.append(question)
        print(len(list))
        return list

    def get_all_questions(self):
        return list(self.__data.values())

    def count_questions(self, difficulty_level):
        return len(self.get_by_difficulty(difficulty_level))

    def write_quiz_file(self, fname, questionlist):
        with open(fname, "w") as file:
            for question in questionlist:
                file.write(str(question.id) + ", " + str(question.text) + ", " + str(question.choice_a + ", " + str(question.choice_b) + ", " + str(question.choice_c) + ", " + str(question.correct_choice) + ", " + str(question.difficulty)))
        file.close()

    def readquizfromfile(self, fname):
        # print(fname)
        quiz = []
        with open(fname, 'r') as f:
            lines = f.readlines()
            for i in lines:
                i = i.strip("\n")
                i = i.split(", ")
                id = i[0]
                text = i[1]
                answer1 = i[2]
                answer2 = i[3]
                answer3 = i[4]
                correct_answer = i[5]
                difficulty = i[6]
                q = Question(id, text, answer1, answer2, answer3, correct_answer, difficulty)
                quiz.append(q)
        f.close()
        return quiz


# repo = Repository()
# all_questions = repo.get_all_questions()
# for q in all_questions:
#     print(str(q))