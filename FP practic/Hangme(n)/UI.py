from Repo import *

class UI:

    def __init__(self):
        self.__repo = Repo()
        self.__hidden_sentence = self.__repo.dysplay_sentence1()
        self.__sentence_handler = str(self.__repo.get_sentence())
        self.__hangman_word = "hangman"
        self.__hangman_progress = " "


    def displa_menu(self):
        print("~~~~~~START~~~~~~")
        print("1. Add sentence")
        print("2. Play (Hang yourself)")
        print("3. Exit")
        try:
            while True:
                choice = input("Enter your choice: ")
                if choice == '1':
                    self.addsentence()
                elif choice == '2':
                    self.start()
                elif choice == '3':
                    print("Exiting...")
                    break
                else:
                    print("Invalid choice. Go and hang yourself. You re stupid")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def addsentence(self):
        try:
            yoursentence = str(input("Enter your input: "))
            self.__repo.addsentence(yoursentence)
            self.displa_menu()
        except Exception as e:
            print (f"Error {str(e)}")

    def start(self):
        incorrect_attempts = 0

        while '_' in self.__hidden_sentence and self.__hangman_progress != self.__hangman_word:
            print(self.__hidden_sentence + " - " + self.__hangman_progress)
            guess = input("Please, take a guess: ").lower()
            if guess in self.__repo.get_duessed_letters() or guess not in self.__sentence_handler:
                incorrect_attempts += 1
                self.__hangman_progress = self.__hangman_word[:incorrect_attempts]
            else:
                new_hidden_sentence = ""
                for i in range(len(self.__sentence_handler)):
                    if self.__sentence_handler[i] == guess:
                        new_hidden_sentence += guess
                    else:
                        new_hidden_sentence += self.__hidden_sentence[i]
                self.__hidden_sentence = []
                self.__hidden_sentence = new_hidden_sentence
            if self.__hangman_progress == self.__hangman_word:
                print(self.__hidden_sentence + " - " + self.__hangman_progress)
                print("You lost!")
            elif '_' not in self.__hidden_sentence:
                print(self.__hidden_sentence + " - " + self.__hangman_progress)
                print("You won!")


if __name__ == "__main__":
    ui = UI()

    ui.displa_menu()
