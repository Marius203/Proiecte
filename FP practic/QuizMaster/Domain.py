class Question:

    def __init__(self, id, text, choice_a, choice_b, choice_c, correct_choice, difficulty):
        self.__id = id
        self.__text = text
        self.__choice_a = choice_a
        self.__choice_b = choice_b
        self.__choice_c = choice_c
        self.__correct_choice = correct_choice
        self.__difficulty = difficulty


    @property
    def id(self):
        return self.__id

    @property
    def text(self):
        return self.__text

    @property
    def choice_a(self):
        return self.__choice_a

    @property
    def choice_b(self):
        return self.__choice_b

    @property
    def choice_c(self):
        return self.__choice_c

    @property
    def correct_choice(self):
        return self.__correct_choice

    @property
    def difficulty(self):
        return self.__difficulty

    def __str__(self):
        return(f" ID: {self.__text}, text: : {self.__text}, a: {self.__choice_a}, b: {self.__choice_b}, c: {self.__choice_c}, correct choice: {self.__correct_choice}, difficulty: {self.__difficulty}")

    def __iter__(self):
        return iter(self.__id + self.__text + self.__choice_a + self.__choice_b + self.__choice_c + self.__correct_choice + self.__difficulty)