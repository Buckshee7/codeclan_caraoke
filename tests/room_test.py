from classes.room import Room
from classes.guest import Guest
import unittest

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room(1, 5)
        self.guest = Guest("Tim", 32)

    def test_room_has_number(self):
        self.assertEqual(1, self.room.number)

    def test_room_has_capacity(self):
        self.assertEqual(5, self.room.capacity)

    def test_room_has_songs_property(self):
        self.assertEqual(list, type(self.room.songs))

    def test_room_has_guests_property(self):
        self.assertEqual(list, type(self.room.guests))

    def test_can_check_in_guest(self):
        self.room.check_in_guest(self.guest)
        self.assertEqual(1, len(self.room.guests))

    def test_can_check_out_guest(self):
        self.room.check_in_guest(self.guest)
        self.room.check_out_guest(self.guest)
        self.assertEqual(0, len(self.room.guests))
        