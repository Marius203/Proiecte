from Controller import *

class UIError(Exception):
    pass

class UI:

    def __init__(self, run):
        self.__controller = Controller()
        self.__run = run

    def Menu(self):
        print("Menu:")
        print("1. Make a reservation")
        print("2. Cancel a reservation")
        print("3. Show available rooms")
        print("4. Monthly report")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            self.make_reservation()
        elif choice == "2":
            self.cancel_reservation()
        elif choice == "3":
            self.show_available_rooms()
        elif choice == "4":
            self.monthly_report()
        elif choice == "5":
            print("Goodbye!")
            return "exit"
        else:
            print("No such command!")

    def make_reservation(self):
        # try:
            name = input("Enter the name of the client: ")
            room_type = input("Enter the type of the room: ")
            number_of_guests = input("Enter the number of guests: ")
            arrival = input("Enter the arrival date: ")
            departure = input("Enter the departure date: ")
            self.__controller.add_rental(name, room_type, number_of_guests, arrival, departure)
            print("Reservation made successfully!")
        # except Exception as e:
        #     print(f"Error: {str(e)}")
        # start <file_name>
    def cancel_reservation(self):
        try:
            number = input("Enter the number of the reservation: ")
            self.__controller.delete_reservation(number)
            print("Reservation canceled successfully!")
        except Exception as e:
            print(f"Error: {str(e)}")

    def show_available_rooms(self):
        arrival = input("Enter the arrival date <day.month>: ")
        arrival1 = arrival.split(".")
        if len(arrival1) != 2:
            raise UIError("The format is wrong!")
        departure = input("Enter the departure date <day.month>: ")
        departure1 = departure.split(".")
        if len(departure1) != 2:
            raise UIError("The format is wrong!")
        print(f"{arrival} - {departure}")
        rooms = self.__controller.show_available_rooms(arrival, departure)
        for room in rooms:
            print(str(room)[:-1])

    def monthly_report(self):
        print(self.__controller.monthly_report())

    def run(self):
        # try:
            while True:
                if self.Menu() == "exit":
                    break
        # except Exception as e:
        #     print(f"Error: {str(e)}")

if __name__ == "__main__":
    ui = UI(input("Enter the name of the file: "))
    ui.run()

