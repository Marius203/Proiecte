from Domain import Rooms, Reservation
from datetime import datetime
import random

class RepoError(Exception):
    pass

class Repo:

    def __init__(self):
        self.__rooms = self.load_rooms()
        self.__file_name = "rooms.txt"

    def load_rooms(self):
        try:
            new_roms = {}
            with open("rooms.txt", "r") as load_file:
                loaded_data = load_file.readlines()
                for data_line in loaded_data:
                    data_line = data_line.split(", ")
                    if len(data_line) == 2:
                        room = Rooms(str(data_line[0]), str(data_line[1]))
                        new_roms[room.number] = room
            load_file.close()
            return new_roms
        except FileNotFoundError:
            return {}

    def save_data(self):
        with open ("rooms.txt", "w") as save_file:
            for room in self.__rooms.values():
                save_data = str(room.number) + ", " + str(room.type)
                save_file.write(save_data)
            save_file.close()

    def get_availabe_rooms(self, rented):
        available_rooms = []
        for room in self.__rooms.values():
            if room.number not in rented:
                available_rooms.append(room)
        return available_rooms


class ReservationRepo:

    def __init__(self):
        self.__reservations = self.load_reservations()
        self.__file_name = "reservations.txt"

    def load_reservations(self):
        try:
            new_reservations = {}
            with open("reservations.txt", "r") as load_file:
                loaded_data = load_file.readlines()
                for data_line in loaded_data:
                    data_line = data_line.split(", ")
                    if len(data_line) == 6:
                        reservation = Reservation(str(data_line[0]), str(data_line[1]), str(data_line[2]), str(data_line[3]), str(data_line[4]), str(data_line[5])[:-1])
                        new_reservations[reservation.id] = reservation
            load_file.close()
            return new_reservations
        except FileNotFoundError:
            return {}

    def save_data(self):
        with open ("reservations.txt", "w") as save_file:
            for reservation in self.__reservations.values():
                save_data = str(reservation.id) + ", " + str(reservation.number) + ", " + str(reservation.client_name) + ", " + str(reservation.no_guests) + ", " + str(reservation.arrival) + ", " + str(reservation.departure) + "\n"
                save_file.write(save_data)
            save_file.close()

    def create_reservation(self, guest_name, room_type, guest_number, arrival, departure):
        """
         enters the guest's family name, room type, number of guests, arrival and departure dates.
         In case of a validation error (no family name, invalid arrival/departure, less than 1 or more than 4 guests),
        the program provides an error message [1p].
        The program creates a reservation number (unique, random, exactly 4 digits [1p]) and select a room from the
        available rooms of that type. If there are no rooms of the desired type available during the reservation dates,
        the program displays an error message
        :param guest_name:
        :param room_type:
        :param arrival:
        :param departure:
        :return:
        """
        repo = Repo()
        if len(guest_name) == 0:
            raise RepoError("No name!")
        if datetime.strptime(arrival, "%d.%m").date() > datetime.strptime(departure, "%d.%m").date():
            raise RepoError("Invalid arrival/departure!")
        ar = arrival.split(".")
        depe = departure.split(".")
        if len(ar) != 2 or len(depe) != 2:
            raise RepoError("Invalid arrival/departure!")
        if datetime.strptime(arrival, "%d.%m").date() == datetime.strptime(departure, "%d.%m").date():
            raise RepoError("Invalid arrival/departure!")
        if room_type not in ["single", "double", "triple", "apartment"]:
            raise RepoError("Invalid room type!")
        if int(guest_number) < 1 or int(guest_number) > 4:
            raise RepoError("Invalid number of guests!")
        #If there are no rooms of the desired type available during the reservation dates, the program displays an error message
        rented = ReservationRepo.get_reserved_rooms(self, arrival, departure)
        available_rooms = repo.get_availabe_rooms(rented)
        if len(available_rooms) == 0:
            raise RepoError("No rooms available!")
        listr = []
        for room in available_rooms:
            if room.type != room_type:
                listr.append(room)
        if len(listr) == 0:
            raise RepoError("No rooms available!")
        room = random.choice(listr)
        number = self.create_reservation_number()
        reservation = Reservation(number, room.number, guest_name, guest_number, arrival, departure)
        self.__reservations[reservation.id] = reservation
        self.save_data()

    def create_reservation_number(self):
        number = random.randint(1000, 9999)
        if number in self.__reservations:
            return self.create_reservation_number()
        return number
    def delete_reservation(self, number):
        if number in self.__reservations:
            del self.__reservations[number]
            self.save_data()
        else:
            raise RepoError ("Nothing to delete!")

    def get_reserved_rooms(self, arrival, departure):
        """
        get rooms that are reserved in a specific time period
        :param arrival: the start date
        :param departure: the end date
        :return: a list wih rented rooms
        """
        reserved_rooms = []
        rooms = self.get_all_reservations()
        for reservation in self.__reservations.values():
            if (datetime.strptime(reservation.arrival, "%d.%m").date() <= datetime.strptime(departure,"%d.%m").date() and datetime.strptime( reservation.departure, "%d.%m").date() >= datetime.strptime(arrival, "%d.%m").date()):
                reserved_rooms.append(reservation.number)
        return reserved_rooms

    def get_all_reservations(self):
        return list(self.__reservations.values())

