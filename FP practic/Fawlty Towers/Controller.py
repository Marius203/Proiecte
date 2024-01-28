from Repository import *
from datetime import datetime, timedelta

class ControllerError(Exception):
    pass

class Controller:

    def __init__(self):
        self.__rooms_repo = Repo()
        self.__reservations_repo = ReservationRepo()

    def add_rental(self, name, room_type, number_of_guests, rented_date, due_date):
        self.__reservations_repo.create_reservation(name, room_type, number_of_guests, rented_date, due_date)

    def delete_reservation(self, number):
        self.__reservations_repo.delete_reservation(number)

    def show_available_rooms(self, arrivel, departure):
        rentals = self.__reservations_repo.get_reserved_rooms(arrivel, departure)
        for room in self.__reservations_repo.get_reserved_rooms(arrivel, departure):
            print(room)
        return self.__rooms_repo.get_availabe_rooms(rentals)

    def monthly_report(self):
        """
         Monthly report. The system will display an ordered list of months, sorted descending by the number of
         reservation days (e.g. a week-long holiday is 1 reservation, but counts as 7 reservation nights) [1p].
         Make sure to handle the case of reservations that start during one month but end during the next one
         (e.g. from July 30 to August 5th)
        :param month:
        :return:
        """
        months = {}
        for reservation in self.__reservations_repo.get_all_reservations():
            arrival = datetime.strptime(reservation.arrival, "%d.%m").date()
            departure = datetime.strptime(reservation.departure, "%d.%m").date()
            while arrival <= departure:
                if arrival.month not in months:
                    months[arrival.month] = 1
                else:
                    months[arrival.month] += 1
                arrival += timedelta(days=1)
        return sorted(months.items(), key=lambda x: x[1], reverse=True)

