from classes.room import Room
from classes.guest import Guest
from classes.song import Song
import unittest

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room(1, 2)
        self.guest = Guest("Tim", 32)
        self.guest_2 = Guest("Beyonce", 38)
        self.song = Song("Don't Stop Believin'", "Journey")

    def test_room_has_number(self):
        self.assertEqual(1, self.room.number)

    def test_room_has_capacity(self):
        self.assertEqual(2, self.room.capacity)

    def test_room_has_songs_property(self):
        self.assertEqual(list, type(self.room.songs))

    def test_room_has_guests_property(self):
        self.assertEqual(list, type(self.room.guests))

    def test_can_check_in_guest(self):
        self.room.check_in_guest(self.guest)
        self.assertEqual(1, len(self.room.guests))

    def test_cant_check_in_guest_over_capacity(self):
        self.room.check_in_guest(self.guest)
        self.room.check_in_guest(self.guest)
        self.room.check_in_guest(self.guest)
        self.assertEqual(1, len(self.room.guests))

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
