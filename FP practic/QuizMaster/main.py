from Service import *


class UIError(Exception):
    pass


class UI:

    def __init__(self):
        self.__service = Service()

    def read_comand(self):
        cmd = input()
        cmd = cmd.split(" ",1)
        if cmd[0] == "add":
            self.add_question(cmd[1])
        elif cmd[0] == "start":
            self.start_quizz(cmd[1])
        elif cmd[0] == "create":
            self.create_quizz(cmd[1])
        elif cmd[0] == "exit":
            return "exit"
        else:
            print("No such command!")

    def add_question(self, parameters):
        try:
            params = parameters.split(", ")
            if len(params) != 7:
                raise UIError("The format is wrong!!")
            else:
                id = params[0]
                text = params[1]
                answer1 = params[2]
                answer2 = params[3]
                answer3 = params[4]
                correct_answer = params[5]
                difficulty = params[6]
                self.__service.add_question(id, text, answer1, answer2, answer3, correct_answer, difficulty)
                print("Question added successfully!!")
        except Exception as e:
            print(f"Error: {str(e)}")

    def create_quizz(self, parameters):
        param = parameters.split(" ")
        if len(param) != 3:
            raise UIError("The format is wrong!")
        else:
            self.__service.create_quiz(parameters)
            print("Quizz created successfully!!")

    def start_quizz(self, parameters):
        questions = self.__service.start_quizz(parameters)
        score = 0
        for question in questions:
            print("\n")
            print(question.difficulty)
            print(question.text)
            print( f"1) {question.choice_a}" + "\n" + f" 2) {question.choice_b}" + "\n" + f"3) {question.choice_c}")
            answer = input("Your choice: ")
            if answer == question.correct_choice:
                if question.difficulty == "easy":
                    score += 1
                elif question.difficulty == "medium":
                    score += 2
                elif question.difficulty == "hard":
                    score += 3
        print("Quiz finished! Your score:", score)


    def Menu(self):
        try:
            inp = self.read_comand()
            while inp != "exit":
                inp = self.read_comand()
        except Exception as e:
            print(f"Error: {str(e)}")


if __name__ == "__main__":
    ui = UI()
    ui.Menu()
