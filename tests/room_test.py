from classes.room import Room
from classes.guest import Guest
from classes.song import Song
from classes.bartab import Bartab
import unittest

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.song = Song("Don't Stop Believin'", "Journey")
        self.room = Room(1, 2, 10)
        self.guest = Guest("Tim", 32, 20.5, self.song)
        self.guest_2 = Guest("Beyonce", 38, 3.2)

    def test_room_has_number(self):
        self.assertEqual(1, self.room.number)

    def test_room_has_capacity(self):
        self.assertEqual(2, self.room.capacity)

    def test_room_has_entry_fee(self):
        self.assertEqual(10, self.room.entry_fee)
    
    def test_room_has_entry_fee_default(self):
        no_fee_argument_room = Room(1, 2)
        self.assertEqual(0, no_fee_argument_room.entry_fee)

    def test_room_has_bartab(self):
        self.assertEqual(Bartab, type(self.room.bartab))

    def test_room_has_songs_property(self):
        self.assertEqual(list, type(self.room.songs))

    def test_room_has_guests_property(self):
        self.assertEqual(list, type(self.room.guests))

    def test_can_check_in_guest(self):
        self.room.check_in_guest(self.guest)
        self.assertEqual(1, len(self.room.guests))

    def test_doesnt_check_in_guest_less_money_than_entry_fee(self):
        self.guest.wallet = 0
        self.room.check_in_guest(self.guest)
        self.assertEqual(0, len(self.room.guests))

    def test_cant_check_in_guest_over_capacity(self):
        self.room.check_in_guest(self.guest)
        self.room.check_in_guest(self.guest)
        self.room.check_in_guest(self.guest)
        self.assertEqual(2, len(self.room.guests))

    def test_guest_check_in_reduces_guest_money_if_fee(self):
        self.room.check_in_guest(self.guest)
        self.assertEqual(10.5, self.guest.wallet)
    
    def test_check_in_produces_bartab_receipt_item(self):
        self.room.check_in_guest(self.guest)
        self.assertEqual(1, len(self.room.bartab.receipt))

    def test_check_in_with_fav_song_cheers(self):
        self.room.add_song(self.song)
        self.assertEqual("Whoo! They have my favourite song!", self.room.check_in_guest(self.guest))

    def test_check_in_without_fav_song_does_not_cheer(self):
        self.assertEqual(None, self.room.check_in_guest(self.guest))

    def test_can_check_out_guest_exists(self):
        self.room.check_in_guest(self.guest)
        self.room.check_out_guest(self.guest)
        self.assertEqual(0, len(self.room.guests))

    def test_can_check_out_guest_doesnt_exists(self):
        self.room.check_in_guest(self.guest)
        self.room.check_out_guest(self.guest_2)
        self.assertEqual(1, len(self.room.guests))

    def test_can_add_songs_to_room(self):
        self.room.add_song(self.song)
        self.assertEqual(1, len(self.room.songs))
