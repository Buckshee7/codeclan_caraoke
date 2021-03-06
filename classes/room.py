from classes.bartab import Bartab

class Room:
    def __init__(self, number, capacity, fee = 0):
        self.number = number
        self.capacity = capacity
        self.songs = []
        self.guests = []
        self.entry_fee = fee
        self.bartab = Bartab()

    def check_in_guest(self, guest):
        if len(self.guests) < self.capacity and guest.wallet >= self.entry_fee:
            self.guests.append(guest)
            guest.reduce_wallet(self.entry_fee)
            self.bartab.add_receipt_item(guest, "Entry Fee", self.entry_fee)
            if guest.fav_song in self.songs:
                return guest.cheer()

    def check_out_guest(self, guest):
        if (guest in self.guests):
            self.guests.remove(guest)
    
    def add_song(self, song):
        self.songs.append(song)