
class Rooms:
    def __init__(self, number, type):
        self.__number = number
        self.__type = type

    @property
    def number(self):
        return self.__number

    @property
    def type(self):
        return self.__type

    def __str__(self):
        return str(self.__number) + ", " + str(self.__type)

    def __iter__(self):
        return iter(self.__number + self.__type)



class Reservation:

    def __init__(self, id, number, client_name, no_guests, arrival, departure):
        self.__id = id
        self.__number = number
        self.__client_name = client_name
        self.__no_guests = no_guests
        self.__arrival = arrival
        self.__departure = departure

    @property
    def id(self):
        return self.__id

    @property
    def number(self):
        return self.__number

    @property
    def client_name(self):
        return self.__client_name

    @property
    def no_guests(self):
        return self.__no_guests

    @property
    def arrival(self):
        return self.__arrival

    @property
    def departure(self):
        return self.__departure

    def __str__(self):
        return str(self.__id) + ", " + str(self.__number) + ", " + str(self.__client_name) + ", " + str(self.__no_guests) + ", " + str(self.__arrival) + ", " + str(self.__departure)

    def __iter__(self):
        return iter(self.__id + self.__number + self.__client_name + self.__no_guests + self.__arrival + self.__departure)
