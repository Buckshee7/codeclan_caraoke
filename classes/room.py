class Room:
    def __init__(self, number, capacity):
        self.number = number
        self.capacity = capacity
        self.songs = []
        self.guests = []

    def check_in_guest(self, guest):
        self.guests.append(guest)

    def check_out_guest(self, guest):
        if (guest in self.guests):
            self.guests.remove(guest)
    
    def add_song(self, song):
        self.songs.append(song)