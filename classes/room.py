class Room:
    def __init__(self, number, capacity):
        self.number = number
        self.capacity = capacity
        self.songs = []
        self.guests = []

    def check_in_guest(self, guest):
        self.guests.append(guest)
