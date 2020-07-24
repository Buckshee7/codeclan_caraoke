from classes.room import Room
import unittest

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room(1, 5)

    def test_room_has_number(self):
        self.assertEqual(1, self.room.number)

    def test_room_has_capacity(self):
        self.assertEqual(5, self.room.capacity)

    def test_room_has_songs_property(self):
        self.assertEqual(list, type(self.room.songs))

    def test_room_has_guests_property(self):
        self.assertEqual(list, type(self.room.guests))